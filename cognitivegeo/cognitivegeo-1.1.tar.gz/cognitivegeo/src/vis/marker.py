#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     January 2019                                                                    #
#                                                                                           #
#############################################################################################

# basic functions for markers

import sys, os
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.vis.color import color as color


__all__ = ['marker']

# List of all available marker properties, including Style and Size
MarkerStyleList = ['*', '+', 'o', 'v', '^', '<', '<',
                   'x', 'X', '.', 'None']
MarkerSizeList = [i for i in range(1, 20)]


class marker:
    # Pack all functions as a class
    #
    MarkerStyleList = MarkerStyleList
    MarkerSizeList = MarkerSizeList
    MarkerColorList = color.ColorList