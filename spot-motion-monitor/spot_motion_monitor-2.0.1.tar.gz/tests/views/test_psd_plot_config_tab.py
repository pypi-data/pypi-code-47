# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import PsdPlotConfig
import spot_motion_monitor.utils as utils
from spot_motion_monitor.views import PsdPlotConfigTab

class TestPsdPlotConfigTab:

    def setup_class(self):
        self.fast_timeout = 250  # ms

    def stateIsFalse(self, state):
        return not state

    def stateIsTrue(self, state):
        return state

    def checkValidations(self, qtbot, checkSignal, checkState, checkFunc, valuesToCheck):
        if checkState:
            statusCheck = self.stateIsTrue
        else:
            statusCheck = self.stateIsFalse

        for valueToCheck in valuesToCheck:
            with qtbot.waitSignal(checkSignal, timeout=self.fast_timeout, check_params_cb=statusCheck):
                checkFunc(str(valueToCheck))

    def test_parametersAfterConstruction(self, qtbot):
        configTab = PsdPlotConfigTab()
        qtbot.addWidget(configTab)
        assert configTab.name == 'PSD'
        assert configTab.waterfallColorMapComboBox.count() == 5

    def test_setParametersFromConfiguration(self, qtbot):
        configTab = PsdPlotConfigTab()
        qtbot.addWidget(configTab)

        truthConfig = PsdPlotConfig()
        truthConfig.autoscaleX1d = True
        truthConfig.x1dMaximum = None
        truthConfig.autoscaleY1d = False
        truthConfig.y1dMaximum = 1320
        truthConfig.numWaterfallBins = 15
        truthConfig.waterfallColorMap = "plasma"

        configTab.setConfiguration(truthConfig)
        assert int(configTab.waterfallNumBinsLineEdit.text()) == truthConfig.numWaterfallBins
        assert configTab.waterfallColorMapComboBox.currentText() == truthConfig.waterfallColorMap
        assert utils.checkStateToBool(configTab.autoscaleX1dCheckBox.checkState()) is True
        assert configTab.x1dMaximumLineEdit.isEnabled() is False
        assert utils.checkStateToBool(configTab.autoscaleY1dCheckBox.checkState()) is False
        assert configTab.y1dMaximumLineEdit.isEnabled() is True
        assert int(configTab.y1dMaximumLineEdit.text()) == truthConfig.y1dMaximum

    def test_getParametersFromConfiguration(self, qtbot):
        configTab = PsdPlotConfigTab()
        qtbot.addWidget(configTab)

        truthConfig = PsdPlotConfig()
        truthConfig.autoscaleX1d = True
        truthConfig.autoscaleY1d = False
        truthConfig.y1dMaximum = 1320.0
        truthConfig.numWaterfallBins = 35
        truthConfig.waterfallColorMap = "magma"

        configTab.waterfallNumBinsLineEdit.setText(str(truthConfig.numWaterfallBins))
        configTab.waterfallColorMapComboBox.setCurrentText(truthConfig.waterfallColorMap)
        configTab.autoscaleX1dCheckBox.setChecked(utils.boolToCheckState(truthConfig.autoscaleX1d))
        configTab.autoscaleY1dCheckBox.setChecked(utils.boolToCheckState(truthConfig.autoscaleY1d))
        configTab.y1dMaximumLineEdit.setText(str(truthConfig.y1dMaximum))
        config = configTab.getConfiguration()
        assert config == truthConfig

    def test_validLineEditParameters(self, qtbot):
        configTab = PsdPlotConfigTab()
        qtbot.addWidget(configTab)
        configTab.show()

        self.checkValidations(qtbot, configTab.hasValidInput, True,
                              configTab.waterfallNumBinsLineEdit.setText,
                              [1, 1000, 150])

    def test_invalidLineEditParameters(self, qtbot):
        configTab = PsdPlotConfigTab()
        qtbot.addWidget(configTab)
        configTab.show()

        self.checkValidations(qtbot, configTab.hasValidInput, False,
                              configTab.waterfallNumBinsLineEdit.setText,
                              [0, 1001, 40.1])
