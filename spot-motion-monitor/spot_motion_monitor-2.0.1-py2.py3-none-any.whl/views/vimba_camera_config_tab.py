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

from ..config import VimbaCameraConfig
from spot_motion_monitor.views import BaseConfigTab
from spot_motion_monitor.views.forms.ui_vimba_camera_config import Ui_VimbaCameraConfigForm

__all__ = ['VimbaCameraConfigTab']

class VimbaCameraConfigTab(BaseConfigTab, Ui_VimbaCameraConfigForm):
    """Class that handles the Vimba camera configuration tab.

    Attributes
    ----------
    name : str
        The name for the tab widget.
    config : `config.VimbaCameraConfig`
        The instance that contains the Vimba camera configuration.
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
        self.name = 'Vimba'
        self.config = VimbaCameraConfig()
        self.roiSizeLineEdit.setValidator(QIntValidator(20, 1000))
        self.roiFluxMinLineEdit.setValidator(QIntValidator(100, 10000))
        self.roiExposureTimeLineEdit.setValidator(QIntValidator(500, 50000))
        self.fullFrameExposureTimeLineEdit.setValidator(QIntValidator(500, 50000))
        self.roiSizeLineEdit.textChanged.connect(self.validateInput)
        self.roiFluxMinLineEdit.textChanged.connect(self.validateInput)
        self.roiExposureTimeLineEdit.textChanged.connect(self.validateInput)
        self.fullFrameExposureTimeLineEdit.textChanged.connect(self.validateInput)

    def getConfiguration(self):
        """Get the configuration parameter's from the tab's widgets.

        Returns
        -------
        `config.VimbaCameraConfig`
            The current set of configuration parameters.
        """
        self.config.roiSize = int(self.roiSizeLineEdit.text())
        self.config.roiFluxMinimum = int(self.roiFluxMinLineEdit.text())
        self.config.roiExposureTime = int(self.roiExposureTimeLineEdit.text())
        self.config.fullExposureTime = int(self.fullFrameExposureTimeLineEdit.text())
        return self.config

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : `config.VimbaCameraConfig`
            The current set of configuration parameters.
        """
        self.roiSizeLineEdit.setText(str(config.roiSize))
        self.roiFluxMinLineEdit.setText(str(config.roiFluxMinimum))
        self.roiExposureTimeLineEdit.setText(str(config.roiExposureTime))
        self.fullFrameExposureTimeLineEdit.setText(str(config.fullExposureTime))
