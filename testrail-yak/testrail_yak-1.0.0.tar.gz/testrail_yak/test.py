#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail_exception import TestRailException, ValidationException
import time


class TestException(TestRailException):
    pass


class TestValidationException(ValidationException):
    pass


class Test:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_run_tests(self, run_id):
        """Get a collection of individual tests by run_id.

        :param run_id: ID of the test run
        :return: response from TestRail API containing the test cases
        """
        if not run_id or run_id is None:
            raise TestValidationException("[*] Invalid run_id")

        if type(run_id) not in [int, float]:
            raise TestValidationException("[*] run_id must be an int or float")

        if run_id <= 0:
            raise TestValidationException("[*] run_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_tests/{}".format(run_id))
        except TestException:
            print("[!] Failed to get tests from test run. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_tests/{}".format(run_id))
            except TestException:
                print("[!] Failed to get tests from test run.")
        finally:
            return result

    def get_test_run_test(self, test_id):
        """Get an individual test.

        :param test_id: ID of the individual test
        :return: response from TestRail API containing the test
        """
        if not test_id or test_id is None:
            raise TestValidationException("[*] Invalid test_id")

        if type(test_id) not in [int, float]:
            raise TestValidationException("[*] test_id must be an int or float")

        if test_id <= 0:
            raise TestValidationException("[*] test_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_test/{}".format(test_id))
        except TestException:
            print("[!] Failed to get individual test. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_test/{}".format(test_id))
            except TestException:
                print("[!] Failed to get individual test.")
        finally:
            return result
