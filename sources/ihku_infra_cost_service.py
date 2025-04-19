
# from http.client import HTTPSConnection
from base64 import b64encode
import os.path
import json

from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication, QEventLoop, QUrl, QSettings, QVariant, QUrl, QByteArray
from PyQt5 import QtNetwork

from qgis.core import (Qgis, QgsVectorLayer, QgsCoordinateReferenceSystem,
    QgsApplication, QgsDataSourceUri, QgsProject, QgsTaskManager,
    QgsProcessingAlgRunnerTask, QgsProcessingContext, QgsProcessingFeedback, QgsMessageLog,
    QgsExpression, QgsFeatureRequest,
    QgsFeature, QgsField, QgsFields, QgsGeometry, QgsJsonUtils)


class IhkuInfraCostService:
    def __init__(self, ykrToolDictionaries, plugin_dir, iface):
        self.ykrToolDictionaries = ykrToolDictionaries
        self.plugin_dir = plugin_dir
        self.iface = iface

        self.connectionSettingsDialog = uic.loadUi(os.path.join(self.plugin_dir, 'ui', 'ykr_tool_ihku_cost_service_connection.ui'))


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


    # https://stackoverflow.com/a/7000784/929516
    def basic_auth(self, username, password):
        token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
        return f'Basic {token}'


    def importData(self):
        self.connectionSettingsDialog.show()
        result = self.connectionSettingsDialog.exec_()
        if result:
            username = self.connectionSettingsDialog.connectionUser.value()
            password = self.connectionSettingsDialog.connectionPass.text()
        else:
            return

        #This sets up the https connection
        QgsMessageLog.logMessage("got user" , 'YKRTool', Qgis.Info)

        url = "https://kartat.tampere.fi/kaavatalous/ihku_hankkeet_tilasto_yms_alueilla.geojson"
        qurl = QUrl(url)
        qurl.setUserName(username)
        qurl.setPassword(password)
        request = QtNetwork.QNetworkRequest(qurl)

        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(request)    


    def handleResponse(self, reply):

        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:

            bytes_string = reply.readAll()

            QgsMessageLog.logMessage("handleResponse NoError" , 'YKRTool', Qgis.Info)

            resultString = str(bytes_string, 'utf-8')

            # QgsMessageLog.logMessage(resultString, 'YKRTool', Qgis.Info)
            # QgsMessageLog.logMessage(json.dumps(str(bytes_string)) , 'YKRTool', Qgis.Info)

            # QgsMessageLog.logMessage("\n\n\ntest" , 'YKRTool', Qgis.Info)

            geojson = json.loads(resultString)

            # QgsMessageLog.logMessage(json.dumps(geojson), 'YKRTool', Qgis.Info)
            # QgsMessageLog.logMessage("\n\n\ntest" , 'YKRTool', Qgis.Info)

            # https://gis.stackexchange.com/q/474498/52577
            layer = QgsVectorLayer('Point?crs=EPSG:4326', "ihku_hankkeet_tilasto_yms_alueilla", 'memory')

            feature = geojson["features"][0]
            # QgsMessageLog.logMessage(json.dumps(feature), 'YKRTool', Qgis.Info)
            # QgsMessageLog.logMessage("\n\n\ntest" , 'YKRTool', Qgis.Info)
            fields = QgsFields()
            for key, value in feature['properties'].items():
                if key == 'paasto' or key == 'varaukset_prosentti' or key == 'omistajatehtavat_prosentti' or key == 'rakennuttamistehtavat_prosentti' or key == 'rakennussuunnittelu_prosentti' or key == 'viranomaisen_vaatima_prosentti' or key == 'tyomaatehtavat_prosentti' or key == 'rakennusaikainen_prosentti' or key == 'maku_pisteluku' or key == 'hinta' or key == 'yleissuunnittelu_prosentti' or key == 'lon' or key == 'lat':
                    field = QgsField(key, QVariant.Double)
                elif key == 'organisaatio_id' or key == 'id':
                    field = QgsField(key, QVariant.Int)
                elif key == 'paivitetty':
                    field = QgsField(key, QVariant.DateTime)
                elif key == 'fid':
                    pass
                else:
                    field = QgsField(key, QVariant.String)

                if key != 'fid':
                    fields.append(field)

            layer.dataProvider().addAttributes(fields)
            layer.updateFields()

            for feature in geojson["features"]:
                x = feature['geometry']['coordinates'][0]
                y = feature['geometry']['coordinates'][1]
                # geometry = QgsJsonUtils.geometryFromGeoJson(json.dumps(feature['geometry']))
                geometry = QgsGeometry.fromWkt('POINT (' + str(x) + ' ' + str(y) + ')')
                new_feature = QgsFeature()
                new_feature.setGeometry(geometry)
                new_feature.setFields(fields)

                for key, value in feature['properties'].items():
                    if key != 'fid':
                        new_feature.setAttribute(key, value)

                layer.dataProvider().addFeature(new_feature)
            

            QgsProject.instance().addMapLayer(layer, True)

        else:
            QgsMessageLog.logMessage("handleResponse Error: " + reply.errorString(), 'YKRTool', Qgis.Error)
            # print("Error occured: ", er)
            # print(reply.errorString())