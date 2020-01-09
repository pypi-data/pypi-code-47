# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import numpy as np
import pytest

from spot_motion_monitor.camera.gaussian_camera import GaussianCamera
from spot_motion_monitor.models import FullFrameModel
from spot_motion_monitor.utils import FrameRejected, TimeHandler

class TestFullFrameModel():

    def setup_class(cls):
        cls.model = FullFrameModel()
        cls.model.timeHandler = TimeHandler()

    def checkFrame(self, flux, maxAdc, comX, comY):
        return flux > 4000 and maxAdc > 130 and comX > 0 and comY > 0

    def test_parametersAfterConstruction(self):
        assert self.model.sigmaScale == 5.0
        assert self.model.minimumNumPixels == 10
        assert self.model.timeHandler is not None

    def test_frameCalculations(self):
        # This test requires the generation of a CCD frame which will be
        # provided by the GaussianCamera
        camera = GaussianCamera()
        camera.seed = 1000
        camera.startup()
        frame = camera.getFullFrame()
        info = self.model.calculateCentroid(frame)
        assert info.centerX == 288.47687644439395
        assert info.centerY == 224.45394404821826
        assert info.flux == 3235.9182163661176
        assert info.maxAdc == 135.83703259361937
        assert info.fwhm == 5.749039360993981
        assert info.stdNoObjects is None

    def test_badFrameCalculation(self):
        frame = np.ones((480, 640))
        with pytest.raises(FrameRejected):
            self.model.calculateCentroid(frame)

    def test_failedFrameCheck(self):
        # This test requires the generation of a CCD frame which will be
        # provided by the GaussianCamera
        self.model.frameCheck = self.checkFrame
        camera = GaussianCamera()
        camera.seed = 1000
        camera.startup()
        frame = camera.getFullFrame()
        with pytest.raises(FrameRejected):
            self.model.calculateCentroid(frame)
        self.model.frameCheck = None
