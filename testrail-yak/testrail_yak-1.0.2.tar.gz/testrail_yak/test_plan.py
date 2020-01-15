#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail_exception import TestRailException, ValidationException
import time


class TestPlanException(TestRailException):
    pass


class TestPlanValidationException(ValidationException):
    pass


class TestPlan:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_plans(self, project_id):
        """Get a list of test plans associated with a given project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the test cases
        """
        if not project_id or project_id is None:
            raise TestPlanValidationException("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise TestPlanValidationException("[*] project_id must be an int or float")

        if project_id <= 0:
            raise TestPlanValidationException("[*] project_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_plans/{}".format(project_id))
        except TestPlanException:
            print("[!] Failed to get test plans. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_plans/{}".format(project_id))
            except TestPlanException:
                print("[!] Failed to get test plans.")
        finally:
            return result

    def get_test_plan(self, plan_id):
        """Get a test plan by plan_id.

        :param plan_id: ID of the test plan
        :return: response from TestRail API containing the test cases
        """
        if not plan_id or plan_id is None:
            raise TestPlanValidationException("[*] Invalid plan_id")

        if type(plan_id) not in [int, float]:
            raise TestPlanValidationException("[*] plan_id must be an int or float")

        if plan_id <= 0:
            raise TestPlanValidationException("[*] plan_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_plan/{}".format(plan_id))
        except TestPlanException:
            print("[!] Failed to get test plan. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_plan/{}".format(plan_id))
            except TestPlanException:
                print("[!] Failed to get test plan.")
        finally:
            return result

    def add_test_plan(self, project_id, name):
        """Add a test plan to a project.

        :param project_id: ID of the TestRail project
        :param name: title of the test plan
        :return: response from TestRail API containing the newly created test plan
        """
        if not project_id or project_id is None:
            raise TestPlanValidationException("[*] Invalid project_id.")

        if type(project_id) not in [int, float]:
            raise TestPlanValidationException("[*] project_id must be an int or float.")

        if project_id <= 0:
            raise TestPlanValidationException("[*] project_id must be > 0.")

        if not name or name is None:
            raise TestPlanValidationException("[*] Test plan name value required.")

        data = dict(name=name, include_all=True)

        result = None
        try:
            result = self.client.send_post("add_plan/{}".format(project_id), data)
        except TestPlanException:
            print("[!] Failed to add test plan. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_post("add_plan/{}".format(project_id), data)
            except TestPlanException:
                print("[!] Failed to add test plan.")
        finally:
            return result
