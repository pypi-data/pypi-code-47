# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from PyQt5.QtCore import Qt

from spot_motion_monitor.config import GaussianCameraConfig
from spot_motion_monitor.utils import boolToCheckState
from spot_motion_monitor.views import GaussianCameraConfigTab

class TestGaussianCameraConfigTab:

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
        gcConfigTab = GaussianCameraConfigTab()
        qtbot.addWidget(gcConfigTab)

        assert gcConfigTab.name == 'Gaussian'
        assert gcConfigTab.config is not None
        assert gcConfigTab.spotOscillationCheckBox.isChecked() is False
        assert gcConfigTab.spotOscillationGroupBox.isEnabled() is False

    def test_setParametersFromConfiguration(self, qtbot):
        gcConfigTab = GaussianCameraConfigTab()
        qtbot.addWidget(gcConfigTab)

        truthConfig = GaussianCameraConfig()
        truthConfig.roiSize = 30
        truthConfig.doSpotOscillation = False
        truthConfig.xAmplitude = 2
        truthConfig.xFrequency = 50.0
        truthConfig.yAmplitude = 7
        truthConfig.yFrequency = 25.0

        gcConfigTab.setConfiguration(truthConfig)
        assert int(gcConfigTab.roiSizeLineEdit.text()) == truthConfig.roiSize
        state = gcConfigTab.spotOscillationCheckBox.checkState()
        boolState = True if state == Qt.Checked else False
        assert boolState == truthConfig.doSpotOscillation
        assert int(gcConfigTab.xAmpLineEdit.text()) == truthConfig.xAmplitude
        assert float(gcConfigTab.xFreqLineEdit.text()) == truthConfig.xFrequency
        assert int(gcConfigTab.yAmpLineEdit.text()) == truthConfig.yAmplitude
        assert float(gcConfigTab.yFreqLineEdit.text()) == truthConfig.yFrequency

    def test_getParametersFromConfiguration(self, qtbot):
        gcConfigTab = GaussianCameraConfigTab()
        qtbot.addWidget(gcConfigTab)
        gcConfigTab.show()

        truthConfig = GaussianCameraConfig()
        truthConfig.roiSize = 30
        truthConfig.doSpotOscillation = True
        truthConfig.xAmplitude = 2
        truthConfig.xFrequency = 50.0
        truthConfig.yAmplitude = 7
        truthConfig.yFrequency = 25.0

        gcConfigTab.roiSizeLineEdit.setText(str(truthConfig.roiSize))
        gcConfigTab.spotOscillationCheckBox.setChecked(boolToCheckState(truthConfig.doSpotOscillation))
        gcConfigTab.xAmpLineEdit.setText(str(truthConfig.xAmplitude))
        gcConfigTab.xFreqLineEdit.setText(str(truthConfig.xFrequency))
        gcConfigTab.yAmpLineEdit.setText(str(truthConfig.yAmplitude))
        gcConfigTab.yFreqLineEdit.setText(str(truthConfig.yFrequency))

        config = gcConfigTab.getConfiguration()
        assert config == truthConfig

        truthConfig.roiSize = 50
        truthConfig.doSpotOscillation = False

        gcConfigTab.roiSizeLineEdit.setText(str(truthConfig.roiSize))
        gcConfigTab.spotOscillationCheckBox.setChecked(boolToCheckState(truthConfig.doSpotOscillation))

        config = gcConfigTab.getConfiguration()
        assert config == truthConfig

    def test_validLineEditParameters(self, qtbot):
        gcConfigTab = GaussianCameraConfigTab()
        qtbot.addWidget(gcConfigTab)
        gcConfigTab.show()

        self.checkValidations(qtbot, gcConfigTab.hasValidInput, True, gcConfigTab.roiSizeLineEdit.setText,
                              [20, 200, 150])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, True, gcConfigTab.xAmpLineEdit.setText,
                              [1, 20, 10])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, True, gcConfigTab.xFreqLineEdit.setText,
                              [1.0, 100.0, 4e1])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, True, gcConfigTab.yAmpLineEdit.setText,
                              [1, 20, 10])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, True, gcConfigTab.yFreqLineEdit.setText,
                              [1.0, 100.0, 4e1])

    def test_invalidLineEditParameters(self, qtbot):
        gcConfigTab = GaussianCameraConfigTab()
        qtbot.addWidget(gcConfigTab)
        gcConfigTab.show()

        self.checkValidations(qtbot, gcConfigTab.hasValidInput, False, gcConfigTab.roiSizeLineEdit.setText,
                              [10, 40.1, 201])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, False, gcConfigTab.xAmpLineEdit.setText,
                              [0, 30, 5.1])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, False, gcConfigTab.xFreqLineEdit.setText,
                              [0.05, 5.6352, 2e2])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, False, gcConfigTab.yAmpLineEdit.setText,
                              [0, 30, 5.1])
        self.checkValidations(qtbot, gcConfigTab.hasValidInput, False, gcConfigTab.yFreqLineEdit.setText,
                              [0.05, 5.6352, 2e2])
