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

from spot_motion_monitor.views import BaseConfigurationDialog

class TestBaseConfigurationDialog:

    def test_inputFromTabsValid(self, qtbot):
        dialog = BaseConfigurationDialog()
        qtbot.addWidget(dialog)
        dialog.show()

        okButton = dialog.buttonBox.button(QDialogButtonBox.Ok)

        dialog.inputFromTabsValid(False)
        assert okButton.isEnabled() is False
        dialog.inputFromTabsValid(True)
        assert okButton.isEnabled() is True
