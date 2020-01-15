__author__ = 'v.denisov'

from ptst_swagger.config_host import ConfigHost as config

class SwaggerClient():

    def __init__(self):
        pass

    @classmethod
    def get_paths_sw(self):
        return config.paths_sw


