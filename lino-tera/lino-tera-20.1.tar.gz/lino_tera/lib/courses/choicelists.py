# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import dd, rt, _

from lino_xl.lib.products.choicelists import PriceFactors
from lino_xl.lib.courses.choicelists import *

CourseAreas.clear()
add = CourseAreas.add_item
add('IT', _("Individual therapies"), 'therapies', 'courses.Therapies')
    # force_guest_states=True)
add('LG', _("Life groups"), 'life_groups', 'courses.LifeGroups')
    # force_guest_states=True)
add('OG', _("Other groups"), 'default', 'courses.Courses')


# Stand der Beratung:
# 01 dauert an                                
# 03 abgeschlossen                            
# 05 automatisch abgeschlossen                
# 06 Abbruch der Beratung                     
# 09 Weitervermittlung                        
# 12 nur Erstkontakt
CourseStates.clear()
add = CourseStates.add_item
add('01', _("Active"), 'active',
    is_editable=True, is_invoiceable=True, is_exposed=True,
    auto_update_calendar=False)
add('03', _("Closed"), 'closed',
    is_editable=False, is_invoiceable=False, is_exposed=False,
    auto_update_calendar=False)
add('05', _("Inactive"), 'inactive',
    is_editable=False, is_invoiceable=False, is_exposed=False,
    auto_update_calendar=False)
add('06', _("Cancelled"), 'cancelled',
    is_editable=False, is_invoiceable=False, is_exposed=False,
    auto_update_calendar=False)
add('09', _("Forwarded"), 'forwarded',
    is_editable=False, is_invoiceable=False, is_exposed=False,
    auto_update_calendar=False)
add('12', _("Draft"), 'draft',
    is_editable=True, is_invoiceable=False, is_exposed=True,
    auto_update_calendar=False)

# EnrolmentStates.default_value = 'confirmed'
EnrolmentStates.clear()
add = EnrolmentStates.add_item
add('01', _("Confirmed"), 'confirmed', invoiceable=True, uses_a_place=True)
add('03', _("Closed"), 'closed', invoiceable=False, uses_a_place=False)
add('05', _("Inactive"), 'inactive', invoiceable=False, uses_a_place=False)
add('06', _("Cancelled"), 'cancelled', invoiceable=False, uses_a_place=False)
add('09', _("Forwarded"), 'forwarded', invoiceable=False, uses_a_place=False)
add('12', _("First contact"), 'requested', invoiceable=False, uses_a_place=False)
add('00', _("Trying"), 'trying', invoiceable=False, uses_a_place=False)
add('02', _("Active"), 'active', invoiceable=True, uses_a_place=True)
# add('04', _("04"), invoiceable=False, uses_a_place=False)
# add('08', _("08"), invoiceable=False, uses_a_place=False)
# add('11', _("11"), invoiceable=False, uses_a_place=False)
# add('99', _("99"), invoiceable=False, uses_a_place=False)


class TranslatorTypes(dd.ChoiceList):
    verbose_name = _("Translator type")
    verbose_name_plural = _("Translator types")

add = TranslatorTypes.add_item
add('10', _("Interpreter"), "interpreter")
add('20', _("SETIS"))
add('30', _("Other"))


class TherapyDomains(dd.ChoiceList):
    verbose_name = _("Therapy domain")
    verbose_name_plural = _("Therapy domain")

add = TherapyDomains.add_item
add('E', _("Adults"), "adults")
add('M', _("Children M"))
add('P', _("Children P"))



class EndingReasons(dd.ChoiceList):

    verbose_name = _("Ending reason")

add = EndingReasons.add_item
add('100', _("Successfully ended"))
add('200', _("Health problems"))
add('300', _("Familiar reasons"))
add('400', _("Missing motivation"))
add('500', _("Return to home country"))
add('900', _("Other"))


class PartnerTariffs(dd.ChoiceList):
    verbose_name = _("Client tariff")
    verbose_name_plural = _("Client tariffs")

add = PartnerTariffs.add_item

add('00', _("Unknown"), 'unknown')
add('10', _("Free"), 'free')
add('11', _("Tariff 2"))
add('12', _("Tariff 5"))
add('13', _("Tariff 10"))
add('14', _("Tariff 15"))
add('15', _("Tariff 20"))
add('16', _("Tariff 39,56"), 'plain')


class InvoicingPolicies(dd.ChoiceList):
    verbose_name = _("Invoicing policy")
    verbose_name_plural = _("Invoicing policies")

add = InvoicingPolicies.add_item
add('00', _("By calendar event"), 'by_event')
add('10', _("By presence"), 'by_guest')


class Residences(dd.ChoiceList):
    verbose_name = _("Residence")
    verbose_name_plural = _("Residences")

add = Residences.add_item
add("10", _("Inside"), "inside")
add("20", _("Outside"), "ouside")

class HouseholdCompositions(dd.ChoiceList):
    verbose_name = _("Household composition")
    verbose_name_plural = _("Household compositions")

# add = HouseholdCompositions.add_item
# add("10", _("Alone"))
# add("20", _("2 members"))
# add("30", _("3 members"))

add = HouseholdCompositions.add_item
add("10", _("No participant below 18"), 'no_child')
add("20", _("One participant below 18"), 'one_child')
add("30", _("More than one participant below 18"), 'more_children')

class IncomeCategories(dd.ChoiceList):
    verbose_name = _("Income category")
    verbose_name_plural = _("Income categories")

add = IncomeCategories.add_item
add("10", "A")
add("20", "B")
add("30", "C")
add("40", "D")
add("50", "E")
# add("10", _("A (< 900 / < 1300 / < 550)"))
# add("20", _("B (900-1100 / 1300-1700 / 550-650)"))
# add("30", _("C (1100-1300 / 1700-2000 / 650-800)"))
# add("40", _("D (1300-1800 / 2000-2500 / 800-900)"))
# add("50", _("E (> 1800 / > 2500 / > 900)"))

# add("110", _("Below 900"))
# add("120", _("900-1100"))
# add("130", _("1100-1300"))
# add("140", _("1300-1800"))
# add("150", _("Above 1800"))
#
# add("210", _("Below 1300"))
# add("220", _("1300-1700"))
# add("230", _("1700-2000"))
# add("240", _("2000-2500"))
# add("250", _("Above 2500"))
#
# add("310", _("Below 550 per member"))
# add("320", _("550-650 per member"))
# add("330", _("650-800 per member"))
# add("340", _("800-900 per member"))
# add("350", _("Above 900 per member"))

add = PriceFactors.add_item
add("10", Residences, "residence")
add("20", IncomeCategories, "income")
add("30", HouseholdCompositions, "composition")

