# -*- coding: UTF-8 -*-
# Copyright 2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Adds default data for `CoachingEnding`.

"""

from __future__ import unicode_literals

from lino.api import rt, _
from lino.utils.mldbc import babel_named as babeld

def objects():
    M = rt.models.coachings.CoachingEnding
    yield babeld(M, _("Transfer to colleague"))
    yield babeld(M, _("Moved away"))
    yield babeld(M, _("Abandoned by client"))

    
