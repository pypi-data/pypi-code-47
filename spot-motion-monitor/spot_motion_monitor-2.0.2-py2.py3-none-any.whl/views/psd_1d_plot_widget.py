# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from pyqtgraph import GraphicsLayoutWidget

from ..utils import HTML_NU, noneToDefaultOrValue

__all__ = ['Psd1dPlotWidget']

class Psd1dPlotWidget(GraphicsLayoutWidget):

    """This class handles managing the 1D Power Spectrum Distribution plots
       for both x and y components.

    Attributes
    ----------
    autoscale : .AutoscaleState
        The status of auto scaling the plot.
    curve : pyqtgraph.PlotDataItem
        Instance of the line in the plot.
    plot : pyqtgraph.PlotItem
        Instance of the graphics plot.
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
        self.plot = self.addPlot()
        self.plot.setLogMode(y=True)
        self.curve = self.plot.plot([], [])
        self.autoscale = True
        self.yRange = None
        self.axis = None

    def clearPlot(self):
        """Reset all data and clear the plot.
        """
        self.curve.setData([], [])
        self.plot.setRange(xRange=(0, 1), yRange=(0.1, 1), padding=0, disableAutoRange=False)

    def getConfiguration(self):
        """Get the current plot configuration.

        Returns
        -------
        bool, tuple
            The set of current configuration parameters.
        """
        if self.yRange is not None:
            yRange = [self.yRange[0], self.yRange[1]]
        else:
            yRange = [None, None]
        return self.autoscale, yRange

    def setConfiguration(self, config):
        """Set the new parameters into the widget.

        Parameters
        ----------
        config : `config.PsdPlotConfig`
            The new parameters to apply.
        """
        self.autoscale = getattr(config, f'autoscale{self.axis}1d')
        if self.autoscale:
            self.plot.enableAutoRange()
            self.yRange = None
        else:
            minimum = noneToDefaultOrValue(getattr(config, f'{self.axis.lower()}1dMinimum'), default=0)
            maximum = noneToDefaultOrValue(getattr(config, f'{self.axis.lower()}1dMaximum'), default=1000)
            self.yRange = [minimum, maximum]
            self.plot.setRange(yRange=self.yRange)
            self.plot.disableAutoRange()

    def setup(self, axisLabel):
        """Provide information for setting up the plot.

        Parameters
        ----------
        axisLabel : str
            The label for the axis.
        """
        self.axis = axisLabel
        self.plot.setLabel('bottom', '{} {}'.format(axisLabel, HTML_NU), units='Hz')
        self.plot.setLabel('left', 'PSD', units='pixel^2 s')

    def updatePlot(self, psdData, frequencies):
        """Update the plot with new PSD and frequency arrays.

        Parameters
        ----------
        psdData : numpy.array
            Instance of the current Power Spectrum Distribution data.
        frequencies : numpy.array
            Instance of the current frequency axis for the PSD data.
        """
        self.curve.setData(frequencies, psdData)
