# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from PyQt5.QtGui import QIntValidator

from .. import config
from .. import utils
from . import BaseConfigTab
from .forms.ui_centroid_plots_config import Ui_CentroidPlotsConfigForm

__all__ = ['CentroidPlotConfigTab']

class CentroidPlotConfigTab(BaseConfigTab, Ui_CentroidPlotsConfigForm):
    """Class that handles the centroid plot configuration tab.

    Attributes
    ----------
    name : str
        The name for the tab widget.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.name = 'Centroid'

        intValidator0 = QIntValidator(1, 10000)
        intValidator1 = QIntValidator(0, utils.LARGE_VALUE_FOR_VALIDATOR)
        intValidator2 = QIntValidator(1, utils.LARGE_VALUE_FOR_VALIDATOR)

        self.pixelAdditionXLineEdit.setValidator(intValidator0)
        self.minXLimitLineEdit.setValidator(intValidator1)
        self.maxXLimitLineEdit.setValidator(intValidator1)
        self.pixelAdditionYLineEdit.setValidator(intValidator0)
        self.minYLimitLineEdit.setValidator(intValidator1)
        self.maxYLimitLineEdit.setValidator(intValidator1)
        self.numHistoBinsLineEdit.setValidator(intValidator2)

        self.pixelAdditionXLineEdit.textChanged.connect(self.validateInput)
        self.minXLimitLineEdit.textChanged.connect(self.validateInput)
        self.maxXLimitLineEdit.textChanged.connect(self.validateInput)
        self.pixelAdditionYLineEdit.textChanged.connect(self.validateInput)
        self.minYLimitLineEdit.textChanged.connect(self.validateInput)
        self.maxYLimitLineEdit.textChanged.connect(self.validateInput)
        self.numHistoBinsLineEdit.textChanged.connect(self.validateInput)

        self.autoscaleXComboBox.currentIndexChanged.connect(self.handleAutoscaleChange)
        self.autoscaleYComboBox.currentIndexChanged.connect(self.handleAutoscaleChange)

    def getConfiguration(self):
        """Get the current configuration parameters from the tab's widgets.

        Returns
        -------
        dict
            The current set of configuration parameters.
        """
        outConfig = config.CentroidPlotConfig()
        xAutoscale = self.autoscaleXComboBox.currentText()
        outConfig.autoscaleX = getattr(utils.AutoscaleState, xAutoscale)
        if xAutoscale == utils.AutoscaleState.OFF.name:
            xMin = utils.defaultToNoneOrValue(self.minXLimitLineEdit.text())
            outConfig.minimumX = xMin if xMin is None else int(xMin)
            xMax = utils.defaultToNoneOrValue(self.maxXLimitLineEdit.text())
            outConfig.maximumX = xMax if xMax is None else int(xMax)
        elif xAutoscale == utils.AutoscaleState.PARTIAL.name:
            xPixelAddition = utils.defaultToNoneOrValue(self.pixelAdditionXLineEdit.text())
            xValue = xPixelAddition if xPixelAddition is None else int(xPixelAddition)
            outConfig.pixelRangeAdditionX = xValue
        yAutoscale = self.autoscaleYComboBox.currentText()
        outConfig.autoscaleY = getattr(utils.AutoscaleState, yAutoscale)
        if yAutoscale == utils.AutoscaleState.OFF.name:
            yMin = utils.defaultToNoneOrValue(self.minYLimitLineEdit.text())
            outConfig.minimumY = yMin if yMin is None else int(yMin)
            yMax = utils.defaultToNoneOrValue(self.maxYLimitLineEdit.text())
            outConfig.maximumY = yMax if yMax is None else int(yMax)
        elif yAutoscale == utils.AutoscaleState.PARTIAL.name:
            yPixelAddition = utils.defaultToNoneOrValue(self.pixelAdditionYLineEdit.text())
            yValue = yPixelAddition if yPixelAddition is None else int(yPixelAddition)
            outConfig.pixelRangeAdditionY = yValue
        outConfig.numHistogramBins = int(self.numHistoBinsLineEdit.text())
        return outConfig

    def handleAutoscaleChange(self, currentIndex):
        """Change state of line edits based on autoscale state.

        Parameters
        ----------
        currentIndex : int
            The current autoscale state.
        """
        axis = self.sender().objectName().split('autoscale')[-1][0]
        if currentIndex == utils.AutoscaleState.ON.value:
            getattr(self, 'pixelAddition{}Label'.format(axis)).setEnabled(False)
            getattr(self, 'min{}LimitLabel'.format(axis)).setEnabled(False)
            getattr(self, 'max{}LimitLabel'.format(axis)).setEnabled(False)
            getattr(self, 'pixelAddition{}LineEdit'.format(axis)).setEnabled(False)
            getattr(self, 'min{}LimitLineEdit'.format(axis)).setEnabled(False)
            getattr(self, 'max{}LimitLineEdit'.format(axis)).setEnabled(False)
        elif currentIndex == utils.AutoscaleState.PARTIAL.value:
            getattr(self, 'pixelAddition{}Label'.format(axis)).setEnabled(True)
            getattr(self, 'min{}LimitLabel'.format(axis)).setEnabled(False)
            getattr(self, 'max{}LimitLabel'.format(axis)).setEnabled(False)
            getattr(self, 'pixelAddition{}LineEdit'.format(axis)).setEnabled(True)
            getattr(self, 'min{}LimitLineEdit'.format(axis)).setEnabled(False)
            getattr(self, 'max{}LimitLineEdit'.format(axis)).setEnabled(False)
        else:
            getattr(self, 'pixelAddition{}Label'.format(axis)).setEnabled(False)
            getattr(self, 'min{}LimitLabel'.format(axis)).setEnabled(True)
            getattr(self, 'max{}LimitLabel'.format(axis)).setEnabled(True)
            getattr(self, 'pixelAddition{}LineEdit'.format(axis)).setEnabled(False)
            getattr(self, 'min{}LimitLineEdit'.format(axis)).setEnabled(True)
            getattr(self, 'max{}LimitLineEdit'.format(axis)).setEnabled(True)

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : `config.CentroidPlotConfig`
            The current set of configuration parameters.
        """
        self.autoscaleXComboBox.setCurrentText(config.autoscaleX.name)
        xPixelAddition = utils.noneToDefaultOrValue(config.pixelRangeAdditionX)
        self.pixelAdditionXLineEdit.setText(str(xPixelAddition))
        self.minXLimitLineEdit.setText(str(utils.noneToDefaultOrValue(config.minimumX)))
        self.maxXLimitLineEdit.setText(str(utils.noneToDefaultOrValue(config.maximumX)))
        self.autoscaleYComboBox.setCurrentText(config.autoscaleY.name)
        yPixelAddition = utils.noneToDefaultOrValue(config.pixelRangeAdditionY)
        self.pixelAdditionYLineEdit.setText(str(yPixelAddition))
        self.minYLimitLineEdit.setText(str(utils.noneToDefaultOrValue(config.minimumY)))
        self.maxYLimitLineEdit.setText(str(utils.noneToDefaultOrValue(config.maximumY)))
        value = utils.noneToDefaultOrValue(config.numHistogramBins)
        self.numHistoBinsLineEdit.setText(str(value))
