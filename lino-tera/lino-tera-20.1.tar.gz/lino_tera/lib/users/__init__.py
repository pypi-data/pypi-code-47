# Copyright 2014-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
Lino Tera extension of :mod:`lino.modlib.users`.

.. autosummary::
   :toctree:

    desktop
    fixtures.demo
    fixtures.demo2

"""

from lino.modlib.users import Plugin


class Plugin(Plugin):
    
    extends_models = ['User']

