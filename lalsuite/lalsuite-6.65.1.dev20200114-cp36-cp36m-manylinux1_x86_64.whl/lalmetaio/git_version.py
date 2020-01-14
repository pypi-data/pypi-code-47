# -*- coding: utf-8 -*-
# git_version.py - vcs information module
#
# Copyright (C) 2010 Nickolas Fotopoulos
# Copyright (C) 2012-2013 Adam Mercer
# Copyright (C) 2016 Leo Singer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with with program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307 USA

id = "e5276972c0a11db79aea29b84e030ed4a008d9ec"
date = "2020-01-13 10:53:40 +0000"
branch = "None"
tag = "None"
if tag == "None":
    tag = None
author = "David Keitel <david.keitel@ligo.org>"
builder = "Unknown User <>"
committer = "David Keitel <david.keitel@ligo.org>"
status = "UNCLEAN: Modified working tree"
version = id
verbose_msg = """Branch: None
Tag: None
Id: e5276972c0a11db79aea29b84e030ed4a008d9ec

Builder: Unknown User <>
Repository status: UNCLEAN: Modified working tree"""

import warnings

class VersionMismatchError(ValueError):
    pass

def check_match(foreign_id, onmismatch="raise"):
    """
    If foreign_id != id, perform an action specified by the onmismatch
    kwarg. This can be useful for validating input files.

    onmismatch actions:
      "raise": raise a VersionMismatchError, stating both versions involved
      "warn": emit a warning, stating both versions involved
    """
    if onmismatch not in ("raise", "warn"):
        raise ValueError(onmismatch + " is an unrecognized value of onmismatch")
    if foreign_id == "e5276972c0a11db79aea29b84e030ed4a008d9ec":
        return
    msg = "Program id (e5276972c0a11db79aea29b84e030ed4a008d9ec) does not match given id (%s)." % foreign_id
    if onmismatch == "raise":
        raise VersionMismatchError(msg)

    # in the backtrace, show calling code
    warnings.warn(msg, UserWarning)
