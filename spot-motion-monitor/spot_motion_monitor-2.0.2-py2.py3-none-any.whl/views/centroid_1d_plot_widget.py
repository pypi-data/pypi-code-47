# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import numpy as np
from pyqtgraph import GraphicsLayoutWidget

from ..utils import AutoscaleState, noneToDefaultOrValue

__all__ = ['Centroid1dPlotWidget']

class Centroid1dPlotWidget(GraphicsLayoutWidget):

    """This class handles managing the centroid plots for both x and y
       coordinates.

    Attributes
    ----------
    autoscale : `utils.AutoscaleState`
        State of plot auto scaling.
    axis : str
        Component axis (X or Y).
    curve : pyqtgraph.PlotDataItem
        Instance of the line in the plot.
    data : numpy.array
        Container for the centroid data.
    dataCounter : int
        Number of times data array has been appended to up until array size.
    dataSize : int
        The requested size of the data array.
    numAccumFrames : int
        The number of frames to accumulate before calculating y range.
    pixelRangeAddition : int
        The value to subtract and add to the mean of the accumulated data.
    plot : pyqtgraph.PlotItem
        Instance of the graphics plot.
    roiFps : float
        The camera ROI FPS.
    rollArray : bool
        Flag as to when to start rolling the data array of centroid values.
    timeRange : numpy.array
        The values for the accumulation time range.
    yRange : list
        The bounds for the y axis of the plot when disabling auto range.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.plot = None
        self.curve = None
        self.dataSize = None
        self.data = None
        self.timeRange = None
        self.rollArray = False
        self.dataCounter = 0
        self.roiFps = None
        self.autoscale = AutoscaleState.PARTIAL
        self.yRange = None
        self.pixelRangeAddition = 10
        self.numAccumFrames = 15
        self.axis = None

    def clearPlot(self):
        """Reset all data and clear the plot.
        """
        self.rollArray = False
        self.dataCounter = 0
        self.data = np.zeros(self.dataSize)
        self.curve.clear()
        self.plot.enableAutoRange()
        self.yRange = None
        self.plot.setRange(yRange=(-0.5, 0.5))

    def getConfiguration(self):
        """Get the current plot configuration.

        Returns
        -------
        bool, tuple, int
            The set of current configuration parameters.
        """
        if self.yRange is not None:
            yRange = [self.yRange[0], self.yRange[1]]
        else:
            yRange = [None, None]
        return self.autoscale, yRange, self.pixelRangeAddition

    def setConfiguration(self, config):
        """Set the new parameters into the widget.

        Parameters
        ----------
        config : `config.CentroidPlotConfig`
            The new parameters to apply.
        """
        self.autoscale = getattr(config, f'autoscale{self.axis}')
        if self.autoscale == AutoscaleState.ON:
            self.plot.enableAutoRange()
            self.yRange = None
        elif self.autoscale == AutoscaleState.PARTIAL:
            self.yRange = None
            self.pixelRangeAddition = getattr(config, f'pixelRangeAddition{self.axis}')
        else:
            minimum = noneToDefaultOrValue(getattr(config, f'minimum{self.axis}'), default=0)
            maximum = noneToDefaultOrValue(getattr(config, f'maximum{self.axis}'), default=1000)
            self.yRange = [minimum, maximum]
            self.plot.setRange(yRange=self.yRange)
            self.plot.disableAutoRange()

    def setup(self, arraySize, axisLabel, roiFps):
        """Provide information for setting up the plot.

        Parameters
        ----------
        arraySize : int
            The size for the plot data array.
        axisLabel : str
            The label for the axis.
        roiFps : float
            The camera ROI FPS.
        """
        self.axis = axisLabel
        self.dataSize = arraySize
        self.data = np.zeros(self.dataSize)
        self.roiFps = roiFps
        self.timeRange = np.arange(self.dataSize) / self.roiFps
        self.plot = self.addPlot()
        self.curve = self.plot.plot(self.timeRange, self.data)
        self.plot.setLabel('bottom', 'Time', units='s')
        self.plot.setLabel('left', axisLabel, units='pixel')

    def setArraySize(self, arraySize):
        """Update the stored array size and adjust arrays.

        Parameters
        ----------
        arraySize : int
            The new array size to use.
        """
        self.dataSize = arraySize
        self.data = np.zeros(self.dataSize)
        self.timeRange = np.arange(self.dataSize) / self.roiFps
        self.curve.setData(self.timeRange, self.data)
        self.rollArray = False

    def setRoiFps(self, roiFps):
        """Update the stored ROI FPS and adjust arrays.

        Parameters
        ----------
        roiFps : int
            The new ROI FPS.
        """
        self.roiFps = roiFps
        self.timeRange = np.arange(self.dataSize) / self.roiFps
        self.curve.setData(self.timeRange, self.data)

    def updatePlot(self, centroid):
        """Update the plot with a new centroid.

        Parameters
        ----------
        centroid : float
            The current centroid value to plot.
        """
        if self.rollArray:
            self.data[:-1] = self.data[1:]
            self.data[-1] = centroid
        else:
            self.data[self.dataCounter] = centroid

        if self.dataCounter < self.dataSize:
            self.dataCounter += 1
            if self.dataCounter == self.dataSize:
                self.rollArray = True

        if self.autoscale == AutoscaleState.PARTIAL:
            if self.dataCounter == self.numAccumFrames and self.yRange is None:
                cmean = int(np.mean(self.data[0:self.numAccumFrames]))
                self.yRange = [cmean - self.pixelRangeAddition, cmean + self.pixelRangeAddition]
                self.plot.setRange(yRange=self.yRange)
                self.plot.disableAutoRange()

        self.curve.setData(self.timeRange, self.data)
