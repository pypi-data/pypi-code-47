# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import GeneralConfig

class TestGeneralConfig:

    def setup_class(cls):
        cls.config = GeneralConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.configVersion is None
        assert self.config.configFile is None
        assert self.config.site is None
        assert self.config.autorun is False
        assert self.config.timezone == "UTC"
        assert self.config.saveBufferData is False
        assert self.config.fullTelemetrySavePath is None
        assert self.config.removeTelemetryDir is True
        assert self.config.removeTelemetryFiles is True

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert ("configVersion" in config_dict["general"]) is False
        assert ("site" in config_dict["general"]) is False
        assert config_dict["general"]["autorun"] is False
        assert config_dict["general"]["timezone"] == "UTC"
        assert config_dict["general"]["saveBufferData"] is False
        assert ("directory" in config_dict["general"]["telemetry"]) is False
        assert config_dict["general"]["telemetry"]["cleanup"]["directory"] is True
        assert config_dict["general"]["telemetry"]["cleanup"]["files"] is True

        writeEmpty = True
        config_dict = self.config.toDict(writeEmpty)
        assert config_dict["general"]["configVersion"] is None
        assert config_dict["general"]["site"] is None
        assert config_dict["general"]["telemetry"]["directory"] is None

    def test_fromDict(self):
        config_dict = {"general": {}}
        config_dict["general"]["configVersion"] = "1.3.3"
        config_dict["general"]["site"] = "Cerro Pachon"
        config_dict["general"]["autorun"] = True
        config_dict["general"]["timezone"] = "CLT"
        config_dict["general"]["saveBufferData"] = True
        config_dict["general"]["telemetry"] = {}
        config_dict["general"]["telemetry"]["directory"] = "/new/path/for/telemetry"
        config_dict["general"]["telemetry"]["cleanup"] = {}
        config_dict["general"]["telemetry"]["cleanup"]["directory"] = False
        config_dict["general"]["telemetry"]["cleanup"]["files"] = False
        self.config.fromDict(config_dict)
        assert self.config.configVersion == config_dict["general"]["configVersion"]
        assert self.config.site == config_dict["general"]["site"]
        assert self.config.autorun is config_dict["general"]["autorun"]
        assert self.config.timezone == config_dict["general"]["timezone"]
        assert self.config.saveBufferData is config_dict["general"]["saveBufferData"]
        assert self.config.fullTelemetrySavePath == config_dict["general"]["telemetry"]["directory"]
        assert self.config.removeTelemetryDir is config_dict["general"]["telemetry"]["cleanup"]["directory"]
        assert self.config.removeTelemetryFiles is config_dict["general"]["telemetry"]["cleanup"]["files"]
