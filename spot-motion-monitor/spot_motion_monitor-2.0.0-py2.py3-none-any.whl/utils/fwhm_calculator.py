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

__all__ = ['fwhm_calculator']

def fwhm_calculator(frame, cx, cy):
    """Calculate the 2D Full-Width Half-Maximum for the given frame.

    Parameters
    ----------
    frame : `np.array`
        The frame information.
    cx : int
        The x pixel index to look along.
    cy : int
        The y pixel index to look along.

    Returns
    -------
    float
        The 2D FWHM.
    """
    def getFWHM1D(p):
        """Calculate the 1D Full-Width Half-Maximum.

        Parameters
        ----------
        p : `np.array`
            The axial slice for calculating FWHM.

        Returns
        -------
        float
            The 1D FWHM.
        """
        hm = np.max(p) / 2
        n = len(p)
        i1 = np.argmax(p > hm)
        i2 = n - np.argmax(p[::-1] > hm) - 1
        a2 = 0 if i2 >= n - 1 else (p[i2] - hm) / (p[i2] - p[i2 + 1])
        a1 = 0 if i1 <= 0 else (p[i1] - hm) / (p[i1] - p[i1 - 1])
        fwhm = i2 - i1 + 1 + a1 + a2
        return fwhm

    try:
        py, px = np.where(frame == np.max(frame))
        fwhmX = getFWHM1D(frame[int(py[0]), :])
        fwhmY = getFWHM1D(frame[:, int(px[0])])

        return (fwhmX + fwhmY) / 2
    except IndexError:
        return np.nan
