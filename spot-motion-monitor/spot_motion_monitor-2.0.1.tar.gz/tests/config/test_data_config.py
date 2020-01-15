# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import DataConfig

class TestDataConfig:

    def setup_class(cls):
        cls.config = DataConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.buffer is not None
        assert self.config.fullFrame is not None
        assert self.config.roiFrame is not None

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert len(config_dict) == 3
        assert list(config_dict.keys()) == ["buffer", "fullFrame", "roiFrame"]

    def test_fromDict(self):
        config_dict = {"buffer": {}, "fullFrame": {}, "roiFrame": {}}
        config_dict["buffer"]["pixelScale"] = 0.92
        config_dict["fullFrame"]["minimumNumPixels"] = 33
        config_dict["roiFrame"]["thresholdFactor"] = 2.45
        self.config.fromDict(config_dict)
        assert self.config.buffer.pixelScale == config_dict["buffer"]["pixelScale"]
        assert self.config.fullFrame.minimumNumPixels == config_dict["fullFrame"]["minimumNumPixels"]
        assert self.config.roiFrame.thresholdFactor == config_dict["roiFrame"]["thresholdFactor"]
