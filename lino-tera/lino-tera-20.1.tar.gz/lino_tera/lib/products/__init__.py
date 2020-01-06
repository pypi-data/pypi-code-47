# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""
The :ref:`tera` extension of :mod:`lino_xl.lib.products`.

In Lino Tera we don't call them "products" but "fees".

And we make them less visible by moving them from the main menu to the
configuration menu.

"""

from lino_xl.lib.products import Plugin, _


class Plugin(Plugin):

    verbose_name = _("Fees")
    extends_models = ['Product', 'ProductCat']
    menu_group = 'sales'

    # def setup_main_menu(self, site, user_type, m):
    #     pass
    #
    # def setup_config_menu(self, site, user_type, m):
    #     m = m.add_menu(self.app_label, self.verbose_name)
    #     for pt in site.models.products.ProductTypes.get_list_items():
    #         m.add_action('products.ProductsByType', pt)
    #     m.add_action('products.ProductCats')

