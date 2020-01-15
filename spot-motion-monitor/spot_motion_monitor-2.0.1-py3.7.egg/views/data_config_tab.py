# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from PyQt5.QtGui import QDoubleValidator, QIntValidator

from ..config import DataConfig
from ..utils import LARGE_FLOAT_VALUE_FOR_VALIDATOR, LARGE_VALUE_FOR_VALIDATOR
from spot_motion_monitor.views import BaseConfigTab
from spot_motion_monitor.views.forms.ui_data_config import Ui_DataConfigForm

__all__ = ['DataConfigTab']

class DataConfigTab(BaseConfigTab, Ui_DataConfigForm):
    """Class that handles the data configuration tab.

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
        self.name = 'Data'
        self.config = DataConfig()
        self.pixelScaleLineEdit.setValidator(QDoubleValidator(0.0, LARGE_FLOAT_VALUE_FOR_VALIDATOR, 5))
        self.sigmaScaleLineEdit.setValidator(QDoubleValidator(-LARGE_FLOAT_VALUE_FOR_VALIDATOR,
                                                              LARGE_FLOAT_VALUE_FOR_VALIDATOR, 5))
        self.minimumNumPixelsLineEdit.setValidator(QIntValidator(1, LARGE_VALUE_FOR_VALIDATOR))
        self.thresholdFactorLineEdit.setValidator(QDoubleValidator(-LARGE_FLOAT_VALUE_FOR_VALIDATOR,
                                                                   LARGE_FLOAT_VALUE_FOR_VALIDATOR, 5))
        self.pixelScaleLineEdit.textChanged.connect(self.validateInput)
        self.sigmaScaleLineEdit.textChanged.connect(self.validateInput)
        self.minimumNumPixelsLineEdit.textChanged.connect(self.validateInput)
        self.thresholdFactorLineEdit.textChanged.connect(self.validateInput)

    def getConfiguration(self):
        """Get the configuration parameter's from the tab's widgets.

        Returns
        -------
        `config.DataConfig`
            The current set of configuration parameters.
        """
        self.config.buffer.pixelScale = float(self.pixelScaleLineEdit.text())
        self.config.fullFrame.sigmaScale = float(self.sigmaScaleLineEdit.text())
        self.config.fullFrame.minimumNumPixels = int(self.minimumNumPixelsLineEdit.text())
        self.config.roiFrame.thresholdFactor = float(self.thresholdFactorLineEdit.text())
        return self.config

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : `config.DataConfig`
            The current set of configuration parameters.
        """
        self.pixelScaleLineEdit.setText(str(config.buffer.pixelScale))
        self.sigmaScaleLineEdit.setText(str(config.fullFrame.sigmaScale))
        self.minimumNumPixelsLineEdit.setText(str(config.fullFrame.minimumNumPixels))
        self.thresholdFactorLineEdit.setText(str(config.roiFrame.thresholdFactor))
