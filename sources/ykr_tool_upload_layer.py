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


    def copySourceLayerFeaturesToTargetTable(self, connParams, sourceLayer, targetTableName, allowOtherUsersToUseUploadedMapLayer=False, copyOnlySelectedFeatures=False, retriesLeft=3):
        try:
            conn = createDbConnection(connParams)
        except Exception as e:
            if retriesLeft > 0:
                return self.copySourceLayerFeaturesToTargetTable(connParams, sourceLayer, targetTableName, checkBoxAllowOtherUsersToUseUploadedMapLayer, copyOnlySelectedFeatures, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
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
    
        # QgsMessageLog.logMessage("quesourceLayer.wkbType()[:1]ry: " + str(sourceLayer.wkbType()), 'YKRTool', Qgis.Info)

        if sourceLayer.wkbType() == 3 or sourceLayer.wkbType() == 1003: # polygon or polygonz
            query += "geom geometry(PolygonZ, 3067)"        
        elif sourceLayer.wkbType() == 6 or sourceLayer.wkbType() == 1006: # MultiPolygon or MultiPolygonZ
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
                QgsMessageLog.logMessage(self.tr('Could not create the table to the database:') + ' {}'.format(e), 'YKRTool', Qgis.Critical)
                raise Exception(self.tr('Could not create the table to the database:') + ' {}'.format(e))
        
        if allowOtherUsersToUseUploadedMapLayer:
            query = "GRANT SELECT ON " + targetTableName + " TO public"

            try:
                cur = conn.cursor()
                cur.execute(query)
                conn.commit()
            except Exception as e:
                self.iface.messageBar().pushMessage(
                    self.tr('Could not give access on table ') + outputSchemaName + '.' + outputTableName + self.tr(' to public.'),
                    str(e), Qgis.Warning, duration=0)
                
        conn.close()

        QgsProject.instance().addMapLayer(targetLayer)
        return True


    def copyFutureNetworkSourceLayerFeaturesToTargetTable(self, connParams, sourceLayer, targetTableName, retriesLeft=3):
        try:
            conn = createDbConnection(connParams)
        except Exception as e:
            if retriesLeft > 0:
                return self.copyFutureNetworkSourceLayerFeaturesToTargetTable(connParams, sourceLayer, targetTableName, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
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
        self.sourceFeatures = sourceLayer.getFeatures()
        # self.sourceFeatureCount = sourceLayer.featureCount()
        self.sourceCRS = sourceLayer.sourceCrs()

        query = """CREATE TABLE {}(
            id serial PRIMARY KEY,
            geom geometry(PointZ, 3067),
            k_ktyyp varchar NOT NULL,
            k_knimi varchar,
            k_kalkuv int4,
            k_kvalmv int4
            )""".format('"' + outputSchemaName + '"."' + outputTableName + '"')

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

        uri = QgsDataSourceUri()
        uri.setConnection(connParams['host'], connParams['port'],\
            connParams['database'], connParams['user'], connParams['password'])
        uri.setDataSource(outputSchemaName, outputTableName, 'geom')

        targetLayer = QgsVectorLayer(uri.uri(False), outputSchemaName + '.' + outputTableName, 'postgres')
        self.targetCRS = targetLayer.sourceCrs()

        transform = None
        if self.sourceCRS != self.targetCRS:
            transform = QgsCoordinateTransform(self.sourceCRS, self.targetCRS, self.transformContext)

        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cursor:
            try:
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

                        query = "INSERT INTO {} (geom".format('"' + outputSchemaName + '"."' + outputTableName + '"')

                        if sourceFeature.fieldNameIndex("k_ktyyp") != -1:
                            query += ", k_ktyyp"
                        else: 
                            raise Exception(self.tr("Future urban center source layer is missing required field: k_ktyyp"))

                        if sourceFeature.fieldNameIndex("k_knimi") != -1:
                            query += ", k_knimi"
                        else: 
                            raise Exception(self.tr("Future urban center source layer is missing required field: k_knimi"))

                        if sourceFeature.fieldNameIndex("k_kalkuv") != -1:
                            query += ", k_kalkuv"
                        else: 
                            raise Exception(self.tr("Future urban center source layer is missing required field: k_kalkuv"))

                        if sourceFeature.fieldNameIndex("k_kvalmv") != -1:
                            query += ", k_kvalmv"
                        else: 
                            raise Exception(self.tr("Future urban center source layer is missing required field: k_kvalmv"))

                        if geom.isMultipart():
                            raise Exception(self.tr('Multipart geometries not supported'))
                        else:
                            query += ") VALUES (ST_SetSRID(ST_Force3D(ST_GeomFromText('{}')), {})".format(wkt, self.targetCRS.authid().split(':')[1])

                        value = sourceFeature["k_ktyyp"]
                        query += ", '" + str(value) + "'"
                        value = sourceFeature["k_knimi"]
                        query += ", '" + str(value) + "'"
                        value = sourceFeature["k_kalkuv"]
                        query += ", '" + str(value) + "'"
                        value = sourceFeature["k_kvalmv"]
                        query += ", '" + str(value) + "'"

                        query += ")"

                        cursor.execute(query)

                conn.commit()
            except psycopg2.Error as e:
                QgsMessageLog.logMessage(self.tr('Could not create the table to the database:') + ' {}'.format(e), 'YKRTool', Qgis.Critical)
                raise Exception(self.tr('Could not create the table to the database:') + ' {}'.format(e))


        query = "GRANT SELECT ON " + '"' + outputSchemaName + '"."' + outputTableName + '"' + " TO public"

        try:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Could not give access on table ') + '"' + outputSchemaName + '"."' + outputTableName + '"' + self.tr(' to public.'),
                str(e), Qgis.Warning, duration=0)
                
        conn.close()

        QgsProject.instance().addMapLayer(targetLayer)
        return True


    def copyFutureStopsSourceLayerFeaturesToTargetTable(self, connParams, sourceLayer, targetTableName, retriesLeft=3):
        try:
            conn = createDbConnection(connParams)
        except Exception as e:
            if retriesLeft > 0:
                return self.copyFutureStopsSourceLayerFeaturesToTargetTable(connParams, sourceLayer, targetTableName, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
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
        self.sourceFeatures = sourceLayer.getFeatures()
        # self.sourceFeatureCount = sourceLayer.featureCount()
        self.sourceCRS = sourceLayer.sourceCrs()

        query = """CREATE TABLE {}(
            id serial PRIMARY KEY,
            geom geometry(PointZ, 3067),
            k_jltyyp integer NOT NULL,
            k_jlnimi varchar,
            k_liikv int4
            )""".format('"' + outputSchemaName + '"."' + outputTableName + '"')

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

        uri = QgsDataSourceUri()
        uri.setConnection(connParams['host'], connParams['port'],\
            connParams['database'], connParams['user'], connParams['password'])
        uri.setDataSource(outputSchemaName, outputTableName, 'geom')

        targetLayer = QgsVectorLayer(uri.uri(False), outputSchemaName + '.' + outputTableName, 'postgres')
        self.targetCRS = targetLayer.sourceCrs()

        transform = None
        if self.sourceCRS != self.targetCRS:
            transform = QgsCoordinateTransform(self.sourceCRS, self.targetCRS, self.transformContext)

        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cursor:
            try:
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

                        query = "INSERT INTO {} (geom".format('"' + outputSchemaName + '"."' + outputTableName + '"')

                        if sourceFeature.fieldNameIndex("k_jltyyp") != -1:
                            query += ", k_jltyyp"
                        else: 
                            raise Exception(self.tr("Future public transit stops source layer is missing required field: k_jltyyp"))

                        if sourceFeature.fieldNameIndex("k_jlnimi") != -1:
                            query += ", k_jlnimi"
                        else: 
                            raise Exception(self.tr("Future public transit stops source layer is missing required field: k_jlnimi"))

                        if sourceFeature.fieldNameIndex("k_liikv") != -1:
                            query += ", k_liikv"
                        else: 
                            raise Exception(self.tr("Future public transit stops source layer is missing required field: k_liikv"))

                        if geom.isMultipart():
                            raise Exception(self.tr('Multipart geometries not supported'))
                        else:
                            query += ") VALUES (ST_SetSRID(ST_Force3D(ST_GeomFromText('{}')), {})".format(wkt, self.targetCRS.authid().split(':')[1])

                        value = sourceFeature["k_jltyyp"]
                        query += ", '" + str(value) + "'"
                        value = sourceFeature["k_jlnimi"]
                        query += ", '" + str(value) + "'"
                        value = sourceFeature["k_liikv"]
                        query += ", '" + str(value) + "'"

                        query += ")"

                        cursor.execute(query)

                conn.commit()
            except psycopg2.Error as e:
                QgsMessageLog.logMessage(self.tr('Could not create the table to the database:') + ' {}'.format(e), 'YKRTool', Qgis.Critical)
                raise Exception(self.tr('Could not create the table to the database:') + ' {}'.format(e))


        query = "GRANT SELECT ON " + '"' + outputSchemaName + '"."' + outputTableName + '"' + " TO public"

        try:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Could not give access on table ') + '"' + outputSchemaName + '"."' + outputTableName + '"' + self.tr(' to public.'),
                str(e), Qgis.Warning, duration=0)
                
        conn.close()

        QgsProject.instance().addMapLayer(targetLayer)
        return True