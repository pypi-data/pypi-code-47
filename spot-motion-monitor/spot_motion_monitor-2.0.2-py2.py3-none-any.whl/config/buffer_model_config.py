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

__all__ = ['BufferModelConfig']

class BufferModelConfig(BaseConfig):
    """Class that handles the configuration of the buffer model.

    Attributes
    ----------
    bufferSize : int
        Size of the buffer for data storage. Should be power of 2.
    pixelScale : float
        Pixel scale in arcseconds per pixel of the optical system in front of
        the camera.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.bufferSize = 1024
        self.pixelScale = 1.0

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.check("bufferSize", config["buffer"], "size")
        self.check("pixelScale", config["buffer"], "pixelScale")

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"buffer": {}}
        config["buffer"]["size"] = self.bufferSize
        config["buffer"]["pixelScale"] = self.pixelScale
        return config
