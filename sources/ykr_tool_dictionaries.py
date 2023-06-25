


class YKRToolDictionaries:
    def __init__(self, iface, locale):

        self.iface = iface
        self.locale = locale

        self.PredefinedAreas = {
            "fi": {
                'Tre ksoyk (yk048)': 'user_input.tre_ksoyk',
                'Tampereen kaupunkiseutu': 'user_input.tre_seutu_kunnat',
                'Tampereen kaupunkiseudun rakennesuunnitelma 2040': 'user_input.seutu_rasu_2040_alue',
                'Kangasala (2.4.2021)': 'user_input.tre_seutu_kunta_kangasala',
                'Lempäälä (2.4.2021)': 'user_input.tre_seutu_kunta_lempaala',
                'Nokia (2.4.2021)': 'user_input.tre_seutu_kunta_nokia',
                'Orivesi (2.4.2021)': 'user_input.tre_seutu_kunta_orivesi',
                'Pirkkala (2.4.2021)': 'user_input.tre_seutu_kunta_pirkkala',
                'Tampere (2.4.2021)': 'user_input.tre_seutu_kunta_tampere',
                'Vesilahti (2.4.2021)': 'user_input.tre_seutu_kunta_vesilahti',
                'Ylöjärvi (2.4.2021)': 'user_input.tre_seutu_kunta_ylojarvi'
            },
            "en": {
                'Tre ksoyk (yk048)': 'user_input.tre_ksoyk',
                'Tampere City Region': 'user_input.tre_seutu_kunnat',
                'Tampere City Region Structural Plan 2040': 'user_input.seutu_rasu_2040_alue',
                'Kangasala (2.4.2021)': 'user_input.tre_seutu_kunta_kangasala',
                'Lempäälä (2.4.2021)': 'user_input.tre_seutu_kunta_lempaala',
                'Nokia (2.4.2021)': 'user_input.tre_seutu_kunta_nokia',
                'Orivesi (2.4.2021)': 'user_input.tre_seutu_kunta_orivesi',
                'Pirkkala (2.4.2021)': 'user_input.tre_seutu_kunta_pirkkala',
                'Tampere (2.4.2021)': 'user_input.tre_seutu_kunta_tampere',
                'Vesilahti (2.4.2021)': 'user_input.tre_seutu_kunta_vesilahti',
                'Ylöjärvi (2.4.2021)': 'user_input.tre_seutu_kunta_ylojarvi'
            }
        }

        self.ykrPopTables = {
            "fi": {
                'Kaupunkiseudun väestö 1/2021': '-',
                'SYKE YKR väestö Pirkanmaa 2019': 'user_input.ykr_vaesto_2019_pirkanmaa'
            },
            "en": {
                'Tampere City Region Population 1/2021': '-',
                'SYKE YKR Population Pirkanmaa 2019': 'user_input.ykr_vaesto_2019_pirkanmaa'
            }
        }

        self.ykrJobTables = {
            "fi": {
                'SYKE YKR työpaikat Pirkanmaa 2017': 'user_input.YKR_tyopaikat_2017_Pirkanmaa'
            },
            "en": {
                'SYKE YKR workplaces Pirkanmaa 2017': 'user_input.YKR_tyopaikat_2017_Pirkanmaa'
            }
        }


        self.PredefinedFutureZoningAreas = {
            "fi": {
                'Kantakaupunki (yk049, valtuustokausi 2017-2021) - ehdotus': 'user_input.kt_bau_kaavaehdotus',
                'Nurmi-Sorila (yk049, valtuustokausi 2017-2021) - luonnos': 'user_input.kt_nurmi_sorila'
            },
            "en": {
                'Tampere downtown (Local master plan, City Council’s term 2017-2021) - proposal': 'user_input.kt_bau_kaavaehdotus',
                'Tampere Nurmi-Sorila (Local master plan, City Council’s term 2017-2021) - draft': 'user_input.kt_nurmi_sorila'
            }
        }

        self.PITKOScenarios = {
            "fi": {
                "static": "static",
                "kasvu": "kasvu",
                "wem": "wem",
                "eu80": "eu80",
                "muutos": "muutos",
                "saasto": "saasto",
                "pysahdys": "pysahdys"
            },
            "en": {
                "static": "static",
                "growth": "kasvu",
                "wem": "wem", 
                "eu80": "eu80", 
                "change": "muutos", 
                "saving": "saasto", 
                "stagnation": "pysahdys"
            }
        }


        self.electricityEmissionClasses = {
            "fi": {
                "hankinta": "hankinta",
                "tuotanto": "tuotanto"
            },
            "en": {
                "purchase": "hankinta",
                "production": "tuotanto"
            }
        }

        self.emissionAllocationMethod = {
            "fi": {
                'Hyödynjakomenetelmä': 'hjm',
                'Energiamenetelmä': 'em'
            },
            "en": {
                'Benefits division method': 'hjm',
                'Energy method': 'em'
            },
        }

        # self.electricityEmissionClass = {
        #     'Tuotanto': 'tuotanto',
        #     'Hankinta': 'hankinta'
        # }


        
        self.PredefinedUrbanCenterLayers = {
            "fi": {
                'Keskusverkko kaupunkiseutu ja kantakaupunki (yk049, valtuustokausi 2017-2021) - ehdotus': 'user_input.keskusverkko_tre_seutu_ve_yk049_vaihekaava_ehdotus'
            },
            "en": {
                'Urban centers of Tampere city region and downtown (Local master plan, City Council’s term 2017-2021) - proposal': 'user_input.keskusverkko_tre_seutu_ve_yk049_vaihekaava_ehdotus'
            }
        }



    def getPITKOScenarioNames(self):
        if self.locale not in self.PITKOScenarios:
            return self.PITKOScenarios["en"].keys()
        else:
            return self.PITKOScenarios[self.locale].keys()


    def getPITKOScenarioShortName(self, userFriendlyName):
        if self.locale not in self.PITKOScenarios:
            return self.PITKOScenarios["en"][userFriendlyName]
        else:
            return self.PITKOScenarios[self.locale][userFriendlyName]


    def getElectricityTypeNames(self):
        if self.locale not in self.electricityEmissionClasses:
            return self.electricityEmissionClasses["en"].keys()
        else:
            return self.electricityEmissionClasses[self.locale].keys()

    def getElectricityTypeShortName(self, userFriendlyName):
        if self.locale not in self.electricityEmissionClasses:
            return self.electricityEmissionClasses["en"][userFriendlyName]
        else:
            return self.electricityEmissionClasses[self.locale][userFriendlyName]


    def getPredefinedAreaNames(self):
        if self.locale not in self.PredefinedAreas:
            return self.PredefinedAreas["en"].keys()
        else:
            return self.PredefinedAreas[self.locale].keys()


    def getPredefinedAreaDatabaseTableName(self, PredefinedArea):
        if self.locale not in self.PredefinedAreas:
            return self.PredefinedAreas["en"][PredefinedArea]
        else:
            return self.PredefinedAreas[self.locale][PredefinedArea]
        

    
    def getPredefinedAreaNameFromDatabaseTableName(self, PredefinedAreaTableName):
        if self.locale not in self.PredefinedAreas:
            key_list = list(self.PredefinedAreas["en"].keys())
            val_list = list(self.PredefinedAreas["en"].values())
        else:
            key_list = list(self.PredefinedAreas[self.locale].keys())
            val_list = list(self.PredefinedAreas[self.locale].values())

        try:
            position = val_list.index(PredefinedAreaTableName)
        except ValueError as e:
            return PredefinedAreaTableName

        return key_list[position]


    def getYkrPopUserFriendlyNames(self):
        if self.locale not in self.ykrPopTables:
            return self.ykrPopTables["en"].keys()
        else:
            return self.ykrPopTables[self.locale].keys()


    def getYkrPopTableDatabaseTableName(self, ykrPopUserFriendlyName):
        if self.locale not in self.ykrPopTables:
            return self.ykrPopTables["en"][ykrPopUserFriendlyName]
        else:
            return self.ykrPopTables[self.locale][ykrPopUserFriendlyName]


    def getYkrJobUserFriendlyNames(self):
        if self.locale not in self.ykrJobTables:
            return self.ykrJobTables["en"].keys()
        else:
            return self.ykrJobTables[self.locale].keys()


    def getYkrJobTableDatabaseTableName(self, ykrJobUserFriendlyName):
        if self.locale not in self.ykrJobTables:
            return self.ykrJobTables["en"][ykrJobUserFriendlyName]
        else:
            return self.ykrJobTables[self.locale][ykrJobUserFriendlyName]

    
    def getPredefinedFutureZoningAreasUserFriendlyNames(self):
        if self.locale not in self.PredefinedFutureZoningAreas:
            return self.PredefinedFutureZoningAreas["en"].keys()
        else:
            return self.PredefinedFutureZoningAreas[self.locale].keys()


    def getPredefinedFutureZoningAreasDatabaseTableName(self, predefinedFutureZoningAreasUserFriendlyName):
        if self.locale not in self.PredefinedFutureZoningAreas:
            return self.PredefinedFutureZoningAreas["en"][predefinedFutureZoningAreasUserFriendlyName]
        else:
            return self.PredefinedFutureZoningAreas[self.locale][predefinedFutureZoningAreasUserFriendlyName]


    def getEmissionAllocationMethodNames(self):
        if self.locale not in self.emissionAllocationMethod:
            return self.emissionAllocationMethod["en"].keys()
        else:
            return self.emissionAllocationMethod[self.locale].keys()


    def getEmissionAllocationMethodShortName(self, emissionAllocationMethodUserFriendlyName):
        if self.locale not in self.emissionAllocationMethod:
            return self.emissionAllocationMethod["en"][emissionAllocationMethodUserFriendlyName]
        else:
            return self.emissionAllocationMethod[self.locale][emissionAllocationMethodUserFriendlyName]


    def getPredefinedUrbanCenterLayersUserFriendlyNames(self):
        if self.locale not in self.PredefinedUrbanCenterLayers:
            return self.PredefinedUrbanCenterLayers["en"].keys()
        else:
            return self.PredefinedUrbanCenterLayers[self.locale].keys()


    def getPredefinedUrbanCenterLayersDatabaseTableName(self, predefinedUrbanCenterLayersUserFriendlyName):
        if self.locale not in self.PredefinedUrbanCenterLayers:
            return self.PredefinedUrbanCenterLayers["en"][predefinedUrbanCenterLayersUserFriendlyName]
        else:
            return self.PredefinedUrbanCenterLayers[self.locale][predefinedUrbanCenterLayersUserFriendlyName]

            