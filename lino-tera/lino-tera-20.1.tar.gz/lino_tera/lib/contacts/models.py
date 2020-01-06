# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Database models for this plugin."""

from __future__ import unicode_literals

from lino.api import _

from lino_xl.lib.contacts.models import *

#from lino_xl.lib.working.mixins import Workable

#from lino_xl.lib.coachings.mixins import Coachable
from lino_xl.lib.courses.mixins import Enrollable

# class Partner(Partner, Coachable):

#     class Meta(Partner.Meta):
#         app_label = 'contacts'
#         abstract = dd.is_abstract_model(__name__, 'Partner')


class Person(Person, Enrollable):

    class Meta(Person.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Person')


# class Company(Partner, Company):

#     class Meta(Company.Meta):
#         app_label = 'contacts'
#         abstract = dd.is_abstract_model(__name__, 'Company')


dd.update_field(Person, 'first_name', blank=True)


class PartnerDetail(PartnerDetail):

    main = 'general address invoicing purchases more'

    # general = dd.Panel(PartnerDetail.main,label=_("General"))

    general = dd.Panel("""
    overview:40 general_middle:20 ledger.MovementsByPartner:30
    general_bottom
    """, label=_("General"))

    general_middle = """
    id
    language
    """

    general_bottom = """
    courses.ActivitiesByPartner
    """
    
    address = dd.Panel("""
    address_box contact_box
    sepa.AccountsByPartner:30
    """, label=_("Address"))

    # A layout for use in Belgium
    address_box = """
    #prefix name 
    addr1
    street:25 street_no #street_box
    # addr2
    country zip_code:10 city
    """

    contact_box = """
    email
    phone
    gsm
    fax
    url
    """

    more = dd.Panel("""
    # courses.CoursesByCompany
    # changes.ChangesByMaster
    excerpts.ExcerptsByOwner
    remarks:50 checkdata.ProblemsByOwner:30
    """, label=_("More"))

    invoicing = dd.Panel("""
    invoicing_left:30 courses.ActivitiesByPartner:50
    sales.InvoicesByPartner
    """, label=_("Invoicing"))

    invoicing_left = """
    pf_residence pf_income  
    pf_composition 
    # salesrule__invoice_recipient 
    payment_term salesrule__paper_type
    """

    # invoicing = dd.Panel("""
    # salesrule__invoice_recipient payment_term salesrule__paper_type
    # sales.InvoicesByPartner
    # """, label=_("Invoicing"))


    purchases = dd.Panel("""
    purchase_account vat_regime vat_id
    ana.InvoicesByPartner
    """, label=_("Purchases"))


class CompanyDetail(PartnerDetail):  # , CompanyDetail):

    # general = dd.Panel("""
    # overview:30 ledger.MovementsByPartner 
    # general_bottom
    # excerpts.ExcerptsByOwner 
    # """, label=_("General"))

    general_middle = """
    id 
    language
    type 
    """
    
    general_bottom = """
    contacts.RolesByCompany courses.ActivitiesByPartner
    """
    

    # address = dd.Panel("""
    # address_box contact_box
    # """, label=_("Address"))

    # more = dd.Panel("""
    # #language #salesrule__invoice_recipient
    # # rooms.BookingsByCompany
    # notes.NotesByCompany
    # """, label=_("More"))

    # address_box = """
    # prefix name id
    # addr1
    # street:25 street_no street_box
    # addr2
    # country zip_code:10 city
    # """    

    # contact_box = dd.Panel("""
    # email:40
    # phone
    # gsm
    # fax
    # url
    # """)  # ,label = _("Contact"))


dd.update_field(Company, 'overview', verbose_name=None)
dd.update_field(Person, 'overview', verbose_name=None)
    
class PersonDetail(PersonDetail, PartnerDetail):

    # main = 'general address invoicing purchases more'

    # general = dd.Panel("""
    # overview:30  ledger.MovementsByPartner #lists.MembersByPartner:20
    # general_bottom
    
    # """, label=_("General"))

    general_middle = """
    id:6 language:8
    gender
    birth_date age:10
    """

    general_bottom = """
    cal.GuestsByPartner courses.EnrolmentsByPupil 
    """

    # address = dd.Panel("""
    # address_box contact_box:30
    # contacts.RolesByPerson 
    # """, label=_("Address"))

    address_box = """
    last_name first_name:15 title:10 
    addr1 
    street:25 street_no #street_box
    # addr2
    country zip_code:10 city
    """

    # contact_box = """
    # email
    # phone
    # gsm
    # url
    # """

    # personal = 'national_id card_number'
   
    # more = dd.Panel("""
    # id language
    # sales.InvoicesByPartner
    # """, label=_("More"))

    # contacts.RolesByPerson


Companies.insert_layout = """
name
country city
vat_regime
"""

from lino_xl.lib.clients.desktop import ClientContactsByCompany, ClientContactsByPerson

Company.used_as_client_contact = dd.ShowSlaveTable(ClientContactsByCompany)
Person.used_as_client_contact = dd.ShowSlaveTable(ClientContactsByPerson)

