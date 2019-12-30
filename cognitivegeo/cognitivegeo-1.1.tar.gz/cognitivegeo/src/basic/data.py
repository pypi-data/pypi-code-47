#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     January 2019                                                                    #
#                                                                                           #
#############################################################################################

# basic functions for processing data

import numpy as np
import os, sys
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.vis.messager import messager as vis_msg


__all__ = ['data']


def str2int(str):
    """
    Covert a string to integer

    Args:
        str:    A string for conversion

    Return:
        The corresponding integer if it is convertable. Otherwise, False is returned.
    """

    try:
        return int(str)
    except ValueError:
        return False


def str2float(str):
    """
    Covert a string to float

    Args:
        str:    A string for conversion

    Return:
        The corresponding float if it is convertable. Otherwise, False is returned.
    """

    try:
        return float(str)
    except ValueError:
        return False


class data:
    # Pack all functions as a class
    str2int = str2int
    str2float = str2float
