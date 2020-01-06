# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""The choicelists for this plugin.

"""

from lino.api import dd, _


class PartnerTariffs(dd.ChoiceList):
    verbose_name = _("Client tariff")
    verbose_name_plural = _("Client tariffs")

add = PartnerTariffs.add_item

add('10', _("Plain"), 'plain')
add('20', _("Reduced"), 'reduced')


