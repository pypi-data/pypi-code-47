from __future__ import absolute_import
import sys
from importlib import reload
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

import threading
from .backend import *

__version__ = '0.3.1'

