#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from taz.auth import UserAssignedIdentity
import sys
import tests.config as cfg


class AuthTests(unittest.TestCase):

    def setUp(self):
        # self.managed_identity = MsiAuthentication()

        self.user_assigned_identity = UserAssignedIdentity(
            cfg.auth["resource_group"],
            cfg.auth["managed_identity"],
            subscription_id=cfg.auth["subscription_id"])

    def test_exists(self):
        self.assertTrue(self.user_assigned_identity is not None)

    def test_container_group_identity(self):
        self.assertTrue(
            self.user_assigned_identity.get_container_group_identity()
            is not None)

    def test_managed_identity(self):
        self.assertTrue(self.user_assigned_identity is not None)


if __name__ == '__main__':
    sys.argv.append('-v')
    unittest.main()
