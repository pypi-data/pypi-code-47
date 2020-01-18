# coding=utf-8
import configparser
from pod_base import ConfigException


class PodConfig:
    __config = None

    def __init__(self, config_path):
        self._config_path = config_path
        self.__read_config()

    def __read_config(self):
        """
        خواند تنظیمات از فایل کانفیگ
        """
        if PodConfig.__config is not None:
            return

        PodConfig.__config = configparser.ConfigParser()
        PodConfig.__config.read(self._config_path)

    @staticmethod
    def get(key, server_type, default=""):
        """
        دریافت تنظیمات از فایل کانفیگ

        :param str key:
        :param str server_type:
        :param str default:
        :return:
        """
        if server_type not in PodConfig.__config.sections():
            raise ConfigException("Can`t find settings for {0} mode".format(server_type))

        if key in PodConfig.__config[server_type]:
            return PodConfig.__config[server_type][key]

        return default
