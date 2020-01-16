from __future__ import absolute_import

from sys import _getframe
import logging

from .istring import istr
from logging import *

class InterpolatedLogger(object):
    def __init__(self, log):        
        self._log = log

    def addHandler(self, handler):
        return self._log.addHandler(handler)
    def removeHandler(self, handler):
        return self._log.removeHandler(handler)

    def isEnabledFor(self,level):
        return self._log.isEnabledFor(level)

    def debug(self, msg, _frame=None, *args, **kwargs):
        self.log(DEBUG, msg, _frame=_frame or _getframe(1), *args, **kwargs)
    def info(self, msg,  _frame=None, *args, **kwargs):
        self.log(INFO, msg, *args, _frame=_frame or _getframe(1), **kwargs)
    def warning(self, msg, _frame=None,*args, **kwargs):
        self.log(WARNING, msg, _frame=_frame or _getframe(1), *args, **kwargs)
    def error(self, msg,  _frame=None, *args, **kwargs):
        self.log(ERROR, msg, _frame=_frame or _getframe(1), *args,  **kwargs)
    def critical(self, msg, _frame=None, *args, **kwargs):
        self.log(CRITICAL, msg, _frame=_frame or _getframe(1), *args, **kwargs)
    def exception(self, msg, _frame=None, *args, **kwargs):
        self.log(ERROR, msg,_frame=_frame or _getframe(1), *args, exc_info=True, **kwargs)

    def log(self, level, msg, _frame=None, *args, **kwargs):
        # bind the istr, need to fix the pass though         
        self._log.log(level, istr(msg, _frame=_frame or _getframe(1)), *args, **kwargs)

def getLogger(name):    
    return InterpolatedLogger(logging.getLogger(name))




