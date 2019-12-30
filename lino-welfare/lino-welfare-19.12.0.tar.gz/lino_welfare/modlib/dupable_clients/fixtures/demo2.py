# -*- coding: UTF-8 -*-
# Copyright 2015 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Loops through all partners and calls their
:meth:`update_dupable_words
<lino.mixins.dupable.Dupable.update_dupable_words>` method.

"""

from lino.api import rt


def objects():

    for o in rt.models.pcsw.Client.objects.all():
        o.update_dupable_words()

    return []
