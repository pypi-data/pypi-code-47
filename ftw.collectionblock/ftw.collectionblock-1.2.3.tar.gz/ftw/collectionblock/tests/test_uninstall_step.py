from ftw.testing import IS_PLONE_5
from ftw.testing.genericsetup import GenericSetupUninstallMixin
from ftw.testing.genericsetup import apply_generic_setup_layer
from unittest import TestCase
from unittest import skipIf

NOT_IS_PLONE_5 = not IS_PLONE_5


@skipIf(NOT_IS_PLONE_5, 'There is no uninstall profile in plone4')
@apply_generic_setup_layer
class TestGenericSetupUninstall(TestCase, GenericSetupUninstallMixin):
    package = 'ftw.collectionblock'
