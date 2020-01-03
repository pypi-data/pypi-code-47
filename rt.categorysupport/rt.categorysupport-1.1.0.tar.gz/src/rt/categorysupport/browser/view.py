# -*- coding: utf-8 -*-
from plone.app.contenttypes.browser.folder import FolderView
from plone import api


class TaxonomyInfo(FolderView):
    """  """

    def get_taxonomies(self):
        if not self.context:
            return {}
        tax_dict = {}
        brains = api.content.find(context=self.context)
        for brain in brains:
            if not brain.taxonomies:
                continue
            for tax in brain.taxonomies:
                if tax in tax_dict:
                    tax_dict[tax] += 1
                else:
                    tax_dict[tax] = 1

        return tax_dict

    def get_subjects(self):
        if not self.context:
            return {}
        _dict = {}
        brains = api.content.find(context=self.context)
        for brain in brains:
            if not brain.Subject:
                continue
            for el in brain.Subject:
                if el in _dict.keys():
                    _dict[el] += 1
                else:
                    _dict[el] = 1

        return _dict

    def batch(self):
        return super(TaxonomyInfo, self).batch()
