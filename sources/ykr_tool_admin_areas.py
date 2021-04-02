


class YKRToolAdminAreas:
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
  
  def getAdminAreaNames(self):
    return self.AdminAreas.keys()
  

  def getAdminAreaNameMatchingAdminDatabaseTable(self, adminArea):
    return self.AdminAreas[adminArea]

  
  def getAdminAreaNameFromDatabaseTableName(self, adminAreatableName):
    key_list = list(self.AdminAreas.keys())
    val_list = list(self.AdminAreas.values())

    position = val_list.index(adminAreatableName)

    return key_list[position]

