#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

from __future__ import absolute_import, division, print_function


__all__ = ['start']


import os, sys
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
#
from cognitivegeo.src.gui.gui_main import start

if __name__ == "__main__":
    start(startpath=os.path.dirname(__file__)[:-8])