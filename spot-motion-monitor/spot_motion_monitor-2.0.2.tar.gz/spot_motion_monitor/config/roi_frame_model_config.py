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

__all__ = ['RoiFrameModelConfig']

class RoiFrameModelConfig(BaseConfig):
    """Class that handles the configuration of the ROI frame model.

    Attributes
    ----------
    thresholdFactor : float
        The scale factor multiplied by the frame max and then subtracted from
        the frame.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.thresholdFactor = 0.3

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        try:
            self.check("thresholdFactor", config["roiFrame"], "thresholdFactor")
        except KeyError:
            pass

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"roiFrame": {}}
        config["roiFrame"]["thresholdFactor"] = self.thresholdFactor
        return config
