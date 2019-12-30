#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     January 2019                                                                    #
#                                                                                           #
#############################################################################################

# pointset processing functions

from PyQt5 import QtCore
import sys, os
import numpy as np
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])


__all__ = ['analysis']


def checkPoint(point):
    """
    Check if a point dictionary in the correct format

    Args:
        point:  Points as a dictionary with at least the following keys: 'Inline', 'Crossline', and 'Z'

    Return:
        True or false
    """

    if len(point.keys()) < 1:
        return False
    #
    if 'Inline' not in point.keys() or 'Crossline' not in point.keys() or 'Z' not in point.keys():
            return False
    #
    return True


def checkPointSet(pointset):
    """
    Check if a pointset dictionary in the correct format

    Args:
        point:  Pointsets as a dictionary with each key representing a point dictionary.
                Each point dictionary contains at least the following keys: 'Inline', 'Crossline', and 'Z'

    Return:
        True or false
    """

    if pointset is None or len(pointset.keys()) < 1:
        return False
    for p in pointset.keys():
        if pointset[p] is None:
            return False
        if checkPoint(pointset[p]) is False:
            return False
    return True


class analysis:
    checkPoint = checkPoint
    checkPointSet = checkPointSet