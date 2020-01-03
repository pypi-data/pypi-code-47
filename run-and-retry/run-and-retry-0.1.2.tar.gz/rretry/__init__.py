import logging

__version__ = '0.1.2'

# define logger
logging.basicConfig()
rrlogger = logging.getLogger('rretry')
rrlogger.setLevel(logging.INFO)

from .main import run
