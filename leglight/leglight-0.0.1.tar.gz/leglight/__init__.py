"""A Python module designed to control the Elgato brand Lights."""

import logging

from .leglight import LegLight
from .discovery import discover

__author__ = 'Obviate.io <python-code@obviate.io>'
__version__ = '0.0.1'
__website__ = 'https://gitlab.com/obviate.io/pyleglight'
__license__ = 'MIT License'

__all__ = [
    'discover',
    'LegLight',
]

logging.getLogger(__name__).addHandler(logging.NullHandler())