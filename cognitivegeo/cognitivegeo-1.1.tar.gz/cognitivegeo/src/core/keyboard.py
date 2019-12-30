#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     January 2019                                                                    #
#                                                                                           #
#############################################################################################

# basic functions for keyboard

import sys, os


__all__ = ['keyboard']

# List of all letter keys
LetterKeyList = ['A', 'B', 'C', 'D', 'E',
                 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of all number keys
NumberKeyList = ['0', '1', '2', '3', '4',
                 '5', '6', '7', '8', '9']


class keyboard:
    # Pack all functions as a class
    #
    LetterKeyList = LetterKeyList
    NumberKeyList = NumberKeyList