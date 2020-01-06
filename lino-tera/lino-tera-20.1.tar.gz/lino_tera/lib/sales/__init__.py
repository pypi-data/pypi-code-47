# -*- coding: UTF-8 -*-
# Copyright 2016-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The :ref:`voga` extension of :mod:`lino_xl.lib.sales`.
"""

from lino_xl.lib.sales import Plugin, _


class Plugin(Plugin):
    verbose_name = _("Invoicing")
    extends_models = ['InvoiceItem']
