from PyQt5 import uic, QtNetwork
from PyQt5.QtCore import QCoreApplication, QEventLoop, QUrl

from qgis.core import (QgsTask, QgsMessageLog, Qgis, QgsVectorLayer, QgsProject)

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
            link_parts = link_text.split('?')
            base_url = link_parts[0].split('/raportti')
            ids = link_parts[1].split(',')

            request = QtNetwork.QNetworkRequest(QUrl(link_text))
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
                    self.iface.messageBar().pushMessage(self.tr('Success downloading data'), cmDialog.windowTitle(), Qgis.Info, duration=3)
                    # QgsMessageLog.logMessage('responseData: ' + responseData[:5], 'Carbon Map (YKRTool)', Qgis.Info)

                    save_path = cmDialog.mQgsFileWidgetDataLocation.filePath()

                    completeNameTotals, completeNameAreas = self.saveReportData(responseData, save_path)
                    self.addMapLayers(responseData, completeNameTotals, completeNameAreas)
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
        # print(completeName + " saved")
        file1 = open(completeNameTotals, "wt")
        file1.write(json.dumps(layerData))
        file1.close()

        layerData = data["report_data"]["areas"]
        file_name = data["name"] + "_areas_" + data["id"]

        completeNameAreas = os.path.join(save_path, file_name + ".geojson")
        # print(completeName + " saved")
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

        layer_name = data["name"] + " - areas (" + data["id"] + ")"
        # layer = QgsVectorLayer(json.dumps(layerData), layer_name, 'memory')
        layer = QgsVectorLayer(completeNameAreas, layer_name,"ogr")

        QgsProject.instance().addMapLayer(layer, False)
        rootGroup.addLayer(layer)

        # for name in layerNames:
            #     layer = QgsVectorLayer(uri.uri(False), name[0], 'postgres')
            # layer.loadNamedStyle(name[1])
            # renderer = layer.renderer()
            # if renderer.type() == 'graduatedSymbol':
            #     renderer.updateClasses(layer, renderer.mode(), len(renderer.ranges()))
            # self.resultLayers.append(layer)
            