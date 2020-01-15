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

__all__ = ['PsdPlotConfig']

class PsdPlotConfig(BaseConfig):
    """Class that handles the configuration of the Power Spectrum Distribution
       plots (1D and waterfall).

    Attributes
    ----------
    autoscaleX1d : bool
        Set autoscaling on the x component 1D PSD plot.
    autoscaleY1d : bool
        Set autoscaling on the y component 1D PSD plot.
    numWaterfallBins : int
        Set the number of vertical bins for the waterfall PSD plots.
    waterfallColorMap : str
        Set the color map for the waterfall PSD plots.
    x1dMaximum : int
        Set the maximum y axis value for on the x component 1D PSD plot.
    x1dMinimum : int
        Set the minimum y axis value for on the x component 1D PSD plot.
    y1dMaximum : int
        Set the maximum y axis value for on the y component 1D PSD plot.
    y1dMinimum : int
        Set the minimum y axis value for on the y component 1D PSD plot.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.autoscaleX1d = False
        self.x1dMinimum = 0
        self.x1dMaximum = 1000
        self.autoscaleY1d = False
        self.y1dMinimum = 0
        self.y1dMaximum = 1000
        self.numWaterfallBins = 25
        self.waterfallColorMap = "viridis"

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.autoscaleX1d = config["xPSD"]["autoscaleY"]
        self.x1dMaximum = config["xPSD"]["maximumY"]
        self.autoscaleY1d = config["yPSD"]["autoscaleY"]
        self.y1dMaximum = config["yPSD"]["maximumY"]
        self.numWaterfallBins = config["waterfall"]["numBins"]
        self.waterfallColorMap = config["waterfall"]["colorMap"]

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
        config = {"xPSD": {}, "yPSD": {}, "waterfall": {}}
        config["xPSD"]["autoscaleY"] = self.autoscaleX1d
        if writeEmpty or self.x1dMaximum is not None:
            config["xPSD"]["maximumY"] = self.x1dMaximum
        config["yPSD"]["autoscaleY"] = self.autoscaleY1d
        if writeEmpty or self.y1dMaximum is not None:
            config["yPSD"]["maximumY"] = self.y1dMaximum
        config["waterfall"]["numBins"] = self.numWaterfallBins
        config["waterfall"]["colorMap"] = self.waterfallColorMap
        return config
