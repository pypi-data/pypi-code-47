# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from datetime import datetime

from matplotlib import cm
import numpy as np
import yaml

__all__ = ['getLutFromColorMap', 'getTimestamp', 'passFrame', 'readYamlFile', 'writeYamlFile']

def getLutFromColorMap(name):
    """Get a LUT from a color map.

    Parameters
    ----------
    name : str
        The name of the color map to retrieve.

    Returns
    -------
    np.array
        The LUT translated from color map.
    """
    colorMap = getattr(cm, name)
    lut = (np.array(colorMap.colors) * 256).astype('int')
    return lut

def getTimestamp():
    """Get the current date/time in UTC.

    NOTE: This should only be used for unit tests. The `TimeHandler` class
    should be used internally to the program.

    Returns
    -------
    datetime.datetime
        The current date/time in UTC.
    """
    return datetime.utcnow()

def passFrame(*args):
    """Say frame is valid no matter what arguments are.

    Parameters
    ----------
    *args
        Any arguments required by API.

    Returns
    -------
    bool
        Always True to pass the frame check.
    """
    return True

def readYamlFile(filename):
    """Read a YAML configuration file.

    Parameters
    ----------
    filename : str
        The name of the YAML file to read.

    Returns
    -------
    dict
        The configuration from the YAML file.
    """
    content = None
    try:
        with open(filename, 'r') as ifile:
            content = yaml.safe_load(ifile)
    except TypeError:
        pass
    return content

def writeYamlFile(filename, content):
    """Write a YAML file with the provided content.

    Parameters
    ----------
    filename : str
        The name of the YAML file to write.
    content : dict
        The content to write to the YAML file.
    """
    with open(filename, 'w') as ofile:
        yaml.dump(content, ofile)
