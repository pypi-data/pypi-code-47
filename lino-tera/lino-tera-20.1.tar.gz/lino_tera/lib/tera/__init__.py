# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""
The main plugin for Lino Tera.

.. autosummary::
   :toctree:

    migrate
    user_types
    workflows
    layouts

"""

from lino.api.ad import Plugin


class Plugin(Plugin):

    def setup_main_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('tera.Clients')

    def setup_config_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('tera.Procurer')
        m.add_action('tera.LifeModes')
        
