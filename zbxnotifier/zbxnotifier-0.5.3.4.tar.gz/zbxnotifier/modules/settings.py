import keyring
from appdirs import *
import configparser
import os.path
import logging

logger = logging.getLogger('basic')

class Settings:
    config = None
    appname = "zbxnotifier"
    appauthor = "kovaxur"

    user_data_dir = None
    user_data_config_path = None

    logfile_path = None

    @staticmethod
    def init_basic_config():
        Settings.user_data_dir = user_data_dir(Settings.appname, Settings.appauthor)
        Settings.user_data_config_path = Settings.user_data_dir + '/zbxnotifier.ini'
        Settings.logfile_path = Settings.user_data_dir + '/zbxnotifier.log'

        if not os.path.exists(Settings.user_data_config_path):
            Settings.create_default_config()
            Settings.save_running_config()
        else:
            Settings.read_config_from_file()

    @staticmethod
    def create_default_config():
        logger.info("Generating default configuration file")
        Settings.config = configparser.ConfigParser()

        Settings.config.add_section('Application')
        Settings.config.set('Application', 'LogLevel', "INFO")
        Settings.config.set('Application', 'AlertTimeout', "5")

        Settings.config.add_section('WindowSettings')
        Settings.config.set('WindowSettings', 'title', "Zabbix Desktop Notification Tool")
        Settings.config.set('WindowSettings', 'height', str(500))
        Settings.config.set('WindowSettings', 'width', str(600))

        Settings.config.add_section('ProblemColors')
        Settings.config.set('ProblemColors', 'not_classified', '151:170:179')
        Settings.config.set('ProblemColors', 'information', '116:153:255')
        Settings.config.set('ProblemColors', 'warning', '255:200:89')
        Settings.config.set('ProblemColors', 'average', '255:160:89')
        Settings.config.set('ProblemColors', 'high', '233:118:89')
        Settings.config.set('ProblemColors', 'disaster', '228:89:89')

        Settings.config.add_section('AlertFilter')
        Settings.config.set('AlertFilter', 'group', '')
        Settings.config.set('AlertFilter', 'min-severity', '0')
        Settings.config.set('AlertFilter', 'exclude-tags', '')

        Settings.config.add_section('ZabbixSettings')
        Settings.config.set('ZabbixSettings', 'username', '')
        Settings.config.set('ZabbixSettings', 'server', '')

        try:
            logger.info("Getting password for the user.")
            Settings.config.set('ZabbixSettings', 'password', keyring.get_password("zabbix", Settings.config.get('ZabbixSettings', 'username')))
        except TypeError:
            logger.warning("Password not found on keyring, going with empty password.")
            Settings.config.set('ZabbixSettings', 'password', '')

        try:
            logger.info("Creating application directory in user folder.")
            os.makedirs(Settings.user_data_dir)
        except FileExistsError:
            pass
        except Exception as e:
            logger.critical("Error during user folder creation. Can't create the following folder PATH: " + str(Settings.user_data_dir))
            logger.critical("Error message: " + str(e))

    @staticmethod
    def save_running_config():
        logger.info("Running config save was triggered.")
        # We dont want to print the password into the settings file..
        temp_pw = Settings.config.get('ZabbixSettings', 'password')
        Settings.config.set('ZabbixSettings', 'password', 'XXXXXXXXXX')

        with open(Settings.user_data_config_path, 'w') as configfile:
            Settings.config.write(configfile)

        Settings.config.set('ZabbixSettings', 'password', temp_pw)

        # But we want to store the password on the keyring
        keyring.set_password("zabbix", Settings.config.get('ZabbixSettings', 'username'), temp_pw)

    @staticmethod
    def read_config_from_file():
        logger.info("Reading configuration from file: " + str(Settings.user_data_config_path))
        Settings.config = configparser.ConfigParser()
        Settings.config.read(Settings.user_data_dir + '/zbxnotifier.ini')

        try:
            Settings.config.set('ZabbixSettings', 'password', keyring.get_password("zabbix", "Admin"))
        except TypeError:
            logger.warning("Password not found on keyring, going with empty password.")
            Settings.config.set('ZabbixSettings', 'password', '')