# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from spot_motion_monitor.config import VimbaCameraConfig
from spot_motion_monitor.views import VimbaCameraConfigTab

class TestVimbaCameraConfigTab:

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
        vcConfigTab = VimbaCameraConfigTab()
        qtbot.addWidget(vcConfigTab)

        assert vcConfigTab.name == 'Vimba'
        assert vcConfigTab.config is not None

    def test_setParametersFromConfiguration(self, qtbot):
        vcConfigTab = VimbaCameraConfigTab()
        qtbot.addWidget(vcConfigTab)

        truthConfig = VimbaCameraConfig()
        truthConfig.roiSize = 20
        truthConfig.roiFluxMinimum = 1000
        truthConfig.roiExposureTime = 5000
        truthConfig.fullExposureTime = 8000
        vcConfigTab.setConfiguration(truthConfig)

        assert int(vcConfigTab.roiSizeLineEdit.text()) == truthConfig.roiSize
        assert int(vcConfigTab.roiFluxMinLineEdit.text()) == truthConfig.roiFluxMinimum
        assert int(vcConfigTab.roiExposureTimeLineEdit.text()) == truthConfig.roiExposureTime
        assert int(vcConfigTab.fullFrameExposureTimeLineEdit.text()) == truthConfig.fullExposureTime

    def test_getParametersFromConfiguration(self, qtbot):
        vcConfigTab = VimbaCameraConfigTab()
        qtbot.addWidget(vcConfigTab)
        vcConfigTab.show()

        truthConfig = VimbaCameraConfig()
        truthConfig.roiSize = 75
        truthConfig.roiFluxMinimum = 1000
        truthConfig.roiExposureTime = 3000
        truthConfig.fullExposureTime = 5000

        vcConfigTab.roiSizeLineEdit.setText(str(truthConfig.roiSize))
        vcConfigTab.roiFluxMinLineEdit.setText(str(truthConfig.roiFluxMinimum))
        vcConfigTab.roiExposureTimeLineEdit.setText(str(truthConfig.roiExposureTime))
        vcConfigTab.fullFrameExposureTimeLineEdit.setText(str(truthConfig.fullExposureTime))
        config = vcConfigTab.getConfiguration()
        assert config == truthConfig

    def test_validLineEditParameters(self, qtbot):
        vcConfigTab = VimbaCameraConfigTab()
        qtbot.addWidget(vcConfigTab)
        vcConfigTab.show()

        self.checkValidations(qtbot, vcConfigTab.hasValidInput, True, vcConfigTab.roiSizeLineEdit.setText,
                              [20, 1000, 853])
        self.checkValidations(qtbot, vcConfigTab.hasValidInput, True, vcConfigTab.roiFluxMinLineEdit.setText,
                              [100, 10000, 1000])
        self.checkValidations(qtbot, vcConfigTab.hasValidInput, True,
                              vcConfigTab.roiExposureTimeLineEdit.setText,
                              [500, 50000, 25000])
        self.checkValidations(qtbot, vcConfigTab.hasValidInput, True,
                              vcConfigTab.fullFrameExposureTimeLineEdit.setText,
                              [500, 50000, 25000])

    def test_invalidLineEditParameters(self, qtbot):
        vcConfigTab = VimbaCameraConfigTab()
        qtbot.addWidget(vcConfigTab)
        vcConfigTab.show()

        self.checkValidations(qtbot, vcConfigTab.hasValidInput, False, vcConfigTab.roiSizeLineEdit.setText,
                              [10, 40.1, 1003])
        self.checkValidations(qtbot, vcConfigTab.hasValidInput, False, vcConfigTab.roiFluxMinLineEdit.setText,
                              [50, 15000, 200.2])
        self.checkValidations(qtbot, vcConfigTab.hasValidInput, False,
                              vcConfigTab.roiExposureTimeLineEdit.setText,
                              [25, 60000, 2300.5])
        self.checkValidations(qtbot, vcConfigTab.hasValidInput, False,
                              vcConfigTab.fullFrameExposureTimeLineEdit.setText,
                              [25, 60000, 2300.5])
