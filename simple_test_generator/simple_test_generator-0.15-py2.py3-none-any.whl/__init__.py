"""A simple cli-based recorder for Python"""

__version__ = '0.15'

from .main import Recorder, get_test_data_filename
from .runtime import parametrize_stg_tests
from . import tests

__all__ = ['parametrize_stg_tests', 'Recorder', 'get_test_data_filename', 'tests']
