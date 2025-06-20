
from PyQt5 import uic
from PyQt5.QtCore import QSettings

from qgis.core import (Qgis)
from qgis.gui import QgsFileWidget

import os.path
import psycopg2
from configparser import ConfigParser



def createDbConnection(connParams):
    '''Creates a database connection and cursor based on connection params'''
    if '' in list(connParams.values()):
        raise Exception('Virhe yhdistäessä tietokantaan: täytä puuttuvat yhteystiedot')
    try:
        conn = psycopg2.connect(host=connParams['host'],\
            port=connParams['port'], database=connParams['database'],\
            user=connParams['user'], password=connParams['password'],\
            connect_timeout=3)
        return conn
    except Exception as e:
        raise e


class YKRDatabaseConnection:
    def __init__(self, iface):

        self.iface = iface
        self.conn = None
        self.connParams = None

        self.plugin_dir = os.path.split(os.path.dirname(__file__))[0]

        self.databaseSettingsDialog = uic.loadUi(os.path.join(self.plugin_dir, 'ui', 'ykr_tool_db_settings.ui'))

        self.loadDatabaseConnectionSettingsAutomatically = True if QSettings().value("/YKRTool/loadDatabaseConnectionSettingsAutomatically", "True", type=str).lower() == 'true' else False
        if self.loadDatabaseConnectionSettingsAutomatically:
            configFilePath = QSettings().value("/YKRTool/configFilePath", "", type=str)
            if configFilePath != "":
                self.connParams = self.parseConfigFile(configFilePath)
        

    def parseConfigFile(self, filePath):
        '''Reads configuration file and returns parameters as a dict'''
        # Setup an empty dict with correct keys to avoid keyerrors
        dbParams = {
            'host': '',
            'port': '',
            'database': '',
            'user': '',
            'password': ''
        }
        if not os.path.exists(filePath):
            self.iface.messageBar().pushMessage(self.tr('Error'), self.tr('File could not be read'),\
                Qgis.Warning)
            return dbParams

        parser = ConfigParser()
        parser.read(filePath)
        if parser.has_section('postgresql'):
            params = parser.items('postgresql')
            for param in params:
                dbParams[param[0]] = param[1]
        else:
            self.iface.messageBar().pushMessage(self.tr('Error'), self.tr('File does not contain database connection parameters'), Qgis.Warning)

        return dbParams
    

    def displayDatabaseSettingsDialog(self):
        '''Sets up and displays the settings dialog'''
        self.databaseSettingsDialog.show()
        self.databaseSettingsDialog.configFileInput.setStorageMode(QgsFileWidget.GetFile)
        configFilePath = QSettings().value("/YKRTool/configFilePath", "", type=str)
        self.databaseSettingsDialog.configFileInput.setFilePath(configFilePath)
        
        if self.loadDatabaseConnectionSettingsAutomatically:
            if configFilePath != "":
                self.setConnectionParamsFromFile()
                # self.ykrZonesStats.setConnectionParams(self.connParams)

        self.databaseSettingsDialog.loadFileButton.clicked.connect(self.setConnectionParamsFromFile)

        result = self.databaseSettingsDialog.exec_()
        if result:
            self.connParams = self.readConnectionParamsFromInput()
            # self.ykrZonesStats.setConnectionParams(self.connParams)


    def setConnectionParamsFromFile(self):
        '''Reads connection parameters from file and sets them to the input fields'''
        filePath = self.databaseSettingsDialog.configFileInput.filePath()
        QSettings().setValue("/YKRTool/configFilePath", filePath)

        try:
            dbParams = self.parseConfigFile(filePath)
        except Exception as e:
            self.iface.messageBar().pushMessage(self.tr('Error in reading a file'),\
                str(e), Qgis.Warning, duration=10)

        self.setConnectionParamsFromInput(dbParams)

    
    def setConnectionParamsFromInput(self, params):
        '''Sets connection parameters to input fields'''
        self.databaseSettingsDialog.dbHost.setValue(params['host'])
        self.databaseSettingsDialog.dbPort.setValue(params['port'])
        self.databaseSettingsDialog.dbName.setValue(params['database'])
        self.databaseSettingsDialog.dbUser.setValue(params['user'])
        self.databaseSettingsDialog.dbPass.setText(params['password'])


    def readConnectionParamsFromInput(self):
        '''Reads connection parameters from user input and returns a dictionary'''
        params = {}
        params['host'] = self.databaseSettingsDialog.dbHost.value()
        params['port'] = self.databaseSettingsDialog.dbPort.value()
        params['database'] = self.databaseSettingsDialog.dbName.value()
        params['user'] = self.databaseSettingsDialog.dbUser.value()
        params['password'] = self.databaseSettingsDialog.dbPass.text()
        return params


    def setLoadDatabaseConnectionSettingsAutomatically(self, loadDatabaseConnectionSettingsAutomatically):
        self.loadDatabaseConnectionSettingsAutomatically = loadDatabaseConnectionSettingsAutomatically
        QSettings().setValue("/YKRTool/loadDatabaseConnectionSettingsAutomatically", 'True' if self.loadDatabaseConnectionSettingsAutomatically else 'False')


    def getConnParams(self):
        return self.connParams
    
    def rollback(self):
        self.conn.rollback()
    
    def commit(self):
        self.conn.commit()

    def close(self):
        if self.conn != None:
            self.conn.close()
            self.conn = None
    

    def createDbConnection(self, connParams):
        '''Creates a database connection and cursor based on connection params'''
        if '' in list(connParams.values()):
            raise Exception('Virhe yhdistäessä tietokantaan: täytä puuttuvat yhteystiedot')
        elif self.conn == None: 
            try:
                self.conn = psycopg2.connect(host=connParams['host'],\
                    port=connParams['port'], database=connParams['database'],\
                    user=connParams['user'], password=connParams['password'],\
                    connect_timeout=3)
                # return self.conn
            except Exception as e:
                raise e
        

    def cursor(self):
        return self.conn.cursor()
    

    def execute(self, query):
        cursor = self.cursor()
        cursor.execute(query)
        self.commit()


    def tableExists(self, schemaName, tableName):
        cursor = self.cursor()
        cursor.execute("select * from information_schema.tables where table_schema=%s AND table_name=%s", (schemaName, tableName,))
        exists = bool(cursor.rowcount)
        cursor.close()
        return exists


    def dropTable(self, schemaName, tableName):
        cursor = self.cursor()
        cursor.execute('DROP TABLE IF EXISTS "{}"."{}"'.format(schemaName, tableName))
        cursor.close()
