# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The `contacts` plugin specific to :ref:`psico`.

.. autosummary::
   :toctree:

    models
    fixtures


"""

from lino_xl.lib.households import Plugin


class Plugin(Plugin):

    extends_models = ['Household']

