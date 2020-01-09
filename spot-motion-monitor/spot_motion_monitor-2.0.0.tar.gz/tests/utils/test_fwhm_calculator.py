# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import numpy as np
import pytest

from spot_motion_monitor.utils import fwhm_calculator

class TestFwhmCalculator:

    def test_calculation(self):
        np.random.seed(4000)
        x, y = np.meshgrid(np.arange(50), np.arange(50))
        x0 = 30
        y0 = 15
        sigma = 5
        z = 10 * np.exp(-((x - x0)**2 + (y - y0)**2) / 2 / sigma)
        z += np.random.uniform(size=2500).reshape(50, 50)

        fwhm = fwhm_calculator(z, x0, y0)
        assert fwhm == pytest.approx(6.11, rel=1e-2)
