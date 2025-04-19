
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


class ARAEnergyRegistry:
    def __init__(self, ykrToolDictionaries, plugin_dir, iface):
        self.ykrToolDictionaries = ykrToolDictionaries
        self.plugin_dir = plugin_dir
        self.iface = iface

        self.connectionSettingsDialog = uic.loadUi(os.path.join(self.plugin_dir, 'ui', 'ykr_tool_ara_energy_registry_connection.ui'))

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

        url = "https://kartat.tampere.fi/energiatodistusrekisteri/henktietoja.geojson"
        qurl = QUrl(url)
        qurl.setUserName(username)
        qurl.setPassword(password)
        request = QtNetwork.QNetworkRequest(qurl)

        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(request)    


    def handleResponse(self, reply):

        QgsMessageLog.logMessage("handleResponse start" , 'YKRTool', Qgis.Info)

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
            layer = QgsVectorLayer('Point?crs=EPSG:4326', "tre_energiatodistukset_henktietoja_sis", 'memory')

            feature = geojson["features"][0]
            # QgsMessageLog.logMessage(json.dumps(feature), 'YKRTool', Qgis.Info)
            # QgsMessageLog.logMessage("\n\n\ntest" , 'YKRTool', Qgis.Info)
            fields = QgsFields()
            for key, value in feature['properties'].items():
                if key == 'Korvattu-energiatodistus-id' or key == 'Korvaava-energiatodistus-id' or key == 'Perustiedot / Kieli' or key == 'Perustiedot / Laatimisvaihe' or key == 'Tulokset / E-luokka-rajat / Raja-uusi-2018' or key == 'Lahtotiedot / Lammitetty-nettoala' or key == 'Lahtotiedot / Rakennusvaippa / Ilmanvuotoluku' or key == 'Lahtotiedot / Rakennusvaippa / Lampokapasiteetti' or key == 'Lahtotiedot / Rakennusvaippa / Ilmatilavuus' or key == 'Lahtotiedot / Rakennusvaippa / Ulkoseinat / Ala' or key == 'Lahtotiedot / Rakennusvaippa / Ulkoseinat / U' or key == 'Lahtotiedot / Rakennusvaippa / Ylapohja / Ala' or key == 'Lahtotiedot / Rakennusvaippa / Ylapohja / U' or key == 'Lahtotiedot / Rakennusvaippa / Alapohja / Ala' or key == 'Lahtotiedot / Rakennusvaippa / Alapohja / U' or key == 'Lahtotiedot / Rakennusvaippa / Ikkunat / Ala' or key == 'Lahtotiedot / Rakennusvaippa / Ikkunat / U' or key == 'Lahtotiedot / Rakennusvaippa / Ulkoovet / Ala' or key == 'Lahtotiedot / Rakennusvaippa / Ulkoovet / U' or key == 'Lahtotiedot / Rakennusvaippa / Kylmasillat-ua' or key == 'Lahtotiedot / Rakennusvaippa / Kylmasillat-osuus-lampohaviosta' or key == 'Lahtotiedot / Rakennusvaippa / Ua-summa' or key == 'Lahtotiedot / Ikkunat / Pohjoinen / Ala' or key == 'Lahtotiedot / Ikkunat / Pohjoinen / U' or key == 'Lahtotiedot / Ikkunat / Pohjoinen / G-ks' or key == 'Lahtotiedot / Ikkunat / Koillinen / Ala' or key == 'Lahtotiedot / Ikkunat / Koillinen / U' or key == 'Lahtotiedot / Ikkunat / Koillinen / G-ks' or key == 'Lahtotiedot / Ikkunat / Ita / Ala' or key == 'Lahtotiedot / Ikkunat / Ita / U' or key == 'Lahtotiedot / Ikkunat / Ita / G-ks' or key == 'Lahtotiedot / Ikkunat / Kaakko / Ala' or key == 'Lahtotiedot / Ikkunat / Kaakko / U' or key == 'Lahtotiedot / Ikkunat / Kaakko / G-ks' or key == 'Lahtotiedot / Ikkunat / Etela / Ala' or key == 'Lahtotiedot / Ikkunat / Etela / U' or key == 'Lahtotiedot / Ikkunat / Etela / G-ks' or key == 'Lahtotiedot / Ikkunat / Lounas / Ala' or key == 'Lahtotiedot / Ikkunat / Lounas / U' or key == 'Lahtotiedot / Ikkunat / Lounas / G-ks' or key == 'Lahtotiedot / Ikkunat / Lansi / Ala' or key == 'Lahtotiedot / Ikkunat / Lansi / U' or key == 'Lahtotiedot / Ikkunat / Lansi / G-ks' or key == 'Lahtotiedot / Ikkunat / Luode / Ala' or key == 'Lahtotiedot / Ikkunat / Luode / U' or key == 'Lahtotiedot / Ikkunat / Luode / G-ks' or key == 'Lahtotiedot / Ikkunat / Valokupu / Ala' or key == 'Lahtotiedot / Ikkunat / Valokupu / U' or key == 'Lahtotiedot / Ikkunat / Valokupu / G-ks' or key == 'Lahtotiedot / Ikkunat / Katto / Ala' or key == 'Lahtotiedot / Ikkunat / Katto / U' or key == 'Lahtotiedot / Ikkunat / Katto / G-ks' or key == 'Lahtotiedot / Ilmanvaihto / Paaiv / Tulo' or key == 'Lahtotiedot / Ilmanvaihto / Paaiv / Poisto' or key == 'Lahtotiedot / Ilmanvaihto / Paaiv / Sfp' or key == 'Lahtotiedot / Ilmanvaihto / Paaiv / Lampotilasuhde' or key == 'Lahtotiedot / Ilmanvaihto / Paaiv / Jaatymisenesto' or key == 'Lahtotiedot / Ilmanvaihto / Erillispoistot / Tulo' or key == 'Lahtotiedot / Ilmanvaihto / Erillispoistot / Poisto' or key == 'Lahtotiedot / Ilmanvaihto / Erillispoistot / Sfp' or key == 'Lahtotiedot / Ilmanvaihto / Ivjarjestelma / Tulo' or key == 'Lahtotiedot / Ilmanvaihto / Ivjarjestelma / Poisto' or key == 'Lahtotiedot / Ilmanvaihto / Ivjarjestelma / Sfp' or key == 'Lahtotiedot / Ilmanvaihto / Lto-vuosihyotysuhde' or key == 'Lahtotiedot / Ilmanvaihto / Tuloilma-lampotila' or key == 'Lahtotiedot / Lammitys / Lammitysmuoto-2 / Id' or key == 'Lahtotiedot / Lammitys / Lammonjako / Id' or key == 'Lahtotiedot / Lammitys / Tilat-ja-iv / Tuoton-hyotysuhde' or key == 'Lahtotiedot / Lammitys / Tilat-ja-iv / Jaon-hyotysuhde' or key == 'Lahtotiedot / Lammitys / Tilat-ja-iv / Lampokerroin' or key == 'Lahtotiedot / Lammitys / Tilat-ja-iv / Apulaitteet' or key == 'Lahtotiedot / Lammitys / Tilat-ja-iv / Lampopumppu-tuotto-osuus' or key == 'Lahtotiedot / Lammitys / Tilat-ja-iv / Lampohavio-lammittamaton-tila' or key == 'Lahtotiedot / Lammitys / Lammin-kayttovesi / Tuoton-hyotysuhde' or key == 'Lahtotiedot / Lammitys / Lammin-kayttovesi / Jaon-hyotysuhde' or key == 'Lahtotiedot / Lammitys / Lammin-kayttovesi / Lampokerroin' or key == 'Lahtotiedot / Lammitys / Lammin-kayttovesi / Apulaitteet' or key == 'Lahtotiedot / Lammitys / Lammin-kayttovesi / Lampopumppu-tuotto-osuus' or key == 'Lahtotiedot / Lammitys / Lammin-kayttovesi / Lampohavio-lammittamaton-tila' or key == 'Lahtotiedot / Lammitys / Takka / Maara' or key == 'Lahtotiedot / Lammitys / Takka / Tuotto' or key == 'Lahtotiedot / Lammitys / Ilmalampopumppu / Maara' or key == 'Lahtotiedot / Lammitys / Ilmalampopumppu / Tuotto' or key == 'Lahtotiedot / Jaahdytysjarjestelma / Jaahdytyskauden-painotettu-kylmakerroin' or key == 'Lahtotiedot / Lkvn-kaytto / Ominaiskulutus' or key == 'Lahtotiedot / Lkvn-kaytto / Lammitysenergian-nettotarve' or key == 'Lahtotiedot / Sis-kuorma / Henkilot / Kayttoaste' or key == 'Lahtotiedot / Sis-kuorma / Henkilot / Lampokuorma' or key == 'Lahtotiedot / Sis-kuorma / Kuluttajalaitteet / Kayttoaste' or key == 'Lahtotiedot / Sis-kuorma / Kuluttajalaitteet / Lampokuorma' or key == 'Lahtotiedot / Sis-kuorma / Valaistus / Kayttoaste' or key == 'Lahtotiedot / Sis-kuorma / Valaistus / Lampokuorma' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukolampo' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukolampo-nettoala' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukolampo-kerroin' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukolampo-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukolampo-nettoala-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Sahko' or key == 'Tulokset / Kaytettavat-energiamuodot / Sahko-nettoala' or key == 'Tulokset / Kaytettavat-energiamuodot / Sahko-kerroin' or key == 'Tulokset / Kaytettavat-energiamuodot / Sahko-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Sahko-nettoala-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Uusiutuva-polttoaine' or key == 'Tulokset / Kaytettavat-energiamuodot / Uusiutuva-polttoaine-nettoala' or key == 'Tulokset / Kaytettavat-energiamuodot / Uusiutuva-polttoaine-kerroin' or key == 'Tulokset / Kaytettavat-energiamuodot / Uusiutuva-polttoaine-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Uusiutuva-polttoaine-nettoala-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Fossiilinen-polttoaine' or key == 'Tulokset / Kaytettavat-energiamuodot / Fossiilinen-polttoaine-nettoala' or key == 'Tulokset / Kaytettavat-energiamuodot / Fossiilinen-polttoaine-kerroin' or key == 'Tulokset / Kaytettavat-energiamuodot / Fossiilinen-polttoaine-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Fossiilinen-polttoaine-nettoala-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukojaahdytys' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukojaahdytys-nettoala' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukojaahdytys-kerroin' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukojaahdytys-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Kaukojaahdytys-nettoala-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 0 / Ostoenergia' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 0 / Muotokerroin' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 0 / Ostoenergia-nettoala' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 0 / Ostoenergia-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 0 / Ostoenergia-nettoala-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 1 / Ostoenergia' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 1 / Muotokerroin' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 1 / Ostoenergia-nettoala' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 1 / Ostoenergia-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 1 / Ostoenergia-nettoala-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 2 / Ostoenergia' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 2 / Muotokerroin' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 2 / Ostoenergia-nettoala' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 2 / Ostoenergia-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Muu / 2 / Ostoenergia-nettoala-kertoimella' or key == 'Tulokset / Kaytettavat-energiamuodot / Summa' or key == 'Tulokset / Kaytettavat-energiamuodot / Kertoimella-summa' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Aurinkosahko' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Aurinkosahko-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Aurinkolampo' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Aurinkolampo-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Tuulisahko' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Tuulisahko-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Lampopumppu' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Lampopumppu-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Muusahko' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Muusahko-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Muulampo' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / Muulampo-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 0 / Vuosikulutus' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 0 / Vuosikulutus-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 1 / Vuosikulutus' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 1 / Vuosikulutus-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 2 / Vuosikulutus' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 2 / Vuosikulutus-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 3 / Vuosikulutus' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 3 / Vuosikulutus-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 4 / Vuosikulutus' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 4 / Vuosikulutus-nettoala' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 5 / Vuosikulutus' or key == 'Tulokset / Uusiutuvat-omavaraisenergiat / 5 / Vuosikulutus-nettoala' or key == 'Tulokset / Tekniset-jarjestelmat / Tilojen-lammitys / Sahko' or key == 'Tulokset / Tekniset-jarjestelmat / Tilojen-lammitys / Lampo' or key == 'Tulokset / Tekniset-jarjestelmat / Tuloilman-lammitys / Sahko' or key == 'Tulokset / Tekniset-jarjestelmat / Tuloilman-lammitys / Lampo' or key == 'Tulokset / Tekniset-jarjestelmat / Kayttoveden-valmistus / Sahko' or key == 'Tulokset / Tekniset-jarjestelmat / Kayttoveden-valmistus / Lampo' or key == 'Tulokset / Tekniset-jarjestelmat / Iv-sahko' or key == 'Tulokset / Tekniset-jarjestelmat / Jaahdytys / Sahko' or key == 'Tulokset / Tekniset-jarjestelmat / Jaahdytys / Lampo' or key == 'Tulokset / Tekniset-jarjestelmat / Jaahdytys / Kaukojaahdytys' or key == 'Tulokset / Tekniset-jarjestelmat / Kuluttajalaitteet-ja-valaistus-sahko' or key == 'Tulokset / Tekniset-jarjestelmat / Sahko-summa' or key == 'Tulokset / Tekniset-jarjestelmat / Lampo-summa' or key == 'Tulokset / Tekniset-jarjestelmat / Kaukojaahdytys-summa' or key == 'Tulokset / Nettotarve / Tilojen-lammitys-vuosikulutus' or key == 'Tulokset / Nettotarve / Tilojen-lammitys-vuosikulutus-nettoala' or key == 'Tulokset / Nettotarve / Ilmanvaihdon-lammitys-vuosikulutus' or key == 'Tulokset / Nettotarve / Ilmanvaihdon-lammitys-vuosikulutus-nettoala' or key == 'Tulokset / Nettotarve / Kayttoveden-valmistus-vuosikulutus' or key == 'Tulokset / Nettotarve / Kayttoveden-valmistus-vuosikulutus-nettoala' or key == 'Tulokset / Nettotarve / Jaahdytys-vuosikulutus' or key == 'Tulokset / Nettotarve / Jaahdytys-vuosikulutus-nettoala' or key == 'Tulokset / Lampokuormat / Aurinko' or key == 'Tulokset / Lampokuormat / Aurinko-nettoala' or key == 'Tulokset / Lampokuormat / Ihmiset' or key == 'Tulokset / Lampokuormat / Ihmiset-nettoala' or key == 'Tulokset / Lampokuormat / Kuluttajalaitteet' or key == 'Tulokset / Lampokuormat / Kuluttajalaitteet-nettoala' or key == 'Tulokset / Lampokuormat / Valaistus' or key == 'Tulokset / Lampokuormat / Valaistus-nettoala' or key == 'Tulokset / Lampokuormat / Kvesi' or key == 'Tulokset / Lampokuormat / Kvesi-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kaukolampo-vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kaukolampo-vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kokonaissahko-vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kokonaissahko-vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kiinteistosahko-vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kiinteistosahko-vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kayttajasahko-vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kayttajasahko-vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kaukojaahdytys-vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Kaukojaahdytys-vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 0 / Vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 0 / Vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 1 / Vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 1 / Vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 2 / Vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 2 / Vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 3 / Vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 3 / Vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 4 / Vuosikulutus' or key == 'Toteutunut-ostoenergiankulutus / Ostettu-energia / Muu / 4 / Vuosikulutus-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Kevyt-polttooljy' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Kevyt-polttooljy-kerroin' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Kevyt-polttooljy-kwh' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Kevyt-polttooljy-kwh-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Pilkkeet-havu-sekapuu' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Pilkkeet-havu-sekapuu-kerroin' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Pilkkeet-havu-sekapuu-kwh' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Pilkkeet-havu-sekapuu-kwh-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Pilkkeet-koivu' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Pilkkeet-koivu-kerroin' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Pilkkeet-koivu-kwh' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Pilkkeet-koivu-kwh-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Puupelletit' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Puupelletit-kerroin' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Puupelletit-kwh' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Puupelletit-kwh-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 0 / Maara-vuodessa' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 0 / Muunnoskerroin' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 0 / Kwh' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 0 / Kwh-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 1 / Maara-vuodessa' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 1 / Muunnoskerroin' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 1 / Kwh' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 1 / Kwh-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 2 / Maara-vuodessa' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 2 / Muunnoskerroin' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 2 / Kwh' or key == 'Toteutunut-ostoenergiankulutus / Ostetut-polttoaineet / Muu / 2 / Kwh-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Sahko-vuosikulutus-yhteensa' or key == 'Toteutunut-ostoenergiankulutus / Sahko-vuosikulutus-yhteensa-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Kaukolampo-vuosikulutus-yhteensa' or key == 'Toteutunut-ostoenergiankulutus / Kaukolampo-vuosikulutus-yhteensa-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Polttoaineet-vuosikulutus-yhteensa' or key == 'Toteutunut-ostoenergiankulutus / Polttoaineet-vuosikulutus-yhteensa-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Kaukojaahdytys-vuosikulutus-yhteensa' or key == 'Toteutunut-ostoenergiankulutus / Kaukojaahdytys-vuosikulutus-yhteensa-nettoala' or key == 'Toteutunut-ostoenergiankulutus / Summa' or key == 'Toteutunut-ostoenergiankulutus / Summa-nettoala' or key == 'Huomiot / Ymparys / Toimenpide / 0 / Lampo' or key == 'Huomiot / Ymparys / Toimenpide / 0 / Sahko' or key == 'Huomiot / Ymparys / Toimenpide / 0 / Jaahdytys' or key == 'Huomiot / Ymparys / Toimenpide / 0 / Eluvun-muutos' or key == 'Huomiot / Ymparys / Toimenpide / 1 / Lampo' or key == 'Huomiot / Ymparys / Toimenpide / 1 / Sahko' or key == 'Huomiot / Ymparys / Toimenpide / 1 / Jaahdytys' or key == 'Huomiot / Ymparys / Toimenpide / 1 / Eluvun-muutos' or key == 'Huomiot / Ymparys / Toimenpide / 2 / Lampo' or key == 'Huomiot / Ymparys / Toimenpide / 2 / Sahko' or key == 'Huomiot / Ymparys / Toimenpide / 2 / Jaahdytys' or key == 'Huomiot / Ymparys / Toimenpide / 2 / Eluvun-muutos' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 0 / Lampo' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 0 / Sahko' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 0 / Jaahdytys' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 0 / Eluvun-muutos' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 1 / Lampo' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 1 / Sahko' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 1 / Jaahdytys' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 1 / Eluvun-muutos' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 2 / Lampo' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 2 / Sahko' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 2 / Jaahdytys' or key == 'Huomiot / Alapohja-ylapohja / Toimenpide / 2 / Eluvun-muutos' or key == 'Huomiot / Lammitys / Toimenpide / 0 / Lampo' or key == 'Huomiot / Lammitys / Toimenpide / 0 / Sahko' or key == 'Huomiot / Lammitys / Toimenpide / 0 / Jaahdytys' or key == 'Huomiot / Lammitys / Toimenpide / 0 / Eluvun-muutos' or key == 'Huomiot / Lammitys / Toimenpide / 1 / Lampo' or key == 'Huomiot / Lammitys / Toimenpide / 1 / Sahko' or key == 'Huomiot / Lammitys / Toimenpide / 1 / Jaahdytys' or key == 'Huomiot / Lammitys / Toimenpide / 1 / Eluvun-muutos' or key == 'Huomiot / Lammitys / Toimenpide / 2 / Lampo' or key == 'Huomiot / Lammitys / Toimenpide / 2 / Sahko' or key == 'Huomiot / Lammitys / Toimenpide / 2 / Jaahdytys' or key == 'Huomiot / Lammitys / Toimenpide / 2 / Eluvun-muutos' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 0 / Lampo' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 0 / Sahko' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 0 / Jaahdytys' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 0 / Eluvun-muutos' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 1 / Lampo' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 1 / Sahko' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 1 / Jaahdytys' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 1 / Eluvun-muutos' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 2 / Lampo' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 2 / Sahko' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 2 / Jaahdytys' or key == 'Huomiot / Iv-ilmastointi / Toimenpide / 2 / Eluvun-muutos' or key == 'Huomiot / Valaistus-muut / Toimenpide / 0 / Lampo' or key == 'Huomiot / Valaistus-muut / Toimenpide / 0 / Sahko' or key == 'Huomiot / Valaistus-muut / Toimenpide / 0 / Jaahdytys' or key == 'Huomiot / Valaistus-muut / Toimenpide / 0 / Eluvun-muutos' or key == 'Huomiot / Valaistus-muut / Toimenpide / 1 / Lampo' or key == 'Huomiot / Valaistus-muut / Toimenpide / 1 / Sahko' or key == 'Huomiot / Valaistus-muut / Toimenpide / 1 / Jaahdytys' or key == 'Huomiot / Valaistus-muut / Toimenpide / 1 / Eluvun-muutos' or key == 'Huomiot / Valaistus-muut / Toimenpide / 2 / Lampo' or key == 'Huomiot / Valaistus-muut / Toimenpide / 2 / Sahko' or key == 'Huomiot / Valaistus-muut / Toimenpide / 2 / Jaahdytys' or key == 'Huomiot / Valaistus-muut / Toimenpide / 2 / Eluvun-muutos' or key == 'geocoding_confidence':
                    field = QgsField(key, QVariant.Double)
                # elif key == 'organisaatio_id' or key == 'id':
                #     field = QgsField(key, QVariant.Int)
                elif key == 'Id' or key == 'Versio' or key == 'Tila-id' or key == 'Laatija-id' or key == 'Perustiedot / Valmistumisvuosi' or key == 'Tulokset / E-luku' or key == 'Lahtotiedot / Ilmanvaihto / Tyyppi-id' or key == 'Lahtotiedot / Lammitys / Lammitysmuoto-1 / Id':
                    field = QgsField(key, QVariant.LongLong)
                # elif key == 'paivitetty':
                #     field = QgsField(key, QVariant.DateTime)
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
            # QgsMessageLog.logMessage("handleResponse Error" , 'YKRTool', Qgis.Info)
            # print("Error occured: ", er)
            # print(reply.errorString())