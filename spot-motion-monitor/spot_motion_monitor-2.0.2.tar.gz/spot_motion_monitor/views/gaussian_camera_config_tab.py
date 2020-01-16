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

from ..config import GaussianCameraConfig
import spot_motion_monitor.utils as utils
from spot_motion_monitor.views import BaseConfigTab
from spot_motion_monitor.views.forms.ui_gaussian_camera_config import Ui_GaussianCameraConfigForm

__all__ = ['GaussianCameraConfigTab']

class GaussianCameraConfigTab(BaseConfigTab, Ui_GaussianCameraConfigForm):
    """Class that handles the Gaussian camera configuration tab.

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
        self.name = 'Gaussian'
        self.config = GaussianCameraConfig()
        self.roiSizeLineEdit.setValidator(QIntValidator(20, 200))
        self.xAmpLineEdit.setValidator(QIntValidator(1, 20))
        self.xFreqLineEdit.setValidator(QDoubleValidator(0.1, 100.0, 1, self))
        self.yAmpLineEdit.setValidator(QIntValidator(1, 20))
        self.yFreqLineEdit.setValidator(QDoubleValidator(0.1, 100.0, 1))
        self.spotOscillationCheckBox.toggled.connect(self.changeGroupBoxState)
        self.roiSizeLineEdit.textChanged.connect(self.validateInput)
        self.xAmpLineEdit.textChanged.connect(self.validateInput)
        self.xFreqLineEdit.textChanged.connect(self.validateInput)
        self.yAmpLineEdit.textChanged.connect(self.validateInput)
        self.yFreqLineEdit.textChanged.connect(self.validateInput)

    def changeGroupBoxState(self, checked):
        """Adjust the oscillation parameters group box based on check box
           state.

        Parameters
        ----------
        checked : bool
            The current state of the check box.
        """
        self.spotOscillationGroupBox.setEnabled(checked)

    def getConfiguration(self):
        """Get the configuration parameter's from the tab's widgets.

        Returns
        -------
        `config.GaussianCameraConfig`
            The current set of configuration parameters.
        """
        self.config.roiSize = int(self.roiSizeLineEdit.text())
        self.config.doSpotOscillation = utils.checkStateToBool(self.spotOscillationCheckBox.checkState())
        if self.config.doSpotOscillation:
            xAmp = utils.defaultToNoneOrValue(self.xAmpLineEdit.text())
            self.config.xAmplitude = utils.convertValueOrNone(xAmp)
            xFreq = utils.defaultToNoneOrValue(self.xFreqLineEdit.text())
            self.config.xFrequency = utils.convertValueOrNone(xFreq, convert=float)
            yAmp = utils.defaultToNoneOrValue(self.yAmpLineEdit.text())
            self.config.yAmplitude = utils.convertValueOrNone(yAmp)
            yFreq = utils.defaultToNoneOrValue(self.yFreqLineEdit.text())
            self.config.yFrequency = utils.convertValueOrNone(yFreq, convert=float)
        return self.config

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : `config.GaussianCameraConfig`
            The current set of configuration parameters.
        """
        self.roiSizeLineEdit.setText(str(config.roiSize))
        self.spotOscillationCheckBox.setCheckState(utils.boolToCheckState(config.doSpotOscillation))
        self.xAmpLineEdit.setText(str(config.xAmplitude))
        self.xFreqLineEdit.setText(str(config.xFrequency))
        self.yAmpLineEdit.setText(str(config.yAmplitude))
        self.yFreqLineEdit.setText(str(config.yFrequency))
