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
from spot_motion_monitor.views import DataConfigTab

class TestDataConfigTab:

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
        gcConfigTab = DataConfigTab()
        qtbot.addWidget(gcConfigTab)

        assert gcConfigTab.name == 'Data'

    def test_setParametersFromConfiguration(self, qtbot):
        gcConfigTab = DataConfigTab()
        qtbot.addWidget(gcConfigTab)

        truthConfig = DataConfig()
        truthConfig.buffer.pixelScale = 0.34
        truthConfig.fullFrame.sigmaScale = 5.25
        truthConfig.fullFrame.minimumNumPixels = 55
        truthConfig.roiFrame.thresholdFactor = 7.2455

        gcConfigTab.setConfiguration(truthConfig)
        assert float(gcConfigTab.pixelScaleLineEdit.text()) == truthConfig.buffer.pixelScale
        assert float(gcConfigTab.sigmaScaleLineEdit.text()) == truthConfig.fullFrame.sigmaScale
        assert int(gcConfigTab.minimumNumPixelsLineEdit.text()) == truthConfig.fullFrame.minimumNumPixels
        assert float(gcConfigTab.thresholdFactorLineEdit.text()) == truthConfig.roiFrame.thresholdFactor

    def test_getParametersFromConfiguration(self, qtbot):
        gcConfigTab = DataConfigTab()
        qtbot.addWidget(gcConfigTab)
        gcConfigTab.show()

        truthConfig = DataConfig()
        truthConfig.buffer.pixelScale = 0.75
        truthConfig.fullFrame.sigmaScale = 1.533
        truthConfig.fullFrame.minimumNumPixels = 30
        truthConfig.roiFrame.thresholdFactor = 10.42

        gcConfigTab.pixelScaleLineEdit.setText(str(truthConfig.buffer.pixelScale))
        gcConfigTab.sigmaScaleLineEdit.setText(str(truthConfig.fullFrame.sigmaScale))
        gcConfigTab.minimumNumPixelsLineEdit.setText(str(truthConfig.fullFrame.minimumNumPixels))
        gcConfigTab.thresholdFactorLineEdit.setText(str(truthConfig.roiFrame.thresholdFactor))

        config = gcConfigTab.getConfiguration()
        try:
            assert config == truthConfig
        except AssertionError:
            print("Getter: ", config)
            print("Truth: ", truthConfig)
            raise

    def test_validLineEditParameters(self, qtbot):
        gcConfigTab = DataConfigTab()
        qtbot.addWidget(gcConfigTab)
        gcConfigTab.show()

        self.checkValidations(qtbot, gcConfigTab.hasValidInput, True, gcConfigTab.pixelScaleLineEdit.setText,
                              [0.0, 1e200, 15000.532])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, True, gcConfigTab.sigmaScaleLineEdit.setText,
                              [-143.502, 1.43, 10.0])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, True,
                              gcConfigTab.minimumNumPixelsLineEdit.setText,
                              [1, int(1e3), int(1e9)])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, True,
                              gcConfigTab.thresholdFactorLineEdit.setText,
                              [-1.0e200, 0.0, 1e200, 34.21532])

    def test_invalidLineEditParameters(self, qtbot):
        gcConfigTab = DataConfigTab()
        qtbot.addWidget(gcConfigTab)
        gcConfigTab.show()

        self.checkValidations(qtbot, gcConfigTab.hasValidInput, False, gcConfigTab.pixelScaleLineEdit.setText,
                              [-1.0, 1e201, 0.05286930])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, False, gcConfigTab.sigmaScaleLineEdit.setText,
                              [-1e201, 1e201, 3.671867393])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, False,
                              gcConfigTab.minimumNumPixelsLineEdit.setText,
                              [(-10, 0, int(1e10))])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, False,
                              gcConfigTab.thresholdFactorLineEdit.setText,
                              [-1.0e201, 1.0e201, 13.248689603])
