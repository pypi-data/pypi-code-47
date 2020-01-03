# -*- coding: UTF-8 -*-
# Copyright 2014-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import dd

@dd.receiver(dd.post_analyze)
def my_details(sender, **kw):
    sender.models.system.SiteConfigs.set_detail_layout("""
    site_company next_partner_id:10 default_build_method
    #site_calendar #simulate_today #hide_events_before
    #default_event_type #max_auto_events
    """)
