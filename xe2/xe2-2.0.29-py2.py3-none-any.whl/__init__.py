#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# @copyright Copyright (C) Guichet Entreprises - All Rights Reserved
# 	All Rights Reserved.
# 	Unauthorized copying of this file, via any medium is strictly prohibited
# 	Dissemination of this information or reproduction of this material
# 	is strictly forbidden unless prior written permission is obtained
# 	from Guichet Entreprises.
###############################################################################

###############################################################################
# @package xenon2
#
###############################################################################

import logging
import sys

from .version import __version_info__
from .version import __release_date__
from .website import generate_site
from .website import create_conf

__version__ = '.'.join(str(c) for c in __version_info__)
__author__ = "Florent Tournois"
__copyright__ = "Copyright 2018, Florent Tournois"
__module_name__ = "xe2"

__credits__ = ["Arnaud Boidard"]
__license__ = "MIT"
__maintainer__ = "Florent Tournois"
__email__ = "florent.tournois@gmail.fr"
__status__ = "Production"
__url__ = 'https://gitlab.com/guichet-entreprises.fr/tools/xenon2'

__all__ = ['generate_site', 'create_conf']
