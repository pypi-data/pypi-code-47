# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from .. import config

__all__ = ['PlotPsdController']

class PlotPsdController:

    """This class handles the interactions between the main program and the
       power spectrum distribution (PSD) waterfall plots.

    Attributes
    ----------
    config : `config.PsdPlotConfig`
        The instance that holds the current configuration.
    psd1dXPlot : Psd1dPlotWidget
        The instance of the 1d plot for the PSD x coordinates.
    psd1dYPlot : Psd1dPlotWidget
        The instance of the 1d plot for the PSD y coordinates.
    psdWaterfallXPlot : PsdWaterfallPlotWidget
        The instance of the waterfall plot for the PSD x coordinates.
    psdWaterfallYPlot : PsdWaterfallPlotWidget
        The instance of the waterfall plot for the PSD y coordinates.
    """

    def __init__(self, psdwfx, psdwfy, psd1dx, psd1dy):
        """Initialize the class.

        Parameters
        ----------
        psdwfx : PsdWaterfallPlotWidget
            The instance of the waterfall plot for the PSD x coordinates.
        psdwfy : PsdWaterfallPlotWidget
            The instance of the waterfall plot for the PSD y coordinates.
        psd1dx : Psd1dPlotWidget
            The instance of the 1d plot for the PSD x coordinates.
        psd1dy : Psd1dPlotWidget
            The instance of the 1d plot for the PSD y coordinates.
        """
        self.psdWaterfallXPlot = psdwfx
        self.psdWaterfallYPlot = psdwfy
        self.psd1dXPlot = psd1dx
        self.psd1dYPlot = psd1dy
        self.config = config.PsdPlotConfig()

    def getPlotConfiguration(self):
        """Get the current camera configuration.

        Returns
        -------
        `config.PsdPlotConfig`
            The set of current camera configuration parameters.
        """

        self.config.numWaterfallBins, self.config.waterfallColorMap = \
            self.psdWaterfallXPlot.getConfiguration()
        self.config.autoscaleX1d, ixrange = self.psd1dXPlot.getConfiguration()
        self.config.x1dMinimum = ixrange[0]
        self.config.x1dMaximum = ixrange[1]
        self.config.autoscaleY1d, iyrange = self.psd1dYPlot.getConfiguration()
        self.config.y1dMinimum = iyrange[0]
        self.config.y1dMaximum = iyrange[1]
        return self.config

    def handleAcquireRoiStateChange(self, checked):
        """Deal with changes in the Acquire ROI checkbox.

        Parameters
        ----------
        checked : bool
            State of the Acquire ROI checkbox.
        """
        if not checked:
            self.psd1dXPlot.clearPlot()
            self.psd1dYPlot.clearPlot()
            self.psdWaterfallXPlot.clearPlot()
            self.psdWaterfallYPlot.clearPlot()

    def setPlotConfiguration(self, config):
        """Set a new configuration on the PSD plots.

        Parameters
        ----------
        config : `config.PsdPlotConfig`
            The new configuration parameters.
        """
        self.psdWaterfallXPlot.setConfiguration(config)
        self.psdWaterfallYPlot.setConfiguration(config)
        self.psd1dXPlot.setConfiguration(config)
        self.psd1dYPlot.setConfiguration(config)

    def setup(self, arraySize, timeScale):
        """Setup the controller's internal information.

        Parameters
        ----------
        arraySize : int
            The vertical dimension of the PSD waterfall plot data.
        timeScale : float
            The total accumulation time from the buffer size and ROI FPS.
        """
        self.psdWaterfallXPlot.setup(arraySize, timeScale, 'X')
        self.psdWaterfallYPlot.setup(arraySize, timeScale, 'Y')
        self.psd1dXPlot.setup('X')
        self.psd1dYPlot.setup('Y')

    def update(self, psdDataX, psdDataY, frequencies):
        """Update the controller's plot widgets with the data provided.

        NOTE: If NoneType data is provided, the updatePlot methods are not called.

        Parameters
        ----------
        psdDataX : numpy.array
            The array of the PSD x coordinate data.
        psdDataY : numpy.array
            The array of the PSD y coordinate data.
        frequencies : numpy.array
            The frequency array associated with the PSD data.
        """
        if psdDataX is None or psdDataY is None or frequencies is None:
            return

        self.psdWaterfallXPlot.updatePlot(psdDataX, frequencies)
        self.psdWaterfallYPlot.updatePlot(psdDataY, frequencies)
        self.psd1dXPlot.updatePlot(psdDataX, frequencies)
        self.psd1dYPlot.updatePlot(psdDataY, frequencies)

    def updateTimeScale(self, newTimeScale):
        """Update the stored timescale in the plot widgets.

        Parameters
        ----------
        newTimeScale : float
            The new timescale.
        """
        self.psdWaterfallXPlot.setTimeScale(newTimeScale)
        self.psdWaterfallYPlot.setTimeScale(newTimeScale)
