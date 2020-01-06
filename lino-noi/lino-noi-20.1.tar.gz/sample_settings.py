# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Defines and instantiates a demo version of Lino Noi."""

import datetime
from lino_noi.lib.noi.settings import *


class Site(Site):
    # workflows_module = 'lino_book.projects.team.workflows'
    # strict_choicelist_values = False
    # use_websockets = True

    def get_installed_apps(self):
        # add lino.modlib.restful to the std list of plugins
        yield super(Site, self).get_installed_apps()
        # yield 'lino.modlib.restful'
        # yield 'lino_xl.lib.caldav'
        # yield 'lino_xl.lib.mailbox'

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        if self.is_installed('extjs'):
            self.plugins.extjs.configure(enter_submits_form=True)

    the_demo_date = datetime.date(2015, 5, 23)

    languages = "en de fr"
    # readonly = True
    
    # use_ipdict = True
    # use_websockets = True
    use_experimental_features = True
    # default_ui = 'lino_extjs6.extjs6'
    # default_ui = 'lino.modlib.bootstrap3'
    # default_ui = 'lino_openui5.openui5'


SITE = Site(globals())

DEBUG = True
ALLOWED_HOSTS=["*"]
