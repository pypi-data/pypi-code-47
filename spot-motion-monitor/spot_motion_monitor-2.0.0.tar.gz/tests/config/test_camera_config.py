# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import CameraConfig

class TestCameraConfig:

    def setup_class(cls):
        cls.config = CameraConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.roiSize == 50
        assert self.config.fpsRoiFrame == 40
        assert self.config.fpsFullFrame == 24

    def test_toDict(self):
        config_dict = self.config.toDict()

        assert config_dict["roi"]["size"] == 50
        assert config_dict["roi"]["fps"] == 40
        assert config_dict["full"]["fps"] == 24

    def test_fromDict(self):
        config_dict = {"roi": {}, "full": {}}
        config_dict["roi"]["size"] = 100
        config_dict["roi"]["fps"] = 120
        config_dict["full"]["fps"] = 30

        self.config.fromDict(config_dict)

        assert self.config.roiSize == config_dict["roi"]["size"]
        assert self.config.fpsRoiFrame == config_dict["roi"]["fps"]
        assert self.config.fpsFullFrame == config_dict["full"]["fps"]
