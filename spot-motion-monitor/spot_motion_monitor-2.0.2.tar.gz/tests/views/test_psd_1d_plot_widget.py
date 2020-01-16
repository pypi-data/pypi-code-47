# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import numpy as np

from spot_motion_monitor.config import PsdPlotConfig
from spot_motion_monitor.views import Psd1dPlotWidget

class TestPsd1dPlotWidget:

    def test_parametersAfterConstruction(self, qtbot):
        p1dpw = Psd1dPlotWidget()
        qtbot.addWidget(p1dpw)
        assert p1dpw.plot is not None
        assert p1dpw.curve is not None
        assert p1dpw.autoscale is True
        assert p1dpw.yRange is None
        assert p1dpw.axis is None

    def test_updatePlot(self, qtbot, mocker):
        p1dpw = Psd1dPlotWidget()
        qtbot.addWidget(p1dpw)
        p1dpw.setup('X')
        mockSetData = mocker.patch.object(p1dpw.curve, 'setData')

        data = np.array([10.0, 3.1, 5.1])
        freqs = np.array([1.3, 2.5, 3.9])
        p1dpw.updatePlot(data, freqs)
        assert mockSetData.call_count == 1

    def test_getConfiguration(self, qtbot):
        p1dpw = Psd1dPlotWidget()
        p1dpw.show()
        qtbot.addWidget(p1dpw)
        truthAutoscale = True
        truthYRange = [None, None]
        autoscale, yRange = p1dpw.getConfiguration()
        assert autoscale is truthAutoscale
        assert yRange == truthYRange

    def test_setConfiguration(self, qtbot):
        p1dpw = Psd1dPlotWidget()
        p1dpw.show()
        qtbot.addWidget(p1dpw)
        p1dpw.setup('X')
        assert p1dpw.axis == 'X'
        truthConfig = PsdPlotConfig()
        truthConfig.x1dMinimum = 10
        truthConfig.x1dMaximum = 100
        p1dpw.setConfiguration(truthConfig)
        assert p1dpw.autoscale is False
        assert p1dpw.yRange == [truthConfig.x1dMinimum, truthConfig.x1dMaximum]
        truthConfig.autoscaleX1d = True
        p1dpw.setConfiguration(truthConfig)
        assert p1dpw.autoscale is True
        assert p1dpw.yRange is None
        truthConfig.autoscaleX1d = False
        truthConfig.x1dMinimum = None
        truthConfig.x1dMaximum = None
        p1dpw.setConfiguration(truthConfig)
        assert p1dpw.autoscale is False
        assert p1dpw.yRange == [0, 1000]

    def test_clearPlot(self, qtbot, mocker):
        p1dpw = Psd1dPlotWidget()
        p1dpw.show()
        qtbot.addWidget(p1dpw)
        p1dpw.setup('X')
        mockSetData = mocker.patch.object(p1dpw.curve, 'setData')
        data = np.array([10.0, 3.1, 5.1])
        freqs = np.array([1.3, 2.5, 3.9])
        p1dpw.updatePlot(data, freqs)
        p1dpw.clearPlot()
        assert mockSetData.call_count == 2
