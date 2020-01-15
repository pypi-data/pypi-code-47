# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

from .. import config
from .. import utils
from . import BaseConfigTab
from .forms.ui_psd_plots_config import Ui_PsdPlotConfigForm

__all__ = ['PsdPlotConfigTab']

class PsdPlotConfigTab(BaseConfigTab, Ui_PsdPlotConfigForm):
    """Class that handles the Power Spectrum Distribution plot configuration
       tab.

    Attributes
    ----------
    name : str
        The name for the tab widget.
    """

    def __init__(self, parent=None):
        """Summary

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.name = 'PSD'
        self.waterfallNumBinsLineEdit.setValidator(QIntValidator(1, 1000))
        self.waterfallNumBinsLineEdit.textChanged.connect(self.validateInput)

        self.waterfallColorMapComboBox.addItems(utils.COLORMAPS)

        self.autoscaleX1dCheckBox.stateChanged.connect(self.handleAutoscaleChange)
        self.autoscaleY1dCheckBox.stateChanged.connect(self.handleAutoscaleChange)

    def getConfiguration(self):
        """Get the current configuration parameters from the tab's widgets.

        Returns
        -------
        `config.PsdPlotConfig`
            The current set of configuration parameters.
        """
        outConfig = config.PsdPlotConfig()
        outConfig.numWaterfallBins = int(self.waterfallNumBinsLineEdit.text())
        outConfig.waterfallColorMap = self.waterfallColorMapComboBox.currentText()
        xAutoscale = utils.checkStateToBool(self.autoscaleX1dCheckBox.checkState())
        outConfig.autoscaleX1d = xAutoscale
        if not xAutoscale:
            xMax = utils.defaultToNoneOrValue(self.x1dMaximumLineEdit.text())
            outConfig.x1dMaximum = xMax if xMax is None else float(xMax)
        yAutoscale = utils.checkStateToBool(self.autoscaleY1dCheckBox.checkState())
        outConfig.autoscaleY1d = yAutoscale
        if not yAutoscale:
            yMax = utils.defaultToNoneOrValue(self.y1dMaximumLineEdit.text())
            outConfig.y1dMaximum = yMax if yMax is None else float(yMax)
        return outConfig

    def handleAutoscaleChange(self, currentState):
        """Change state of line edits based on autoscale state.

        Parameters
        ----------
        currentState : int
            The current autoscale state.
        """
        axis = self.sender().objectName().split('autoscale')[-1][0].lower()
        if currentState == Qt.Checked:
            getattr(self, '{}1dMaximumLabel'.format(axis)).setEnabled(False)
            getattr(self, '{}1dMaximumLineEdit'.format(axis)).setEnabled(False)
        else:
            getattr(self, '{}1dMaximumLabel'.format(axis)).setEnabled(True)
            getattr(self, '{}1dMaximumLineEdit'.format(axis)).setEnabled(True)

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : `config.PsdPlotConfig`
            The current set of configuration parameters.
        """
        self.waterfallNumBinsLineEdit.setText(str(config.numWaterfallBins))
        value = utils.noneToDefaultOrValue(config.waterfallColorMap)
        self.waterfallColorMapComboBox.setCurrentText(value)
        self.autoscaleX1dCheckBox.setCheckState(utils.boolToCheckState(config.autoscaleX1d))
        self.x1dMaximumLineEdit.setText(str(utils.noneToDefaultOrValue(config.x1dMaximum)))
        self.autoscaleY1dCheckBox.setCheckState(utils.boolToCheckState(config.autoscaleY1d))
        self.y1dMaximumLineEdit.setText(str(utils.noneToDefaultOrValue(config.y1dMaximum)))
