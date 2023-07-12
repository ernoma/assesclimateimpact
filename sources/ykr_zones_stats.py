from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication, QVariant

from qgis.core import (Qgis, QgsVectorLayer, QgsDataSourceUri, QgsMessageLog)
# from qgis.core import (QgsTemporalNavigationObject, QgsVectorLayerTemporalProperties)

from .createdbconnection import createDbConnection
from .ykr_tool_dictionaries import YKRToolDictionaries


class YKRZonesStats:
    def __init__(self, ykrToolDictionaries, connParams, iface):
        self.ykrToolDictionaries = ykrToolDictionaries
        self.connParams = connParams
        self.iface = iface


    def setConnectionParams(self, connParams):
        self.connParams = connParams


    def createDBConnection(self, retriesLeft=3):
        conn = None
        try:
            conn = createDbConnection(self.connParams)
        except Exception as e:
            if retriesLeft > 0:
                return self.addQueriesToDatabase(queries, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
                    str(e), Qgis.Warning, duration=0)
                return None
        return conn
    

    def calculateYKRZoneEmissions(self, uuid, outputSchemaName, outputBaseTableName):
        tableNames = self.createYKRZoneEmissionsStatsTables(uuid, outputSchemaName, outputBaseTableName)

        # Update session info table with the table names
        queries = []
        sql = 'UPDATE ' + outputSchemaName + '.sessions_v2 SET results_summary_table_names = \'array[' + tableNames[0] + ', ' + tableNames[1] + ']\'' + ' WHERE sid = \'' + uuid + '\';'
        queries.append(sql)

        # Log SQL queries to QGIS log
        for sql in queries:
            QgsMessageLog.logMessage(sql, 'YKRTool', Qgis.Info)

        # Execute SQL queries
        self.addQueriesToDatabase(queries)

    
    def createYKRZoneEmissionsStatsTables(self, uuid, outputSchemaName, outputBaseTableName):

        queries = []

        uri = QgsDataSourceUri()
        uri.setConnection(self.connParams['host'], self.connParams['port'],\
            self.connParams['database'], self.connParams['user'], self.connParams['password'])
        uri.setDataSource(outputSchemaName, outputBaseTableName, 'geom')

        ykrLayer = QgsVectorLayer(uri.uri(False), "UZ-urban-rural layer", 'postgres')

        if not ykrLayer.isValid():
            self.iface.messageBar().pushMessage(self.tr('Layer failed to load: ') + ykrLayer.name(), Qgis.Warning, duration=10)
            return
        
        baseYear = None
        targetYear = None

        # 0. Get base year and target year from YKR zone emission calculation results
        for ykrFeature in ykrLayer.getFeatures():
            if baseYear is None or ykrFeature['year'].year() < baseYear:
                baseYear = ykrFeature['year'].year()
            if targetYear is None or ykrFeature['year'].year() > targetYear:
                targetYear = ykrFeature['year'].year()

        # Create list for storing YKR zone emission calculation result types and
        # add CO2 emissions of living related personal trips also separately from work related trips to results type list, if they are separately in calculation results
        emissionCalculationResultTypes = []
        for ykrFeature in ykrLayer.getFeatures():
            for field in ykrFeature.fields():
                if field.name() not in ['id', 'xyind', 'mun', 'zone', 'year', 'geom', 'sum_liikenne_tco2_per_sum_yhteensa_tco2', 'sum_liikenne_tco2_per_asukas', 'liikenne_hlo_tco2_per_sum_liikenne_tco2', 'liikenne_hlo_tco2_per_sum_yhteensa_tco2', 'liikenne_hlo_tco2_per_asukas', 'liikenne_hlo_tco2_per_tp', 'liikenne_hlo_tco2_per_as_tp', 'pop_per_popjob_percentage', 'sum_yhteensa_tco2_per_asukas', 'sum_yhteensa_tco2_per_tp', 'sum_yhteensa_tco2_per_as_tp', 'sum_yhteensa_tco2_per_kem']:
                    if field.name() not in emissionCalculationResultTypes:
                        emissionCalculationResultTypes.append(field.name())


        outputTableName = 'stats_' + outputBaseTableName
        # Create table for storing YKR zone emission calculation results
        sql = 'CREATE TABLE IF NOT EXISTS ' + outputSchemaName + '."' + outputTableName + '" (id serial primary key, sid varchar, geom geometry(MultiPolygon, 3067), zone_name varchar, year integer, '
        for emissionCalculationResultType in emissionCalculationResultTypes:
            sql += emissionCalculationResultType + ' numeric, '
        sql = sql[:-2] + ');'
        queries.append(sql)


        # Calculate statistics for each YKR zone and each year
        # 1. Create dictionary for storing results separately for each YKR zone and separately for each year and seprarately for each emission calculation result type
        ykrEmissions = {}
        zoneNames = self.ykrToolDictionaries.getPredefinedUrbanRuralZoningAreaKeys()
        for zoneName in zoneNames:
            ykrEmissions[zoneName] = {}
            # iterate from base year to target year
            for year in range(baseYear, targetYear + 1):
                ykrEmissions[zoneName][year] = {}
                for emissionCalculationResultType in emissionCalculationResultTypes:
                    ykrEmissions[zoneName][year][emissionCalculationResultType] = 0
        
        # 2. Calculate emission calculation result summaries for each YKR zone year by year
        for ykrFeature in ykrLayer.getFeatures():
            ykrZone = ykrFeature['zone']
            ykrZoneName = self.ykrToolDictionaries.getPredefinedUrbanRuralZoningAreaName(str(ykrZone))
            year = ykrFeature['year'].year()
            for emissionCalculationResultType in emissionCalculationResultTypes:
                if type(ykrFeature[emissionCalculationResultType]) == QVariant:
                    if not ykrFeature[emissionCalculationResultType].isNull():
                       ykrEmissions[ykrZoneName][year][emissionCalculationResultType] += ykrFeature[emissionCalculationResultType].value()
                else:
                    ykrEmissions[ykrZoneName][year][emissionCalculationResultType] += ykrFeature[emissionCalculationResultType]
                

        # 3. Create SQL query that creates database table entry separately for each emission calculation result type year by year
        for ykrZoneName in ykrEmissions:
            for year in ykrEmissions[ykrZoneName]:
                sql = 'INSERT INTO ' + outputSchemaName + '."' + outputTableName + '" (sid, zone_name, year, '
                for emissionCalculationResultType in ykrEmissions[ykrZoneName][year]:
                    sql += emissionCalculationResultType + ', '
                sql = sql[:-2]
                sql += ') VALUES (\'' + uuid + "', '" + ykrZoneName + "', " + str(year) + ', '
                for emissionCalculationResultType in ykrEmissions[ykrZoneName][year]:
                    sql += str(ykrEmissions[ykrZoneName][year][emissionCalculationResultType]) + ', '
                sql = sql[:-2] + ');'
                queries.append(sql)

        # 4. Create new table for storing quickchart.io charts for each emission calculation result type year by year, if it does not exist
        sql = 'CREATE TABLE IF NOT EXISTS ' + outputSchemaName + '."stats_charts_' + outputBaseTableName + '" (id serial primary key, sid varchar, geom geometry(MultiPolygon, 3067), year integer, emission_calculation_result_type varchar, chart_url varchar);'
        queries.append(sql)
        
        # 5. Create SQL query that creates database table entry separately for each emission calculation result type
        for year in range(baseYear, targetYear + 1):
            for emissionCalculationResultType in emissionCalculationResultTypes:
                sql = 'INSERT INTO ' + outputSchemaName + '."stats_charts_' + outputBaseTableName + '" (sid, year, emission_calculation_result_type, chart_url) VALUES (\'' + uuid + "\', " + str(year) + ", '" + emissionCalculationResultType + "', "
                sql += "'https://quickchart.io/chart?w=600&h=300&c={type:''bar'',data:{labels:["
                for ykrZoneName in ykrEmissions:
                    sql += "''" + ykrZoneName + "'', "
                sql = sql[:-2] + "]," + "datasets:["
                sql += (
                    "{backgroundColor:[''rgba(117,213,205,1)'',''rgba(238,36,100,1)'',''rgba(174,107,24,1)'',''rgba(213,180,60,1)'',''rgba(48,108,35,1)'',''rgba(235,102,58,1)'',''rgba(119,73,226,1)'',''rgba(238,169,65,1)'',''rgba(145,222,77,1)'',''rgba(207,30,169,1)'',''rgba(66,118,221,1)'',''rgba(21,24,155,1)'',''rgba(115,92,158,1)'',''rgba(155,155,155,1)''],data:["
                )
                for ykrZoneName in ykrEmissions:
                    sql += str(ykrEmissions[ykrZoneName][year][emissionCalculationResultType]) + ', '
                sql = sql[:-2] + "]}]}"
                sql += ",options:{title:{display:true,text:''" + emissionCalculationResultType + ", " + str(year) + "''},legend:{display:false}}}'"

                sql += ");"

                queries.append(sql)

        # # 6. Log SQL queries to QGIS log
        # for sql in queries:
        #     QgsMessageLog.logMessage(sql, 'YKRTool', Qgis.Info)

        # 7. Execute SQL queries
        self.addQueriesToDatabase(queries)

        # 8. Return table names list
        return [outputSchemaName + '.' + outputTableName, outputSchemaName + '.stats_charts_' + outputBaseTableName]
        


    def addQueriesToDatabase(self, queries, retriesLeft=3):
        if len(queries) > 0 and self.connParams is not None:
            conn = None
            conn = self.createDBConnection()

            try:
                cur = conn.cursor()
                for query in queries:
                    cur.execute(query)
                    conn.commit()
            except Exception as e:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in adding the summary statistics to the database ') + "{}".format(query),
                    str(e), Qgis.Warning, duration=0)
                conn.rollback()
                conn.close()

                return False

            conn.commit()

            return True


    # noinspection PyMethodMayBeStatic
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