# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from PyQt5.QtWidgets import QDialogButtonBox

from spot_motion_monitor.config import DataConfig
from spot_motion_monitor.views import DataConfigurationDialog

class TestDataConfigurationDialog:

    def test_parametersAfterConstruction(self, qtbot):
        ccDialog = DataConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        assert ccDialog.tabWidget.count() == 1
        assert ccDialog.tabWidget.currentWidget().name == 'Data'

    def test_setConfiguration(self, qtbot):
        ccDialog = DataConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        truthConfig = DataConfig()
        truthConfig.buffer.pixelScale = 0.54

        ccDialog.setConfiguration(truthConfig)
        assert float(ccDialog.dataConfigTab.pixelScaleLineEdit.text()) == truthConfig.buffer.pixelScale

    def test_getConfiguration(self, qtbot, mocker):
        ccDialog = DataConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()
        mockGetConfiguration = mocker.patch.object(ccDialog.dataConfigTab, 'getConfiguration')

        ccDialog.getConfiguration()
        assert mockGetConfiguration.call_count == 1

    def test_validInputFromTabs(self, qtbot):
        ccDialog = DataConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        ccDialog.dataConfigTab.pixelScaleLineEdit.setText(str(-1))
        assert ccDialog.buttonBox.button(QDialogButtonBox.Ok).isEnabled() is False
