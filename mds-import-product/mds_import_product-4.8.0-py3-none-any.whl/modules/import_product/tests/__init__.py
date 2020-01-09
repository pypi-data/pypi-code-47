# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import trytond.tests.test_tryton
import unittest

try:
    from trytond.modules.import_product.tests.test_product import ProductTestCase
except ImportError:
    from .test_product import ProductTestCase

__all__ = ['suite']


class ImportProductTestCase(\
            ProductTestCase,\
            ):
    'Test import-product module'
    module = 'import_product'

#end ImportProductTestCase


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ImportProductTestCase))
    return suite
