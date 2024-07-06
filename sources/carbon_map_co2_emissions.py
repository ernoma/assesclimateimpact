from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication, QEventLoop, QUrl, QSettings, QVariant
from PyQt5.QtWidgets import QDialogButtonBox

from qgis.core import (
    QgsTask, 
    QgsMessageLog, 
    Qgis, 
    QgsVectorLayer, 
    QgsProject, 
    QgsField, 
    QgsMapLayerProxyModel,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsGeometry,
    QgsVectorFileWriter
    )
from qgis import processing

import os.path
import json

class CarbonMapCO2Emissions:
    def __init__(self, ykrToolDictionaries, plugin_dir, iface):
        self.ykrToolDictionaries = ykrToolDictionaries
        self.plugin_dir = plugin_dir
        self.iface = iface
        
        self.combiningCarbonMapCO2EmissionsDialog = uic.loadUi(os.path.join(self.plugin_dir, 'ui', 'ykr_tool_carbon_stock_co2_emissions_combinining.ui'))

        self.first_start = True


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


    def setupCombiningCarbonMapCO2EmissionsDialog(self):
        self.combiningCarbonMapCO2EmissionsDialog.buttonBox.button(QDialogButtonBox.Ok).setText("Run")
        self.combiningCarbonMapCO2EmissionsDialog.mMapLayerComboBoxCO2Emissions.setFilters(QgsMapLayerProxyModel.PolygonLayer)
        self.combiningCarbonMapCO2EmissionsDialog.mMapLayerComboBoxCarbonMap.setFilters(QgsMapLayerProxyModel.PolygonLayer)


    def combineResults(self):
        cmDialog = self.combiningCarbonMapCO2EmissionsDialog

        if self.first_start:
            self.first_start = False
            self.setupCombiningCarbonMapCO2EmissionsDialog()

        cmDialog.show()
        # Run the dialog event loop
        result = cmDialog.exec_()
        # See if OK was pressed
        if result:
            """ TODO iterate plan areas by year (earliest, 2030, 2035, ...) and
                * with square intersections
                  ** add carbon stock change values on squares
                  ** caclulate sum of CO2 emissions - carbon stock
                  ** present results with and without plan changes
            """
            layerEmissions = cmDialog.mMapLayerComboBoxCO2Emissions.currentLayer()
            layerStocks = cmDialog.mMapLayerComboBoxCarbonMap.currentLayer()

            if layerEmissions.isValid() and layerStocks.isValid():
                featuresEmissions = layerEmissions.getFeatures()
                featuresStocks = layerStocks.getFeatures()

                # Find years
                firstStockYear = 2100
                yearsStocks = []
                for featureStocks in featuresStocks:
                    if featureStocks.attributeCount() > 0:
                        attrs = featureStocks.attributeMap()
                        for k in attrs.keys():
                            if ("_planned_") in k:
                                parts = k.split("_planned_")
                                year = int(parts[1])
                                if year not in yearsStocks:
                                    yearsStocks.append(year)
                                if year < firstStockYear:
                                    firstStockYear = year
                    else:
                        self.iface.messageBar().pushMessage(self.tr('The Carbon Map layer is not valid'), cmDialog.windowTitle(), Qgis.Warning)
                        return
                    break
                yearsStocks.sort()

                keyEmissionsYear = None
                yearsEmissions = []
                for featureEmissions in featuresEmissions:
                    if featureEmissions.attributeCount() > 0:
                        attrs = featureEmissions.attributeMap()
                        for k in attrs.keys():
                            if k == "year" or k == "vuosi":
                                keyEmissionsYear = k
                                year = int(featureEmissions[k])
                                if year not in yearsEmissions:
                                    yearsEmissions.append(year)
                                break
                    else:
                        self.iface.messageBar().pushMessage(self.tr('The CO2 emissions layer is not valid'), cmDialog.windowTitle(), Qgis.Warning)
                        return

                commonYears = set(yearsStocks) & set(yearsEmissions)

                # QgsMessageLog.logMessage(str(commonYears), 'Carbon Map and USCIAT', Qgis.Info)


                layerEmissions.selectAll()
                layerEmissionsClone = processing.run("native:saveselectedfeatures", {'INPUT': layerEmissions, 'OUTPUT': 'memory:'})['OUTPUT']
                layerEmissions.removeSelection()
                # QgsProject.instance().addMapLayer(clone_layer)


                # if layerEmissionsClone.dataProvider().fieldNameIndex("carbon_stock_change_total_planned") == -1 and layerEmissionsClone.dataProvider().fieldNameIndex("carbon_balance_total_planned_tco2"):
                layerEmissionsClone.startEditing()
                layerEmissionsClone.dataProvider().addAttributes([QgsField("carbon_stock_change_total_planned", QVariant.Double), QgsField("carbon_balance_total_planned_tco2", QVariant.Double)])
                layerEmissionsClone.updateFields()
                layerEmissionsClone.commitChanges()
                # else:
                #     self.iface.messageBar().pushMessage(self.tr('The Carbon Map layer is not valid'), cmDialog.windowTitle(), Qgis.Warning)

                crsSrc = QgsCoordinateReferenceSystem(layerStocks.crs().authid())
                crsDest = QgsCoordinateReferenceSystem('EPSG:3067')
                xformLayerStocks = QgsCoordinateTransform(crsSrc, crsDest, QgsProject.instance())

                crsSrc = QgsCoordinateReferenceSystem(layerEmissionsClone.crs().authid())
                crsDest = QgsCoordinateReferenceSystem('EPSG:3067')
                xformLayerEmissionsClone = QgsCoordinateTransform(crsSrc, crsDest, QgsProject.instance())

                for year in list(commonYears):
                    # QgsMessageLog.logMessage("year: " + str(year), 'Carbon Map and USCIAT', Qgis.Info)
                    layerEmissionsClone.setSubsetString(keyEmissionsYear + "=" + str(year))
                    featuresStocks = layerStocks.getFeatures()
                    layerEmissionsClone.startEditing()
                    for featureStocks in featuresStocks:
                        featureStocksGeometry = QgsGeometry(featureStocks.geometry())
                        featureStocksGeometry.transform(xformLayerStocks)
                        featureStocksArea = featureStocksGeometry.area()

                        featuresEmissions = layerEmissionsClone.getFeatures()
                        for featureEmissions in featuresEmissions:
                            featureEmissionsGeometry = QgsGeometry(featureEmissions.geometry())
                            featureEmissionsGeometry.transform(xformLayerEmissionsClone)
                            # if year == 2030:
                            #     QgsMessageLog.logMessage("year: " + str(year), 'Carbon Map and USCIAT', Qgis.Info)
                            if featureEmissions[keyEmissionsYear] == year and featureEmissionsGeometry.intersects(featureStocksGeometry):
                                intersectionArea = featureEmissionsGeometry.intersection(featureStocksGeometry).area()
                                multiplier = intersectionArea / featureStocksArea

                                carbon_stock_change_total_planned = multiplier * featureStocks["carbon_total_change_planned_" + str(firstStockYear) + "_" + str(year)]
                                featureEmissions['carbon_stock_change_total_planned'] = carbon_stock_change_total_planned

                                carbon_balance_total_planned_tco2 = featureEmissions['sum_yhteensa_tco2'] - featureEmissions['carbon_stock_change_total_planned']
                                featureEmissions['carbon_balance_total_planned_tco2'] = carbon_balance_total_planned_tco2
                                # if year == 2030:
                                #     QgsMessageLog.logMessage("multiplier: " + str(multiplier), 'Carbon Map and USCIAT', Qgis.Info)
                                #     QgsMessageLog.logMessage("carbon_stock_change_total_planned: " + str(carbon_stock_change_total_planned), 'Carbon Map and USCIAT', Qgis.Info)
                                #     QgsMessageLog.logMessage("carbon_balance_total_planned_tco2: " + str(carbon_balance_total_planned_tco2), 'Carbon Map and USCIAT', Qgis.Info)
                                layerEmissionsClone.updateFeature(featureEmissions)
                                # layerEmissionsClone.changeAttributeValue(featureEmissions.id())
                        
                    layerEmissionsClone.commitChanges()
                    layerEmissionsClone.setSubsetString("")

                outputFilePath = cmDialog.mQgsFileWidgetCombinedOutputFile.filePath()
                if outputFilePath != None and outputFilePath != '':
                    driverName = None
                    if outputFilePath.lower().endswith("gpkg"):
                        driverName = "GPKG"
                    elif outputFilePath.lower().endswith("shp"):
                       driverName = "ESRI Shapefile"
                    elif outputFilePath.lower().endswith("json"):
                       driverName = "GeoJSON"
                    else:
                        self.iface.messageBar().pushMessage(self.tr('Unsupported output file format'), cmDialog.windowTitle(), Qgis.Warning)
                        return
                    QgsVectorFileWriter.writeAsVectorFormat(layerEmissionsClone, outputFilePath, "UTF-8", layerEmissionsClone.crs(), driverName)
                
                    last_part = os.path.basename(os.path.normpath(outputFilePath))
                    layer_name = None
                    if '.' in last_part:
                        layer_name = last_part.split('.')[0]
                    else:
                        layer_name = last_part
                    layer = QgsVectorLayer(outputFilePath, layer_name,"ogr")
                    QgsProject.instance().addMapLayer(layer)
                else:    
                    QgsProject.instance().addMapLayer(layerEmissionsClone)
            else:
                self.iface.messageBar().pushMessage(self.tr('The selected layers are not valid'), cmDialog.windowTitle(), Qgis.Warning)
                return

            

