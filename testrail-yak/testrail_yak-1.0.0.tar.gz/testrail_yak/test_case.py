#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail_exception import TestRailException, ValidationException
import time


class TestCaseException(TestRailException):
    pass


class TestCaseValidationException(ValidationException):
    pass


class TestCase:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_cases(self, project_id):
        """Get a list of test cases associated with a given project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the test cases
        """
        if not project_id or project_id is None:
            raise TestCaseValidationException("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise TestCaseValidationException("[*] project_id must be an int or float")

        if project_id <= 0:
            raise TestCaseValidationException("[*] project_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_cases/{}".format(project_id))    # wtf? [0]
        except TestCaseException:
            print("[!] Failed to get test cases. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_cases/{}".format(project_id))    # [0]
            except TestCaseException:
                print("[!] Failed to get test cases.")
        finally:
            return result

    def get_test_case(self, case_id):
        """Get a test case by case_id.

        :param case_id: ID of the test case
        :return: response from TestRail API containing the test cases
        """
        if not case_id or case_id is None:
            raise TestCaseValidationException("[*] Invalid case_id")

        if type(case_id) not in [int, float]:
            raise TestCaseValidationException("[*] case_id must be an int or float")

        if case_id <= 0:
            raise TestCaseValidationException("[*] case_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_case/{}".format(case_id))
        except TestCaseException:
            print("[!] Failed to get test case. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_case/{}".format(case_id))
            except TestCaseException:
                print("[!] Failed to get test case.")
        finally:
            return result

    def add_test_case(self, section_id, title):
        """Add a test case to a project by section_id.

        :param section_id: ID of the TestRail section
        :param title: title of the test case
        :return: response from TestRail API containing the newly created test case
        """
        if not section_id or section_id is None:
            raise TestCaseValidationException("[*] Invalid section_id.")

        if type(section_id) not in [int, float]:
            raise TestCaseValidationException("[*] section_id must be an int or float.")

        if section_id <= 0:
            raise TestCaseValidationException("[*] section_id must be > 0.")

        if not title or title is None:
            raise TestCaseValidationException("[*] Test case title required.")

        data = dict(title=title)

        result = None
        try:
            result = self.client.send_post("add_case/{}".format(section_id), data)
        except TestCaseException:
            print("[!] Failed to add test case. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_post("add_case/{}".format(section_id), data)
            except TestCaseException:
                print("[!] Failed to add test case.")
        finally:
            return result
