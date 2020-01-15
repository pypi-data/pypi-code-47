# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from . import BaseConfig

__all__ = ("CameraConfig")

class CameraConfig(BaseConfig):
    """Class that handles the general configuration of cameras.

    Attributes
    ----------
    fpsFullFrame : int
        The acquisition frame rate for full frames.
    fpsRoiFrame : int
        The acquisition frame rate for ROI frames.
    roiSize : int
        The size (pixels) of the ROI on the camera.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.roiSize = 50
        self.fpsFullFrame = 24
        self.fpsRoiFrame = 40

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.check("roiSize", config["roi"], "size")
        self.check("fpsRoiFrame", config["roi"], "fps")
        try:
            self.check("fpsFullFrame", config["full"], "fps")
        except KeyError:
            pass

    def toDict(self, writeEmpty=False):
        """Translate class attributes to configuration dict.

        Parameters
        ----------
        writeEmpty : bool
            Flag to write parameters with None as values.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"roi": {}, "full": {}}
        config["roi"]["size"] = self.roiSize
        config["roi"]["fps"] = self.fpsRoiFrame
        config["full"]["fps"] = self.fpsFullFrame
        return config
