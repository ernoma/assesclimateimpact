from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication

from qgis.core import (Qgis, QgsVectorLayer, QgsDataSourceUri, QgsMessageLog)
# from qgis.core import (QgsTemporalNavigationObject, QgsVectorLayerTemporalProperties)


from .ykr_tool_dictionaries import YKRToolDictionaries

class YKRZonesStats:
    def __init__(self, ykrToolDictionaries, connParams, iface):
        self.ykrToolDictionaries = ykrToolDictionaries
        self.connParams = connParams
        self.iface = iface
        

    def setConnParams(self, connParams):
        self.connParams = connParams


    def calculateYKRZoneEmissions(self, uuid, outputSchemaName, outputBaseTableName):

        queries = []

        outputTableName = 'stats_' + outputBaseTableName

        # Create table for storing YKR zone emissions
        sql = 'CREATE TABLE IF NOT EXISTS ' + outputSchemaName + '.' + outputTableName + ' (id serial primary key, sid varchar, geom geometry(MultiPolygon, 3067), zone_name varchar, year integer, pop integer, employ integer, floorspace numeric, sum_yhteensa_tco2 numeric, sum_liikenne_tco2 numeric, liikenne_hlo_tco2 numeric, liikenne_tv_tco2 numeric, liikenne_palv_tco2 numeric, sum_lammonsaato_tco2 numeric, tilat_vesi_tco2 numeric, tilat_lammitys_tco2 numeric, tilat_jaahdytys_tco2 numeric, sum_sahko_tco2 numeric, sahko_kiinteistot_tco2, numeric, sahko_kotitaloudet_tco2 numeric, sahko_palv_tco2 numeric, sahko_tv_tco2 numeric, sum_rakentaminen_tco2 numeric, rak_korjaussaneeraus_tco2 numeric, rak_purku_tco2 numeric, rak_uudis_tco2 numeric);'
        queries.append(sql)

        uri = QgsDataSourceUri()
        uri.setConnection(self.connParams['host'], self.connParams['port'],\
            self.connParams['database'], self.connParams['user'], self.connParams['password'])
        uri.setDataSource(outputSchemaName, outputBaseTableName, 'geom')

        ykrLayer = QgsVectorLayer(uri.uri(False), "UZ-urban-rural layer", 'postgres')

        if not ykrLayer.isValid():
            self.iface.messageBar().pushMessage(self.tr('Layer failed to load: ') + ykrLayer.name(), Qgis.Warning, duration=10)
            return
        
        baseYear = 2023
        targetYear = 2040

        # Calculate statistics for each YKR zone and each year
        # 1. Create dictionary for storing results separately for each YKR zone and separately for each year and seprarately for each emission type
        ykrEmissions = {}
        zoneNames = self.ykrToolDictionaries.getPredefinedUrbanRuralZoningAreaKeys()
        for zoneName in zoneNames:
            ykrEmissions[zoneName] = {}
            # iterate from base year to target year
            for year in range(baseYear, targetYear + 1):
                ykrEmissions[zoneName][year] = {}
                ykrEmissions[zoneName][year]['pop'] = 0
                ykrEmissions[zoneName][year]['employ'] = 0
                ykrEmissions[zoneName][year]['floorspace'] = 0
                ykrEmissions[zoneName][year]['sum_yhteensa_tco2'] = 0
                ykrEmissions[zoneName][year]['sum_liikenne_tco2'] = 0
                ykrEmissions[zoneName][year]['liikenne_hlo_tco2'] = 0
                ykrEmissions[zoneName][year]['liikenne_tv_tco2'] = 0
                ykrEmissions[zoneName][year]['liikenne_palv_tco2'] = 0
                ykrEmissions[zoneName][year]['sum_lammonsaato_tco2'] = 0
                ykrEmissions[zoneName][year]['tilat_vesi_tco2'] = 0
                ykrEmissions[zoneName][year]['tilat_lammitys_tco2'] = 0
                ykrEmissions[zoneName][year]['tilat_jaahdytys_tco2'] = 0
                ykrEmissions[zoneName][year]['sum_sahko_tco2'] = 0
                ykrEmissions[zoneName][year]['sahko_kiinteistot_tco2'] = 0
                ykrEmissions[zoneName][year]['sahko_kotitaloudet_tco2'] = 0
                ykrEmissions[zoneName][year]['sahko_palv_tco2'] = 0
                ykrEmissions[zoneName][year]['sahko_tv_tco2'] = 0
                ykrEmissions[zoneName][year]['sum_rakentaminen_tco2'] = 0
                ykrEmissions[zoneName][year]['rak_korjaussaneeraus_tco2'] = 0
                ykrEmissions[zoneName][year]['rak_purku_tco2'] = 0
                ykrEmissions[zoneName][year]['rak_uudis_tco2'] = 0
                # ykrEmissions[zoneName][year]['tco2_per_pop'] = 0
                # ykrEmissions[zoneName][year]['tco2_per_employ'] = 0
        
        # 2. Calculate emissions for each YKR zone year by year
        for ykrFeature in ykrLayer.getFeatures():
            ykrZone = ykrFeature['zone']
            ykrZoneName = self.ykrToolDictionaries.getPredefinedUrbanRuralZoningAreaName(str(ykrZone))
            year = ykrFeature['year'].year()
            ykrEmissions[ykrZoneName][year]['pop'] += ykrFeature['pop']
            ykrEmissions[ykrZoneName][year]['employ'] += ykrFeature['employ']
            ykrEmissions[ykrZoneName][year]['floorspace'] += ykrFeature['floorspace']
            ykrEmissions[ykrZoneName][year]['sum_yhteensa_tco2'] += ykrFeature['sum_yhteensa_tco2']
            ykrEmissions[ykrZoneName][year]['sum_liikenne_tco2'] += ykrFeature['sum_liikenne_tco2']
            ykrEmissions[ykrZoneName][year]['liikenne_hlo_tco2'] += ykrFeature['liikenne_hlo_tco2']
            ykrEmissions[ykrZoneName][year]['liikenne_tv_tco2'] += ykrFeature['liikenne_tv_tco2']
            ykrEmissions[ykrZoneName][year]['liikenne_palv_tco2'] += ykrFeature['liikenne_palv_tco2']
            ykrEmissions[ykrZoneName][year]['sum_lammonsaato_tco2'] += ykrFeature['sum_lammonsaato_tco2']
            ykrEmissions[ykrZoneName][year]['tilat_vesi_tco2'] += ykrFeature['tilat_vesi_tco2']
            ykrEmissions[ykrZoneName][year]['tilat_lammitys_tco2'] += ykrFeature['tilat_lammitys_tco2']
            ykrEmissions[ykrZoneName][year]['tilat_jaahdytys_tco2'] += ykrFeature['tilat_jaahdytys_tco2']
            ykrEmissions[ykrZoneName][year]['sum_sahko_tco2'] += ykrFeature['sum_sahko_tco2']
            ykrEmissions[ykrZoneName][year]['sahko_kiinteistot_tco2'] += ykrFeature['sahko_kiinteistot_tco2']
            ykrEmissions[ykrZoneName][year]['sahko_kotitaloudet_tco2'] += ykrFeature['sahko_kotitaloudet_tco2']
            ykrEmissions[ykrZoneName][year]['sahko_palv_tco2'] += ykrFeature['sahko_palv_tco2']
            ykrEmissions[ykrZoneName][year]['sahko_tv_tco2'] += ykrFeature['sahko_tv_tco2']
            ykrEmissions[ykrZoneName][year]['sum_rakentaminen_tco2'] += ykrFeature['sum_rakentaminen_tco2']
            ykrEmissions[ykrZoneName][year]['rak_korjaussaneeraus_tco2'] += ykrFeature['rak_korjaussaneeraus_tco2']
            ykrEmissions[ykrZoneName][year]['rak_purku_tco2'] += ykrFeature['rak_purku_tco2']
            ykrEmissions[ykrZoneName][year]['rak_uudis_tco2'] += ykrFeature['rak_uudis_tco2']
            # ykrEmissions[ykrZoneName][year]['tco2_per_pop'] += (ykrFeature['sum_yhteensa_tco2'] / ykrFeature['pop']) if ykrFeature['pop'] > 0 else 0
            # ykrEmissions[ykrZoneName][year]['tco2_per_employ'] += (ykrFeature['sum_yhteensa_tco2'] / ykrFeature['employ']) if ykrFeature['employ'] > 0 else 0

        # 3. Create new quickchart.io chart for each each emission type year by year
        # 3.1. Create SQL query that adds new column for each emission type
        # sql = 'ALTER TABLE ' + outputSchemaName + '.' + outputTableName + ' ADD COLUMN IF NOT EXISTS '
        # for emissionType in ykrEmissions[ykrZoneName][year]:
        #     sql += 'qc_io_' + emissionType + ' numeric, '
        # sql = sql[:-2] + ';'
        # 3.2. Append SQL query to queries list
        # queries.append(sql)
        # 3.3. Create SQL query that creates quickchart.io chart separately for each emission type year by year
        for ykrZoneName in ykrEmissions:
            for year in ykrEmissions[ykrZoneName]:
                sql = 'INSERT INTO ' + outputSchemaName + '.' + outputTableName + ' (sid, zone_name, year, pop, employ, floorspace, sum_yhteensa_tco2, sum_liikenne_tco2, liikenne_hlo_tco2, liikenne_tv_tco2, liikenne_palv_tco2, sum_lammonsaato_tco2, tilat_vesi_tco2, tilat_lammitys_tco2, tilat_jaahdytys_tco2, sum_sahko_tco2, sahko_kiinteistot_tco2, sahko_kotitaloudet_tco2, sahko_palv_tco2, sahko_tv_tco2, sum_rakentaminen_tco2, rak_korjaussaneeraus_tco2, rak_purku_tco2, rak_uudis_tco2) VALUES (' + uuid + ", '" + ykrZoneName + "', " + str(year) + ', '
                for emissionType in ykrEmissions[ykrZoneName][year]:
                    sql += str(ykrEmissions[ykrZoneName][year][emissionType]) + ', '
                sql = sql[:-2] + ');'
                queries.append(sql)
        # 3.4. Log SQL queries to QGIS log
        for sql in queries:
            QgsMessageLog.logMessage(sql, 'YKRTool', Qgis.Info)

        # 4. Return queries list
        return queries
    

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