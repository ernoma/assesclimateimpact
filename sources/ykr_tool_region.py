# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication #, QSettings, QTranslator, qVersion, QVariant
# from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox #, QAction

from qgis.core import (Qgis, QgsVectorLayer, QgsMessageLog, 
    QgsApplication, QgsDataSourceUri, QgsProject#,
    # QgsCoordinateReferenceSystem, QgsTaskManager,
    # QgsProcessingAlgRunnerTask, QgsProcessingContext, QgsProcessingFeedback, 
    # QgsExpression, QgsFeatureRequest,
    # QgsFeature, QgsField
    )
# from qgis.gui import QgsFileWidget

# Initialize Qt resources from file resources.py
from ..resources import *
# Import the code for the dialog
# import processing
import uuid
import os.path
import datetime, getpass
import traceback

from .ykr_tool_tasks import QueryTask


class YKRToolRegion:
    """QGIS Plugin Implementation."""

    MAX_TABLE_NAME_LENGTH = 62

    def __init__(self, iface, databaseConnection, ykrToolDictionaries, infoDialog):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        self.databaseConnection = databaseConnection
        self.ykrToolDictionaries = ykrToolDictionaries
        self.infoDialog = infoDialog

        self.NameOfTheCO2EstimationRun = None

        self.plugin_dir = os.path.split(os.path.dirname(__file__))[0]
        self.mainDialog = uic.loadUi(os.path.join(self.plugin_dir, 'ui', 'ykr_tool_main_region.ui'))

        self.futureAreasLayer = None
        self.futureNetworkLayer = None
        self.futureStopsLayer = None
        self.futureZoningAreasTableName = None
        self.futureNetworkLayerDBTableName = None
        self.futureStopsLayerDBTableName = None

        self.calculateFuture = False

        self.inputLayers = []

        self.outputTableName = None

        self.resultLayers = []


    def runCityRegion(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started

        self.setupMainDialog()

        self.mainDialog.show()

        # Run the dialog event loop
        result = self.mainDialog.exec_()
        # See if OK was pressed
        if result:
            self.runProcess()



    def setupMainDialog(self):
        '''Sets up the main dialog'''
        md = self.mainDialog

        md.finished.connect(self.calculationDialogFinished)

        # md.radioButtonUseMapLayerForInvestigatedArea.clicked.connect(self.handleRadioButtonUseMapLayerForInvestigatedAreaToggle)
        # md.radioButtonUsePredefinedAreaForInvestigatedArea.clicked.connect(self.handleRadioButtonUsePredefinedAreaForInvestigatedAreaToggle)

        names = self.ykrToolDictionaries.getPredefinedAreaNames()
        md.comboBoxPredefinedArea.addItems(names)
        predefinedAreaName = self.ykrToolDictionaries.getPredefinedAreaNameFromDatabaseTableName('user_input.seutu_rasu_2040_alue')
        md.comboBoxPredefinedArea.setCurrentText(predefinedAreaName)

        names = self.ykrToolDictionaries.getPITKOScenarioNames()
        md.pitkoScenario.addItems(names)
        md.pitkoScenario.setCurrentText('wemp')

        md.futureBox.setEnabled(False)
        # names = self.ykrToolDictionaries.getPredefinedFutureZoningAreasUserFriendlyNames()
        # md.comboBoxPredefinedFutureAreas.addItems(names)

        # urbanCenterNames = self.ykrToolDictionaries.getPredefinedUrbanCenterLayersUserFriendlyNames()
        # md.comboBoxPredefinedFutureNetwork.addItems(urbanCenterNames)

        # publicTransportStopsNames = self.ykrToolDictionaries.getPredefinedFuturePublicTransportStopsUserFriendlyNames()
        # md.comboBoxPredefinedFutureStops.addItems(publicTransportStopsNames)

        # md.pushButtonRestoreDefaultCalculationSettings.clicked.connect(self.restoreDefaultCalculationSettings)
        # md.buttonUserSettings.clicked.connect(self.displayUserSettingsDialog)
        md.buttonDatabaseSettings.clicked.connect(self.databaseConnection.displayDatabaseSettingsDialog)
        md.infoButton.clicked.connect(lambda: self.infoDialog.show())

        # md.futureAreasLayerList.hide()
        # md.futureNetworkLayerList.hide()
        # md.futureStopsLayerList.hide()

        # md.futureAreasLoadLayer.clicked.connect(self.handleLayerToggle)
        # md.futureNetworkLoadLayer.clicked.connect(self.handleLayerToggle)
        # md.futureStopsLoadLayer.clicked.connect(self.handleLayerToggle)

        # md.checkBoxCalculateFuture.clicked.connect(self.handleLayerToggle)

        # md.checkBoxCalculateEmissionsPerPerson.clicked.connect(self.handleCalculateEmissionsPerPersonToggle)
        # md.checkBoxCalculateEmissionsPerJob.clicked.connect(self.handleCalculateEmissionsPerJobToggle)
        # md.checkBoxCalculateEmissionsPerFloorSpaceSquares.clicked.connect(self.handleCalculateEmissionsPerFloorSpaceSquaresToggle)
        # md.checkBoxVisualizeTrafficEmissions.clicked.connect(self.handleVisualizeTrafficEmissionsToggle)
        # md.checkBoxVisualizeSustainableUrbanStructure.clicked.connect(self.handleVisualizeSustainableUrbanStructureToggle)
        # md.checkBoxAddQuickchartIoLinksOfRelativeEmissionsByZone.clicked.connect(self.handleAddQuickchartIoLinksOfRelativeEmissionsByZoneToggle)

    def calculationDialogFinished(self):
        # tallenna aina, kun käyttäjä sulkee laskentaikkunan (finished-signaali)
        pass
        # self.saveCalculationSettings()


    def runProcess(self, retriesLeft=3):
        try:
            shouldRun = self.preProcess()
            if shouldRun == False:
                return False
        except Exception as e:
            if retriesLeft > 0:
                return self.runProcess(retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(self.tr('Error in preprocessing'),
                    str(e), Qgis.Critical, duration=0)
                self.cleanUpSession()
                return False

        return True
    

    def preProcess(self):
        self.resultLayers = []
        '''Starts calculation'''
        if not self.databaseConnection.getConnParams():
            self.iface.messageBar().pushMessage(self.tr('Database connection not setup'), Qgis.Critical, duration=0)
            return False
        self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
        self.sessionParams = self.generateSessionParameters()
        self.readProcessingInput()
        return True
    
    
    def generateSessionParameters(self):
        '''Get necessary values for processing session'''
        sessionParams = {}

        usr = getpass.getuser()
        sessionParams["user"] = usr.replace(" ", "_")
        now = datetime.datetime.now()
        sessionParams["startTime"] = now.strftime("%Y%m%d_%H%M%S")
        sessionParams["baseYear"] = now.year
        sessionParams["uuid"] = str(uuid.uuid4())

        return sessionParams
    

    def readProcessingInput(self):
        '''Read user input from main dialog'''
        md = self.mainDialog

        self.NameOfTheCO2EstimationRun = md.lineEditNameOfTheCO2EstimationRun.text()

        self.inputLayers = []

        # if md.radioButtonUseMapLayerForInvestigatedArea.isChecked():
        #     self.predefinedAreaDBTableName = None
        #     self.investigatedAreaMapLayer = md.comboBoxMapLayer.currentLayer()
        #     if self.investigatedAreaMapLayer == None:
        #         raise Exception(self.tr("Investigation area map layer has not been selected"))
        #     elif not self.investigatedAreaMapLayer.isValid():
        #         raise Exception(self.tr("Investigation area map layer is not valid"))
        #     dataProvider = self.investigatedAreaMapLayer.dataProvider()
        #     dataSourceUri = dataProvider.dataSourceUri()
        #     # QgsMessageLog.logMessage("dataSourceUri: {}".format(dataProvider.dataSourceUri()), 'YKRTool', Qgis.Info)
        #     uri = dataProvider.uri()
        #     if uri.host() == "" or uri.host() != self.connParams['host'] or uri.database() == "" or uri.database() != self.connParams['database']:
        #         self.predefinedAreaDBTableName = 'user_input.' + '"' + self.investigatedAreaMapLayer.name()[:YKRToolRegion.MAX_TABLE_NAME_LENGTH] + '"'
        #         self.ykrToolUploadLayer.copySourceLayerFeaturesToTargetTable(self.connParams, self.investigatedAreaMapLayer, self.predefinedAreaDBTableName, md.checkBoxAllowOtherUsersToUseUploadedMapLayer.isChecked(), md.checkBoxUploadOnlySelectedFeatures.isChecked())
        #     else:
        #         self.investigatedAreaMapLayer = None
        #         QgsMessageLog.logMessage("schema: {}".format(uri.schema()) , 'YKRTool', Qgis.Info)
        #         QgsMessageLog.logMessage("quotedTablename: {}".format(uri.quotedTablename()) , 'YKRTool', Qgis.Info)
        #         self.predefinedAreaDBTableName = uri.quotedTablename()
        # else:
        self.investigatedAreaMapLayer = None
        self.predefinedAreaDBTableName = self.ykrToolDictionaries.getPredefinedAreaDatabaseTableName(md.comboBoxPredefinedArea.currentText())

        self.municipalitiesArrayString = self.ykrToolDictionaries.createMunicipalitiesArrayString(self.mainDialog.checkBoxMunicipalitiesKangasala.isChecked(), self.mainDialog.checkBoxMunicipalitiesLempaala.isChecked(),  self.mainDialog.checkBoxMunicipalitiesNokia.isChecked(), self.mainDialog.checkBoxMunicipalitiesOrivesi.isChecked(), self.mainDialog.checkBoxMunicipalitiesPirkkala.isChecked(), self.mainDialog.checkBoxMunicipalitiesTampere.isChecked(), self.mainDialog.checkBoxMunicipalitiesVesilahti.isChecked(), self.mainDialog.checkBoxMunicipalitiesYlojarvi.isChecked())

        self.pitkoScenario = self.ykrToolDictionaries.getPITKOScenarioShortName(md.pitkoScenario.currentText())

        self.includeLongDistance = md.checkBoxIncludeLongDistance.isChecked()
        self.includeBusinessTravel = md.checkBoxIncludeBusinessTravel.isChecked()

        # if not md.checkBoxCalculateFuture.isChecked():
        self.calculateFuture = False
        # else:
        #     self.readFutureProcessingInput()


        self.runCalculation()


    def cleanUpSession(self):
        pass
        # if self.rememberCalculationSettingsBetweenRuns == False:
        #     # * if true then nothing to do
        #     # * if false then set the settings according to the QT Dialog (.ui) default settings at the end of the calculation run
        #     #    (* also reset to default settings button sets the settings according to the QT Dialog (.ui) default settings)
        #     self.restoreDefaultCalculationSettings()

        '''Delete temporary data and close db connection'''

        # self.databaseConnection.close()

    
    def runCalculation(self):
        '''Runs the main calculation'''

        success = False

        try:
            success = self.writeSessionInfoToDatabase()
            # self.iface.messageBar().pushMessage(self.tr('Ready'), self.tr('Emission calculation ') +\
            #     str(self.outputTableName) + self.tr(' is ready'), Qgis.Success, duration=0)
        except Exception as e:
            self.iface.messageBar().pushMessage(self.tr('Error in storing session data to the database: '),\
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()

        if success:
            try:
                queries = self.getCalculationQueries()
                queryTask = QueryTask(self.databaseConnection.getConnParams(), queries)
                queryTask.taskCompleted.connect(self.postCalculation)
                queryTask.taskTerminated.connect(self.postError)
                QgsApplication.taskManager().addTask(queryTask)
                self.iface.messageBar().pushMessage(self.tr('Emission calculation'),
                    self.tr('Calculating emissions'), Qgis.Info, duration=15)
            except Exception as e:
                self.iface.messageBar().pushMessage(self.tr('Error in calculation'), str(e), Qgis.Critical, duration=0)
                self.cleanUpSession()
                return False


    def writeSessionInfoToDatabase(self):
        '''Writes session info to user_output.sessions_v2 table'''

        success = self.getOutputTableName()
        if not success or self.outputTableName == None:
            return False

        aoi = self.predefinedAreaDBTableName
        aoiDatabaseTableName = self.ykrToolDictionaries.getPredefinedAreaNameFromDatabaseTableName(self.predefinedAreaDBTableName)
        if aoiDatabaseTableName != None and aoiDatabaseTableName != '' and aoiDatabaseTableName != aoi:
            aoi = aoiDatabaseTableName + ' (' + aoi + ')'

        self.latestSessionInfo = {
            'session_name': self.NameOfTheCO2EstimationRun if self.NameOfTheCO2EstimationRun != None else '',
            'results_table_name': self.outputTableName,
            'aoi': aoi,
            'municipalities': self.municipalitiesArrayString,
            'kt_table_name': self.futureZoningAreasTableName,
            'kv_table_name': self.futureNetworkLayerDBTableName,
            'joli_table_name': self.futureStopsLayerDBTableName,
            'sid': self.sessionParams['uuid'],
            'usr': self.sessionParams['user'],
            'starttime': self.sessionParams['startTime'],
            'baseyear': self.sessionParams['baseYear'],
            'targetyear': self.targetYear if self.calculateFuture else None,
            'calculationScenario': self.pitkoScenario
            # 'metodi': self.emissionsAllocation,
            # 'paastolaji': self.elecEmissionType
        }

        # query = "INSERT INTO user_output.sessions_v2(session_name, results_table_name, aoi, municipalities, kt_table_name, kv_table_name, joli_table_name, sid, usr, starttime, baseyear, targetyear, calculationScenario) VALUES ('{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.latestSessionInfo['session_name'], self.latestSessionInfo['results_table_name'], self.latestSessionInfo['aoi'], self.latestSessionInfo['municipalities'], self.latestSessionInfo['kt_table_name'], self.latestSessionInfo['kv_table_name'], self.latestSessionInfo['joli_table_name'], self.latestSessionInfo['sid'], self.latestSessionInfo['usr'], self.latestSessionInfo['starttime'], self.latestSessionInfo['baseyear'], self.latestSessionInfo['targetyear'],\
        #     self.latestSessionInfo['calculationScenario'])
        # self.databaseConnection.execute(query)
        cursor = self.databaseConnection.cursor()
        cursor.execute('''INSERT INTO user_output.sessions_v2(session_name, results_table_name, aoi, municipalities, kt_table_name, kv_table_name, joli_table_name, sid, usr, starttime, baseyear, targetyear, calculationScenario) VALUES (%s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s)''', (self.latestSessionInfo['session_name'], self.latestSessionInfo['results_table_name'], self.latestSessionInfo['aoi'], self.latestSessionInfo['municipalities'], self.latestSessionInfo['kt_table_name'], self.latestSessionInfo['kv_table_name'], self.latestSessionInfo['joli_table_name'], self.latestSessionInfo['sid'], self.latestSessionInfo['usr'], self.latestSessionInfo['starttime'], self.latestSessionInfo['baseyear'], self.latestSessionInfo['targetyear'],\
            self.latestSessionInfo['calculationScenario'], ))
        self.databaseConnection.commit()

        return True


    def getOutputTableName(self):
        '''Returns the name of the output table'''

        table_name = self.mainDialog.lineEditNameOfTheOutputTable.text()

        # Replace spaces with underscores
        table_name = table_name.replace(' ', '_')
    
        # # Convert to lowercase
        # table_name = table_name.lower()
        
        # Replace scandinavian characters
        table_name = table_name.replace('ä', 'a')
        table_name = table_name.replace('ö', 'o')
        table_name = table_name.replace('å', 'a')

        self.outputTableName = table_name

        if self.outputTableName == '' or self.outputTableName == None:
            self.outputTableName = None
            return False
        # Check if table already exists...
        elif self.databaseConnection.tableExists('user_output', self.outputTableName):
            if not self.mainDialog.checkBoxOverwriteExistingOutputTable.isChecked():
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText(self.tr("The database table exists. Do you want to overwrite it?"))
                msgBox.setWindowTitle(self.tr("The database table exists"))
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # msgBox.buttonClicked.connect(msgButtonClick)

                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Yes:
                    QgsMessageLog.logMessage("The database table exists. Ok to continue.", 'YKRTool', Qgis.Info)
                    # print('OK clicked')
                    self.databaseConnection.dropTable('user_output', self.outputTableName)
                else:
                    self.outputTableName = None
                    return False
            else:
                self.databaseConnection.dropTable('user_output', self.outputTableName)
        
        return True


    def getCalculationQueries(self):
        '''Generate queries to call processing functions in database'''

        vals = {
            'municipalities': self.municipalitiesArrayString,
            'aoi': self.predefinedAreaDBTableName,
            # 'geomArea': self.geomArea,
            # 'popTable': (self.tableNames[self.ykrPopLayer]).lower(),
            # 'jobTable': (self.tableNames[self.ykrJobsLayer]).lower(),
            # 'buildingTable': (self.tableNames[self.ykrBuildingsLayer]).lower(),
            # 'calcYear': 2023, #self.sessionParams['baseYear'],
            'pitkoScenario': self.pitkoScenario,
            # 'emissionsAllocation': self.emissionsAllocation,
            # 'elecEmissionType': self.elecEmissionType,
            'baseYear': self.sessionParams['baseYear'],
            # 'targetYear': 2023, #self.sessionParams['baseYear'],
            'outputTableName': self.outputTableName,
            'includeLongDistance': 'true' if self.includeLongDistance else 'false',
            'includeBusinessTravel': 'true' if self.includeBusinessTravel else 'false'
        }
        queries = []
        if not self.calculateFuture:
            # presentYearVals = {
            #     'calculationYears': 'array[{0}, {0}, {0}]'.format(self.sessionParams["baseYear"]),
            # }
            # vals.update(presentYearVals)
            
            query = '''CREATE TABLE user_output."{outputTableName}" AS SELECT * FROM CO2_CalculateEmissionsLoop({municipalities}, '{aoi}', '{pitkoScenario}', '{baseYear}', '{baseYear}', NULL, NULL, NULL, {includeLongDistance}, {includeBusinessTravel});'''.format(**vals)

            # query = '''CREATE TABLE user_output."output_{0}" AS SELECT * FROM CO2_CalculateEmissions(array{1}, '{2}', {3}, {4}, array{5}, '{6}', '{7}', '{8}', {9}, {10});'''.format(self.sessionParams['uuid'], [837], self.predefinedAreaDBTableName, 'false' ,'true', [2023, 2023, 2023], self.pitkoScenario, self.emissionsAllocation, self.elecEmissionType, 2023, 2023)

            # query = '''CREATE TABLE user_output."output_{uuid}" AS
            #     SELECT * FROM CO2_CalculateEmissions('{municipalities}', '{aoi}', '{includeLongDistance}', '{includeBusinessTravel}', '{calculationYears}', '{pitkoScenario}',
            #     '{emissionsAllocation}', '{elecEmissionType}', '{baseYear}', '{targetYear}')'''.format(**vals)
            QgsMessageLog.logMessage(query, 'YKRTool', Qgis.Info)
            queries.append(query)
            # queries.append('''CREATE TABLE user_output."output_{uuid}" AS
            # SELECT * FROM CO2_CalculateEmissions('{aoi}', '{calcYear}', '{pitkoScenario}',
            # '{emissionsAllocation}', '{elecEmissionType}')'''.format(**vals))
            # # queries.append('''CREATE TABLE user_output."output_{uuid}" AS
            # # SELECT * FROM il_calculate_emissions('{popTable}', '{jobTable}',
            # # '{buildingTable}', '{aoi}', '{calcYear}', '{pitkoScenario}',
            # # '{emissionsAllocation}', '{elecEmissionType}', '{geomArea}',
            # # '{baseYear}')'''.format(**vals))
            QgsMessageLog.logMessage("getCalculationQueries, not self.calculateFuture", 'YKRTool', Qgis.Info)
        else:
            pass
            # futureQuery = self.generateFutureQuery(vals)
            # queries.append(futureQuery)
        return queries


    def postCalculation(self):
        '''Called after QueryTask finishes. Updates session info in sessions_v2 table and closes session'''

        try:
            now = datetime.datetime.now()
            endtime = now.strftime("%Y%m%d_%H%M%S")
            cursor = self.databaseConnection.cursor()
            cursor.execute('UPDATE user_output.sessions_v2 SET endtime = %s WHERE sid = %s', (endtime, self.sessionParams['uuid'],))
            self.databaseConnection.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Error in adding endtime to sessions_v2 table ') + '{}'.format(self.sessionParams['uuid']),
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()

        self.iface.messageBar().pushMessage(self.tr('Ready'), self.tr('Emission calculation ') +\
                str(self.outputTableName) + self.tr(' is ready'), Qgis.Success, duration=0)

        try:
            self.addResultAsLayers()
        except Exception as e:
            self.iface.messageBar().pushMessage(self.tr('Error in adding emissions results to the QGIS: '), str(e), Qgis.Warning, duration=0)
            QgsMessageLog.logMessage(traceback.format_exc(), 'YKRTool', Qgis.Warning)
        try:
            self.cleanUpSession()
        except Exception as e:
            self.iface.messageBar().pushMessage(self.tr('Error in cleaning up: '), str(e), Qgis.Warning, duration=0)


    def postError(self):
        '''Called after querytask is terminated. Closes session'''
        try:
            cursor = self.databaseConnection.cursor()
            cursor.execute('UPDATE user_output.sessions_v2 SET results_table_name = NULL WHERE sid = %s', (self.sessionParams['uuid'],))
            self.databaseConnection.commit()
            cursor.execute('DROP TABLE IF EXISTS user_input."ykr_{}"'.format(self.sessionParams['uuid']))
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Error in cleaning up session after error ') + '{}'.format(self.sessionParams['uuid']),
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()
        self.cleanUpSession()
        self.iface.messageBar().pushMessage(self.tr('Error in performing calculation'),\
            self.tr('See further info in the error log'), Qgis.Critical, duration=0)
        

    def addResultAsLayers(self):
        outputSchemaName = 'user_output'
        outputTableName = self.outputTableName
        uid = self.sessionParams['uuid']

        groupName = self.tr("emissions calculation results") + " {}".format(outputTableName)

        rootGroup = self.iface.layerTreeView().currentGroupNode()
        if rootGroup != None:
            rootGroup = rootGroup.addGroup(groupName) # ret QgsLayerTreeGroup 
        else:
            root = QgsProject.instance().layerTreeRoot()
            rootGroup = root.insertGroup(0, groupName)


        self.visualizeTrafficEmissions(rootGroup, uid, outputSchemaName, outputTableName)
        # self.visualizeThermoEmissions(rootGroup, uid, outputSchemaName, outputTableName)
        # self.visualizeElectricityEmissions(rootGroup, uid, outputSchemaName, outputTableName)
        self.createUrbanDevelopmentVisualizations(rootGroup, uid, outputSchemaName, outputTableName)

        layerNames = []
        layerNames.append((self.tr('CO2 sources grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/CO2_sources.qml')))
        layerNames.extend(self.calculateRelativeGeneralEmissions(uid, outputSchemaName, outputTableName))
        layerNames.append((self.tr('CO2 total grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/CO2_t_grid.qml')))
        layerNames.append((self.tr('YKR Zones (UZ and urban-countryside)') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/zones.qml')))
        # Visualize population grid, employees grid and floor space grid
        layerNames.append((self.tr('Population count') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/Population.qml')))
        layerNames.append((self.tr('Employee count') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/employees.qml')))
        layerNames.append((self.tr('Floor space (m2)') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/floorspace.qml')))

        # if self.mainDialog.checkBoxCreateYKRZoneSummaryStats.isChecked():
        #     self.ykrZonesStats.calculateYKRZoneEmissions(uid, outputSchemaName, outputTableName)

        # self.createQuickchartIoLinks(uid, outputSchemaName, outputTableName)

        uri = QgsDataSourceUri()
        uri.setConnection(self.databaseConnection.getConnParams()['host'], self.databaseConnection.getConnParams()['port'],\
            self.databaseConnection.getConnParams()['database'], self.databaseConnection.getConnParams()['user'], self.databaseConnection.getConnParams()['password'])
        uri.setDataSource(outputSchemaName, outputTableName, 'geom')


        groupName = self.tr("general")
        group = rootGroup.addGroup(groupName)

        for name in layerNames:
            layer = QgsVectorLayer(uri.uri(False), name[0], 'postgres')
            layer.loadNamedStyle(name[1])
            renderer = layer.renderer()
            if renderer != None and renderer.type() == 'graduatedSymbol':
                renderer.updateClasses(layer, renderer.mode(), len(renderer.ranges()))
            self.resultLayers.append(layer)
            QgsProject.instance().addMapLayer(layer, False)
            group.addLayer(layer)

        for layer in self.resultLayers: # To have all columns in all layers
            layer.setDataSource( layer.source(), layer.name(), layer.providerType() )



    
    def createUrbanDevelopmentVisualizations(self, rootGroup, uid, outputSchemaName, outputTableName):
        layerNames = []
        
        groupName = self.tr("urban devlopment")
        group = rootGroup.addGroup(groupName)

        # if self.mainDialog.checkBoxVisualizePopJobMix.isChecked():
        success = self.calculatePopJobMix(outputSchemaName, outputTableName)
        if success:
            layerNames.append((self.tr('pop employ mix grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/pop_job_mix_grid.qml')))

        # if self.mainDialog.checkBoxVisualizeGoodZonesForPopJobDensityAndSustainableTransport.isChecked():
        #     layerNames.append((self.tr('good UZ zones for population, jobs and sustainable transport grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/good_uz_zones_grid.qml')))
        
        # if self.mainDialog.checkBoxVisualizeFloorSpaceRatio.isChecked():
        #     layerNames.append((self.tr('Buildings floor space / YKR square area >= 0.2') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/floor_space_ratio.qml')))

        # if self.mainDialog.checkBoxVisualizeSustainableUrbanStructure.isChecked():
        #     success = self.caclulateSustainableUrbanStructure(group, uid, outputSchemaName, outputTableName)

        uri = QgsDataSourceUri()
        uri.setConnection(self.databaseConnection.getConnParams()['host'], self.databaseConnection.getConnParams()['port'],\
            self.databaseConnection.getConnParams()['database'], self.databaseConnection.getConnParams()['user'], self.databaseConnection.getConnParams()['password'])
        uri.setDataSource(outputSchemaName, outputTableName, 'geom')

        for name in layerNames:
            layer = QgsVectorLayer(uri.uri(False), name[0], 'postgres')
            layer.loadNamedStyle(name[1])
            renderer = layer.renderer()
            if renderer.type() == 'graduatedSymbol':
                renderer.updateClasses(layer, renderer.mode(), len(renderer.ranges()))
            self.resultLayers.append(layer)
            QgsProject.instance().addMapLayer(layer, False)
            group.addLayer(layer)


    # def createSustainableUrbanStructureResultLayer(self, uid, outputSchemaName, outputTableName, retriesLeft=3):
    #     queries = []
    #     tableName = "output_sustainable_urban_structure_{}".format(outputTableName)

    #     query = """CREATE TABLE \"{}\".\"{}\"(
    #     id integer PRIMARY KEY,
    #     geom geometry(MultiPolygon, 3067),
    #     xyind varchar,
    #     mun varchar,
    #     asukkaat integer,
    #     tyopaikat integer,
    #     tiiveys_asukkaat_plus_tyopaikat_per_ha real,
    #     joukkoliikennekaup_mahd_tiiveys varchar,
    #     kavelykaup_mahd_tiiveys varchar,
    #     asukkaat_per_asukkaat_plus_tyopaikat real,
    #     keskustamainen_toim_seko varchar,
    #     asuntokunta_0_autoa_pros_osuus real,
    #     asuntokunta_1_autoa_pros_osuus real,
    #     asuntokunta_2_autoa_pros_osuus real,
    #     autottomuus_suht_yleista varchar,
    #     kahd_auton_omistus_suht_vahaista varchar,
    #     liikenne_hlo_tco2 real,
    #     liikenne_hlo_tco2_per_as_tp real,
    #     verrat_alh_henkliik_paast varchar,
    #     kestavan_kaupunkirakenteen_mittarit_toteutuu_yht integer
    #     )
    #     """.format(outputSchemaName.replace('"', ''), tableName)

    #     queries.append(query)

    #     if self.mainDialog.checkBoxAllowOtherUsersToUseSustainableUrbanStructureTable.isChecked():
    #         query = "GRANT SELECT ON \"{}\".\"{}\" TO public".format(outputSchemaName.replace('"', ''), tableName)


    #     try:
    #         self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
    #     except Exception as e:
    #         if retriesLeft > 0:
    #             self.createSustainableUrbanStructureResultLayer(uid, outputSchemaName, outputTableName, retriesLeft - 1)
    #         else:
    #             self.iface.messageBar().pushMessage(
    #                 self.tr('Error in connecting to the database'),
    #                 str(e), Qgis.Warning, duration=0)

    #     try:
    #         cur = self.databaseConnection.cursor()
    #         for query in queries:
    #             cur.execute(query)
    #             self.databaseConnection.commit()
    #     except Exception as e:
    #         self.iface.messageBar().pushMessage(
    #             self.tr('Error in modifying the results table ') + "{}".format(query),
    #             str(e), Qgis.Warning, duration=0)
    #         self.databaseConnection.rollback()
    #         self.databaseConnection.close()


    #     uri = QgsDataSourceUri()
    #     uri.setConnection(self.databaseConnection.getConnParams()['host'], self.databaseConnection.getConnParams()['port'],\
    #         self.databaseConnection.getConnParams()['database'], self.databaseConnection.getConnParams()['user'], self.databaseConnection.getConnParams()['password'])
        
    #     uri.setDataSource(outputSchemaName.replace('"', ''), tableName, 'geom')
    #     layer = QgsVectorLayer(uri.uri(False), tableName, 'postgres')
    #     provider = layer.dataProvider()

    #     return (layer, provider)


    # def caclulateSustainableUrbanStructure(self, group, uid, outputSchemaName, outputTableName):
    #     # 1. laske autonomistustiedot QGIS:ssä olevan karttatason avulla pythonin muuttujiin
    #     # 2. Lisää laskennan tulostasoon kentät toteutuu vs. ei-toteudu kullekin ehtokentälle ja päivitä
    #     # 3. tee erilliset tasot ja visualisoinnit kullekin muuttujalle ja myös yhteinen taso ja visualisointi

    #     md = self.mainDialog

    #     carOwnershipMapLayer = md.mMapLayerComboBoxYKRCarOwnershipData.currentLayer()
    #     if carOwnershipMapLayer == None:
    #         raise Exception(self.tr("YRK Car Ownership Data layer has not been selected"))
    #     elif not carOwnershipMapLayer.isValid():
    #         raise Exception(self.tr("YRK Car Ownership Data layer is not valid"))
    #     else:
    #         # (TODO check that contains all expected data) 
    #         fields = carOwnershipMapLayer.fields()
    #         if fields.indexOf('xyind') == -1:
    #             raise Exception(self.tr("YRK Car Ownership Data layer does not contain field xyind"))
    #         if fields.indexOf('kunta') == -1:
    #             raise Exception(self.tr("YRK Car Ownership Data layer does not contain field kunta"))
    #         if fields.indexOf('kunta') == -1:
    #             raise Exception(self.tr("YRK Car Ownership Data layer does not contain field autoja_1"))
    #         if fields.indexOf('kunta') == -1:
    #             raise Exception(self.tr("YRK Car Ownership Data layer does not contain field autoja_2"))
    #         if fields.indexOf('kunta') == -1:
    #             raise Exception(self.tr("YRK Car Ownership Data layer does not contain field ak_yht"))

    #     queries = []

    #     (tempLayer, tempProvider) = self.createSustainableUrbanStructureResultLayer(uid, outputSchemaName, outputTableName)
    #     tempLayer.startEditing()

    #     features = []

    #     # Get result layer (to calculate only for xyind sqaures on the investigation area)
    #     uri = QgsDataSourceUri()
    #     uri.setConnection(self.databaseConnection.getConnParams()['host'], self.databaseConnection.getConnParams()['port'],\
    #         self.databaseConnection.getConnParams()['database'], self.databaseConnection.getConnParams()['user'], self.databaseConnection.getConnParams()['password'])
    #     uri.setDataSource(outputSchemaName, outputTableName, 'geom')

    #     targetLayer = QgsVectorLayer(uri.uri(False), "emissions target layer", 'postgres')

    #     targetFeatures = targetLayer.getFeatures()

    #     xyinds = set()
    #     muns = set()

    #     for targetFeature in targetFeatures:

    #         kestavan_kaupunkirakenteen_mittarit_toteutuu_yht = 0
    #         kestavan_kaupunkirakenteen_mittarit_toteutuu_yht_none_flag = False

    #         geometry = targetFeature.geometry()

    #         qgs_feature = QgsFeature()
    #         qgs_feature.setGeometry(geometry)
    #         fields = tempLayer.fields()
    #         qgs_feature.setFields(fields)

    #         xyind = targetFeature['xyind']
    #         mun = targetFeature['mun']
    #         xyinds.add(xyind)
    #         muns.add(mun)

    #         qgs_feature['id'] = targetFeature.id()
    #         qgs_feature['xyind'] = xyind
    #         qgs_feature['mun'] = mun

    #         '''joukkoliikennekaup_mahd_tiiveys, kavelykaup_mahd_tiiveys ja keskustamainen_toim_seko'''
    #         asukkaat = targetFeature['pop']
    #         tyopaikat = targetFeature['employ']
    #         qgs_feature['asukkaat'] = asukkaat
    #         qgs_feature['tyopaikat'] = tyopaikat
    #         asukkaat = float(asukkaat) if asukkaat != None else 0
    #         tyopaikat = float(tyopaikat) if tyopaikat != None else 0
    #         tiiveys_asukkaat_plus_tyopaikat_per_ha = (asukkaat + tyopaikat) / 6.25
    #         qgs_feature['tiiveys_asukkaat_plus_tyopaikat_per_ha'] = tiiveys_asukkaat_plus_tyopaikat_per_ha
    #         if (tiiveys_asukkaat_plus_tyopaikat_per_ha >= 35): # 6,25 hehtaaria = 250x250m
    #             query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET joukkoliikennekaup_mahd_tiiveys = 'Toteutuu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #             kestavan_kaupunkirakenteen_mittarit_toteutuu_yht += 1
    #             qgs_feature['joukkoliikennekaup_mahd_tiiveys'] = 'Toteutuu'
    #         else:
    #             query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET joukkoliikennekaup_mahd_tiiveys = 'Ei toteudu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #             qgs_feature['joukkoliikennekaup_mahd_tiiveys'] = 'Ei toteudu'
    #         # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #         queries.append(query)
    #         if (tiiveys_asukkaat_plus_tyopaikat_per_ha >= 100): # 6,25 hehtaaria = 250x250m
    #             query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET kavelykaup_mahd_tiiveys = 'Toteutuu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #             kestavan_kaupunkirakenteen_mittarit_toteutuu_yht += 1
    #             qgs_feature['kavelykaup_mahd_tiiveys'] = 'Toteutuu'
    #         else:
    #             query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET kavelykaup_mahd_tiiveys = 'Ei toteudu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #             qgs_feature['kavelykaup_mahd_tiiveys'] = 'Ei toteudu'
    #         # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #         queries.append(query)
    #         if (asukkaat + tyopaikat > 0):
    #             asukkaat_per_asukkaat_plus_tyopaikat = asukkaat / (asukkaat + tyopaikat)
    #             qgs_feature['asukkaat_per_asukkaat_plus_tyopaikat'] = asukkaat_per_asukkaat_plus_tyopaikat
    #             if (asukkaat_per_asukkaat_plus_tyopaikat >= 0.2) and (asukkaat_per_asukkaat_plus_tyopaikat <= 0.8):
    #                 query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET keskustamainen_toim_seko = 'Toteutuu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #                 kestavan_kaupunkirakenteen_mittarit_toteutuu_yht += 1
    #                 qgs_feature['keskustamainen_toim_seko'] = 'Toteutuu'
    #             else:
    #                 query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET keskustamainen_toim_seko = 'Ei toteudu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #                 qgs_feature['keskustamainen_toim_seko'] = 'Ei toteudu'
    #             # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #             queries.append(query)

    #         '''verrat_alh_henkliik_paast'''

    #         qgs_feature['liikenne_hlo_tco2'] = targetFeature['liikenne_hlo_tco2']
    #         liikenne_hlo_tco2_per_as_tp = targetFeature['liikenne_hlo_tco2_per_as_tp']
    #         if liikenne_hlo_tco2_per_as_tp != None:
    #             qgs_feature['liikenne_hlo_tco2_per_as_tp'] = liikenne_hlo_tco2_per_as_tp
    #             if liikenne_hlo_tco2_per_as_tp <= 0.05:
    #                 query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET verrat_alh_henkliik_paast = 'Toteutuu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #                 kestavan_kaupunkirakenteen_mittarit_toteutuu_yht += 1
    #                 qgs_feature['verrat_alh_henkliik_paast'] = 'Toteutuu'
    #             else:
    #                 query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET verrat_alh_henkliik_paast = 'Ei toteudu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #                 qgs_feature['verrat_alh_henkliik_paast'] = 'Ei toteudu'
    #             # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #             queries.append(query)
    #         else:
    #             kestavan_kaupunkirakenteen_mittarit_toteutuu_yht_none_flag = True

    #         if kestavan_kaupunkirakenteen_mittarit_toteutuu_yht > 0:
    #             qgs_feature['kestavan_kaupunkirakenteen_mittarit_toteutuu_yht'] = kestavan_kaupunkirakenteen_mittarit_toteutuu_yht
    #             query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET kestavan_kaupunkirakenteen_mittarit_toteutuu_yht = {} WHERE xyind ='{}' and mun='{}'".format(kestavan_kaupunkirakenteen_mittarit_toteutuu_yht, xyind, mun)
    #             # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #             queries.append(query)

    #         features.append(qgs_feature)

    #     tempProvider.addFeatures(features)
    #     tempLayer.commitChanges()
    #     tempLayer.startEditing()

    #     '''kahd_auton_omistus_suht_vahaista ja autottomuus_suht_yleista''' # Erikseen, jotta nopeampaa
    #     fields = tempLayer.fields()
    #     index_asuntokunta_0_autoa_pros_osuus = fields.indexOf("asuntokunta_0_autoa_pros_osuus")
    #     index_asuntokunta_1_autoa_pros_osuus = fields.indexOf("asuntokunta_1_autoa_pros_osuus")
    #     index_asuntokunta_2_autoa_pros_osuus = fields.indexOf("asuntokunta_2_autoa_pros_osuus")
    #     index_kahd_auton_omistus_suht_vahaista = fields.indexOf("kahd_auton_omistus_suht_vahaista")
    #     index_autottomuus_suht_yleista = fields.indexOf("autottomuus_suht_yleista")
    #     index_kestavan_kaupunkirakenteen_mittarit_toteutuu_yht = fields.indexOf("kestavan_kaupunkirakenteen_mittarit_toteutuu_yht")
    #     for carOwnershipFeature in carOwnershipMapLayer.getFeatures():
    #         mun = carOwnershipFeature['kunta']
    #         xyind = carOwnershipFeature['xyind']
    #         if mun in muns and xyind in xyinds:
    #             # QgsMessageLog.logMessage("mun {} in muns and xyind {} in xyinds".format(mun, xyind), 'YKRTool', Qgis.Info)
    #             exp = QgsExpression("xyind = '{}' AND mun = '{}'".format(xyind, mun))
    #             qgs_features = list(tempLayer.getFeatures(QgsFeatureRequest(exp)))
    #             if len(qgs_features) == 1:
    #                 # QgsMessageLog.logMessage("found 1 qgs_features", 'YKRTool', Qgis.Info)
    #                 qgs_feature = qgs_features[0]
    #                 kestavan_kaupunkirakenteen_mittarit_toteutuu_yht = qgs_feature['kestavan_kaupunkirakenteen_mittarit_toteutuu_yht'] if qgs_feature['kestavan_kaupunkirakenteen_mittarit_toteutuu_yht'] != None else 0
    #                 # QgsMessageLog.logMessage("kestavan_kaupunkirakenteen_mittarit_toteutuu_yht alkup: {}".format(kestavan_kaupunkirakenteen_mittarit_toteutuu_yht), 'YKRTool', Qgis.Info)
    #                 autoja_1 = carOwnershipFeature['autoja_1']
    #                 autoja_2 = carOwnershipFeature['autoja_2']
    #                 ak_yht = carOwnershipFeature['ak_yht']
    #                 if autoja_1 != -1 and autoja_2 != -1:
    #                     asuntokunta_0_autoa_pros_osuus = (float(ak_yht) - (autoja_1 + autoja_2)) / ak_yht * 100
    #                     asuntokunta_1_autoa_pros_osuus = float(autoja_1) / ak_yht * 100
    #                     asuntokunta_2_autoa_pros_osuus = float(autoja_2) / ak_yht * 100
                        
    #                     tempLayer.changeAttributeValue(qgs_feature.id(), index_asuntokunta_0_autoa_pros_osuus, asuntokunta_0_autoa_pros_osuus)
    #                     tempLayer.changeAttributeValue(qgs_feature.id(), index_asuntokunta_1_autoa_pros_osuus, asuntokunta_1_autoa_pros_osuus)
    #                     tempLayer.changeAttributeValue(qgs_feature.id(), index_asuntokunta_2_autoa_pros_osuus, asuntokunta_2_autoa_pros_osuus)

    #                     if asuntokunta_1_autoa_pros_osuus > asuntokunta_2_autoa_pros_osuus and asuntokunta_2_autoa_pros_osuus < 30:
    #                         query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET kahd_auton_omistus_suht_vahaista = 'Toteutuu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #                         kestavan_kaupunkirakenteen_mittarit_toteutuu_yht += 1
    #                         tempLayer.changeAttributeValue(qgs_feature.id(), index_kahd_auton_omistus_suht_vahaista, 'Toteutuu')
    #                     else:
    #                         query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET kahd_auton_omistus_suht_vahaista = 'Ei toteudu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #                         tempLayer.changeAttributeValue(qgs_feature.id(), index_kahd_auton_omistus_suht_vahaista, 'Ei toteudu')
    #                     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #                     queries.append(query)

    #                     if asuntokunta_0_autoa_pros_osuus > asuntokunta_1_autoa_pros_osuus and asuntokunta_0_autoa_pros_osuus > 40:
    #                         query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET autottomuus_suht_yleista = 'Toteutuu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #                         kestavan_kaupunkirakenteen_mittarit_toteutuu_yht += 1
    #                         tempLayer.changeAttributeValue(qgs_feature.id(), index_autottomuus_suht_yleista, 'Toteutuu')
    #                     else:
    #                         query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET autottomuus_suht_yleista = 'Ei toteudu' WHERE xyind ='{}' and mun='{}'".format(xyind, mun)
    #                         tempLayer.changeAttributeValue(qgs_feature.id(), index_autottomuus_suht_yleista, 'Ei toteudu')
    #                     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #                     queries.append(query)
    #                 else:
    #                     kestavan_kaupunkirakenteen_mittarit_toteutuu_yht_none_flag = True
    #             elif len(qgs_features) > 1:
    #                 raise Exception(self.tr("temporary layer had unexpected count of features for xyind") + " {} " + self.tr("and municipality code" + " {}: {}").format(xyind, mun, len(qgs_features)))
    #             else:
    #                 kestavan_kaupunkirakenteen_mittarit_toteutuu_yht_none_flag = True

    #             # if kestavan_kaupunkirakenteen_mittarit_toteutuu_yht_none_flag == False:
    #             if kestavan_kaupunkirakenteen_mittarit_toteutuu_yht > 0:
    #                 tempLayer.changeAttributeValue(qgs_feature.id(), index_kestavan_kaupunkirakenteen_mittarit_toteutuu_yht, kestavan_kaupunkirakenteen_mittarit_toteutuu_yht)
    #                 query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET kestavan_kaupunkirakenteen_mittarit_toteutuu_yht = {} WHERE xyind ='{}' and mun='{}'".format(kestavan_kaupunkirakenteen_mittarit_toteutuu_yht, xyind, mun)
    #                 # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #                 queries.append(query)


    #     tempLayer.commitChanges()

    #     layerNames = []

    #     layerNames.append((self.tr('Sustainable Urban Structure, Count of True Value Indicators') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/sustainable_urban_structure.qml')))
    #     layerNames.append((self.tr('Sufficient Density of Population and Jobs for Public Transport - Sustainable Urban Structure') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/sust_urb_struct_sufficient_pop_job_density_pub_transport.qml')))
    #     layerNames.append((self.tr('Sufficient Density of Population and Jobs for Walkable City - Sustainable Urban Structure') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/sust_urb_struct_sufficient_pop_job_density_walk_city.qml')))
    #     layerNames.append((self.tr('Sufficient Mix of Population and Jobs - Sustainable Urban Structure') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/sust_urb_struct_sufficient_mix_pop_job.qml')))
    #     layerNames.append((self.tr('Density Induced Households Car Owning; More Households Owning 1 Car than 2 or More Cars; Portion of Households Owning 2 or More Cars < 30% - Sustainable Urban Structure') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/sust_urb_struct_households_below_2_cars_common.qml')))
    #     layerNames.append((self.tr('Density Induced Households Car Owning; More Households Not Owning Car than Owning 1 Car; Portion of Households Not Owning Car > 40% - Sustainable Urban Structure') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/sust_urb_struct_households_no_cars_common.qml')))
    #     layerNames.append((self.tr('Relatively Low Personal Traffic Emissions - Sustainable Urban Structure') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/urban_development/sust_urb_struct_relat_low_pers_traffic_emissions.qml')))

    #     for name in layerNames:
    #         layer = tempLayer.clone()
    #         layer.setName(name[0])
    #         layer.loadNamedStyle(name[1])
    #         renderer = layer.renderer()
    #         if renderer.type() == 'graduatedSymbol':
    #             renderer.updateClasses(layer, renderer.mode(), len(renderer.ranges()))
    #         QgsProject.instance().addMapLayer(layer, False)
    #         group.addLayer(layer)

    #     return True


    # def visualizeElectricityEmissions(self, rootGroup, uid, outputSchemaName, outputTableName):
    #     layerNames = []
    
    #     if self.mainDialog.checkBoxVisualizeElectricityConsumptionEmissions.isChecked():
    #         layerNames.append((self.tr('CO2 electricity sources grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/electricity/CO2_electricity_sources_grid.qml')))
    #         layerNames.append((self.tr('CO2 electricity total grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/electricity/CO2_electricity_grid.qml')))
    #         layerNames.append((self.tr('CO2 buildings electricity grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/electricity/CO2_buildings_electricity_grid.qml')))
    #         layerNames.append((self.tr('CO2 household electricity grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/electricity/CO2_household_electricity_grid.qml')))
    #         layerNames.append((self.tr('CO2 amenities electricity grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/electricity/CO2_amenities_electricity_grid.qml')))
    #         layerNames.append((self.tr('CO2 industry and warehouses electricity grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/electricity/CO2_industry_warehouses_electricity_grid.qml')))

    #         layerNames.extend(self.calculateRelativeElectricityEmissions(uid, outputSchemaName, outputTableName))

    #         groupName = self.tr("electricity emissions")
    #         group = rootGroup.addGroup(groupName)

    #         uri = QgsDataSourceUri()
    #         uri.setConnection(self.databaseConnection.getConnParams()['host'], self.databaseConnection.getConnParams()['port'],\
    #             self.databaseConnection.getConnParams()['database'], self.databaseConnection.getConnParams()['user'], self.databaseConnection.getConnParams()['password'])
    #         uri.setDataSource(outputSchemaName, outputTableName, 'geom')

    #         for name in layerNames:
    #             layer = QgsVectorLayer(uri.uri(False), name[0], 'postgres')
    #             layer.loadNamedStyle(name[1])
    #             renderer = layer.renderer()
    #             if renderer.type() == 'graduatedSymbol':
    #                 renderer.updateClasses(layer, renderer.mode(), len(renderer.ranges()))
    #             self.resultLayers.append(layer)
    #             QgsProject.instance().addMapLayer(layer, False)
    #             group.addLayer(layer)


    # def calculateRelativeElectricityEmissions(self, uid, outputSchemaName, outputTableName):
    #     layerNames = []
    #     success = self.calculateElectricityEmissionsPerPerson(outputSchemaName, outputTableName)
    #     if success:
    #         layerNames.append((self.tr('CO2 electricity emissions / pop grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/electricity/CO2_electricity_pop_grid.qml')))

    #     return layerNames


    # def visualizeThermoEmissions(self, rootGroup, uid, outputSchemaName, outputTableName):
    #     layerNames = []
    
    #     if self.mainDialog.checkBoxVisualizeThermoEmissions.isChecked():
    #         layerNames.append((self.tr('CO2 buildings thermo sources grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/thermo/CO2_buildings_thermo_sources_grid.qml')))
    #         layerNames.append((self.tr('CO2 buildings thermo total grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/thermo/CO2_buildings_thermo_grid.qml')))
    #         layerNames.append((self.tr('CO2 buildings water heating grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/thermo/CO2_buildings_water_heating_grid.qml')))
    #         layerNames.append((self.tr('CO2 buildings heating grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/thermo/CO2_buildings_heating_grid.qml')))
    #         layerNames.append((self.tr('CO2 buildings cooling grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/thermo/CO2_buildings_cooling_grid.qml')))

    #         layerNames.extend(self.calculateRelativeThermoEmissions(uid, outputSchemaName, outputTableName))

    #         groupName = self.tr("buildings thermo emissions")
    #         group = rootGroup.addGroup(groupName)

    #         uri = QgsDataSourceUri()
    #         uri.setConnection(self.databaseConnection.getConnParams()['host'], self.databaseConnection.getConnParams()['port'],\
    #             self.databaseConnection.getConnParams()['database'], self.databaseConnection.getConnParams()['user'], self.databaseConnection.getConnParams()['password'])
    #         uri.setDataSource(outputSchemaName, outputTableName, 'geom')

    #         for name in layerNames:
    #             layer = QgsVectorLayer(uri.uri(False), name[0], 'postgres')
    #             layer.loadNamedStyle(name[1])
    #             renderer = layer.renderer()
    #             if renderer.type() == 'graduatedSymbol':
    #                 renderer.updateClasses(layer, renderer.mode(), len(renderer.ranges()))
    #             self.resultLayers.append(layer)
    #             QgsProject.instance().addMapLayer(layer, False)
    #             group.addLayer(layer)


    # def calculateRelativeThermoEmissions(self, uid, outputSchemaName, outputTableName):
    #     layerNames = []
    #     success = self.calculateThermoEmissionsPerPerson(outputSchemaName, outputTableName)
    #     if success:
    #         layerNames.append((self.tr('CO2 buildings thermo emissions / pop grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/thermo/CO2_buildings_thermo_pop_grid.qml')))

    #     return layerNames


    def visualizeTrafficEmissions(self, rootGroup, uid, outputSchemaName, outputTableName):
        layerNames = []
    
        # if self.mainDialog.checkBoxVisualizeTrafficEmissions.isChecked():
        success = self.calculateSumOfPersonalTraffic(outputSchemaName, outputTableName)

        if success:
            layerNames.append((self.tr('CO2 traffic sources grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/traffic/CO2_traffic_sources_grid.qml')))
            layerNames.append((self.tr('CO2 traffic total grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/traffic/CO2_traffic_grid.qml')))
            layerNames.append((self.tr('CO2 commuter and other population traffic grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/traffic/CO2_personal_traffic_grid.qml')))
            layerNames.append((self.tr('CO2 industry and warehouses traffic grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/traffic/CO2_iwhs_traffic_grid.qml')))
            layerNames.append((self.tr('CO2 amenities traffic grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/traffic/CO2_amenities_traffic_grid.qml')))

            layerNames.extend(self.calculateRelativeTrafficEmissions(uid, outputSchemaName, outputTableName))


            groupName = self.tr("traffic emissions")
            group = rootGroup.addGroup(groupName)

            uri = QgsDataSourceUri()
            uri.setConnection(self.databaseConnection.getConnParams()['host'], self.databaseConnection.getConnParams()['port'],\
                self.databaseConnection.getConnParams()['database'], self.databaseConnection.getConnParams()['user'], self.databaseConnection.getConnParams()['password'])
            uri.setDataSource(outputSchemaName, outputTableName, 'geom')

            for name in layerNames:
                layer = QgsVectorLayer(uri.uri(False), name[0], 'postgres')
                layer.loadNamedStyle(name[1])
                renderer = layer.renderer()
                if renderer.type() == 'graduatedSymbol':
                    renderer.updateClasses(layer, renderer.mode(), len(renderer.ranges()))
                self.resultLayers.append(layer)
                QgsProject.instance().addMapLayer(layer, False)
                group.addLayer(layer)


    def calculateSumOfPersonalTraffic(self, outputSchemaName, outputTableName, retriesLeft=3):
        md = self.mainDialog
        queries = []

        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN liikenne_hlo_tco2 real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET liikenne_hlo_tco2 = (liikenne_as_tco2 + liikenne_tp_tco2)"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        try:
            self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
        except Exception as e:
            if retriesLeft > 0:
                return self.calculateSumOfPersonalTraffic(outputSchemaName, outputTableName, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
                    str(e), Qgis.Warning, duration=0)
                return False

        try:
            cur = self.databaseConnection.cursor()
            for query in queries:
                cur.execute(query)
                self.databaseConnection.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Error in modifying the results table ') + "{}".format(query),
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()
            self.databaseConnection.close()

            return False

        return True

    def calculateRelativeTrafficEmissions(self, uid, outputSchemaName, outputTableName):
        layerNames = []

        success = self.calculateRelativeTrafficEmissionsToDatabase(outputSchemaName, outputTableName)
        if success:
            layerNames.append((self.tr('CO2 traffic emissions / pop grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/traffic/CO2_traffic_pop_grid.qml')))

        return layerNames


    def calculateRelativeGeneralEmissions(self, uid, outputSchemaName, outputTableName):
        layerNames = []

        # if self.mainDialog.checkBoxCalculateEmissionsPerPerson.isChecked():
        success = self.calculateEmissionsPerPerson(outputSchemaName, outputTableName)
        if success:
            layerNames.append((self.tr('CO2 / pop grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/CO2_pop_grid.qml')))
    

        # if self.mainDialog.checkBoxCalculateEmissionsPerJob.isChecked():
        success = self.calculateEmissionsPerJob(uid, outputSchemaName, outputTableName)
        if success:
            layerNames.append((self.tr('CO2 / job grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/CO2_job_grid.qml')))

        # if self.mainDialog.checkBoxCalculateEmissionsPerPerson.isChecked() and self.mainDialog.checkBoxCalculateEmissionsPerJob.isChecked():
        success = self.calculateEmissionsPerPersonJob(outputSchemaName, outputTableName)
        if success:
            layerNames.append((self.tr('CO2 / (pop + employ) grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/CO2_pop_job_grid.qml')))

        # if self.mainDialog.checkBoxCalculateEmissionsPerFloorSpaceSquares.isChecked():
        success = self.calculateEmissionsPerFloorSpaceSquares(outputSchemaName, outputTableName)
        if success:
            layerNames.append((self.tr('CO2 / floor space squares grid') + ' {}'.format(outputTableName), os.path.join(self.plugin_dir, 'docs/CO2_floor_space_squares_grid.qml')))

        return layerNames


    # def calculateElectricityEmissionsPerPerson(self, outputSchemaName, outputTableName, retriesLeft=3):
    #     md = self.mainDialog
    #     queries = []

    #     query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_sahko_tco2_per_sum_yhteensa_tco2 real"
    #     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #     queries.append(query)

    #     query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_sahko_tco2_per_asukas real"
    #     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #     queries.append(query)

    #     query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_sahko_tco2_per_sum_yhteensa_tco2 = (sum_sahko_tco2 / NULLIF(sum_yhteensa_tco2 , 0))"
    #     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #     queries.append(query)

    #     query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_sahko_tco2_per_asukas = (sum_sahko_tco2 / NULLIF(pop, 0))"
    #     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #     queries.append(query)


    #     try:
    #         self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
    #     except Exception as e:
    #         if retriesLeft > 0:
    #             return self.calculateElectricityEmissionsPerPerson(outputSchemaName, outputTableName, retriesLeft - 1)
    #         else:
    #             self.iface.messageBar().pushMessage(
    #                 self.tr('Error in connecting to the database'),
    #                 str(e), Qgis.Warning, duration=0)
    #             return False

    #     try:
    #         cur = self.databaseConnection.cursor()
    #         for query in queries:
    #             cur.execute(query)
    #             self.databaseConnection.commit()
    #     except Exception as e:
    #         self.iface.messageBar().pushMessage(
    #             self.tr('Error in modifying the results table ') + "{}".format(query),
    #             str(e), Qgis.Warning, duration=0)
    #         self.databaseConnection.rollback()
    #         self.databaseConnection.close()

    #         return False

    #     return True


    # def calculateThermoEmissionsPerPerson(self, outputSchemaName, outputTableName, retriesLeft=3):
    #     md = self.mainDialog
    #     queries = []

    #     query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_lammonsaato_tco2_per_sum_yhteensa_tco2 real"
    #     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #     queries.append(query)

    #     query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_lammonsaato_tco2_per_asukas real"
    #     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #     queries.append(query)

    #     query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_lammonsaato_tco2_per_sum_yhteensa_tco2 = (sum_lammonsaato_tco2 / NULLIF(sum_yhteensa_tco2 , 0))"
    #     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #     queries.append(query)

    #     query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_lammonsaato_tco2_per_asukas = (sum_lammonsaato_tco2 / NULLIF(pop, 0))"
    #     # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
    #     queries.append(query)

    #     try:
    #         self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
    #     except Exception as e:
    #         if retriesLeft > 0:
    #             return self.calculateThermoEmissionsPerPerson(outputSchemaName, outputTableName, retriesLeft - 1)
    #         else:
    #             self.iface.messageBar().pushMessage(
    #                 self.tr('Error in connecting to the database'),
    #                 str(e), Qgis.Warning, duration=0)
    #             return False

    #     try:
    #         cur = self.databaseConnection.cursor()
    #         for query in queries:
    #             cur.execute(query)
    #             self.databaseConnection.commit()
    #     except Exception as e:
    #         self.iface.messageBar().pushMessage(
    #             self.tr('Error in modifying the results table ') + "{}".format(query),
    #             str(e), Qgis.Warning, duration=0)
    #         self.databaseConnection.rollback()
    #         self.databaseConnection.close()

    #         return False

    #     return True


    def calculateRelativeTrafficEmissionsToDatabase(self, outputSchemaName, outputTableName, retriesLeft=3):
        md = self.mainDialog
        queries = []

        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_liikenne_tco2_per_sum_yhteensa_tco2 real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)
        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_liikenne_tco2_per_asukas real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN liikenne_hlo_tco2_per_sum_liikenne_tco2 real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)
        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN liikenne_hlo_tco2_per_sum_yhteensa_tco2 real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)
        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN liikenne_hlo_tco2_per_asukas real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)
        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN liikenne_hlo_tco2_per_tp real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)
        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN liikenne_hlo_tco2_per_as_tp real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)


        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_liikenne_tco2_per_sum_yhteensa_tco2 = (sum_liikenne_tco2 / NULLIF(sum_yhteensa_tco2, 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_liikenne_tco2_per_asukas = (sum_liikenne_tco2 / NULLIF(pop, 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET liikenne_hlo_tco2_per_sum_liikenne_tco2 = (liikenne_hlo_tco2 / NULLIF(sum_liikenne_tco2, 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET liikenne_hlo_tco2_per_sum_yhteensa_tco2 = (liikenne_hlo_tco2 / NULLIF(sum_yhteensa_tco2, 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET liikenne_hlo_tco2_per_asukas = (liikenne_hlo_tco2 / NULLIF(pop, 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET liikenne_hlo_tco2_per_tp = (liikenne_hlo_tco2 / NULLIF(employ, 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)
   
        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET liikenne_hlo_tco2_per_as_tp = (liikenne_hlo_tco2 / NULLIF(COALESCE(pop, 0) + COALESCE(employ, 0), 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        try:
            self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
        except Exception as e:
            if retriesLeft > 0:
                return self.calculateRelativeTrafficEmissionsToDatabase(outputSchemaName, outputTableName, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
                    str(e), Qgis.Warning, duration=0)
                return False

        try:
            cur = self.databaseConnection.cursor()
            for query in queries:
                cur.execute(query)
                self.databaseConnection.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Error in modifying the results table ') + "{}".format(query),
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()
            self.databaseConnection.close()

            return False

        return True

    def calculatePopJobMix(self, outputSchemaName, outputTableName, retriesLeft=3):
        md = self.mainDialog
        queries = []

        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN pop_per_popjob_percentage numeric(10, 1)"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET pop_per_popjob_percentage = (COALESCE(pop, 0)::real / NULLIF(COALESCE(pop, 0) + COALESCE(employ, 0), 0) * 100)"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)


        try:
            self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
        except Exception as e:
            if retriesLeft > 0:
                return self.calculatePopJobMix(outputSchemaName, outputTableName, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
                    str(e), Qgis.Warning, duration=0)
                return False

        try:
            cur = self.databaseConnection.cursor()
            for query in queries:
                cur.execute(query)
                self.databaseConnection.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Error in modifying the results table ') + "{}".format(query),
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()
            self.databaseConnection.close()

            return False

        return True



    def calculateEmissionsPerFloorSpaceSquares(self, outputSchemaName, outputTableName, retriesLeft=3):
        md = self.mainDialog
        queries = []

        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_yhteensa_tco2_per_kem real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_yhteensa_tco2_per_kem = (sum_yhteensa_tco2 / NULLIF(floorspace, 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)


        try:
            self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
        except Exception as e:
            if retriesLeft > 0:
                return self.calculateEmissionsPerFloorSpaceSquares(outputSchemaName, outputTableName, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
                    str(e), Qgis.Warning, duration=0)
                return False

        try:
            cur = self.databaseConnection.cursor()
            for query in queries:
                cur.execute(query)
                self.databaseConnection.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Error in modifying the results table ') + "{}".format(query),
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()
            self.databaseConnection.close()

            return False

        return True


    def calculateEmissionsPerPersonJob(self, outputSchemaName, outputTableName, retriesLeft=3):
        md = self.mainDialog
        queries = []

        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_yhteensa_tco2_per_as_tp real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_yhteensa_tco2_per_as_tp = (sum_yhteensa_tco2 / NULLIF(COALESCE(pop, 0) + COALESCE(employ, 0), 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)
        

        try:
            self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
        except Exception as e:
            if retriesLeft > 0:
                return self.calculateEmissionsPerPersonJob(outputSchemaName, outputTableName, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
                    str(e), Qgis.Warning, duration=0)
                return False

        try:
            cur = self.databaseConnection.cursor()
            for query in queries:
                cur.execute(query)
                self.databaseConnection.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Error in modifying the results table ') + "{}".format(query),
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()
            self.databaseConnection.close()

            return False

        return True

    def calculateEmissionsPerPerson(self, outputSchemaName, outputTableName, retriesLeft=3):
        md = self.mainDialog
        queries = []

        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_yhteensa_tco2_per_asukas real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)

        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_yhteensa_tco2_per_asukas = (sum_yhteensa_tco2 / NULLIF(pop, 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)


        try:
            self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
        except Exception as e:
            if retriesLeft > 0:
                return self.calculateEmissionsPerPerson(outputSchemaName, outputTableName, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
                    str(e), Qgis.Warning, duration=0)
                return False

        try:
            cur = self.databaseConnection.cursor()
            for query in queries:
                cur.execute(query)
                self.databaseConnection.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Error in modifying the results table ') + "{}".format(query),
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()
            self.databaseConnection.close()

            return False

        return True


    def calculateEmissionsPerJob(self, uid, outputSchemaName, outputTableName, retriesLeft=3):
        md = self.mainDialog
        queries = []

        query = "ALTER TABLE " + outputSchemaName + ".\"" + outputTableName + "\" ADD COLUMN sum_yhteensa_tco2_per_tp real"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)
        
        query = "UPDATE " + outputSchemaName + ".\"" + outputTableName + "\" AS out_grid SET sum_yhteensa_tco2_per_tp = (sum_yhteensa_tco2 / NULLIF(employ, 0))"
        # QgsMessageLog.logMessage("query: " + query, 'YKRTool', Qgis.Info)
        queries.append(query)


        try:
            self.databaseConnection.createDbConnection(self.databaseConnection.getConnParams())
        except Exception as e:
            if retriesLeft > 0:
                return self.calculateEmissionsPerJob(outputSchemaName, outputTableName, retriesLeft - 1)
            else:
                self.iface.messageBar().pushMessage(
                    self.tr('Error in connecting to the database'),
                    str(e), Qgis.Warning, duration=0)
                return False

        try:
            cur = self.databaseConnection.cursor()
            for query in queries:
                cur.execute(query)
                self.databaseConnection.commit()
        except Exception as e:
            self.iface.messageBar().pushMessage(
                self.tr('Error in modifying the results table ') + "{}".format(query),
                str(e), Qgis.Warning, duration=0)
            self.databaseConnection.rollback()
            self.databaseConnection.close()

            return False

        self.databaseConnection.commit()

        return True
    

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
