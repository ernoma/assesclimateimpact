from PyQt5.QtCore import QCoreApplication

import uuid
import psycopg2
import psycopg2.extras

from qgis.core import (
    Qgis, QgsMessageLog,
    QgsGeometry, QgsCoordinateTransform,
    QgsDataSourceUri, QgsVectorLayer,
    QgsProject, QgsFeature)

from .createdbconnection import createDbConnection


class YKRToolUploadLayer:
    
    def __init__(self, iface):
        self.iface = iface
        self.sourceLayer = None
        self.sourceFeatures = None
        self.sourceFeatureCount = -1
        self.sourceCRS = None
        self.targetCRS = None
        # self.sourceLayerFields = None

        self.transformContext = QgsProject.instance().transformContext()

    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('YKRTool', message)


    def copySourceLayerFeaturesToTargetTable(self, connParams, sourceLayer, targetTableName, allowOtherUsersToUseUploadedMapLayer, copyOnlySelectedFeatures, retriesLeft=3):
        try:
            conn = createDbConnection(connParams)
        except Exception as e:
            if retriesLeft > 0:
                return self.copySourceLayerFeaturesToTargetTable(connParams, sourceLayer, targetTableName, checkBoxAllowOtherUsersToUseUploadedMapLayer, copyOnlySelectedFeatures, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    'Virhe tietokantayhteyden muodostamisessa',
                    str(e), Qgis.Warning, duration=0)
                return False

        try:
            outputSchemaName, outputTableName = targetTableName.replace('"', '').split('.')
            cur = conn.cursor()
            cur.execute("select exists(select * from information_schema.tables where table_schema = '{}' AND table_name='{}')".format(outputSchemaName, outputTableName))
            if cur.fetchone()[0] == True:
                self.iface.messageBar().pushMessage(
                    self.tr('A table with the name ') + targetTableName + self.tr(' already exists'), Qgis.Warning, duration=0)
                return False
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Unexpected database error'),
                str(e), Qgis.Warning, duration=0)
            conn.close()
            return False

        self.sourceLayer = sourceLayer
        if copyOnlySelectedFeatures:
            self.sourceFeatures = sourceLayer.selectedFeatures()
            self.sourceFeatureCount = sourceLayer.selectedFeatureCount()
        else:
            self.sourceFeatures = sourceLayer.getFeatures()
            self.sourceFeatureCount = sourceLayer.featureCount()

        self.sourceCRS = sourceLayer.sourceCrs()
        # self.sourceLayerFields = sourceLayer.fields().toList()
        #  for index, field in enumerate(self.sourceLayerFields):
        # if field.name() != 'id' and self.yleiskaavaUtils.getStringTypeForFeatureField(field) != 'uuid':
        #         data.append({
        #             "name": field.name(),
        #             "type": self.getStringTypeForFeatureField(field),
        #             "value": QVariant(sourceFeature[field.name()])
        #         })


        query = "CREATE TABLE " + targetTableName + "(" + \
            "id serial PRIMARY KEY, "
    
        if int(str(sourceLayer.wkbType())[:1]) == 3: # polygon
            query += "geom geometry(PolygonZ, 3067)"        
        elif int(str(sourceLayer.wkbType())[:1]) == 6: # MultiPolygon
            query += "geom geometry(MultiPolygonZ, 3067)"
        else:
            raise Exception(self.tr("Unsupported geometry type"))

        query += ")"

        QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)

        try:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Could not create the table to the database'),
                str(e), Qgis.Warning, duration=0)
            conn.close()
            return False


        outputSchemaName, outputTableName = targetTableName.replace('"', '').split('.')

        uri = QgsDataSourceUri()
        uri.setConnection(connParams['host'], connParams['port'],\
            connParams['database'], connParams['user'], connParams['password'])
        uri.setDataSource(outputSchemaName, outputTableName, 'geom')

        targetLayer = QgsVectorLayer(uri.uri(False), outputSchemaName + '.' + outputTableName, 'postgres')
        self.targetCRS = targetLayer.sourceCrs()

        transform = None
        if self.sourceCRS != self.targetCRS:
            transform = QgsCoordinateTransform(self.sourceCRS, self.targetCRS, self.transformContext)

        for index, sourceFeature in enumerate(self.sourceFeatures):
            targetLayerFeature = QgsFeature()
            sourceGeom = sourceFeature.geometry()

            if not sourceGeom.isNull() and transform is not None:
                transformedSourceGeom = QgsGeometry(sourceGeom)
                transformedSourceGeom.transform(transform)
            else:
                transformedSourceGeom = QgsGeometry(sourceGeom)

            targetLayerFeature.setGeometry(transformedSourceGeom)

            geom = targetLayerFeature.geometry()

            try:
                with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cursor:
                    query = ""

                    if geom.isNull() or geom.isEmpty():
                        
                        geom_lack_type = None
                        if geom.isNull():
                            message = self.tr('Feature to upload had NULL geometry.')
                        else:
                            message = self.tr('Feature to upload had empty geometry.')

                        QgsMessageLog.logMessage(message, 'YKRTool', Qgis.Warning)
                        # self.iface.messageBar().pushMessage(, Qgis.Warning, duration=0)

                    else:
                        wkt = geom.asWkt().replace('nan', '0')

                        query = "INSERT INTO {} (geom".format(targetTableName)

                        if geom.isMultipart():
                            query += ") VALUES (ST_SetSRID(ST_Force3D(ST_GeomFromText('{}')), {})".format(wkt, self.targetCRS.authid().split(':')[1])
                        else:
                            query += ") VALUES (ST_Collect(ARRAY[ ST_SetSRID(ST_Force3D(ST_GeomFromText('{}')), {}) ])".format(wkt, self.targetCRS.authid().split(':')[1])

                        query += ")"
                    cursor.execute(query)
                    conn.commit()
            except psycopg2.Error as e:
                QgsMessageLog.logMessage(self.tr('Could not create the table to the database:') + ' {}'.format(e), 'YKRTool', Qgis.Error)
                raise Exception(self.tr('Could not create the table to the database:') + ' {}'.format(e))
        
        if allowOtherUsersToUseUploadedMapLayer:
            query = "GRANT SELECT ON " + targetTableName + " TO public"

            try:
                cur = conn.cursor()
                cur.execute(query)
                conn.commit()
            except Exception as e:
                self.iface.messageBar().pushMessage(
                    self.tr('Could not give access on table ' + outputSchemaName + '.' + outputTableName + ' to public.'),
                    str(e), Qgis.Warning, duration=0)
                
        conn.close()

        QgsProject.instance().addMapLayer(targetLayer)
        return True


    