__version__ = '6.0.2'

from .col_logging import logging
# noinspection PyUnresolvedReferences
from zuper_ipce import __version__ as _v
logger = logging.getLogger('zuper-nodes')
logger.setLevel(logging.DEBUG)
logger.info(f'zuper-nodes {__version__}')

from .language import *

from .language_parse import *
from .language_recognize import *

from .structures import  *
