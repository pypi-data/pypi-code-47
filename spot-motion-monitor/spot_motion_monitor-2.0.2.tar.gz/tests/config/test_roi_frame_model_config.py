# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import RoiFrameModelConfig

class TestRoiFrameModelConfig:

    def setup_class(cls):
        cls.config = RoiFrameModelConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.thresholdFactor == 0.3

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert config_dict["roiFrame"]["thresholdFactor"] == 0.3

    def test_fromDict(self):
        config_dict = {"roiFrame": {}}
        config_dict["roiFrame"]["thresholdFactor"] = 0.5
        self.config.fromDict(config_dict)
        assert self.config.thresholdFactor == config_dict["roiFrame"]["thresholdFactor"]
