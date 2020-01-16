# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

__all__ = ['BaseConfig']

class BaseConfig:

    """Base class of the configuration information.
    """

    def __init__(self):
        """Initialize the class.
        """
        pass

    def __eq__(self, other):
        """Check equality.

        Parameters
        ----------
        other : Any derived `BaseConfig`
            Other instance to check.

        Returns
        -------
        bool
            True is objects are equal, False if not
        """
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
        """Print the object contents.

        Returns
        -------
        str
            The object string representation.
        """
        return str(self.__dict__)

    def check(self, attr, cdict, key):
        """Set parameter from incoming information.

        Parameters
        ----------
        attr : str
            Attribute to set.
        cdict : dict
            Instance of configuration.
        key : str
            Key to get value from.
        """
        try:
            setattr(self, attr, cdict[key])
        except KeyError:
            pass

    def fromDict(self, config):
        """Convert the stored configuration to a dictionary.

        Parameters
        ----------
        config : dict
            The configuration to translate.

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def toDict(self, writeEmpty=False):
        """Convert the stored configuration to a dictionary.

        Parameters
        ----------
        writeEmpty : bool
            Flag to write parameters with None as values.

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError
