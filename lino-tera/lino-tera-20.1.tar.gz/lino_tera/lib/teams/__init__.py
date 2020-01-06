# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The `teams` plugin specific to :ref:`psico`.

.. autosummary::
   :toctree:

    models
    fixtures


"""

from lino_xl.lib.teams import Plugin

from lino.api import _


class Plugin(Plugin):

    verbose_name = _("Departments")

    extends_models = ['Team']
