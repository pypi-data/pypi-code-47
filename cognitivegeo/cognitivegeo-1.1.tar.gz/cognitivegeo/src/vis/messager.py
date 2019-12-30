#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     December 2019                                                                   #
#                                                                                           #
#############################################################################################

# basic functions for messager

import sys
import os
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])

# Print format
# Text color: black (30), red (31), green (32), yellow (33), blue (34), purple (35), cyan (36), white (37)
# Text style: no effect (0), bold (1), underline (2), negative1 (3), negative2 (5)
# Background color: black (40), red (41), green (42), yellow (43), blue (44), purple (45), cyan (46),white (47)


__all__ = ['messager']

def print2Terminal(message, type='Normal'):
    """
    Print message to terminal with format, to differentiate errors and warnings

    Args:
        message:    A string for print
        type:       Message type: 'Normal', 'Warning', 'Error'

    Return:
         N/A
    """
    if type != 'Normal' and type != 'normal' and type != 'NORMAL' \
        and type != 'Warning' and type != 'warning' and type != 'WARNING' \
        and type != 'Error' and type != 'error' and type != 'ERROR':
        type = 'normal'
    if type == 'normal' or type == 'Normal' or type == 'NORMAL':
        # print('\033[0;30;47m' + message)
        print('\033[0;0;0m' + message)
    if type == 'Warning' or type == 'warning' or type == 'WARNING':
        print('\033[1;34;40m' + message)
    if type == 'Error' or type == 'error' or type == 'ERROR':
        print('\033[1;31;40m' + message)
    # reset
    print('\033[0;0;0m', end='\r')

class messager:
    print = print2Terminal