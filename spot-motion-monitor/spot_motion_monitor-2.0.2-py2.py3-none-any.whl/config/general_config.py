# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import os

from . import BaseConfig

__all__ = ['GeneralConfig']

class GeneralConfig(BaseConfig):
    """Class that handles the configuration of general information.

    Attributes
    ----------
    autorun : bool
        Run application in ROI mode at launch.
    configFile : str
        The configuration file used, if applicable.
    configVersion : str
        The current version of the configuration, if applicable.
    fullTelemetrySavePath : str
        The full path for where to save the telemetry files.
    removeTelemetryDir : bool
        Whether or not to remove the telemetry directory when ROI acquisition
        ends.
    removeTelemetryFiles : bool
        Whether or not to remove the telemetry files when ROI acquisition ends.
    saveBufferData : bool
        Whether or not to write buffer data to file.
    site : str
        The location the program is used.
    timezone : str
        The timezone to use for all dates and times.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.configVersion = None
        self.configFile = None
        self.site = None
        self.autorun = False
        self.timezone = "UTC"
        self.saveBufferData = False
        self.fullTelemetrySavePath = None
        self.removeTelemetryDir = True
        self.removeTelemetryFiles = True

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.check("configVersion", config["general"], "configVersion")
        self.check("site", config["general"], "site")
        self.check("autorun", config["general"], "autorun")
        self.check("timezone", config["general"], "timezone")
        self.check("saveBufferData", config["general"], "saveBufferData")
        try:
            td = config["general"]["telemetry"]["directory"]
            if td is not None:
                self.fullTelemetrySavePath = os.path.abspath(os.path.expanduser(td))
            else:
                self.fullTelemetrySavePath = td
        except KeyError:
            pass
        self.check("removeTelemetryDir", config["general"]["telemetry"]["cleanup"], "directory")
        self.check("removeTelemetryFiles", config["general"]["telemetry"]["cleanup"], "files")

    def toDict(self, writeEmpty=False):
        """Translate class attributes to configuration dict.

        Parameters
        ----------
        writeEmpty : bool
            Flag to write parameters with None as values.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"general": {}}
        if writeEmpty or self.configVersion is not None:
            config["general"]["configVersion"] = self.configVersion
        if writeEmpty or self.site is not None:
            config["general"]["site"] = self.site
        config["general"]["autorun"] = self.autorun
        config["general"]["timezone"] = self.timezone
        config["general"]["saveBufferData"] = self.saveBufferData
        config["general"]["telemetry"] = {}
        if writeEmpty or self.fullTelemetrySavePath is not None:
            config["general"]["telemetry"]["directory"] = self.fullTelemetrySavePath
        config["general"]["telemetry"]["cleanup"] = {}
        config["general"]["telemetry"]["cleanup"]["directory"] = self.removeTelemetryDir
        config["general"]["telemetry"]["cleanup"]["files"] = self.removeTelemetryFiles
        return config
