# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import CentroidPlotConfig
from spot_motion_monitor.utils import AutoscaleState

class TestCentroidPlotConfig:

    def setup_class(cls):
        cls.config = CentroidPlotConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.autoscaleX == AutoscaleState.OFF
        assert self.config.minimumX == 0
        assert self.config.maximumX == 100
        assert self.config.pixelRangeAdditionX == 25
        assert self.config.autoscaleY == AutoscaleState.OFF
        assert self.config.minimumY == 0
        assert self.config.maximumY == 100
        assert self.config.pixelRangeAdditionY == 25
        assert self.config.numHistogramBins == 40

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert config_dict["xCentroid"]["autoscaleY"] == AutoscaleState.OFF.name
        assert config_dict["xCentroid"]["minimumY"] == 0
        assert config_dict["xCentroid"]["maximumY"] == 100
        assert config_dict["xCentroid"]["pixelRangeAddition"] == 25
        assert config_dict["yCentroid"]["autoscaleY"] == AutoscaleState.OFF.name
        assert config_dict["yCentroid"]["minimumY"] == 0
        assert config_dict["yCentroid"]["maximumY"] == 100
        assert config_dict["yCentroid"]["pixelRangeAddition"] == 25
        assert config_dict["scatterPlot"]["histograms"]["numBins"] == 40

        self.config.minimumX = None
        self.config.maximumX = None
        self.config.pixelRangeAdditionX = None
        self.config.minimumY = None
        self.config.maximumY = None
        self.config.pixelRangeAdditionY = None

        config_dict = self.config.toDict()
        assert "minimumY" not in config_dict["xCentroid"]
        assert "maximumY" not in config_dict["xCentroid"]
        assert "pixelRangeAddition" not in config_dict["xCentroid"]
        assert "minimumY" not in config_dict["yCentroid"]
        assert "maximumY" not in config_dict["yCentroid"]
        assert "pixelRangeAddition" not in config_dict["yCentroid"]

        config_dict = self.config.toDict(True)
        assert config_dict["xCentroid"]["minimumY"] is None
        assert config_dict["xCentroid"]["maximumY"] is None
        assert config_dict["xCentroid"]["pixelRangeAddition"] is None
        assert config_dict["yCentroid"]["minimumY"] is None
        assert config_dict["yCentroid"]["maximumY"] is None
        assert config_dict["yCentroid"]["pixelRangeAddition"] is None

    def test_fromDict(self):
        config_dict = {"xCentroid": {}, "yCentroid": {}, "scatterPlot": {}}
        config_dict["xCentroid"]["autoscaleY"] = AutoscaleState.ON.name
        config_dict["xCentroid"]["minimumY"] = 50
        config_dict["xCentroid"]["maximumY"] = 300
        config_dict["xCentroid"]["pixelRangeAddition"] = 50
        config_dict["yCentroid"]["autoscaleY"] = AutoscaleState.ON.name
        config_dict["yCentroid"]["minimumY"] = 20
        config_dict["yCentroid"]["maximumY"] = 400
        config_dict["yCentroid"]["pixelRangeAddition"] = 60
        config_dict["scatterPlot"]["histograms"] = {}
        config_dict["scatterPlot"]["histograms"]["numBins"] = 100
        self.config.fromDict(config_dict)
        assert self.config.autoscaleX == AutoscaleState.ON
        assert self.config.minimumX == config_dict["xCentroid"]["minimumY"]
        assert self.config.maximumX == config_dict["xCentroid"]["maximumY"]
        assert self.config.pixelRangeAdditionX == config_dict["xCentroid"]["pixelRangeAddition"]
        assert self.config.autoscaleY == AutoscaleState.ON
        assert self.config.minimumY == config_dict["yCentroid"]["minimumY"]
        assert self.config.maximumY == config_dict["yCentroid"]["maximumY"]
        assert self.config.pixelRangeAdditionY == config_dict["yCentroid"]["pixelRangeAddition"]
        assert self.config.numHistogramBins == config_dict["scatterPlot"]["histograms"]["numBins"]
