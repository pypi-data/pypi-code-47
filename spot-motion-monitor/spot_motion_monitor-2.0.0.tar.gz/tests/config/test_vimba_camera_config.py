# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import VimbaCameraConfig

class TestVimbaCameraConfig:

    def setup_class(cls):
        cls.config = VimbaCameraConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.modelName is None
        assert self.config.roiSize == 50
        assert self.config.roiFluxMinimum == 2000
        assert self.config.roiExposureTime == 8000
        assert self.config.fullExposureTime == 8000
        assert self.config.cameraIndex == 0

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert ("modelName" in config_dict) is False
        assert config_dict["roi"]["size"] == 50
        assert config_dict["roi"]["fluxMin"] == 2000
        assert config_dict["roi"]["exposureTime"] == 8000
        assert config_dict["full"]["exposureTime"] == 8000

        config_dict = self.config.toDict(True)
        assert config_dict["modelName"] is None

    def test_fromDict(self):
        config_dict = {"roi": {}, "full": {}}
        config_dict["modelName"] = "GT-3300"
        config_dict["roi"]["size"] = 75
        config_dict["roi"]["fps"] = 50
        config_dict["roi"]["fluxMin"] = 1000
        config_dict["roi"]["exposureTime"] = 5000
        config_dict["full"]["fps"] = 20
        config_dict["full"]["exposureTime"] = 5000
        config_dict["cameraIndex"] = 1
        self.config.fromDict(config_dict)
        assert self.config.modelName == config_dict["modelName"]
        assert self.config.roiSize == config_dict["roi"]["size"]
        assert self.config.roiFluxMinimum == config_dict["roi"]["fluxMin"]
        assert self.config.roiExposureTime == config_dict["roi"]["exposureTime"]
        assert self.config.fullExposureTime == config_dict["full"]["exposureTime"]
        assert self.config.cameraIndex == config_dict["cameraIndex"]
