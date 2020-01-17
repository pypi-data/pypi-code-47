import re
from watched_schema import validators
from .cache import create_cache


class Config(object):
    cache = None
    repository = None
    addons = {}

    def set_cache(self, cache):
        if cache is None:
            cache = create_cache()
        self.cache = cache

    def register_addon(self, addon):
        if addon.id == 'addons':
            raise ValueError('Addon ID ' + addon.id +
                             ' for ' + addon.type + ' is forbidden')
        if addon.id in self.addons:
            raise ValueError('Addon ' + addon.id + ' already exists')
        if addon.type == 'repository':
            if self.repository:
                raise ValueError('Repository already set')
            self.repository = addon
        self.addons[addon.id] = addon


config = Config()
set_cache = config.set_cache
