# -*- coding: UTF-8 -*-
# Copyright 2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import _

from lino_xl.lib.coachings.desktop import *

class CoachingDetail(dd.DetailLayout):

    # main = 'general address more sales ledger'
    main = 'general address more ledger'

    # general = dd.Panel(PartnerDetail.main,label=_("General"))

    general = dd.Panel("""
    overview:30 contact_box:30 lists.MembersByPartner:20
    bottom_box
    """, label=_("General"))

    address = dd.Panel("""
    address_box
    sepa.AccountsByPartner
    """, label=_("Address"))

    more = dd.Panel("""
    id language
    addr1 url
    #courses.CoursesByCompany
    # changes.ChangesByMaster
    excerpts.ExcerptsByOwner cal.GuestsByPartner
    """, label=_("More"))

    ledger_a = """
    salesrule__invoice_recipient vat_regime
    payment_term salesrule__paper_type
    """

    # sales = dd.Panel("""
    # """, label=dd.plugins.sales.verbose_name)

    bottom_box = """
    remarks:50 checkdata.ProblemsByOwner:30
    """

    # A layout for use in Belgium
    address_box = """
    name
    street:25 #street_no street_box
    addr2
    country zip_code:10 city
    """

    contact_box = """
    #mti_navigator
    email
    phone
    #fax
    gsm
    """

    ledger = dd.Panel("""
    ledger_a ledger.MovementsByPartner
    sales.InvoicesByPartner
    """, label=dd.plugins.ledger.verbose_name)




Coachings.set_detail_layout(CoachingDetail())
