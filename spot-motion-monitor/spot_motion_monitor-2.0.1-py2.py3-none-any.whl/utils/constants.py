# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import enum

"""Constants for program use.

Attributes
----------
COLORMAPS : tuple
    Set of colormaps provided by the program.
DEFAULT_FPS : int
    The default Frames per Second.
DEFAULT_PSD_ARRAY_SIZE : int
    The default size of the Power Spectrum Distribution plot vertical axis.
HTML_NU : str
    The HTML string representation for the Greek letter nu.
LARGE_FLOAT_VALUE_FOR_VALIDATOR : float
    Default value for QDoubleValidators.
LARGE_VALUE_FOR_VALIDATOR
    Default value for QIntValidators.
NO_DATA_VALUE : str
    Default text for no camera data value.
ONE_SECOND_IN_MILLISECONDS : int
    One second expressed in milliseconds.
STATUSBAR_FAST_TIMEOUT : int
    A fast timeout for the status bar.
TIMEFMT : str
    Formatting for date/time strings.
"""
ONE_SECOND_IN_MILLISECONDS = 1000
STATUSBAR_FAST_TIMEOUT = 100
DEFAULT_FPS = 1
NO_DATA_VALUE = " --- "
DEFAULT_PSD_ARRAY_SIZE = 25
COLORMAPS = ('viridis', 'plasma', 'inferno', 'magma', 'cividis')
TIMEFMT = '%Y-%m-%d %H:%M:%S'
HTML_NU = '&#957;'
LARGE_VALUE_FOR_VALIDATOR = 1e9
LARGE_FLOAT_VALUE_FOR_VALIDATOR = 1.0e200

class AutoscaleState(enum.Enum):
    """Enumeration for handling autoscale states.

    Attributes
    ----------
    OFF : int
        Turn autoscaling off.
    ON : int
        Turn autoscaling on.
    PARTIAL : int
        Autoscaling is on until as number of frames recorded, then turned off.
    """
    OFF = 0
    PARTIAL = 1
    ON = 2

class SaveConfigMask(enum.IntFlag):
    """Enumeration for saving configuration information.

    Attributes
    ----------
    EMPTY : int
        Write out attributes that contain None types.
    PLOT : int
        Write out plot configuration.
    """
    PLOT = 1
    EMPTY = 2
