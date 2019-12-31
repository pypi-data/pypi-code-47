# -*- coding: utf-8 -*-


import logging


class _LoggerConfig(object):

    _LOGGER_NAME = "gddriver"

    def __init__(self):
        self._logger = None

    @property
    def logger(self):
        return self._logger

    def get_logger(self, logger_name=None):
        if self.logger:
            return self.logger

        return logging.getLogger(logger_name or self._LOGGER_NAME)


_DEFAULT_LOGGER_CONFIG = _LoggerConfig()


def get_logger(name=None):
    return _DEFAULT_LOGGER_CONFIG.get_logger(name)


def set_logger(logger):
    _DEFAULT_LOGGER_CONFIG._logger = logger
    get_logger().debug("logger changed.")
