# Copyright 2019-- Derk Kappelle
#
# This file is part of MooPy, a Python package with
# Multi-Objective Optimization (MOO) tools.
#
# MooPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MooPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MooPy.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import absolute_import, division, print_function

from .test import *
from .core import *
from ._solve import *
from .show_results import *
from .test_cases import *

__version__ = "0.0.5" # Update setup.py if the version changes!