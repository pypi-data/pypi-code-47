# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from collections import OrderedDict
import os

from spot_motion_monitor.views import CameraInformationDialog

class TestCameraInformationDialog:

    def test_parametersAfterConstruction(self, qtbot):
        dialog = CameraInformationDialog()
        qtbot.addWidget(dialog)
        dialog.show()

        assert dialog.cameraInfoTextBrowser.toPlainText() == ''

    def test_formattedText(self, qtbot):
        dialog = CameraInformationDialog()
        qtbot.addWidget(dialog)

        cameraInfo = OrderedDict()
        cameraInfo['Model'] = "Tester"
        cameraInfo['Vendor'] = "Good Times"
        cameraInfo['Width'] = 600
        cameraInfo['Height'] = 400

        dialog.setCameraInformation(cameraInfo)
        dialog.show()

        truthText = ['Model: Tester', 'Vendor: Good Times',
                     'Width: 600', 'Height: 400']
        truthString = os.linesep.join(truthText)

        assert dialog.cameraInfoTextBrowser.toPlainText() == truthString
