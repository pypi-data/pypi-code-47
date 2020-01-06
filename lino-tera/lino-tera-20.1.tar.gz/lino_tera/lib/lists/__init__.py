# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The `lists` plugin specific to :ref:`psico`.

.. autosummary::
   :toctree:

    models
    fixtures


"""

from lino_xl.lib.lists import Plugin


class Plugin(Plugin):

    extends_models = ['List']

