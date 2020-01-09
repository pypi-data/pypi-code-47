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

import spot_motion_monitor.utils as utils

class TestConfigHelpers:

    def test_boolToCheckState(self):
        assert utils.boolToCheckState(False) == Qt.Unchecked
        assert utils.boolToCheckState(True) == Qt.Checked

    def test_checkStateToBool(self):
        assert utils.checkStateToBool(Qt.Checked) is True
        assert utils.checkStateToBool(Qt.Unchecked) is False

    def test_noneToDefaultOrValue(self):
        value = None
        assert utils.noneToDefaultOrValue(value) == ''
        default = 'None'
        assert utils.noneToDefaultOrValue(value, default=default) == default
        value = 100
        assert utils.noneToDefaultOrValue(value) == value

    def test_defaultToNoneOrValue(self):
        value = ''
        assert utils.defaultToNoneOrValue(value) is None
        value = 'None'
        default = 'None'
        assert utils.defaultToNoneOrValue(value, default=default) is None
        value = 100
        assert utils.defaultToNoneOrValue(value) == value

    def test_convertValueOrNone(self):
        value = None
        assert utils.convertValueOrNone(value) == value
        value = 10
        assert utils.convertValueOrNone(value) == value
        value = 14.42542
        assert utils.convertValueOrNone(value, convert=float) == value
