import logging
import os
import shutil

class Vagrant(object):

    def __init__(self):
        self._prechecks()

    def _prechecks(self):
        
        if shutil.which("vagrant") is None:
            err = "Cannot find vagrant. Please install: https://www.vagrantup.com/downloads.html"
            LOGGER.error(err)
            raise Exception(err)

    @property
    def plugins(self):
        return Plugins(self)

from .plugins import Plugins

LOGGER = logging.getLogger(__name__)
