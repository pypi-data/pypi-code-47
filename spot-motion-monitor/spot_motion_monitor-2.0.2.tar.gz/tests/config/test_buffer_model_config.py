# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import BufferModelConfig

class TestBufferModelConfig:

    def setup_class(cls):
        cls.config = BufferModelConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.bufferSize == 1024
        assert self.config.pixelScale == 1.0

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert config_dict["buffer"]["size"] == 1024
        assert config_dict["buffer"]["pixelScale"] == 1.0

    def test_fromDict(self):
        config_dict = {"buffer": {}}
        config_dict["buffer"]["size"] = 512
        config_dict["buffer"]["pixelScale"] = 1.3
        self.config.fromDict(config_dict)
        assert self.config.bufferSize == config_dict["buffer"]["size"]
        assert self.config.pixelScale == config_dict["buffer"]["pixelScale"]
