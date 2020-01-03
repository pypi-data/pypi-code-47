# -*- coding: utf-8 -*-
from plone.indexer import indexer
from rt.categorysupport.behaviors.category import ICategory


@indexer(ICategory)
def taxonomies(object, **kw):
    return getattr(object, 'taxonomies', None)
