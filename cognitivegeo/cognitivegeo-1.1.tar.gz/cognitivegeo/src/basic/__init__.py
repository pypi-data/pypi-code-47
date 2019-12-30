#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

from __future__ import absolute_import, division, print_function

__all__ = ['data', 'mdict', 'curve', 'image', 'video']


import os, sys
sys.path.append(os.path.dirname(__file__)[:-6][:-4][:-13])
#
from cognitivegeo.src.basic.data import data as data
from cognitivegeo.src.basic.matdict import matdict as mdict
from cognitivegeo.src.basic.curve import curve as curve
from cognitivegeo.src.basic.image import image as image
from cognitivegeo.src.basic.video import video as video