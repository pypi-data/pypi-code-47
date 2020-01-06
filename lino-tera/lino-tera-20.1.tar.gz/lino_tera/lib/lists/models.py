# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Database models for this plugin."""

from __future__ import unicode_literals

from lino.api import _

from lino_xl.lib.lists.models import *
# from lino_xl.lib.coachings.mixins import Coachable
from lino_tera.lib.contacts.models import Partner


class List(List, Partner):
    
    class Meta(List.Meta):
        app_label = 'lists'
        abstract = dd.is_abstract_model(__name__, 'List')
        verbose_name = _("Therapeutical group")
        verbose_name = _("Therapeutical groups")


    def full_clean(self, *args, **kw):
        """Set the `name` field of this list.  This field is visible in the
        Partner's detail but not in the Lists's detail where it is
        filled automatically from the designation in the site's main
        language. and serves for sorting when selecting a List as
        Partner.

        """
        # self.name = dd.babelattr(self, 'designation', language=)
        if self.designation:
            self.name = self.designation
        else:
            self.designation = self.name
        super(List, self).full_clean(*args, **kw)

        
