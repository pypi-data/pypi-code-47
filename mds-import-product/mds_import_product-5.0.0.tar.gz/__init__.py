# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .product import CsvImportWizard, CsvImportSchritt1, CsvImportSchritt2
from .configuration import Configuration


def register():
    Pool.register(
        Configuration,
        CsvImportSchritt1,
        CsvImportSchritt2,
        module='import_product', type_='model')
    Pool.register(
        CsvImportWizard,
        module='import_product', type_='wizard')
