# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import spot_motion_monitor.views
from spot_motion_monitor.views import BaseConfigurationDialog

__all__ = ['CameraConfigurationDialog']

class CameraConfigurationDialog(BaseConfigurationDialog):
    """Class that generates the dialog for handling camera configuration.

    Attributes
    ----------
    cameraConfigTab : GaussianCameraConfigTab or VimbaCameraConfigTab
        Instance of the appropriate camera configuration tab.
    """

    def __init__(self, camera, parent=None):
        """Initialize the class.

        Parameters
        ----------
        camera : str
            The name of the camera to get the configuration tab for.
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.cameraConfigTab = getattr(spot_motion_monitor.views, '{}ConfigTab'.format(camera))()

        self.tabWidget.addTab(self.cameraConfigTab, self.cameraConfigTab.name)
        self.setMinimumSize(self.cameraConfigTab.minimumSize())
        self.cameraConfigTab.hasValidInput.connect(self.inputFromTabsValid)

    def getCameraConfiguration(self):
        """Get the current camera configuration from the tab.

        Returns
        -------
        dict
            The current set of configuration parameters.
        """
        config = self.cameraConfigTab.getConfiguration()
        return config

    def setCameraConfiguration(self, config):
        """Set the current camera configuration in the tab.

        Parameters
        ----------
        config : dict
          The current set of configuration parameters.
        """
        self.cameraConfigTab.setConfiguration(config)
