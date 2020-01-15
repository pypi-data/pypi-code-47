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
from scipy.fftpack import fftfreq, rfft

__all__ = ['fft_calculator']

def fft_calculator(xVals, yVals, collectRate):
    """Calculate the FFT of the given arrays.

    Parameters
    ----------
    xVals : numpy.array
        The x coordinates of the centroids.
    yVals : numpy.array
        The y coordinates of the centroids.
    collectRate : float
        The rate at which the data was collected (FPS).

    Returns
    -------
    (numpy.array, numpy.array, numpy.array)
        The FFTX, FFTY and Frequency arrays on the positive Frequency portion.
    """
    # Assume both arrays are same length.
    arrayLen = xVals.size

    xMean = np.mean(xVals)
    yMean = np.mean(yVals)

    xFft = rfft(xVals - xMean)
    yFft = rfft(yVals - yMean)

    frequencies = fftfreq(arrayLen, 1 / collectRate)

    dslice = slice(1, arrayLen // 2)

    return xFft[dslice], yFft[dslice], frequencies[dslice]
