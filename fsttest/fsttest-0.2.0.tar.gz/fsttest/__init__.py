#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
FST test -- test your Foma finite-state transducers!
"""

from .__version__ import VERSION as __version__
from .exceptions import FSTTestError, TestCaseDefinitionError
from .fsttest import TestResults, execute_test_case, run_tests, load_fst

__all__ = [
    "FSTTestError",
    "TestCaseDefinitionError",
    "run_tests",
    "TestResults",
    "execute_test_case",
]
