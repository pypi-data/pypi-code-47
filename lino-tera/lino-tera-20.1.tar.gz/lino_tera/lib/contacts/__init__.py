# -*- coding: UTF-8 -*-
# Copyright 2016-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The `contacts` plugin specific to :ref:`psico`.

.. autosummary::
   :toctree:

    fixtures
    choicelists


"""

from lino_xl.lib.contacts import Plugin


class Plugin(Plugin):

    extends_models = ['Person']
    
#     def setup_main_menu(self, site, user_type, m):
#         m = m.add_menu(self.app_label, self.verbose_name)
#         def add(a):
#             m.add_action(a)
#         add('contacts.Persons')
#         add('contacts.Companies')
#         add('tera.Clients')
#         add('households.Households')
#         # add('tera.MyClients')
#         m.add_separator()
#         add('lists.Lists')

