# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import pytest

from spot_motion_monitor.camera.base_camera import BaseCamera

class TestBaseCamera(object):

    def setup_class(self):
        self.baseCamera = BaseCamera()

    def test_nullParametersAfterConstruction(self):
        assert self.baseCamera.height is None
        assert self.baseCamera.width is None
        assert self.baseCamera.fpsFullFrame is None
        assert self.baseCamera.fpsRoiFrame is None
        assert self.baseCamera.roiSize is None
        assert self.baseCamera.name == 'Base'
        assert self.baseCamera.config is None

    def test_noApiAfterConstruction(self):
        with pytest.raises(NotImplementedError):
            self.baseCamera.startup()

        with pytest.raises(NotImplementedError):
            self.baseCamera.shutdown()

        with pytest.raises(NotImplementedError):
            self.baseCamera.getFullFrame()

        with pytest.raises(NotImplementedError):
            self.baseCamera.getRoiFrame()

        with pytest.raises(NotImplementedError):
            self.baseCamera.getOffset()

        with pytest.raises(NotImplementedError):
            self.baseCamera.updateOffset(1, 1)

        with pytest.raises(NotImplementedError):
            self.baseCamera.resetOffset()

        with pytest.raises(NotImplementedError):
            self.baseCamera.waitOnRoi()

        with pytest.raises(NotImplementedError):
            self.baseCamera.showFrameStatus()

        with pytest.raises(NotImplementedError):
            self.baseCamera.getConfiguration()

        with pytest.raises(NotImplementedError):
            self.baseCamera.setConfiguration({})

        assert self.baseCamera.checkFullFrame(1, 1, 1, 1) is True
        assert self.baseCamera.checkRoiFrame(1) is True

        with pytest.raises(NotImplementedError):
            self.baseCamera.getCameraInformation()
