


class YKRToolDictionaries:
    def __init__(self, iface, locale):

        self.iface = iface
        self.locale = locale

        self.PredefinedAreas = {
            "fi": {
                # 'Tampereen kaupunkiseutu (2021)': 'user_input.tre_seutu_kunnat',
                'Tampereen kaupunkiseudun rasu 2040 (2021)': 'user_input.seutu_rasu_2040_alue',
                'Kangasala (2.4.2021)': 'user_input.tre_seutu_kunta_kangasala',
                'Lempäälä (2.4.2021)': 'user_input.tre_seutu_kunta_lempaala',
                'Nokia (2.4.2021)': 'user_input.tre_seutu_kunta_nokia',
                'Orivesi (2.4.2021)': 'user_input.tre_seutu_kunta_orivesi',
                'Pirkkala (2.4.2021)': 'user_input.tre_seutu_kunta_pirkkala',
                'Tampere (2.4.2021)': 'user_input.tre_seutu_kunta_tampere',
                'Vesilahti (2.4.2021)': 'user_input.tre_seutu_kunta_vesilahti',
                'Ylöjärvi (2.4.2021)': 'user_input.tre_seutu_kunta_ylojarvi',
                'Tre ksoyk (yk048)': 'user_input.tre_ksoyk'
            },
            "en": {
                # 'Tampere City Region (2021)': 'user_input.tre_seutu_kunnat',
                'Tampere City Region Structural Plan 2040 (2021)': 'user_input.seutu_rasu_2040_alue',
                'Kangasala (2.4.2021)': 'user_input.tre_seutu_kunta_kangasala',
                'Lempäälä (2.4.2021)': 'user_input.tre_seutu_kunta_lempaala',
                'Nokia (2.4.2021)': 'user_input.tre_seutu_kunta_nokia',
                'Orivesi (2.4.2021)': 'user_input.tre_seutu_kunta_orivesi',
                'Pirkkala (2.4.2021)': 'user_input.tre_seutu_kunta_pirkkala',
                'Tampere (2.4.2021)': 'user_input.tre_seutu_kunta_tampere',
                'Vesilahti (2.4.2021)': 'user_input.tre_seutu_kunta_vesilahti',
                'Ylöjärvi (2.4.2021)': 'user_input.tre_seutu_kunta_ylojarvi',
                'Tre ksoyk (yk048)': 'user_input.tre_ksoyk'
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

        self.municipalitiesWithCodes = {
            'Kangasala': '211',
            'Lempaala': '418',
            'Nokia': '536',
            'Orivesi': '562',
            'Pirkkala': '604',
            'Tampere': '837',
            'Vesilahti': '922',
            'Ylojarvi': '980'
        }

        self.PredefinedFutureZoningAreas = {
            "fi": {
                'Tre kantakaupunki - yk049, valtuustokausi 2017-2021 - kaavaehdotus': 'user_input.kt_bau_kaavaehdotus',
                'Tre asemakaavoitusohjelma 2023-2027 (13.12.2022)': 'user_input.kt_ak_23_27_20221213_dev',
                'Nurmi-Sorila - yk049, valtuustokausi 2017-2021 - kaavaluonnos': 'user_input.kt_nurmi_sorila'
            },
            "en": {
                'Tampere downtown - Local master plan, City Council’s term 2017-2021 - plan proposal': 'user_input.kt_bau_kaavaehdotus',
                'Tre detailed land use planning program 2023-2027 (13.12.2022)': 'user_input.kt_ak_23_27_20221213_dev',
                'Tampere Nurmi-Sorila - Local master plan, City Council’s term 2017-2021 - plan draft': 'user_input.kt_nurmi_sorila'
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
                "tuotanto": "tuotanto",
                "hankinta": "hankinta"
            },
            "en": {
                "production": "tuotanto",
                "purchase": "hankinta"
            }
        }

        self.emissionAllocationMethod = {
            "fi": {
                'Energiamenetelmä': 'em',
                'Hyödynjakomenetelmä': 'hjm'
            },
            "en": {
                'Energy method': 'em',
                'Benefits division method': 'hjm'
            },
        }

        # self.electricityEmissionClass = {
        #     'Tuotanto': 'tuotanto',
        #     'Hankinta': 'hankinta'
        # }


        
        self.PredefinedUrbanCenterLayers = {
            "fi": {
                'Keskusverkko kaupunkiseutu, myös suunniteltu, 2023/07 tilanne': 'user_input.keskusverkko_tre_seutu_2023_07',
                'Keskusverkko kaupunkiseutu ja kantakaupunki - yk049, valtuustokausi 2017-2021 - kaavaehdotus': 'user_input.keskusverkko_tre_seutu_ve_yk049_vaihekaava_ehdotus',
                'Tre keskusverkko - yk049, valtuustokausi 2017-2021 - kaavaehdotus': 'user_input.kv_ehdotus_ve3'
            },
            "en": {
                'Urban centers of Tampere city region, also planned, 2023/07 situation': 'user_input.keskusverkko_tre_seutu_2023_07',
                'Urban centers of Tampere city region and downtown - Local master plan, City Council’s term 2017-2021 - plan proposal': 'user_input.keskusverkko_tre_seutu_ve_yk049_vaihekaava_ehdotus',
                'Tre centers - Local master plan, City Council’s term 2017-2021 - plan proposal': 'user_input.kv_ehdotus_ve3'
            }
        }


        self.PredefinedFuturePublicTransportStopsLayers = {
            "fi": {
                'Juna-asema- ja raitiotiepysäkkiverkko kaupunkiseutu, myös suunniteltu, 2023/07 tilanne': 'user_input.joli_lahijuna_ja_raitiotie_seutu_myos_suunniteltu_2023_07',
                'Juna-asema- ja raitiotiepysäkkiverkko kaupunkiseutu ja kantakaupunki - yk049, valtuustokausi 2017-2021 - kaavaehdotus': 'user_input.joli_lahijuna_ja_raitiotie_tre_seutu_ve_yk049_vaihekaava_ehdotu',
                'Juna-asema- ja raitiotiepysäkkiverkko - Tre asemakaavoitusohjelma 2023-2027': 'user_input.joli_lahijuna_ja_raitiotie_ak_23_27_v2'
            },
            "en": {
                'Railway and tram station transport stops of Tampere city region, also planned, 2023/07 situation': 'user_input.joli_lahijuna_ja_raitiotie_seutu_myos_suunniteltu_2023_07',
                'Railway and tram station transport stops of Tampere city region and downtown - Local master plan, City Council’s term 2017-2021 - plan proposal': 'user_input.joli_lahijuna_ja_raitiotie_tre_seutu_ve_yk049_vaihekaava_ehdotu',
                'Railway and tram station transport stops - Tre detailed land use planning program 2023-2027': 'user_input.joli_lahijuna_ja_raitiotie_ak_23_27_v2'
            }
        }

        # the list of YKR zones
        self.PredefinedUrbanRuralZoningAreas = {
            "fi": {
                'Keskustan jalankulkuvyöhyke': '1',
                'Keskustan reunavyöhyke': '2',
                'Intensiivinen joukkoliikennevyöhyke': '3',
                'Joukkoliikennevyöhyke': '4',
                'Autovyöhyke': '5',
                'Alakeskuksen jalankulkuvyöhyke': '10',
                'Sisempi kaupunkialue': '81',
                'Ulompi kaupunkialue': '82',
                'Kaupungin kehysalue': '83',
                'Maaseudun paikalliskeskus': '84',
                'Kaupungin läheinen maaseutu': '85',
                'Ydinmaaseutu': '86',
                'Harvaan asuttu maaseutu': '87',
                'Hervanta (alakeskus, HLT:ssä eroja)': '837101'
            },
            "en": {
                'Pedestrian zone': '1',
                'Fringe of pedestrian zone': '2',
                'Intensive transit zone': '3',
                'Transit zone': '4',
                'Car-oriented zone': '5',
                'Pedestrian zone of a subcentre': '10',
                'Inner urban area': '81',
                'Outer urban area': '82',
                'Peri-urban area': '83',
                'Local centres in rural areas': '84',
                'Rural areas close to urban areas': '85',
                'Rural heartland areas': '86',
                'Sparsely populated rural areas': '87',
                'Hervanta (subcentre, HLT differs)': '837101'
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



    def getMunicipalityCode(self, municipalityName):
        return self.municipalitiesWithCodes[municipalityName]


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


    def getPredefinedFutureZoningAreaNumber(self, predefinedFutureZoningAreasUserFriendlyName):
        if self.locale not in self.PredefinedFutureZoningAreas:
            return self.PredefinedFutureZoningAreas["en"][predefinedFutureZoningAreasUserFriendlyName]
        else:
            return self.PredefinedFutureZoningAreas[self.locale][predefinedFutureZoningAreasUserFriendlyName]


    def getPredefinedFutureZoningAreaUserFriendlyName(self, PredefinedFutureZoningAreaNumber):
        if self.locale not in self.PredefinedFutureZoningAreas:
            key_list = list(self.PredefinedFutureZoningAreas["en"].keys())
            val_list = list(self.PredefinedFutureZoningAreas["en"].values())
        else:
            key_list = list(self.PredefinedFutureZoningAreas[self.locale].keys())
            val_list = list(self.PredefinedFutureZoningAreas[self.locale].values())

        try:
            position = val_list.index(PredefinedFutureZoningAreaNumber)
        except ValueError as e:
            return PredefinedFutureZoningAreaNumber

        return key_list[position]

    ##

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


    def getPredefinedFutureUrbanCenterNameFromDatabaseTableName(self, PredefinedFutureUrbanCenterTableName):
        if self.locale not in self.PredefinedUrbanCenterLayers:
            key_list = list(self.PredefinedUrbanCenterLayers["en"].keys())
            val_list = list(self.PredefinedUrbanCenterLayers["en"].values())
        else:
            key_list = list(self.PredefinedUrbanCenterLayers[self.locale].keys())
            val_list = list(self.PredefinedUrbanCenterLayers[self.locale].values())

        try:
            position = val_list.index(PredefinedFutureUrbanCenterTableName)
        except ValueError as e:
            return PredefinedFutureUrbanCenterTableName

        return key_list[position]
 
    ##

    def getPredefinedFuturePublicTransportStopsUserFriendlyNames(self):
        if self.locale not in self.PredefinedFuturePublicTransportStopsLayers:
            return self.PredefinedFuturePublicTransportStopsLayers["en"].keys()
        else:
            return self.PredefinedFuturePublicTransportStopsLayers[self.locale].keys()


    def getPredefinedFuturePublicTransportStopsDatabaseTableName(self, predefinedFuturePublicTransportStopsUserFriendlyName):
        if self.locale not in self.PredefinedFuturePublicTransportStopsLayers:
            return self.PredefinedFuturePublicTransportStopsLayers["en"][predefinedFuturePublicTransportStopsUserFriendlyName]
        else:
            return self.PredefinedFuturePublicTransportStopsLayers[self.locale][predefinedFuturePublicTransportStopsUserFriendlyName]


    def getPredefinedFuturePublicTransportStopsNameFromDatabaseTableName(self, PredefinedFuturePublicTransportStopsTableName):
        if self.locale not in self.PredefinedFuturePublicTransportStopsLayers:
            key_list = list(self.PredefinedFuturePublicTransportStopsLayers["en"].keys())
            val_list = list(self.PredefinedFuturePublicTransportStopsLayers["en"].values())
        else:
            key_list = list(self.PredefinedFuturePublicTransportStopsLayers[self.locale].keys())
            val_list = list(self.PredefinedFuturePublicTransportStopsLayers[self.locale].values())

        try:
            position = val_list.index(PredefinedFuturePublicTransportStopsTableName)
        except ValueError as e:
            return PredefinedFuturePublicTransportStopsTableName

        return key_list[position]

    ##
    ##
    ##
            
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

    def getPredefinedEmissionAllocationMethodName(self, EmissionAllocationMethodName):
        if self.locale not in self.emissionAllocationMethod:
            key_list = list(self.emissionAllocationMethod["en"].keys())
            val_list = list(self.emissionAllocationMethod["en"].values())
        else:
            key_list = list(self.emissionAllocationMethod[self.locale].keys())
            val_list = list(self.emissionAllocationMethod[self.locale].values())

        try:
            position = val_list.index(EmissionAllocationMethodName)
        except ValueError as e:
            return EmissionAllocationMethodName

        return key_list[position]


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
    
    def getPredefinedElectricityTypeName(self, ElectricityTypeName):
        if self.locale not in self.electricityEmissionClasses:
            key_list = list(self.electricityEmissionClasses["en"].keys())
            val_list = list(self.electricityEmissionClasses["en"].values())
        else:
            key_list = list(self.electricityEmissionClasses[self.locale].keys())
            val_list = list(self.electricityEmissionClasses[self.locale].values())

        try:
            position = val_list.index(ElectricityTypeName)
        except ValueError as e:
            return ElectricityTypeName

        return key_list[position]

    
    def getPredefinedUrbanRuralZoningAreaKeys(self):
        if self.locale not in self.PredefinedUrbanRuralZoningAreas:
            return self.PredefinedUrbanRuralZoningAreas["en"].keys()
        else:
            return self.PredefinedUrbanRuralZoningAreas[self.locale].keys()
        
    def getPredefinedUrbanRuralZoningAreaValue(self, userFriendlyName):
        if self.locale not in self.PredefinedUrbanRuralZoningAreas:
            return self.PredefinedUrbanRuralZoningAreas["en"][userFriendlyName]
        else:
            return self.PredefinedUrbanRuralZoningAreas[self.locale][userFriendlyName]
        
    def getPredefinedUrbanRuralZoningAreaName(self, predefinedUrbanRuralZoningAreaValue):
        if self.locale not in self.PredefinedUrbanRuralZoningAreas:
            key_list = list(self.PredefinedUrbanRuralZoningAreas["en"].keys())
            val_list = list(self.PredefinedUrbanRuralZoningAreas["en"].values())
        else:
            key_list = list(self.PredefinedUrbanRuralZoningAreas[self.locale].keys())
            val_list = list(self.PredefinedUrbanRuralZoningAreas[self.locale].values())

        try:
            position = val_list.index(predefinedUrbanRuralZoningAreaValue)
        except ValueError as e:
            return predefinedUrbanRuralZoningAreaValue

        return key_list[position]
    
