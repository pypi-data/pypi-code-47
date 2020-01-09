# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from spot_motion_monitor.views.forms.ui_configuration_dialog import Ui_ConfigurationDialog

__all__ = ['BaseConfigurationDialog']

class BaseConfigurationDialog(QDialog, Ui_ConfigurationDialog):
    """Class that handles to base API for the configuration dialogs.
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

    def inputFromTabsValid(self, hasValidInput):
        """Disable OK button is input from tab is invalid.

        Parameters
        ----------
        hasValidInput : bool
            True is input is valid, False if not.
        """
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(hasValidInput)
