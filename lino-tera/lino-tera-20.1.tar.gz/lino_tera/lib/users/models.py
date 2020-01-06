# -*- coding: UTF-8 -*-
# Copyright 2013-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


from lino.modlib.users.models import *

from lino.api import _


class User(User):
    
    class Meta(User.Meta):
        app_label = 'users'
        abstract = dd.is_abstract_model(__name__, 'User')
        
    cash_daybook = dd.ForeignKey(
        'products.Product',
        blank=True, null=True,
        verbose_name=_("Cash daybook"))

    @dd.chooser()
    def cash_daybook_choices(self):
        ProductTypes = rt.models.products.ProductTypes
        qs = rt.models.products.Product.objects.filter(product_type=ProductTypes.daybooks)
        return qs
