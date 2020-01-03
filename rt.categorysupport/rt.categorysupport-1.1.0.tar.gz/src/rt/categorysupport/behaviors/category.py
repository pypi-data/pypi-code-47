# -*- coding: utf-8 -*-
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from rt.categorysupport import _
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implementer


class ICategory(model.Schema):

    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=['taxonomies'],
    )

    taxonomies = schema.Tuple(
        title=_(u'taxonomies', default=u'Taxonomies'),
        description=_(
            u'taxonomies_description',
            default=u'Un campo aggiuntivo per la gestione di nuove parole chiave.'  # noqa
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=None,
    )
    directives.widget(
        'taxonomies',
        AjaxSelectFieldWidget,
        vocabulary='rt.categorysupport.category_list',
        pattern_options={
            'allowNewItems': False
        }
    )


alsoProvides(ICategory, IFormFieldProvider)


@implementer(ICategory)
class Category(object):

    def __init__(self, context):
        self.context = context
