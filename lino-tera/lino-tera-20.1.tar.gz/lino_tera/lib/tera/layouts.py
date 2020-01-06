# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""The default :attr:`custom_layouts_module
<lino.core.site.Site.custom_layouts_module>` for Lino Tera.

"""

from lino.api import dd, rt, _

if dd.is_installed('tera'):
    # avoid "AttrDict instance has no key 'tera'" when importing this
    # with autosummary

    rt.models.ledger.Accounts.column_names = "\
    ref name purchases_allowed sheet_item *"

    rt.models.countries.Places.detail_layout = """
    name country
    type parent zip_code id
    PlacesByPlace contacts.PartnersByCity
    """
    rt.models.ledger.Accounts.detail_layout = """
    name
    ref:10 sheet_item id common_account vat_column
    needs_partner clearable purchases_allowed
    needs_ana ana_account default_amount:10 vat_class
    ledger.MovementsByAccount
    """


    # rt.models.ledger.FiscalYears.detail_layout = """
    # ref id start_date end_date printed
    # #sheets.EntriesByYear
    # sheets.BalanceByYear
    # sheets.ResultsByYear
    # """

    rt.models.system.SiteConfigs.detail_layout = """
    site_company next_partner_id:10
    default_build_method simulate_today
    site_calendar default_event_type #pupil_guestrole
    max_auto_events hide_events_before
    """

    # dd.plugins.lists.verbose_name = _("Topics")
    # rt.models.lists.List._meta.verbose_name = _("Topic")
    # rt.models.lists.List._meta.verbose_name_plural = _("Topic")
    # rt.models.lists.Member._meta.verbose_name = _("Interest")
    # rt.models.lists.Member._meta.verbose_name_plural = _("Interests")
    # rt.models.lists.Member._meta.get_field('list').verbose_name = _("Topic")

    # dd.plugins.courses.verbose_name = _("Therapies")
    # rt.models.courses.Course.verbose_name = _("Therapy")
    # rt.models.courses.Course.verbose_name_plural = _("Therapies")


    # rt.models.vat.ItemsByInvoice.column_names = "account title ana_account vat_class total_base total_vat total_incl"

    # select Belgian VAT declaration layout
    # from lino_xl.lib.declarations import be

    from .roles import ClientsUser
    rt.models.tera.NotesByPartner.required_roles = dd.login_required(
        ClientsUser)
    # rt.models.lists.MembersByPartner.required_roles = dd.login_required(
    #     ClientsUser)
    rt.models.topics.InterestsByPartner.required_roles = dd.login_required(
        ClientsUser)

    rt.models.sales.VatProductInvoice._meta.verbose_name_plural = _("Sales invoices")

    rt.models.ana.AnaAccountInvoice._meta.verbose_name_plural = _("Purchase invoices")
