# -*- coding: UTF-8 -*-
# Copyright 2016-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
This is an example of how the application developer can provide
automatic data migrations.

This module is used because a :ref:`tera` Site has
:attr:`migration_class <lino.core.site.Site.migration_class>` set to
``"lino_tera.lib.tera.migrate.Migrator"``.
"""

from decimal import Decimal
from django.conf import settings
from lino.api import dd, rt
from lino.utils.dpy import Migrator, override
from lino.utils.dpy import create_mti_child


def noop(*args):
    return None


class Migrator(Migrator):
    "The standard migrator for :ref:`tera`."

    def migrate_from_18_8_0(self, globals_dict):
        """
        min_asset and number_of_events now in Tarif instead Product

        """

        bv2kw = globals_dict['bv2kw']
        products_Product = rt.models.products.Product
        
        @override(globals_dict)
        def create_products_product(id, name, description, cat_id, delivery_unit, vat_class, number_of_events, min_asset, sales_account_id, sales_price):
        #    if delivery_unit: delivery_unit = settings.SITE.models.products.DeliveryUnits.get_by_value(delivery_unit)
        #    if vat_class: vat_class = settings.SITE.models.vat.VatClasses.get_by_value(vat_class)
            if sales_price is not None: sales_price = Decimal(sales_price)
            kw = dict()
            kw.update(id=id)
            if name is not None: kw.update(bv2kw('name',name))
            if description is not None: kw.update(bv2kw('description',description))
            kw.update(cat_id=cat_id)
            kw.update(delivery_unit=delivery_unit)
            kw.update(vat_class=vat_class)
            #kw.update(number_of_events=number_of_events)
            #kw.update(min_asset=min_asset)
            kw.update(sales_account_id=sales_account_id)
            kw.update(sales_price=sales_price)
            return products_Product(**kw)

        return '18.11.0'

    def migrate_from_18_12_0(self, globals_dict):

        bv2kw = globals_dict['bv2kw']
        courses_PriceRule = rt.models.products.PriceRule
        courses_Course = rt.models.courses.Course
        courses_Enrolment = rt.models.courses.Enrolment

        @override(globals_dict)
        def create_courses_enrolment(id, start_date, end_date, printed_by_id,
                                     user_id, course_area, course_id, pupil_id,
                                     request_date, state, places, option_id,
                                     remark, confirmation_details, tariff_id,
                                     guest_role_id):
            #    if course_area: course_area = settings.SITE.models.courses.CourseAreas.get_by_value(course_area)
            #    if state: state = settings.SITE.models.courses.EnrolmentStates.get_by_value(state)
            kw = dict()
            kw.update(id=id)
            kw.update(start_date=start_date)
            kw.update(end_date=end_date)
            kw.update(printed_by_id=printed_by_id)
            kw.update(user_id=user_id)
            kw.update(course_area=course_area)
            kw.update(course_id=course_id)
            kw.update(pupil_id=pupil_id)
            kw.update(request_date=request_date)
            kw.update(state=state)
            kw.update(places=places)
            kw.update(option_id=option_id)
            kw.update(remark=remark)
            kw.update(confirmation_details=confirmation_details)
            # kw.update(tariff_id=tariff_id)
            kw.update(guest_role_id=guest_role_id)
            return courses_Enrolment(**kw)

        @override(globals_dict)
        def create_courses_course(id, modified, ref, start_date, start_time,
                                  end_date, end_time, healthcare_plan_id,
                                  user_id, every_unit, every, monday, tuesday,
                                  wednesday, thursday, friday, saturday,
                                  sunday, max_events, room_id, max_date,
                                  line_id, teacher_id, slot_id, description,
                                  remark, state, max_places, name,
                                  enrolments_until, tariff_id, payment_term_id,
                                  procurer_id, mandatory, ending_reason,
                                  partner_tariff, translator_type,
                                  therapy_domain, team_id, partner_id,
                                  paper_type_id):
            #    if every_unit: every_unit = settings.SITE.models.cal.Recurrencies.get_by_value(every_unit)
            #    if state: state = settings.SITE.models.courses.CourseStates.get_by_value(state)
            #    if ending_reason: ending_reason = settings.SITE.models.courses.EndingReasons.get_by_value(ending_reason)
            #    if partner_tariff: partner_tariff = settings.SITE.models.courses.PartnerTariffs.get_by_value(partner_tariff)
            #    if translator_type: translator_type = settings.SITE.models.courses.TranslatorTypes.get_by_value(translator_type)
            #    if therapy_domain: therapy_domain = settings.SITE.models.courses.TherapyDomains.get_by_value(therapy_domain)
            kw = dict()
            kw.update(id=id)
            kw.update(modified=modified)
            kw.update(ref=ref)
            kw.update(start_date=start_date)
            kw.update(start_time=start_time)
            kw.update(end_date=end_date)
            kw.update(end_time=end_time)
            kw.update(healthcare_plan_id=healthcare_plan_id)
            kw.update(user_id=user_id)
            kw.update(every_unit=every_unit)
            kw.update(every=every)
            kw.update(monday=monday)
            kw.update(tuesday=tuesday)
            kw.update(wednesday=wednesday)
            kw.update(thursday=thursday)
            kw.update(friday=friday)
            kw.update(saturday=saturday)
            kw.update(sunday=sunday)
            kw.update(max_events=max_events)
            kw.update(room_id=room_id)
            kw.update(max_date=max_date)
            kw.update(line_id=line_id)
            kw.update(teacher_id=teacher_id)
            kw.update(slot_id=slot_id)
            if description is not None: kw.update(
                bv2kw('description', description))
            kw.update(remark=remark)
            kw.update(state=state)
            kw.update(max_places=max_places)
            kw.update(name=name)
            kw.update(enrolments_until=enrolments_until)
            # kw.update(tariff_id=tariff_id)
            kw.update(payment_term_id=payment_term_id)
            kw.update(procurer_id=procurer_id)
            kw.update(mandatory=mandatory)
            kw.update(ending_reason=ending_reason)
            kw.update(partner_tariff=partner_tariff)
            kw.update(translator_type=translator_type)
            kw.update(therapy_domain=therapy_domain)
            kw.update(team_id=team_id)
            kw.update(partner_id=partner_id)
            kw.update(paper_type_id=paper_type_id)
            return courses_Course(**kw)

        @override(globals_dict)
        def create_courses_pricerule(id, seqno, fee_id, tariff, event_type_id,
                                     pf_residence, pf_composition, pf_income):
            #    if tariff: tariff = settings.SITE.models.courses.PartnerTariffs.get_by_value(tariff)
            #    if pf_residence: pf_residence = settings.SITE.models.courses.Residences.get_by_value(pf_residence)
            #    if pf_composition: pf_composition = settings.SITE.models.courses.HouseholdCompositions.get_by_value(pf_composition)
            #    if pf_income: pf_income = settings.SITE.models.courses.IncomeCategories.get_by_value(pf_income)
            kw = dict()
            kw.update(id=id)
            kw.update(seqno=seqno)
            kw.update(fee_id=fee_id)
            # kw.update(tariff=tariff)
            kw.update(event_type_id=event_type_id)
            kw.update(pf_residence=pf_residence)
            kw.update(pf_composition=pf_composition)
            kw.update(pf_income=pf_income)
            return courses_PriceRule(**kw)

        return '19.1.0'

    def migrate_from_19_1_0(self, globals_dict):
        globals_dict['courses_PriceFactors'] = rt.models.products.PriceFactors
        globals_dict['courses_PriceRule'] = rt.models.products.PriceRule
        return '19.2.0'
