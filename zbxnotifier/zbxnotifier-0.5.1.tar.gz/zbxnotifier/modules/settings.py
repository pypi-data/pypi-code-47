import sys

if sys.platform == 'darwin':
    import keyring.backends.OS_X
    keyring.set_keyring(keyring.backends.OS_X.Keyring())
else:
    import keyring.backends.Windows
    keyring.set_keyring(keyring.backends.Windows.WinVaultKeyring())

from appdirs import *
import configparser
import os.path


class Settings:
    config = None
    appname = "zbxnotifier"
    appauthor = "kovaxur"

    user_data_dir = None
    user_data_config_path = None

    @staticmethod
    def init_config():
        Settings.user_data_dir = user_data_dir(Settings.appname, Settings.appauthor)
        Settings.user_data_config_path = Settings.user_data_dir + '/zbxnotifier.ini'

        if not os.path.exists(Settings.user_data_config_path):
            Settings.create_default_config()
            Settings.save_running_config()
        else:
            Settings.read_config_from_file()

    @staticmethod
    def create_default_config():
        Settings.config = configparser.ConfigParser()

        Settings.config.add_section('WindowSettings')
        Settings.config.set('WindowSettings', 'title', "RoboAlert 3000")
        Settings.config.set('WindowSettings', 'height', str(500))
        Settings.config.set('WindowSettings', 'width', str(600))

        Settings.config.add_section('ZabbixSettings')
        Settings.config.set('ZabbixSettings', 'username', 'Admin')
        Settings.config.set('ZabbixSettings', 'server', 'http://192.168.1.160')

        password = keyring.get_password("zabbix", "Admin")
        if password is None:
            print("Password must be set in the Windows Credential store.")
            password = ''
        Settings.config.set('ZabbixSettings', 'password', password)

        try:
            os.makedirs(Settings.user_data_dir)
        except FileExistsError:
            pass

    @staticmethod
    def save_running_config():
        # We dont want to print the password into the settings file..
        temp_pw = Settings.config.get('ZabbixSettings', 'password')
        Settings.config.set('ZabbixSettings', 'password', 'XXXXXXXXXX')

        with open(Settings.user_data_config_path, 'w') as configfile:
            Settings.config.write(configfile)

        Settings.config.set('ZabbixSettings', 'password', temp_pw)

    @staticmethod
    def read_config_from_file():
        Settings.config = configparser.ConfigParser()
        Settings.config.read(Settings.user_data_dir + '/zbxnotifier.ini')
        Settings.config.set('ZabbixSettings', 'password', keyring.get_password("zabbix", "Admin"))