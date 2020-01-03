# -*- coding: UTF-8 -*-
# Copyright 2015-2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""Database models for :mod:`lino_care.modlib.contacts`.

"""


from lino.api import dd, _
from lino.utils import join_words
from lino.mixins import  Hierarchical

from lino_xl.lib.contacts.models import *
from lino.modlib.comments.mixins import Commentable
from lino_xl.lib.phones.mixins import ContactDetailsOwner
# from lino.modlib.printing.mixins import DirectPrintAction


PartnerDetail.address_box = dd.Panel("""
    name_box
    country #region city zip_code:10
    #addr1
    #street_prefix street:25 street_no street_box
    #addr2
    """, label=_("Address"))

PartnerDetail.contact_box = dd.Panel("""
    url
    phone
    gsm #fax
    """, label=_("Contact"))

# from lino_xl.lib.addresses.mixins import AddressOwner


class Person(Person, Commentable):

    # do_print = DirectPrintAction()
    
    class Meta(Person.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Person')
        
    def __str__(self):
        words = []
        words.append(self.first_name)
        words.append(self.last_name)
        return join_words(*words)

    # def get_overview_elems(self, ar):
    #     elems = super(Person, self).get_overview_elems(ar)
    #     elems += AddressOwner.get_overview_elems(self, ar)
    #     elems += ContactDetailsOwner.get_overview_elems(self, ar)
    #     return elems

    @classmethod
    def setup_parameters(cls, fields):
        fields.setdefault(
            'company', dd.ForeignKey(
                'contacts.Company', blank=True, null=True))
        fields.setdefault(
            'skill', dd.ForeignKey(
                'skills.Skill', blank=True, null=True))
        super(Person, cls).setup_parameters(fields)
    
    @classmethod
    def get_simple_parameters(cls):
        for p in  super(Person, cls).get_simple_parameters():
            yield p
        yield 'company'
        yield 'skill'
    
    @classmethod
    def add_param_filter(cls, qs, lookup_prefix='', company=None,
                         skill=None, **kwargs):
        qs = super(Person, cls).add_param_filter(qs, **kwargs)
        if company:
            fkw = dict()
            wanted = company.whole_clan()
            fkw[lookup_prefix + 'rolesbyperson__company__in'] = wanted
            qs = qs.filter(**fkw)
        
        if skill:
            fkw = dict()
            wanted = skill.whole_clan()
            fkw[lookup_prefix + 'end_user_set__faculty__in'] = wanted
        return qs
        

    # @classmethod
    # def get_request_queryset(cls, ar):
    #     qs = super(Person, cls).get_request_queryset(ar)
    #     pv = ar.param_values
    #     if pv.skill:
    #     return qs

# We use the `overview` field only in detail forms, and we
# don't want it to have a label "Description":
dd.update_field(Person, 'overview', verbose_name=None)    

class Company(Company, Hierarchical, Commentable):
    
    class Meta(Company.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Company')
        
    # def get_overview_elems(self, ar):
    #     elems = super(Company, self).get_overview_elems(ar)
    #     # elems += AddressOwner.get_overview_elems(self, ar)
    #     elems += ContactDetailsOwner.get_overview_elems(self, ar)
    #     return elems



class PersonDetail(PersonDetail):
    main = """
    overview:30 contact_box:40 contacts.RolesByPerson:30
    skills.OffersByEndUser:45 comments.CommentsByRFC:45
    """
    
    # main = "general #contact #more"

    # general = dd.Panel("""
    # overview:30 contact_box:40 contacts.RolesByPerson:30
    # skills.OffersByEndUser:45 comments.CommentsByRFC:45
    # """, label=_("General"))

    contact_box = dd.Panel("""
    last_name 
    first_name
    title:20 gender:10 language:10 
    birth_date age:10 id:6
    """)  #, label=_("Contact"))

    # more = dd.Panel("""
    # remarks comments.CommentsByRFC:30
    # """, label=_("More"))


class CompaniesByCompany(Companies):
    master_key = 'parent'

    
class CompanyDetail(CompanyDetail):
    main = "general contact"

    general = dd.Panel("""
    overview general_middle CompaniesByCompany
    contacts.RolesByCompany:30 skills.OffersByEndUser
    """, label=_("General"))

    general_middle = """
    type
    parent
    language:10 id:6
    """
    contact = dd.Panel("""
    # address_box
    remarks comments.CommentsByRFC:30
    """, label=_("Contact"))

   

# @dd.receiver(dd.post_analyze)
# def my_details(sender, **kw):
#     contacts = sender.models.contacts
#     contacts.Companies.set_detail_layout(contacts.CompanyDetail())

Companies.set_detail_layout(CompanyDetail())
Persons.set_detail_layout(PersonDetail())
Person.column_names = 'last_name first_name gsm email city *'
Persons.params_layout = 'observed_event start_date end_date skill company'


# PartnerDetail.address_box = dd.Panel("""
#     name_box
#     country #region city zip_code:10
#     #addr1
#     #street_prefix street:25 street_no street_box
#     #addr2
#     """, label=_("Address"))

# PartnerDetail.contact_box = dd.Panel("""
#     url
#     phone
#     gsm #fax
#     """, label=_("Contact"))


# 
# class Person(Person):
    
#     class Meta(Person.Meta):
#         app_label = 'contacts'
#         abstract = dd.is_abstract_model(__name__, 'Person')
        
#     def __str__(self):
#         words = []
#         words.append(self.first_name)
#         words.append(self.last_name)
#         return join_words(*words)


# class PersonDetail(PersonDetail):
    
#     main = "general contact #skills"

#     general = dd.Panel("""
#     overview info_box
#     contacts.RolesByPerson
#     """, label=_("General"))

#     info_box = """
#     id:5
#     language:10
#     email:40
#     """
    
#     contact = dd.Panel("""
#     address_box:60 contact_box:30
#     remarks skills.OffersByEndUser
#     """, label=_("Contact"))

#     # skills = dd.Panel("""
#     # topics.InterestsByPartner #tickets.SuggestedTicketsByEndUser
#     # """, label=dd.plugins.skills.verbose_name)

#     # tickets = dd.Panel("""
#     # tickets.TicketsByEndUser tickets.ProjectsByPerson
#     # """, label=dd.plugins.tickets.verbose_name)


#     name_box = "last_name first_name:15 gender #title:10"

    
# class CompanyDetail(CompanyDetail):
#     main = "general contact #skills #tickets"

#     general = dd.Panel("""
#     overview info_box
#     contacts.RolesByCompany skills.OffersByEndUser
#     """, label=_("General"))

#     info_box = """
#     id:5
#     language:10
#     email:40
#     """
    
#     contact = dd.Panel("""
#     address_box:60 contact_box:30 
#     remarks
#     """, label=_("Contact"))

#     # skills = dd.Panel("""
#     # skills.OffersByEndUser topics.InterestsByPartner
#     # """, label=dd.plugins.skills.verbose_name)

#     # tickets = dd.Panel("""
#     # tickets.TicketsByEndUser tickets.ProjectsByCompany
#     # """, label=dd.plugins.tickets.verbose_name)


# # @dd.receiver(dd.post_analyze)
# # def my_details(sender, **kw):
# #     contacts = sender.models.contacts
# #     contacts.Companies.set_detail_layout(contacts.CompanyDetail())

# Companies.set_detail_layout(CompanyDetail())
# Persons.set_detail_layout(PersonDetail())
# Person.column_names = 'last_name first_name gsm email city *'
