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

from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QDialog

from .forms.ui_camera_info_dialog import Ui_CameraInformationDialog

__all__ = ['CameraInformationDialog']

class CameraInformationDialog(QDialog, Ui_CameraInformationDialog):
    """Class that generates the dialog for showing camera information.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        camera : str
            The name of the camera to get the configuration tab for.
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)

    def setCameraInformation(self, cameraInfo):
        """Take the camera information, format and display it.

        Parameters
        ----------
        cameraInfo : OrderedDict
            The set of camera information to display.
        """
        lines = []
        max_width = 0
        max_height = len(cameraInfo.keys())
        for key, value in cameraInfo.items():
            lines.append(f'<p><b>{key}</b>: {value}</p>')
            max_width = max(max_width, len(key) + len(str(value)) + 2)

        fontMetrics = QFontMetrics(self.cameraInfoTextBrowser.font())

        scale_factor = 1.75

        browser_height = int(max_height * fontMetrics.lineSpacing() * scale_factor)
        browser_width = max_width * fontMetrics.averageCharWidth()

        self.cameraInfoTextBrowser.setHtml(os.linesep.join(lines))

        if self.cameraInfoTextBrowser.minimumHeight() < browser_height:
            self.cameraInfoTextBrowser.setMinimumHeight(browser_height)
            self.cameraInfoTextBrowser.setMaximumHeight(browser_height)
        if self.cameraInfoTextBrowser.minimumWidth() < browser_width:
            self.cameraInfoTextBrowser.setMinimumWidth(browser_width)
            self.cameraInfoTextBrowser.setMaximumWidth(browser_width)
