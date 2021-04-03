


class YKRToolDictionaries:
    def __init__(self):
        self.AdminAreas = {
            'Tampereen kaupunkiseutu': 'user_input.tre_seutu_kunnat',
            'Tampereen kaupunkiseudun rakennesuunnitelma 2040': 'tests.rasu',
            'Kangasala (2.4.2021)': 'user_input.tre_seutu_kunta_kangasala',
            'Lempäälä (2.4.2021)': 'user_input.tre_seutu_kunta_lempaala',
            'Nokia (2.4.2021)': 'user_input.tre_seutu_kunta_nokia',
            'Orivesi (2.4.2021)': 'user_input.tre_seutu_kunta_orivesi',
            'Pirkkala (2.4.2021)': 'user_input.tre_seutu_kunta_pirkkala',
            'Tampere (2.4.2021)': 'user_input.tre_seutu_kunta_tampere',
            'Vesilahti (2.4.2021)': 'user_input.tre_seutu_kunta_vesilahti',
            'Ylöjärvi (2.4.2021)': 'user_input.tre_seutu_kunta_ylojarvi',
            'Tampere (Tampereen yhdyskuntarakenteen ilmastovaikutukset -projekti)': 'aluejaot.kuntaraja_Tampere'
        }

        self.ykrPopTables = {
            'Kaupunkiseudun väestö 1/2021': '-',
            'YKR väestö Pirkanmaa 2019': 'user_input.ykr_vaesto_2019_pirkanmaa'
        }

        self.ykrJobTables = {
            'YKR työpaikat Pirkanmaa 2017': 'user_input.YKR_tyopaikat_2017_Pirkanmaa'
        }


    def getAdminAreaNames(self):
        return self.AdminAreas.keys()


    def getAdminAreaDatabaseTableName(self, adminArea):
        return self.AdminAreas[adminArea]

    
    def getAdminAreaNameFromDatabaseTableName(self, adminAreaTableName):
        key_list = list(self.AdminAreas.keys())
        val_list = list(self.AdminAreas.values())

        position = val_list.index(adminAreaTableName)

        return key_list[position]


    def getYkrPopUserFriendlyNames(self):
        return self.ykrPopTables.keys()


    def getYkrPopTableDatabaseTableName(self, ykrPopUserFriendlyName):
        return self.ykrPopTables[ykrPopUserFriendlyName]


    def getYkrJobUserFriendlyNames(self):
        return self.ykrJobTables.keys()


    def getYkrJobTableDatabaseTableName(self, ykrJobUserFriendlyName):
        return self.ykrJobTables[ykrJobUserFriendlyName]