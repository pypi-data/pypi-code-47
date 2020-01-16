# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import FullFrameModelConfig

class TestFullFrameModelConfig:

    def setup_class(cls):
        cls.config = FullFrameModelConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.sigmaScale == 5.0
        assert self.config.minimumNumPixels == 10

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert config_dict["fullFrame"]["sigmaScale"] == 5.0
        assert config_dict["fullFrame"]["minimumNumPixels"] == 10

    def test_fromDict(self):
        config_dict = {"fullFrame": {}}
        config_dict["fullFrame"]["sigmaScale"] = 2.5
        config_dict["fullFrame"]["minimumNumPixels"] = 20
        self.config.fromDict(config_dict)
        assert self.config.sigmaScale == config_dict["fullFrame"]["sigmaScale"]
        assert self.config.minimumNumPixels == config_dict["fullFrame"]["minimumNumPixels"]
