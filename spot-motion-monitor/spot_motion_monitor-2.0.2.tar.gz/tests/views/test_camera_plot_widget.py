# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.views.camera_plot_widget import CameraPlotWidget

class TestCameraPlotWidget():

    def test_parametersAfterConstruction(self, qtbot):
        cpw = CameraPlotWidget()
        cpw.show()
        qtbot.addWidget(cpw)
        assert cpw.image is not None
