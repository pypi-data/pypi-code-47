#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
FST test -- test your Foma finite-state transducers!
"""

from .__version__ import VERSION as __version__
from ._fst import FST
from .exceptions import FSTTestError, TestCaseDefinitionError
from .fsttest import TestResults, execute_test_case, load_fst, run_tests

__all__ = [
    "FST",
    "FSTTestError",
    "TestCaseDefinitionError",
    "TestResults",
    "execute_test_case",
    "run_tests",
]
