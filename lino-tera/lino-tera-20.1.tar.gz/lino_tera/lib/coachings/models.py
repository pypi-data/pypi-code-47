# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Database models for this plugin."""

from __future__ import unicode_literals

from lino.api import _, dd

from lino_xl.lib.coachings.models import *

#from lino_xl.lib.working.mixins import Workable

# from lino_xl.lib.coachings.mixins import Coachable
# from lino_xl.lib.cal.mixins import EventGenerator
# from lino_xl.lib.courses.mixins import Enrollable

# from .choicelists import PartnerTariffs

# class Coaching(Coaching, EventGenerator, Enrollable):

#     class Meta(Coaching.Meta):
#         app_label = 'coachings'
#         abstract = dd.is_abstract_model(__name__, 'Coaching')

#     # tariff = PartnerTariffs.field(
#     #     default=PartnerTariffs.plain.as_callable())
#     event_policy = dd.ForeignKey(
#         'products.Product', blank=True, null=True)
    
    
#     event_policy = dd.ForeignKey(
#         'cal.EventPolicy', blank=True, null=True)
    
#     def get_events_user(self):
#         return self.user
        
#     def update_cal_rset(self):
#         return self.event_policy
    
#     def update_cal_event_type(self):
#         return self.event_policy.event_type
        
#     def update_cal_from(self, ar):
#         return dd.today()
#         # pc = self.get_primary_coaching()
#         # if pc:
#         #     return pc.start_date
    
#     def update_cal_until(self):
#         return dd.today(365)
#         # pc = self.get_primary_coaching()
#         # if pc:
#         #     return pc.end_date


# CoachingsByClient.params_layout += " course enrolment_state"
