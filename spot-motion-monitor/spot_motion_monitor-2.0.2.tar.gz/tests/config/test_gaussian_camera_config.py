# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import GaussianCameraConfig

class TestGaussianCameraConfig:

    def setup_class(cls):
        cls.config = GaussianCameraConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.roiSize == 50
        assert self.config.doSpotOscillation is False
        assert self.config.xAmplitude == 10
        assert self.config.xFrequency == 5.0
        assert self.config.yAmplitude == 5
        assert self.config.yFrequency == 10.0

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert config_dict["roi"]["size"] == 50
        assert config_dict["spotOscillation"]["do"] is False
        assert config_dict["spotOscillation"]["x"]["amplitude"] == 10
        assert config_dict["spotOscillation"]["x"]["frequency"] == 5.0
        assert config_dict["spotOscillation"]["y"]["amplitude"] == 5
        assert config_dict["spotOscillation"]["y"]["frequency"] == 10.0

        # Check to make sure function accepts argument.
        config_dict = self.config.toDict(True)
        assert config_dict["roi"]["size"] == 50

    def test_fromDict(self):
        config_dict = {"roi": {}, "full": {}, "spotOscillation": {"x": {}, "y": {}}}
        config_dict["roi"]["size"] = 75
        config_dict["roi"]["fps"] = 50
        config_dict["full"]["fps"] = 20
        config_dict["spotOscillation"]["do"] = True
        config_dict["spotOscillation"]["x"]["amplitude"] = 20
        config_dict["spotOscillation"]["x"]["frequency"] = 3.0
        config_dict["spotOscillation"]["y"]["amplitude"] = 12
        config_dict["spotOscillation"]["y"]["frequency"] = 30.0
        self.config.fromDict(config_dict)
        assert self.config.roiSize == config_dict["roi"]["size"]
        assert self.config.doSpotOscillation is config_dict["spotOscillation"]["do"]
        assert self.config.xAmplitude == config_dict["spotOscillation"]["x"]["amplitude"]
        assert self.config.xFrequency == config_dict["spotOscillation"]["x"]["frequency"]
        assert self.config.yAmplitude == config_dict["spotOscillation"]["y"]["amplitude"]
        assert self.config.yFrequency == config_dict["spotOscillation"]["y"]["frequency"]
