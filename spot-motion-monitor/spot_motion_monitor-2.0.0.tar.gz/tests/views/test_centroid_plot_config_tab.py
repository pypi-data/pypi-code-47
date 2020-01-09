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
from spot_motion_monitor.views import CentroidPlotConfigTab

class TestCentroidPlotConfigTab:

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
        configTab = CentroidPlotConfigTab()
        qtbot.addWidget(configTab)
        assert configTab.name == 'Centroid'

    def test_setParametersFromConfiguration(self, qtbot):
        configTab = CentroidPlotConfigTab()
        qtbot.addWidget(configTab)

        truthConfig = CentroidPlotConfig()
        truthConfig.autoscaleX = AutoscaleState.OFF
        truthConfig.minimumX = 10
        truthConfig.maximumX = 1000
        truthConfig.pixelRangeAdditionX = None
        truthConfig.autoscaleY = AutoscaleState.ON
        truthConfig.minimumY = None
        truthConfig.maximumY = None
        truthConfig.pixelRangeAdditionY = None
        truthConfig.numHistogramBins = 50

        configTab.setConfiguration(truthConfig)
        xState = configTab.autoscaleXComboBox.currentText()
        assert xState == truthConfig.autoscaleX.name
        assert configTab.pixelAdditionXLineEdit.text() == ''
        assert configTab.pixelAdditionXLabel.isEnabled() is False
        assert configTab.pixelAdditionXLineEdit.isEnabled() is False
        assert configTab.minXLimitLabel.isEnabled() is True
        assert configTab.minXLimitLineEdit.isEnabled() is True
        assert configTab.maxXLimitLabel.isEnabled() is True
        assert configTab.maxXLimitLineEdit.isEnabled() is True
        assert int(configTab.minXLimitLineEdit.text()) == truthConfig.minimumX
        assert int(configTab.maxXLimitLineEdit.text()) == truthConfig.maximumX
        yState = configTab.autoscaleYComboBox.currentText()
        assert yState == truthConfig.autoscaleY.name
        assert configTab.pixelAdditionYLabel.isEnabled() is False
        assert configTab.pixelAdditionYLineEdit.isEnabled() is False
        assert configTab.minYLimitLabel.isEnabled() is False
        assert configTab.minYLimitLineEdit.isEnabled() is False
        assert configTab.maxYLimitLabel.isEnabled() is False
        assert configTab.maxYLimitLineEdit.isEnabled() is False
        assert configTab.pixelAdditionXLineEdit.text() == ''
        assert configTab.minYLimitLineEdit.text() == ''
        assert configTab.maxYLimitLineEdit.text() == ''
        assert int(configTab.numHistoBinsLineEdit.text()) == truthConfig.numHistogramBins

        truthConfig.autoscaleY = AutoscaleState.PARTIAL
        truthConfig.pixelRangeAdditionY = 10
        configTab.setConfiguration(truthConfig)
        yState = configTab.autoscaleYComboBox.currentText()
        assert yState == truthConfig.autoscaleY.name
        assert configTab.pixelAdditionYLineEdit.isEnabled() is True
        assert configTab.minYLimitLineEdit.isEnabled() is False
        assert configTab.maxYLimitLineEdit.isEnabled() is False
        assert int(configTab.pixelAdditionYLineEdit.text()) == truthConfig.pixelRangeAdditionY

    def test_getParametersFromConfiguration(self, qtbot):
        configTab = CentroidPlotConfigTab()
        qtbot.addWidget(configTab)
        configTab.show()

        truthConfig = CentroidPlotConfig()
        truthConfig.autoscaleX = AutoscaleState.OFF
        truthConfig.minimumX = 10
        truthConfig.maximumX = 1000
        truthConfig.autoscaleY = AutoscaleState.ON
        truthConfig.numHistogramBins = 30

        configTab.autoscaleXComboBox.setCurrentText(truthConfig.autoscaleX.name)
        configTab.minXLimitLineEdit.setText(str(truthConfig.minimumX))
        configTab.maxXLimitLineEdit.setText(str(truthConfig.maximumX))
        configTab.autoscaleYComboBox.setCurrentText(truthConfig.autoscaleY.name)
        configTab.numHistoBinsLineEdit.setText(str(truthConfig.numHistogramBins))
        config = configTab.getConfiguration()
        assert config == truthConfig

        truthConfig.autoscaleY = AutoscaleState.PARTIAL
        truthConfig.pixelRangeAdditionY = 10
        configTab.autoscaleYComboBox.setCurrentText(truthConfig.autoscaleY.name)
        configTab.pixelAdditionYLineEdit.setText(str(truthConfig.pixelRangeAdditionY))
        config = configTab.getConfiguration()
        assert config == truthConfig

    def test_validLineEditParameters(self, qtbot):
        configTab = CentroidPlotConfigTab()
        qtbot.addWidget(configTab)
        configTab.show()

        self.checkValidations(qtbot, configTab.hasValidInput, True, configTab.pixelAdditionXLineEdit.setText,
                              [1, 10000, 150])
        self.checkValidations(qtbot, configTab.hasValidInput, True, configTab.minXLimitLineEdit.setText,
                              [0, int(1e9), int(1e4)])
        self.checkValidations(qtbot, configTab.hasValidInput, True, configTab.maxXLimitLineEdit.setText,
                              [0, int(1e9), int(1e4)])
        self.checkValidations(qtbot, configTab.hasValidInput, True, configTab.pixelAdditionYLineEdit.setText,
                              [1, 10000, 150])
        self.checkValidations(qtbot, configTab.hasValidInput, True, configTab.minYLimitLineEdit.setText,
                              [0, int(1e9), int(1e4)])
        self.checkValidations(qtbot, configTab.hasValidInput, True, configTab.maxYLimitLineEdit.setText,
                              [0, int(1e9), int(1e4)])
        self.checkValidations(qtbot, configTab.hasValidInput, True, configTab.numHistoBinsLineEdit.setText,
                              [1, int(1e9), int(1e4)])

    def test_invalidLineEditParameters(self, qtbot):
        configTab = CentroidPlotConfigTab()
        qtbot.addWidget(configTab)
        configTab.show()

        self.checkValidations(qtbot, configTab.hasValidInput, False, configTab.pixelAdditionXLineEdit.setText,
                              [0, 10001, 40.1])
        self.checkValidations(qtbot, configTab.hasValidInput, False, configTab.minXLimitLineEdit.setText,
                              [-1, int(1e10), 1.1e4])
        self.checkValidations(qtbot, configTab.hasValidInput, False, configTab.maxXLimitLineEdit.setText,
                              [-1, int(1e10), 1.1e4])
        self.checkValidations(qtbot, configTab.hasValidInput, False, configTab.pixelAdditionYLineEdit.setText,
                              [0, 10001, 40.1])
        self.checkValidations(qtbot, configTab.hasValidInput, False, configTab.minYLimitLineEdit.setText,
                              [-1, int(1e10), 1.1e4])
        self.checkValidations(qtbot, configTab.hasValidInput, False, configTab.maxYLimitLineEdit.setText,
                              [-1, int(1e10), 1.1e4])
        self.checkValidations(qtbot, configTab.hasValidInput, False, configTab.numHistoBinsLineEdit.setText,
                              [0, int(1e10), 1.1e4])
