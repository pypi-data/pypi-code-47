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

from spot_motion_monitor.config import GaussianCameraConfig
from spot_motion_monitor.camera.gaussian_camera import GaussianCamera

class TestGaussianCamera():

    def setup_class(self):
        self.camera = GaussianCamera()

    def test_parametersAfterConstruction(self):
        assert self.camera.name == 'Gaussian'
        assert self.camera.seed is None
        assert self.camera.height == 480
        assert self.camera.width == 640
        assert self.camera.spotSize == 20
        assert self.camera.fpsFullFrame == 24
        assert self.camera.fpsRoiFrame == 40
        assert self.camera.roiSize == 50
        assert self.camera.postageStamp is None
        assert self.camera.xPoint is None
        assert self.camera.yPoint is None
        assert self.camera.doSpotOscillation is True
        assert self.camera.xAmp == 10
        assert self.camera.xFreq == 1.0
        assert self.camera.yAmp == 5
        assert self.camera.yFreq == 2.0
        assert self.camera.config is not None

    def test_parametersAfterStartup(self):
        self.camera.startup()
        assert self.camera.postageStamp is not None
        assert self.camera.xPoint is not None
        assert self.camera.yPoint is not None

    def test_getFullFrame(self):
        self.camera.seed = 1000
        self.camera.startup()
        frame = self.camera.getFullFrame()
        assert frame.shape == (480, 640)
        max_point1, max_point2 = np.where(frame == np.max(frame))
        assert max_point1[0] == 225
        assert max_point2[0] == 288

    def test_getRoiFrame(self):
        self.camera.seed = 1000
        self.camera.startup()
        frame = self.camera.getRoiFrame()
        assert frame.shape == (50, 50)
        max_point1, max_point2 = np.where(frame == np.max(frame))
        assert max_point1[0] == 26
        assert max_point2[0] == 26

    def test_getOffset(self):
        self.camera.seed = 1000
        self.camera.startup()
        offset = self.camera.getOffset()
        assert offset == (264, 200)

    def test_getConfiguration(self):
        truthConfig = GaussianCameraConfig()
        truthConfig.roiSize = 50
        truthConfig.fpsRoiFrame = 40
        truthConfig.fpsFullFrame = 24
        truthConfig.doSpotOscillation = True
        truthConfig.xAmplitude = 10
        truthConfig.xFrequency = 1.0
        truthConfig.yAmplitude = 5
        truthConfig.yFrequency = 2.0
        currentConfig = self.camera.getConfiguration()
        assert currentConfig == truthConfig

    def test_setConfiguration(self):
        camera = GaussianCamera()

        truthConfig = GaussianCameraConfig()
        truthConfig.roiSize = 75
        truthConfig.fpsRoiFrame = 20
        truthConfig.fpsFullFrame = 10
        truthConfig.doSpotOscillation = True
        truthConfig.xAmplitude = 1
        truthConfig.xFrequency = 40.0
        truthConfig.yAmplitude = 8
        truthConfig.yFrequency = 75.0

        camera.setConfiguration(truthConfig)
        assert camera.roiSize == truthConfig.roiSize
        assert camera.fpsRoiFrame == truthConfig.fpsRoiFrame
        assert camera.fpsFullFrame == truthConfig.fpsFullFrame
        assert camera.doSpotOscillation == truthConfig.doSpotOscillation
        assert camera.xAmp == truthConfig.xAmplitude
        assert camera.xFreq == truthConfig.xFrequency
        assert camera.yAmp == truthConfig.yAmplitude
        assert camera.yFreq == truthConfig.yFrequency

    def test_cameraInformation(self):
        camera = GaussianCamera()
        cameraInfo = camera.getCameraInformation()

        assert cameraInfo['Model'] == 'Gaussian'
        assert cameraInfo['CCD Width (pixels)'] == 640
        assert cameraInfo['CCD Height (pixels)'] == 480
