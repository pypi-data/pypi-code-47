# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from . import BaseConfigurationDialog, GeneralConfigTab

__all__ = ['GeneralConfigurationDialog']

class GeneralConfigurationDialog(BaseConfigurationDialog):
    """Class that generates the dialog for handling general configuration.

    Attributes
    ----------
    generalConfigTab : GeneralConfigTab
        Instance of the general configuration tab.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.generalConfigTab = GeneralConfigTab()

        self.tabWidget.addTab(self.generalConfigTab, self.generalConfigTab.name)
        self.setMinimumSize(self.generalConfigTab.minimumSize())

    def getConfiguration(self):
        """Get the current general configuration from the tab.

        Returns
        -------
        `config.GeneralConfig`
            The current set of configuration parameters.
        """
        config = self.generalConfigTab.getConfiguration()
        return config

    def setConfiguration(self, config):
        """Set the current general configuration in the tab.

        Parameters
        ----------
        config : `config.GeneralConfig`
          The current set of configuration parameters.
        """
        self.generalConfigTab.setConfiguration(config)
