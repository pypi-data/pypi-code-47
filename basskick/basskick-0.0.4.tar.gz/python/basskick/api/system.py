'''




'''

import sys
import os
import json

import logging
logger = logging.getLogger(__name__)

_SETTINGS = {}

class Settings(object):

    _THE = None

    @classmethod
    def THE(cls):
        if cls._THE is None:
            cls._THE = cls()
        return cls._THE

    def __init__(self):
        super(Settings, self).__init__()
        self._init_storage()

    def _init_storage(self):
        if self.__class__._THE is not None:
            raise Exception(
                'You can build more than one {} !'.format(
                    self.__class__,
                )
            )
        #FIXME: this wont work w/o admin authorisation :/
        self._storage_filename = os.path.join(sys.prefix, 'basskick_settings.json')
        if not os.path.exists(self._storage_filename):
            self._dump({})

    def _dump(self, data):
        with open(self._storage_filename, 'w') as fp:
            json.dump(data, fp)

    def _load(self):
        with open(self._storage_filename, 'r') as fp:
            return json.load(fp)

    def get(self, name, *default):
        data = self._load()
        return data.get(name, *default)

    def set(self, name, value):
        data = self._load()
        data[name] = value
        self._dump(data)

def get_setting(name, *default):
    return Settings.THE().get(name, *default)

def set_setting(name, value):
    logger.info('{!r} set to {!r}'.format(name, value))
    Settings.THE().set(name, value)

def get_install_dir():
    return get_setting('install_dir')

def set_install_dir(path):
    return set_setting('install_dir', path)

def install(version=None, repair=False, url=None):
    logger.info(
        'Installing {}Blender {}{}'.format(
            repair and '(or repair) ' or '',
            version and 'version {}'.format(version) or 'last version',
            url and ' from {}'.format(url) or ''
        )
    )

    # 1) download blender from https://download.blender.org/release/ or given url
    # 2) extract it to get_install_dir() under 'Blender <version>'
    # 3) check pip
    #    - if pip not there chech ensurepip
    #         - if ensure pip not there copy this env's ensurepip package to its python libs
    #         - run it with --b --python-expr "import ensurepip as ep; ep._main([])"
    #           => actually, try and use runpy.run_module() instead.

def run(app_name='blender', version=None):
    logger.info(
        'Running {}{}'.format(
            app_name,
            version and ' version {}'.format(version) or ''
        )
    )

