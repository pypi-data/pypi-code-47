# -*- coding: UTF-8 -*-
# Copyright 2016-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals

from lino.api import _

from lino_xl.lib.teams.models import *

class Team(Team):
    
    class Meta(Team.Meta):
        app_label = 'teams'
        abstract = dd.is_abstract_model(__name__, 'Team')
        verbose_name = _("Division")
        verbose_name_plural = _("Divisions")


# dd.inject_field(
#     'contacts.Partner', 'team',
#     dd.ForeignKey('teams.Team', blank=True, null=True))

# dd.inject_field(
#     'working.Session', 'team',
#     dd.ForeignKey('teams.Team', blank=True, null=True))

# dd.inject_field(
#     'ledger.Journal', 'team',
#     dd.ForeignKey('teams.Team', blank=True, null=True))


