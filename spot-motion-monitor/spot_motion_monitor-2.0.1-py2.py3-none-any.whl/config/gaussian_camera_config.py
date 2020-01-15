# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from . import CameraConfig

__all__ = ['GaussianCameraConfig']

class GaussianCameraConfig(CameraConfig):
    """Class that handles the configuration of the Gaussian camera.

    Attributes
    ----------
    doSpotOscillation : bool
        Flag tp make the generated spot oscillate.
    xAmplitude : int
        The amplitude of the x component of the spot oscillation.
    xFrequency : float
        The frequency of the x component of the spot oscillation.
    yAmplitude : int
        The amplitude of the y component of the spot oscillation.
    yFrequency : float
        The frequency of the y component of the spot oscillation.
    """

    def __init__(self):
        """Summary
        """
        super().__init__()
        self.doSpotOscillation = False
        self.xAmplitude = 10
        self.xFrequency = 5.0
        self.yAmplitude = 5
        self.yFrequency = 10.0

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        super().fromDict(config)
        self.doSpotOscillation = config["spotOscillation"]["do"]
        self.xAmplitude = config["spotOscillation"]["x"]["amplitude"]
        self.xFrequency = config["spotOscillation"]["x"]["frequency"]
        self.yAmplitude = config["spotOscillation"]["y"]["amplitude"]
        self.yFrequency = config["spotOscillation"]["y"]["frequency"]

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
        config = super().toDict(writeEmpty)
        config["spotOscillation"] = {"x": {}, "y": {}}
        config["spotOscillation"]["do"] = self.doSpotOscillation
        config["spotOscillation"]["x"]["amplitude"] = self.xAmplitude
        config["spotOscillation"]["x"]["frequency"] = self.xFrequency
        config["spotOscillation"]["y"]["amplitude"] = self.yAmplitude
        config["spotOscillation"]["y"]["frequency"] = self.yFrequency
        return config
