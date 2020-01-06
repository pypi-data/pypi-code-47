# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""The `demo` fixture for this plugin."""

from lino.api import rt, dd, _

from lino.utils.mldbc import babeld

def objects():
    List = rt.models.lists.List
    for y in (2014, 2015, 2016):
        yield babeld(List, _("Women's group {0}").format(y))
        yield babeld(List, _("Men's group {0}").format(y))
        yield babeld(List, _("Children's group {0}").format(y))


