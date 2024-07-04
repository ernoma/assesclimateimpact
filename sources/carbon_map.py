from PyQt5 import uic, QtNetwork
from PyQt5.QtCore import QCoreApplication, QEventLoop, QUrl, QSettings, QVariant

from qgis.core import (QgsTask, QgsMessageLog, Qgis, QgsVectorLayer, QgsProject, QgsField)

import os.path
import json

class CarbonMap:
    def __init__(self, ykrToolDictionaries, plugin_dir, iface):
        self.ykrToolDictionaries = ykrToolDictionaries
        self.plugin_dir = plugin_dir
        self.iface = iface
        
        self.carbonMapDataDownloadDialog = uic.loadUi(os.path.join(self.plugin_dir, 'ui', 'ykr_tool_carbon_map_report_data_download.ui'))

        self.nManager = QtNetwork.QNetworkAccessManager()


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
    

    def downloadCarbonMapResults(self):
        """User has chosen to download Carbon Map results"""

        save_path = QSettings().value("/YKRTool/CarbonMapDataFilePath", "", type=str)
        if save_path != "":
            self.carbonMapDataDownloadDialog.mQgsFileWidgetDataLocation.setFilePath(save_path)

        self.carbonMapDataDownloadDialog.show()
        # Run the dialog event loop
        result = self.carbonMapDataDownloadDialog.exec_()
        # See if OK was pressed
        if result:
            self.downloadData()


    def downloadData(self):
        cmDialog = self.carbonMapDataDownloadDialog
        link_text = cmDialog.lineEditCarbonMapReportURL.text()
        if link_text == '':
            self.iface.messageBar().pushMessage(self.tr('Link to report was not provided'), cmDialog.windowTitle(), Qgis.Info, duration=3)
        else:
            link_parts = link_text.split('?id=')
            base_url = link_parts[0].split('/raportti')[0]
            ids = link_parts[1].split(',')
            # http://localhost:3000/raportti?id=9f3e609d-3c8c-40bd-a2af-47e617ffc21a,9f3e609d-3c8c-40bd-a2af-47e617ffc21b

            for id in ids:
                url = base_url + "/" + "api/report?id=" + id
                QgsMessageLog.logMessage('url: ' + url, 'Carbon Map (YKRTool)', Qgis.Info)

                request = QtNetwork.QNetworkRequest(QUrl(url))
                # userAgent = b'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
                userAgent = b'Urban Structure Climate Impact Assessment Tool (USCIAT)'
                request.setRawHeader(b'User-Agent', userAgent)
                reply = self.nManager.get(request) # QNetworkReply
                reply.deleteLater()
                loop = QEventLoop()
                reply.finished.connect(loop.quit)
                loop.exec_()
                bytes_string = reply.readAll()

                if reply.error() == QtNetwork.QNetworkReply.NoError:

                    # contentTypeHeader = reply.header(QtNetwork.QNetworkRequest.ContentTypeHeader)
                    # if isinstance(contentTypeHeader, str):
                    #     QgsMessageLog.logMessage('Header: ' + contentTypeHeader, 'Carbon Map (YKRTool)', Qgis.Info)

                    # responseData = str(bytes_string, 'utf-8')
                    if not bytes_string.isEmpty():
                        responseData = bytes(bytes_string).decode("utf-8")
                        # self.iface.messageBar().pushMessage(self.tr('Success downloading data'), cmDialog.windowTitle(), Qgis.Info, duration=1)
                        # QgsMessageLog.logMessage('responseData: ' + responseData[:5], 'Carbon Map (YKRTool)', Qgis.Info)

                        save_path = cmDialog.mQgsFileWidgetDataLocation.filePath()
                        if save_path != "":
                            QSettings().setValue("/YKRTool/CarbonMapDataFilePath", save_path)

                        completeNameTotals, completeNameAreas = self.saveReportData(responseData, save_path)
                        self.addMapLayers(responseData, completeNameTotals, completeNameAreas)

                        complexResponseData = self.processDataToComplexFeatures(responseData)
                        self.saveReportDataWithYearAttributeFeatures(complexResponseData, save_path)

                    else:
                        self.iface.messageBar().pushMessage(self.tr('The response data was empty'), cmDialog.windowTitle(), Qgis.Warning)
                else:
                    self.iface.messageBar().pushMessage(self.tr('Error downloading data'), cmDialog.windowTitle(), Qgis.Warning)
            

    def saveReportData(self, responseData, save_path):
        # TODO Create map layers of the responseData GeoJSON and add them to the project
        data = json.loads(responseData)


        layerData = data["report_data"]["totals"]
        file_name = data["name"] + "_totals_" + data["id"]

        completeNameTotals = os.path.join(save_path, file_name + ".geojson")
        index = 0

        while os.path.exists(completeNameTotals):
            index += 1
            completeNameTotals = os.path.join(save_path, file_name + " (" + str(index) + ").geojson")

        file1 = open(completeNameTotals, "wt")
        file1.write(json.dumps(layerData))
        file1.close()


        layerData = data["report_data"]["areas"]
        file_name = data["name"] + "_areas_" + data["id"]

        completeNameAreas = os.path.join(save_path, file_name + ".geojson")
        index = 0

        while os.path.exists(completeNameAreas):
            index += 1
            completeNameAreas = os.path.join(save_path, file_name + " (" + str(index) + ").geojson")

        file1 = open(completeNameAreas, "wt")
        file1.write(json.dumps(layerData))
        file1.close()

        return completeNameTotals, completeNameAreas


    def addMapLayers(self, responseData, completeNameTotals, completeNameAreas):

        data = json.loads(responseData)

        groupName = self.tr("Carbon Map") + " {}".format(data["name"] + " (" + data["id"] + ")")
        rootGroup = self.iface.layerTreeView().currentGroupNode()
        if rootGroup != None:
            rootGroup = rootGroup.addGroup(groupName) # ret QgsLayerTreeGroup 
        else:
            root = QgsProject.instance().layerTreeRoot()
            rootGroup = root.insertGroup(0, groupName)


        layer_name = data["name"] + " - totals (" + data["id"] + ")"
        # layer = QgsVectorLayer(json.dumps(layerData), layer_name, 'memory')
        layer = QgsVectorLayer(completeNameTotals, layer_name,"ogr")

        QgsProject.instance().addMapLayer(layer, False)
        rootGroup.addLayer(layer)

        ##
        ## Areas
        ##
        
        # Calculate carbon stock CO2-eq/ha and total change value for each plan area from year 2024 to year 2030 and visualization for the areas layer based on the value

        layer_name = data["name"] + " - areas (CO2-eq change 2024-2030, " + data["id"] + ")"
        # layer = QgsVectorLayer(json.dumps(layerData), layer_name, 'memory')
        layer_area_total = QgsVectorLayer(completeNameAreas, layer_name,"ogr")

        QgsProject.instance().addMapLayer(layer_area_total, False)
        rootGroup.addLayer(layer_area_total)
    
        symbology_path = os.path.join(self.plugin_dir, 'docs', 'carbon_map', 'carbon_total_change.qml')
        layer_area_total.loadNamedStyle(symbology_path)
        field = QgsField('carbon_total_planned_2024', QVariant.Double)
        layer_area_total.addExpressionField(' ("ground_carbon_total_planned_2024" + "bio_carbon_total_planned_2024") ', field)
        field = QgsField('carbon_total_planned_2030', QVariant.Double)
        layer_area_total.addExpressionField(' ("ground_carbon_total_planned_2030" + "bio_carbon_total_planned_2030") ', field)
        field = QgsField('carbon_total_change_planned_2024_2030', QVariant.Double)
        layer_area_total.addExpressionField(' ("ground_carbon_total_planned_2030" + "bio_carbon_total_planned_2030") - ("ground_carbon_total_planned_2024" + "bio_carbon_total_planned_2024")', field)
        layer_area_total.triggerRepaint()  


        layer_name = data["name"] + " - areas (CO2-eq/ha change 2024-2030, " + data["id"] + ")"
        # layer = QgsVectorLayer(json.dumps(layerData), layer_name, 'memory')
        layer_area_ha = QgsVectorLayer(completeNameAreas, layer_name,"ogr")

        QgsProject.instance().addMapLayer(layer_area_ha, False)
        rootGroup.addLayer(layer_area_ha)

        symbology_path = os.path.join(self.plugin_dir, 'docs', 'carbon_map', 'carbon_ha_change.qml')
        layer_area_ha.loadNamedStyle(symbology_path)
        field = QgsField('carbon_ha_planned_2024', QVariant.Double)
        layer_area_ha.addExpressionField(' ("ground_carbon_ha_planned_2024" + "bio_carbon_ha_planned_2024") ', field)
        field = QgsField('carbon_ha_planned_2030', QVariant.Double)
        layer_area_ha.addExpressionField(' ("ground_carbon_ha_planned_2030" + "bio_carbon_ha_planned_2030") ', field)
        field = QgsField('carbon_ha_change_planned_2024_2030', QVariant.Double)
        layer_area_ha.addExpressionField(' ("ground_carbon_ha_planned_2030" + "bio_carbon_ha_planned_2030") - ("ground_carbon_ha_planned_2024" + "bio_carbon_ha_planned_2024") ', field)
        layer_area_ha.triggerRepaint()  

        # for name in layerNames:
            #     layer = QgsVectorLayer(uri.uri(False), name[0], 'postgres')
            # layer.loadNamedStyle(name[1])
            # renderer = layer.renderer()
            # if renderer.type() == 'graduatedSymbol':
            #     renderer.updateClasses(layer, renderer.mode(), len(renderer.ranges()))
            # self.resultLayers.append(layer)
            


    def processDataToComplexFeatures(self, responseData):
        
        data = json.loads(responseData)

        comlexData = {
            "id": data["id"],
            "name": data["name"],
            "reportData": {
                "areas": {
                    "type": "FeatureCollection",
                    "features": []
                },
                "totals": {
                    "type": "FeatureCollection",
                    "features": []
                }
            }
        }

        for feature in data["report_data"]["areas"]["features"]:

            newFeature = {
                "id": feature["id"],
                "type": feature["type"],
                "geometry": feature["geometry"],
                "properties": {
                    "bio_carbon_total": {
                        "nochange": {},
                        "planned": {}
                    },
                    "ground_carbon_total": {
                        "nochange": {},
                        "planned": {}
                    },
                    "bio_carbon_ha": {
                        "nochange": {},
                        "planned": {}
                    },
                    "ground_carbon_ha": {
                        "nochange": {},
                        "planned": {}
                    }
                }
            }

            for key in feature['properties'].keys():
                value = feature['properties'][key]
                if "_nochange_" in key:
                    parts = key.split('_nochange_')
                    newFeature["properties"][parts[0]]["nochange"][parts[1]] = value
                elif "_planned_" in key:
                    parts = key.split('_planned_')
                    newFeature["properties"][parts[0]]["planned"][parts[1]] = value
                else:
                    newFeature["properties"][key] = value
                    if key != "area" and key != "zoning_code":
                        QgsMessageLog.logMessage('Unknown feature property type: ' + key, 'Carbon Map (YKRTool)', Qgis.Info)

            comlexData["reportData"]["areas"]["features"].append(newFeature)


        for feature in data["report_data"]["totals"]["features"]:

            newFeature = {
                "id": feature["id"],
                "type": feature["type"],
                "geometry": feature["geometry"],
                "properties": {
                    "bio_carbon_total": {
                        "nochange": {},
                        "planned": {}
                    },
                    "ground_carbon_total": {
                        "nochange": {},
                        "planned": {}
                    },
                    "bio_carbon_ha": {
                        "nochange": {},
                        "planned": {}
                    },
                    "ground_carbon_ha": {
                        "nochange": {},
                        "planned": {}
                    }
                }
            }

            for key in feature['properties'].keys():
                value = feature['properties'][key]
                if "_nochange_" in key:
                    parts = key.split('_nochange_')
                    newFeature["properties"][parts[0]]["nochange"][parts[1]] = value
                elif "_planned_" in key:
                    parts = key.split('_planned_')
                    newFeature["properties"][parts[0]]["planned"][parts[1]] = value
                else:
                    newFeature["properties"][key] = value
                    if key != "area" and key != "zoning_code":
                        QgsMessageLog.logMessage('Unknown feature property type: ' + key, 'Carbon Map (YKRTool)', Qgis.Info)

            comlexData["reportData"]["totals"]["features"].append(newFeature)


        # QgsMessageLog.logMessage(str(comlexData), 'Carbon Map (YKRTool)', Qgis.Info)

        return comlexData
    
    
    def saveReportDataWithYearAttributeFeatures(self, complexResponseData, save_path):


        origFeatures = complexResponseData["reportData"]["totals"]["features"]

        layerData = {
            "type": "FeatureCollection",
            "features": []
        }

        for feature in origFeatures:
            years = feature["properties"]["bio_carbon_total"]["nochange"].keys()

            for year in years:
                newFeature = {
                    "id": feature["id"],
                    "type": feature["type"],
                    "geometry": feature["geometry"],
                    "properties": {
                        "year": year,
                        "bio_carbon_total_nochange": None,
                        "bio_carbon_total_planned": None,
                        "ground_carbon_total_nochange": None,
                        "ground_carbon_total_planned": None,
                        "bio_carbon_ha_nochange": None,
                        "bio_carbon_ha_planned": None,
                        "ground_carbon_ha_nochange": None,
                        "ground_carbon_ha_planned": None
                    }
                }
                
                newFeature["properties"]["bio_carbon_total_nochange"] = feature["properties"]["bio_carbon_total"]["nochange"][year]
                newFeature["properties"]["bio_carbon_total_planned"] = feature["properties"]["bio_carbon_total"]["planned"][year]
                newFeature["properties"]["ground_carbon_total_nochange"] = feature["properties"]["ground_carbon_total"]["nochange"][year]
                newFeature["properties"]["ground_carbon_total_planned"] = feature["properties"]["ground_carbon_total"]["planned"][year]
                newFeature["properties"]["bio_carbon_ha_nochange"] = feature["properties"]["bio_carbon_ha"]["nochange"][year]
                newFeature["properties"]["bio_carbon_ha_planned"] = feature["properties"]["bio_carbon_ha"]["planned"][year]
                newFeature["properties"]["ground_carbon_ha_nochange"] = feature["properties"]["ground_carbon_ha"]["nochange"][year]
                newFeature["properties"]["ground_carbon_ha_planned"] = feature["properties"]["ground_carbon_ha"]["planned"][year]

                layerData["features"].append(newFeature)


        file_name = complexResponseData["name"] + "_totals_with_year_" + complexResponseData["id"]
        completeNameTotals = os.path.join(save_path, file_name + ".geojson")
        index = 0
        while os.path.exists(completeNameTotals):
            index += 1
            completeNameTotals = os.path.join(save_path, file_name + " (" + str(index) + ").geojson")
        file1 = open(completeNameTotals, "wt")
        file1.write(json.dumps(layerData))
        file1.close()


        return completeNameTotals