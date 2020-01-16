# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import os

from PyQt5.QtWidgets import QFileDialog

from ..config import GeneralConfig
from . import BaseConfigTab
from .forms.ui_general_config import Ui_GeneralConfigForm
from ..utils import defaultToNoneOrValue, noneToDefaultOrValue, TimeHandler

__all__ = ["GeneralConfigTab"]

class GeneralConfigTab(BaseConfigTab, Ui_GeneralConfigForm):
    """Class that handles the general configuration tab.

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
        timezones = TimeHandler.getTimezones()
        self.timezoneComboBox.insertItems(len(timezones), timezones)
        self.name = 'General'
        self.config = GeneralConfig()
        self.telemetryDirPushButton.clicked.connect(self.handleTelemetryDir)
        self.removeDirectoryCheckBox.toggled.connect(self.handleRemoveTelemetryDir)
        self.clearTelemetryDirPushButton.clicked.connect(self.telemetryDirLineEdit.clear)

    def _openFileDialog(self):
        """Open the directory file dialog

        Returns
        -------
        str
            The selected directory path, empty string if nothing selected.
        """
        options = QFileDialog.DontUseNativeDialog | QFileDialog.ShowDirsOnly
        return QFileDialog.getExistingDirectory(directory=os.path.expanduser("~/"), options=options)

    def getConfiguration(self):
        """Get the configuration parameter's from the tab's widgets.

        Returns
        -------
        `config.GeneralConfig`
            The current set of configuration parameters.
        """
        self.config.site = defaultToNoneOrValue(self.siteNameLineEdit.text())
        self.config.configVersion = defaultToNoneOrValue(self.configVersionLineEdit.text())
        self.config.autorun = self.autorunCheckBox.isChecked()
        timezone = self.timezoneComboBox.currentText()
        self.config.timezone = 'UTC' if timezone == '' else timezone
        self.config.fullTelemetrySavePath = defaultToNoneOrValue(self.telemetryDirLineEdit.text())
        self.config.removeTelemetryDir = self.removeDirectoryCheckBox.isChecked()
        self.config.removeTelemetryFiles = self.removeFilesCheckBox.isChecked()
        return self.config

    def handleTelemetryDir(self):
        """Handle the telemetry directory select push button.
        """
        dirSelected = self._openFileDialog()
        if dirSelected != '':
            self.telemetryDirLineEdit.setText(dirSelected)

    def handleRemoveTelemetryDir(self, state):
        """Handle the remove telemetry directory checkbox state.

        The remove files checkbox should be enabled when this checkbox is
        unchecked. If this checkbox is checked, the remove files checkbox
        should also be checked.

        Parameters
        ----------
        state : bool
            The current state of the checkbox.
        """
        self.removeFilesCheckBox.setEnabled(not state)
        if state:
            self.removeFilesCheckBox.setChecked(True)

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : `config.GeneralConfig`
            The current set of configuration parameters.
        """
        self.siteNameLineEdit.setText(noneToDefaultOrValue(config.site))
        self.configVersionLineEdit.setText(noneToDefaultOrValue(config.configVersion))
        self.autorunCheckBox.setChecked(config.autorun)
        self.timezoneComboBox.setCurrentText(config.timezone)
        self.telemetryDirLineEdit.setText(noneToDefaultOrValue(config.fullTelemetrySavePath))
        self.removeDirectoryCheckBox.setChecked(config.removeTelemetryDir)
        self.removeFilesCheckBox.setChecked(config.removeTelemetryFiles)
