# -*- coding: utf-8 -*-
from plone import api
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from rt.categorysupport import logger
from rt.categorysupport.setuphandlers import setRegistyIndexes
from zope.component import queryUtility

try:
    from rer.sitesearch.interfaces import IRERSiteSearchSettings
except Exception:
    pass

default_profile = "profile-rt.categorysupport:default"


def migrate_to_1001(context):
    setup_tool = api.portal.get_tool("portal_setup")
    setup_tool.runImportStepFromProfile(default_profile, "catalog")
    logger.info(u"Updated to 1001")


def add_taxonomies_to_indexes(context):

    # check if rer.sitesearch was installed
    qi = getToolByName(context, "portal_quickinstaller")
    prods = qi.listInstallableProducts(skipInstalled=False)
    prods = [x["id"] for x in prods if x["status"] == "installed"]

    if "rer.sitesearch" in prods:
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IRERSiteSearchSettings, check=False)

        TAXONOMIES_INDEX = [("taxonomies", "Temi"), ("Subject", "Subject")]
        indexes = setRegistyIndexes(context, TAXONOMIES_INDEX)
        settings.available_indexes = indexes

        # aggiungo il campo taxonomies a quelli visibili nella vista
        if "taxonomies" not in settings.indexes_order:
            settings.indexes_order += ("taxonomies",)

        logger.info(u"taxonomies added")
    else:
        logger.info(u"rer.sitesearch was not installed")
