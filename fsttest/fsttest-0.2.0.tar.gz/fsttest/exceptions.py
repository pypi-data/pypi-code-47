#!/usr/local/bin python3
# -*- coding: UTF-8 -*-


class FSTTestError(Exception):
    """
    Base class for all exceptions in FST Test.
    """


class TestCaseDefinitionError(FSTTestError):
    """
    Should be raised when there's an issue parsing a test suite.
    """
