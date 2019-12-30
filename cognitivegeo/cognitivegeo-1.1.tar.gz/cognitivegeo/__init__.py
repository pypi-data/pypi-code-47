#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

from __future__ import absolute_import, division, print_function

__version__ = '1.1'

__all__ = ['basic', 'core', 'vis', 'seismic', 'psseismic', 'pointset', 'gui']

import os, sys
#
sys.path.append(os.path.dirname(__file__)[:-13])

import cognitivegeo.src.basic as basic
import cognitivegeo.src.core as core
import cognitivegeo.src.vis as vis
import cognitivegeo.src.seismic as seismic
import cognitivegeo.src.psseismic as psseismic
import cognitivegeo.src.pointset as pointset
import cognitivegeo.src.gui as gui

if __name__ == "__main__":
    gui.start(startpath=os.path.dirname(__file__))