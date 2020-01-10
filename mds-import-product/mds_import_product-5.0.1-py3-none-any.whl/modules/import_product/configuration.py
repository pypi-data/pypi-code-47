# -*- coding: utf-8 -*-

from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.pool import Pool, PoolMeta


__metaclass__ = PoolMeta
__all__ = ['Configuration']


class Configuration(ModelSingleton, ModelSQL, ModelView):
    'Config Import'
    __name__ = 'import_product.configuration'

    prodcat = fields.Many2One(model_name='product.category',
                    string=u'Product Category', 
                    help=u'select category for imported products',
                    domain=[
                        ('accounting', '=', True),
                    ], required=True)
    attribute_set = fields.Many2One('product.attribute.set', 'Attribute Set',
        help="Select a set of attributes to apply on the variants.")

# ende Configuration
