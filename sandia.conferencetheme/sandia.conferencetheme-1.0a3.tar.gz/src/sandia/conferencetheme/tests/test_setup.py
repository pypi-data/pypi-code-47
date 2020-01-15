# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from sandia.conferencetheme.testing import SANDIA_CONFERENCETHEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that sandia.conferencetheme is properly installed."""

    layer = SANDIA_CONFERENCETHEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sandia.conferencetheme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'sandia.conferencetheme'))

    def test_browserlayer(self):
        """Test that ISandiaConferencethemeLayer is registered."""
        from sandia.conferencetheme.interfaces import (
            ISandiaConferencethemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ISandiaConferencethemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SANDIA_CONFERENCETHEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['sandia.conferencetheme'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if sandia.conferencetheme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'sandia.conferencetheme'))

    def test_browserlayer_removed(self):
        """Test that ISandiaConferencethemeLayer is removed."""
        from sandia.conferencetheme.interfaces import \
            ISandiaConferencethemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ISandiaConferencethemeLayer,
            utils.registered_layers(),
        )
