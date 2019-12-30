#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     January 2019                                                                    #
#                                                                                           #
#############################################################################################

# basic functions for lines

import sys, os
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.vis.color import color as color


__all__ = ['line']

# List of all available line properties, including Style and Width
LineStyleList = ['Solid', 'Dashed', 'Dashdot', 'Dotted', 'None']
LineWidthList = [i for i in range(1, 20)]


class line:
    # Pack all functions as a class
    #
    LineStyleList = LineStyleList
    LineWidthList = LineWidthList
    LineColorList = color.ColorList