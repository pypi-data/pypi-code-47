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

from spot_motion_monitor.camera.gaussian_camera import GaussianCamera
from spot_motion_monitor.models.roi_frame_model import RoiFrameModel
from spot_motion_monitor.utils import FrameRejected, TimeHandler

class TestRoiFrameModel():

    def setup_class(cls):
        cls.model = RoiFrameModel()
        cls.model.timeHandler = TimeHandler()

    def checkFrame(self, flux):
        return flux > 3000

    def test_parametersAfterConstruction(self):
        assert self.model.thresholdFactor == 0.3
        assert self.model.timeHandler is not None

    def test_frameCalculations(self):
        # This test requires the generation of a CCD frame which will be
        # provided by the GaussianCamera
        camera = GaussianCamera()
        camera.seed = 1000
        camera.startup()
        frame = camera.getRoiFrame()
        info = self.model.calculateCentroid(frame)
        assert info.centerX == 24.492516009567165
        assert info.centerY == 24.46080549340329
        assert info.flux == 2592.2000000000003
        assert info.maxAdc == 125.30000000000001
        assert info.fwhm == 5.471227956825783
        assert info.objectSize == 54
        #assert info.stdNoObjects == 5.1785375980622534
        # See speed improvement in RoiFrameModel::calculateCentroid
        assert info.stdNoObjects == -999

    def test_failedFrameCheck(self):
        # This test requires the generation of a CCD frame which will be
        # provided by the GaussianCamera
        self.model.frameCheck = self.checkFrame
        camera = GaussianCamera()
        camera.seed = 1000
        camera.startup()
        frame = camera.getRoiFrame()
        with pytest.raises(FrameRejected):
            self.model.calculateCentroid(frame)
        self.model.frameCheck = None
