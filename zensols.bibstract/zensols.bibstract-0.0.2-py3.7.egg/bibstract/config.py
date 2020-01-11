"""Application configuration class.

"""
__author__ = 'Paul Landes'

from zensols.actioncli import (
    CommandLineConfig,
    ExtendedInterpolationConfig,
)


class AppConfig(ExtendedInterpolationConfig, CommandLineConfig):
    def __init__(self, *args, **kwargs):
        super(AppConfig, self).__init__(*args, default_expect=True, **kwargs)

    def set_defaults(self, master_bib: str = None):
        self.set_default('master_bib', None, master_bib)
