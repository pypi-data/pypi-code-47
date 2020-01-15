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
from .. import utils

__all__ = ['CentroidPlotConfig']

class CentroidPlotConfig(BaseConfig):
    """Class for handling the configuration of the centroid plots (1D line,
       scatter and 1D histogram)

    Attributes
    ----------
    autoscaleX : `utils.AutoscaleState`
        Set autoscaling on the x component 1D centroid line plot.
    autoscaleY : `utils.AutoscaleState`
        Set autoscaling on the y component 1D centroid line plot.
    maximumX : int
        Set the maximum y axis value for on the x component 1D centroid line
        plot.
    maximumY : int
        Set the maximum y axis value for on the y component 1D centroid line
        plot.
    minimumX : int
        Set the minimum y axis value for on the x component 1D centroid line
        plot.
    minimumY : int
        Set the minimum y axis value for on the y component 1D centroid line
        plot.
    numHistogramBins : int
        Set the number of histogram bins on the 1D centroid histogram plots.
    pixelRangeAdditionX : int
        Set the extra scale for the x component 1D centroid line once the quick
        average is taken.
    pixelRangeAdditionY : int
        Set the extra scale for the y component 1D centroid line once the quick
        average is taken.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.autoscaleX = utils.AutoscaleState.OFF
        self.minimumX = 0
        self.maximumX = 100
        self.pixelRangeAdditionX = 25
        self.autoscaleY = utils.AutoscaleState.OFF
        self.minimumY = 0
        self.maximumY = 100
        self.pixelRangeAdditionY = 25
        self.numHistogramBins = 40

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.autoscaleX = getattr(utils.AutoscaleState, config["xCentroid"]["autoscaleY"])
        self.minimumX = config["xCentroid"]["minimumY"]
        self.maximumX = config["xCentroid"]["maximumY"]
        self.pixelRangeAdditionX = config["xCentroid"]["pixelRangeAddition"]
        self.autoscaleY = getattr(utils.AutoscaleState, config["yCentroid"]["autoscaleY"])
        self.minimumY = config["yCentroid"]["minimumY"]
        self.maximumY = config["yCentroid"]["maximumY"]
        self.pixelRangeAdditionY = config["yCentroid"]["pixelRangeAddition"]
        self.numHistogramBins = config["scatterPlot"]["histograms"]["numBins"]

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
        config = {"xCentroid": {}, "yCentroid": {}, "scatterPlot": {"histograms": {}}}
        config["xCentroid"]["autoscaleY"] = self.autoscaleX.name
        if writeEmpty or self.minimumX is not None:
            config["xCentroid"]["minimumY"] = self.minimumX
        if writeEmpty or self.maximumX is not None:
            config["xCentroid"]["maximumY"] = self.maximumX
        if writeEmpty or self.pixelRangeAdditionX is not None:
            config["xCentroid"]["pixelRangeAddition"] = self.pixelRangeAdditionX
        config["yCentroid"]["autoscaleY"] = self.autoscaleY.name
        if writeEmpty or self.minimumY is not None:
            config["yCentroid"]["minimumY"] = self.minimumY
        if writeEmpty or self.maximumY is not None:
            config["yCentroid"]["maximumY"] = self.maximumY
        if writeEmpty or self.pixelRangeAdditionY is not None:
            config["yCentroid"]["pixelRangeAddition"] = self.pixelRangeAdditionY
        config["scatterPlot"]["histograms"]["numBins"] = self.numHistogramBins
        return config
