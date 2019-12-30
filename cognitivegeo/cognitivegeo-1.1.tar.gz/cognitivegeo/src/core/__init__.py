#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

from __future__ import absolute_import, division, print_function

__all__ = ['keyboard', 'settings']


import os, sys
sys.path.append(os.path.dirname(__file__)[:-5][:-4][:-13])
#
from cognitivegeo.src.core.keyboard import keyboard as keyboard
from cognitivegeo.src.core.settings import settings as settings