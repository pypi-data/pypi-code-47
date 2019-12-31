""" Postgres Configuration """
from utils_package.py_utils import primary_utils
from utils_package.definitions import CONFIG_PARSER, LIB_DIR


class PGConfig:
    """ All methods for postgres configuration """

    def __init__(self):
        """ Set up class variables """
        self.def_pg_config_path = primary_utils.get_project_file('/data_controller/json_libraries/')
        self.env = primary_utils.get_current_env()
        self.utils = primary_utils

    def get_db_dict(self, user, db_name):
        """
        Method to build the proper database dictionary to generate a connection
        :param user: User that will be running the SQL command
        :param db_name: Name of the database the command will be run against
        :return: Dictionary of the user and connection informaiton
        """
        db_dict = {}
        pg_dict = self.__get_default_pg_override()
        db_dict['host'] = pg_dict['db_connections'][db_name]['server']
        db_dict['port'] = pg_dict['db_connections'][db_name]['port']
        db_dict['dbname'] = pg_dict['db_connections'][db_name]['db_name']
        db_dict['username'] = pg_dict['user_credentials'][self.env][user]['user']
        db_dict['password'] = pg_dict['user_credentials'][self.env][user]['password']
        return db_dict

    def get_smtp_dict(self, account):
        """
        Method to get the login dictionary to be used for SMTP accounts
        :param account: Account name
        :return: Login dictionary [user, pass]
        """
        login_dict = self.__read_config_file('smtp.json')
        login_dict = login_dict[account]
        return login_dict

    def __read_config_file(self, file_name):
        """
        Method to read the default config file for the postgres database
        :return: Dictionary of the config file
        """
        response = self.utils.open_file(file_name)
        return response

    def __get_default_pg_override(self):
        """
        Separate method to override the env settings
        :return:
        """
        pg_dict = self.utils.open_file('postgres.json')
        return pg_dict
