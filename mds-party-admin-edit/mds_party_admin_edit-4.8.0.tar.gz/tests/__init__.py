# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import trytond.tests.test_tryton
import unittest

try:
    from trytond.modules.party_admin_edit.tests.test_party import PartyTestCase
except ImportError:
    from .test_party import PartyTestCase

__all__ = ['suite']


class PartyAdminEditTestCase(\
            PartyTestCase,\
            ):
    'Test party-admin-edit module'
    module = 'party_admin_edit'

#end PartyAdminEditTestCase


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(PartyAdminEditTestCase))
    return suite
