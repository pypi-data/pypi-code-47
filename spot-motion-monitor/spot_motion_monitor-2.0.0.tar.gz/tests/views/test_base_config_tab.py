# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLineEdit

import pytest

from spot_motion_monitor.views import BaseConfigTab

class TestBaseConfigTab:

    def setup_class(self):
        self.fast_timeout = 250  # ms

    def stateIsFalse(self, state):
        return not state

    def stateIsTrue(self, state):
        return state

    def test_parametersAfterConstruction(self, qtbot):
        baseTab = BaseConfigTab()
        qtbot.addWidget(baseTab)
        assert baseTab.name == 'Base'

    def test_noApiCallAfterConstruction(self, qtbot):
        baseTab = BaseConfigTab()
        qtbot.addWidget(baseTab)

        with pytest.raises(NotImplementedError):
            baseTab.getConfiguration()

        with pytest.raises(NotImplementedError):
            baseTab.setConfiguration({})

    def test_validInput(self, qtbot):
        baseTab = BaseConfigTab()
        qtbot.addWidget(baseTab)

        # Insert a widget for testing
        baseTab.lineEdit = QLineEdit()
        baseTab.lineEdit.setValidator(QIntValidator(1, 5))
        baseTab.lineEdit.textChanged.connect(baseTab.validateInput)

        with qtbot.waitSignal(baseTab.hasValidInput, timeout=self.fast_timeout,
                              check_params_cb=self.stateIsTrue) as valid:
            baseTab.lineEdit.setText('3')

        assert valid.signal_triggered

        with qtbot.waitSignal(baseTab.hasValidInput, timeout=self.fast_timeout,
                              check_params_cb=self.stateIsFalse) as valid:
            baseTab.lineEdit.setText('6')

        assert valid.signal_triggered
