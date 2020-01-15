#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail_exception import TestRailException, ValidationException
import time


class UserException(TestRailException):
    pass


class UserValidationException(ValidationException):
    pass


class User:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_users(self):
        """Get a list of TestRail users.

        :return: response from TestRail API containing the user collection
        """
        result = None
        try:
            result = self.client.send_get("get_users")
        except UserException:
            print("[!] Failed to get users. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_users")
            except UserException:
                print("[!] Failed to get users.")
        finally:
            return result

    def get_user(self, user_id):
        """Get a TestRail user by user_id.

        :param user_id: user ID of the user we want to grab
        :return: response from TestRail API containing the user
        """
        if not user_id or user_id is None:
            raise UserValidationException("[*] Invalid user_id")

        result = None
        try:
            result = self.client.send_get("get_user/{}".format(user_id))
        except UserException:
            print("[!] Failed to get user. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_user/{}".format(user_id))
            except UserException:
                print("[!] Failed to get user.")
        finally:
            return result
