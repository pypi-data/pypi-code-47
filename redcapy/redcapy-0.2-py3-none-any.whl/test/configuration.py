import configparser


class Configuration:

    def __init__(self):
        config_file = './config.cfg'
        self.__config = configparser.ConfigParser()
        self.__config.read(config_file)

    def get_configuration(self, section=None):
        if section is not None:
            if section in self.__config:
                return self.__config[section]
        return self.__config
