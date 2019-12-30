# -*- coding: UTF-8 -*-
# Copyright 2012-2018 Rumma & Ko Ltd
# This file is part of Lino Welfare.
#
# Lino Welfare is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Welfare is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Welfare.  If not, see
# <http://www.gnu.org/licenses/>.

"""
Database models for `lino_welfare.modlib.debts`.

"""

from __future__ import unicode_literals

from django.db import models

from lino.api import dd, _

from lino_xl.lib.ledger.utils import DEBIT, CREDIT
from lino_xl.lib.ledger.fields import DebitOrCreditField
from lino_xl.lib.ledger.roles import LedgerStaff



class Sheet(object):

    # Comptes annuels Jahresabschluss Jaarverslag  Aastaaruanne
    verbose_name = _("Financial statement")

    @classmethod
    def account_types(cls):
        """
        Return a list the top-level account types included in this Sheet
        """
        return [o for o in AccountTypes.objects() if o.sheet == cls]


class BalanceSheet(Sheet):

    verbose_name = _("Balance sheet")  # Bilan  Bilanz  Balans  Bilanss


class EarningsSheet(Sheet):

    # Compte de résultat Gewinn- und Verlustrechnung
    # Winst-en-verliesrekening ...
    verbose_name = _("Profit & Loss statement")


Sheet.objects = (BalanceSheet, EarningsSheet)


class AccountType(dd.Choice):
    # top_level = True
    sheet = None
    
    def __init__(self, *args, **kwargs):
        # the class attribute `name` ís used as value
        super(AccountType, self).__init__(*args, **kwargs)
        self.top_level = len(self.value) == 1

    

class AccountTypes(dd.ChoiceList):
    verbose_name = _("Account type")
    verbose_name_plural = _("Account types")
    item_class = AccountType
    column_names = 'value name text dc sheet'
    required_roles = dd.login_required(LedgerStaff)
    
    @dd.virtualfield(DebitOrCreditField(_("D/C")))
    def dc(cls, choice, ar):
        return choice.dc

    @dd.virtualfield(models.CharField(_("Sheet"), max_length=20))
    def sheet(cls, choice, ar):
        return choice.sheet.__name__


add = AccountTypes.add_item_instance

class Assets(AccountType):
    value = 'A'
    text = _("Assets")   # Aktiva, Anleihe, Vermögen, Anlage
    name = "assets"
    dc = DEBIT
    sheet = BalanceSheet
add(Assets())


class Liabilities(AccountType):
    value = 'L'
    text = _("Liabilities")  # Guthaben, Schulden, Verbindlichkeit
    name = "liabilities"
    dc = CREDIT
    sheet = BalanceSheet
add(Liabilities())


class Capital(AccountType):  # aka Owner's Equities
    value = 'C'
    text = _("Capital")  # Kapital
    name = "capital"
    dc = CREDIT
    sheet = BalanceSheet
add(Capital())


class Incomes(AccountType):
    value = 'I'
    text = _("Incomes")  # Gain/Revenue     Einnahmen  Produits
    name = "incomes"
    dc = CREDIT
    balance_sheet = True
    sheet = EarningsSheet
add(Incomes())


class Expenses(AccountType):
    value = 'E'
    text = _("Expenses")  # Loss/Cost       Ausgaben   Charges
    name = "expenses"
    dc = DEBIT
    sheet = EarningsSheet
add(Expenses())



class TableLayout(dd.Choice):
    columns_spec = None

    def __init__(self, value, verbose_name, columns_spec):
        self.columns_spec = columns_spec
        super(TableLayout, self).__init__(value, verbose_name, None)


class TableLayouts(dd.ChoiceList):
    item_class = TableLayout
    verbose_name = _("Table layout")
    verbose_name_plural = _("Table layouts")
    column_names = 'value text columns_spec'

    @dd.virtualfield(models.CharField(_("Columns"), max_length=20))
    def columns_spec(cls, choice, ar):
        return choice.columns_spec

AMOUNT_WIDTH = ":15"

add = TableLayouts.add_item
add('10',  # used by PrintExpensesByBudget
    _("Description, remarks, yearly amount, actor amounts"),
    "description remarks yearly_amount{} dynamic_amounts".format(
        AMOUNT_WIDTH))

add('11',
    _("Description, remarks, actor amounts"),
    "description remarks dynamic_amounts")

add('20',  # used by PrintLiabilitiesByBudget
    _("Partner, remarks, monthly rate, actor amounts"),
    "partner:20 remarks:20 monthly_rate:10 dynamic_amounts")

add('30',  # used by PrintAssetsByBudget, PrintIncomesByBudget
    _("Full description, actor amounts"),
    "full_description dynamic_amounts")

add('40',  # used by Inkasso-Unternehmen and Gerichtsvollzieher
    _("Debt-collector, partner, remarks, monthly rate, amounts"),
    "bailiff:20 partner:20 remarks:20 monthly_rate:10 dynamic_amounts")

# add('I', '10',  # used by PrintAssetsByBudget, PrintIncomesByBudget
#     _("Full description, actor amounts"),
#     "full_description dynamic_amounts")

