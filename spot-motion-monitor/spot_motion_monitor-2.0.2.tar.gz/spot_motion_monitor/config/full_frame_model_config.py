# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import BaseConfig

__all__ = ['FullFrameModelConfig']

class FullFrameModelConfig(BaseConfig):
    """Class that handles the configuration of the full frame model.

    Attributes
    ----------
    minimumNumPixels : int
        The minimum number of pixels that must be in an object.
    sigmaScale : float
        Multiplier for the frame standard deviation.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.sigmaScale = 5.0
        self.minimumNumPixels = 10

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        try:
            self.check("sigmaScale", config["fullFrame"], "sigmaScale")
            self.check("minimumNumPixels", config["fullFrame"], "minimumNumPixels")
        except KeyError:
            pass

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"fullFrame": {}}
        config["fullFrame"]["sigmaScale"] = self.sigmaScale
        config["fullFrame"]["minimumNumPixels"] = self.minimumNumPixels
        return config
