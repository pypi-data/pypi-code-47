# -*- coding: utf-8 -*-
# author:      hj
# create_time: 2020/1/8 17:04
# update_time: 2020/1/8 17:04


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class YamlConfigurationUtils(metaclass=Singleton):
    def __init__(self):
        self._config = {}
        self._caches = {}

    @staticmethod
    def instance():
        return YamlConfigurationUtils()

    def initialization(self, config_file_path):
        import yaml
        with open(config_file_path, "r") as fp:
            self._config = yaml.safe_load(fp.read())

    def acquire_config(self):
        return self._config

    def get_node_value(self, path, default=None):
        return YamlReaderUtils.get_node_value(self._config, path, default)


class YamlReaderUtils(object):

    @staticmethod
    def get_node_value(data, keys_str, default=''):
        keys = keys_str.split('.')
        value = YamlReaderUtils._get_value(data, keys)
        if value is None:
            value = default
        return value

    @staticmethod
    def _get_value(data, keys):
        size = len(keys)
        for index, key in enumerate(keys, 1):
            value = data.get(key)
            if size == index:
                return value
            if value:
                return YamlReaderUtils._get_value(value, keys[index:size])
            return None




