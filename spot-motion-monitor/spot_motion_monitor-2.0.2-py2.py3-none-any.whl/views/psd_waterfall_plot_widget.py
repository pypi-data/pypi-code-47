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
from PyQt5 import QtCore
from pyqtgraph import GraphicsLayoutWidget, ImageItem

from spot_motion_monitor.utils import HTML_NU, getLutFromColorMap

__all__ = ['PsdWaterfallPlotWidget']

class PsdWaterfallPlotWidget(GraphicsLayoutWidget):

    """This class manages and displays the power spectrum distribution (PSD)
       data in a waterfall plot.

    Attributes
    ----------
    arraySize : int
        The size of the data array to display.
    boundingRect : QtCore.QRectF
        The actual coordinate space base on frequency and time of acquisition.
    data : numpy.ndarray
        The 2D array for the PSD data.
    image : pyqtgraph.ImageItem
        The instance of the image item for display.
    timeScale : float
        The total time for the buffer to accumulate at the ROI FPS.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.plot = self.addPlot()
        self.plot.invertY()

        self.image = ImageItem()
        self.image.setOpts(axisOrder='row-major')
        self.plot.addItem(self.image)

        self.data = None
        self.arraySize = None
        self.boundingRect = None
        self.timeScale = None
        self.colorMap = 'viridis'
        self.image.setLookupTable(getLutFromColorMap(self.colorMap))

    def clearPlot(self):
        """Reset all data and clear the plot.
        """
        self.data = None
        self.boundingRect = None
        self.image.clear()

    def getConfiguration(self):
        """Get the current plot configuration.

        Returns
        -------
        int, str
            The set of current configuration parameters.
        """
        return self.arraySize, self.colorMap

    def setConfiguration(self, config):
        """Set the new parameters into the widget.

        Parameters
        ----------
        config : `config.PsdPlotConfig`
            The new parameters to apply.
        """
        numBins = config.numWaterfallBins
        if self.arraySize != numBins:
            self.arraySize = numBins
            # Invalidate data
            self.data = None
            self.boundingRect = None

        colorMap = config.waterfallColorMap
        if self.colorMap != colorMap:
            self.colorMap = colorMap
            self.image.setLookupTable(getLutFromColorMap(self.colorMap))

    def setTimeScale(self, timeScale):
        """Update the stored timescale and invalidate data and bounding rect.

        Parameters
        ----------
        timeScale : float
            The new timescale.
        """
        self.timeScale = timeScale
        self.data = None
        self.boundingRect = None

    def setup(self, arraySize, timeScale, axisLabel):
        """Setup the widget with the array size.

        Parameters
        ----------
        arraySize : int
            The size fo the data array to display in terms of history.
        timeScale : float
            The total time for the buffer to accumulate at the ROI FPS.
        axisLabel : str
            Label for particular centroid coordinate.
        """
        self.arraySize = arraySize
        self.timeScale = timeScale
        self.plot.setLabel('bottom', '{} {}'.format(axisLabel, HTML_NU), units='Hz')
        self.plot.setLabel('left', 'Time', units='s')

    def updatePlot(self, psd, freqs):
        """Update the current plot with the given data.

        Parameters
        ----------
        psd : numpy.array
            The PSD data of a given centroid coordinate.
        freqs : numpy.array
            The frequency array associated with the PSD data.
        """
        if self.data is None:
            self.data = np.zeros((self.arraySize, psd.size))
        else:
            self.data[1:, ...] = self.data[:-1, ...]
        self.data[0, ...] = np.log(psd)

        self.image.setImage(self.data)
        if self.boundingRect is None:
            self.boundingRect = QtCore.QRectF(0, 0, freqs[-1], self.arraySize * self.timeScale)
            self.image.setRect(self.boundingRect)
