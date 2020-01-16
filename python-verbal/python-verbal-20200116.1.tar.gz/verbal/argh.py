from __future__ import absolute_import

from argh import *
from argh.helpers import ArghParser as _ArghParser

import sys
import logging
import coverage

try:
    coverage.process_startup()
except ImportError:
    pass

class ArghParser(_ArghParser):
    def dispatch(self, *args, **kwargs):
        try:
            # find the module of the top level dispatcher, and install a log?
            return super(ArghParser, self).dispatch(self, *args, **kwargs)
        except SystemExit as e:
            if e.code:
                log = logging.getLogger('')
                log.exception(e)
            raise
        except:
            log = logging.getLogger('')
            exc_info = sys.exc_info()
            log.critical(exc_info[1], exc_info=exc_info)
            raise


