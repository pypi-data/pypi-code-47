# -*- coding: utf-8 -*-
from plone import api
from rt.categorysupport.browser.settings import ITaxonomySettingsSchema
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class CategoryList(object):
    FIELDNAME = 'category_list'

    def __call__(self, context=None):
        values = api.portal.get_registry_record(
            self.FIELDNAME,
            interface=ITaxonomySettingsSchema
        )
        terms = []
        for value in values:
            terms.append(SimpleTerm(
                value=value,
                token=value.encode('utf-8'),
                title=value)
            )
        return SimpleVocabulary(terms)


# CategoryListFactory = CategoryList()
