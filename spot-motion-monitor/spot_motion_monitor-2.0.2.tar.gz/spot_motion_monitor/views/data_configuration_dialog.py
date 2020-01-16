# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.views import BaseConfigurationDialog, DataConfigTab

__all__ = ['DataConfigurationDialog']

class DataConfigurationDialog(BaseConfigurationDialog):
    """Class that generates the dialog for handling data configuration.

    Attributes
    ----------
    dataConfigTab : DataConfigTab
        Instance of the data configuration tab.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.dataConfigTab = DataConfigTab()

        self.tabWidget.addTab(self.dataConfigTab, self.dataConfigTab.name)
        self.dataConfigTab.hasValidInput.connect(self.inputFromTabsValid)

    def getConfiguration(self):
        """Get the current data configuration from the tab.

        Returns
        -------
        dict
            The current set of configuration parameters.
        """
        config = self.dataConfigTab.getConfiguration()
        return config

    def setConfiguration(self, config):
        """Set the current data configuration in the tab.

        Parameters
        ----------
        config : dict
          The current set of configuration parameters.
        """
        self.dataConfigTab.setConfiguration(config)
