#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     November 2019                                                                   #
#                                                                                           #
#############################################################################################

# basic functions for 3d viewer

import sys, os
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.core.keyboard import keyboard as core_key


__all__ = ['viewer3d']

GoHomeKeyList = core_key.LetterKeyList

ViewFromPropertyList = ['Inline', 'Crossline', 'Z']
ViewFromKeyList = core_key.LetterKeyList


class viewer3d:
    # Pack all functions as a class
    #
    GoHomeKeyList = GoHomeKeyList
    #
    ViewFromPropertyList = ViewFromPropertyList
    ViewFromKeyList = ViewFromKeyList