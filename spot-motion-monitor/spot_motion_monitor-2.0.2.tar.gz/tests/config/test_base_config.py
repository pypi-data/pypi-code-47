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

from spot_motion_monitor.config import BaseConfig

class TestBaseConfig:

    def setup_class(cls):
        cls.baseConfig = BaseConfig()

    def test_noApiAfterConstruction(self):

        with pytest.raises(NotImplementedError):
            self.baseConfig.toDict()

        with pytest.raises(NotImplementedError):
            self.baseConfig.fromDict({})

    def test_equality(self):
        config1 = BaseConfig()
        config1.x = 10
        config2 = BaseConfig()
        config2.x = 4
        config3 = BaseConfig()
        config3.x = 10
        config4 = BaseConfig()
        config4.x = None
        config5 = BaseConfig()
        config5.x = None

        assert config1 != config2
        assert config1 == config3
        assert config1 != config4
        assert config4 == config5

    def test_check(self):
        config1 = BaseConfig()
        config1.x = 10
        config1.y = 2.5
        idict = {"x": 14}
        config1.check("x", idict, "x")
        assert config1.x == idict["x"]
        config1.check("y", idict, "y")
        assert config1.y == 2.5
