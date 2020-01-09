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

from spot_motion_monitor.config import GeneralConfig
from spot_motion_monitor.views import GeneralConfigTab

class TestGeneralConfigTab:

    def test_parametersAfterConstruction(self, qtbot):
        gcConfigTab = GeneralConfigTab()
        qtbot.addWidget(gcConfigTab)

        assert gcConfigTab.name == 'General'

    def test_setParametersFromConfiguration(self, qtbot):
        gcConfigTab = GeneralConfigTab()
        qtbot.addWidget(gcConfigTab)

        truthConfig = GeneralConfig()

        gcConfigTab.setConfiguration(truthConfig)
        assert gcConfigTab.siteNameLineEdit.text() == ''
        assert gcConfigTab.configVersionLineEdit.text() == ''
        assert gcConfigTab.autorunCheckBox.isChecked() is False
        assert gcConfigTab.timezoneComboBox.currentText() == truthConfig.timezone
        assert gcConfigTab.telemetryDirLineEdit.text() == ''
        assert gcConfigTab.removeDirectoryCheckBox.isChecked() is True
        assert gcConfigTab.removeFilesCheckBox.isEnabled() is False
        assert gcConfigTab.removeFilesCheckBox.isChecked() is True

        truthConfig.site = "Testing"
        truthConfig.configVersion = "0.0.1"
        truthConfig.timezone = "US/Arizona"
        truthConfig.autorun = True
        truthConfig.fullTelemetrySavePath = "/home/testuser/telemetry"
        truthConfig.removeTelemetryDir = False

        gcConfigTab.setConfiguration(truthConfig)
        assert gcConfigTab.siteNameLineEdit.text() == truthConfig.site
        assert gcConfigTab.configVersionLineEdit.text() == truthConfig.configVersion
        assert gcConfigTab.timezoneComboBox.currentText() == truthConfig.timezone
        assert gcConfigTab.autorunCheckBox.isChecked() is True
        assert gcConfigTab.telemetryDirLineEdit.text() == truthConfig.fullTelemetrySavePath
        assert gcConfigTab.removeDirectoryCheckBox.isChecked() is False
        assert gcConfigTab.removeFilesCheckBox.isEnabled() is True
        assert gcConfigTab.removeFilesCheckBox.isChecked() is True

        truthConfig.removeTelemetryFiles = False
        gcConfigTab.setConfiguration(truthConfig)
        assert gcConfigTab.removeFilesCheckBox.isEnabled() is True
        assert gcConfigTab.removeFilesCheckBox.isChecked() is False

    def test_getParametersFromConfiguration(self, qtbot):
        gcConfigTab = GeneralConfigTab()
        qtbot.addWidget(gcConfigTab)

        truthConfig = GeneralConfig()
        truthConfig.site = "New Mountain"
        truthConfig.autorun = True
        truthConfig.fullTelemetrySavePath = "/home/demouser/telemetry"
        truthConfig.removeTelemetryDir = False

        gcConfigTab.siteNameLineEdit.setText(truthConfig.site)
        gcConfigTab.autorunCheckBox.setChecked(truthConfig.autorun)
        gcConfigTab.telemetryDirLineEdit.setText(truthConfig.fullTelemetrySavePath)
        gcConfigTab.removeDirectoryCheckBox.setChecked(truthConfig.removeTelemetryDir)
        gcConfigTab.removeFilesCheckBox.setChecked(truthConfig.removeTelemetryFiles)

        config = gcConfigTab.getConfiguration()
        try:
            assert config == truthConfig
        except AssertionError:
            print("Getter: ", config)
            print("Truth: ", truthConfig)
            raise

    def test_telemetryDirectorySelection(self, qtbot, mocker):
        gcConfigTab = GeneralConfigTab()
        qtbot.addWidget(gcConfigTab)
        gcConfigTab.show()

        truthDirectory = "/home/demouser/telemetry"

        gcConfigTab._openFileDialog = mocker.Mock(return_value=truthDirectory)

        assert gcConfigTab.telemetryDirLineEdit.text() == ''

        qtbot.mouseClick(gcConfigTab.telemetryDirPushButton, Qt.LeftButton)
        assert gcConfigTab.telemetryDirLineEdit.text() == truthDirectory

        qtbot.mouseClick(gcConfigTab.clearTelemetryDirPushButton, Qt.LeftButton)
        assert gcConfigTab.telemetryDirLineEdit.text() == ''
