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
from scipy import ndimage

from spot_motion_monitor.utils import GenericFrameInformation, FrameRejected, passFrame
from spot_motion_monitor.utils import fwhm_calculator

__all__ = ["FullFrameModel"]

class FullFrameModel():

    """This class handles the calculations for a full CCD frame.

    The class handles all of the calculations necessary to produce information
    to fill out a GenericFrameInformation instance. The class references the
    term object which means a collection of contiguous pixels that are over
    a calculated frame threshold.

    Attributes
    ----------
    frameCheck : function
        The function providing the frame selection criteria.
    minimumNumPixels : int
        The minimum number of pixels that must be in an object.
    sigmaScale : float
        Multiplier for the frame standard deviation.
    timeHandler : `utils.TimeHandler`
        The instance of the TimeHandler.
    """

    def __init__(self):
        """Initialize the class
        """
        self.sigmaScale = 5.0
        self.minimumNumPixels = 10
        self.frameCheck = None
        self.timeHandler = None

    def calculateCentroid(self, fullFrame):
        """This function performs calculations for the full CCD frame.

        Parameters
        ----------
        fullFrame : numpy.array
            A full CCD frame.

        Returns
        -------
        GenericInformation
            The instance containing the results of the calculations.

        Raises
        ------
        FrameRejected
            Reject frames for different reasons. Messages tell why.
        """
        if self.frameCheck is None:
            self.frameCheck = passFrame

        # Background and noise threshold calculations
        frameStd = ndimage.standard_deviation(fullFrame)
        threshold = np.median(fullFrame) + self.sigmaScale * frameStd
        thresholdMask = fullFrame > threshold
        frameLabels, numLabels = ndimage.label(thresholdMask)

        # Sizes and mean values of all objects found
        labelSizes = ndimage.sum(thresholdMask, frameLabels, range(numLabels + 1))

        # Cleanup small objects
        maskSize = labelSizes < self.minimumNumPixels
        removePixel = maskSize[frameLabels]
        frameLabels[removePixel] = 0

        # Reassign labels
        labels = np.unique(frameLabels)
        frameLabels = np.searchsorted(labels, frameLabels)
        objects = ndimage.find_objects(frameLabels)

        try:
            objectSize = ndimage.sum(thresholdMask, frameLabels, 1)
            # Object slice coordinates refer to image origin
            ySlice, xSlice = objects[0]
            objectFrame = fullFrame[ySlice, xSlice] - threshold
            objectFrame[objectFrame < 0] = 0
            flux = objectFrame.sum()
            maxAdc = objectFrame.max()
            comY, comX = ndimage.center_of_mass(objectFrame)
            if self.frameCheck(flux, maxAdc, comX, comY):
                fwhm = fwhm_calculator(objectFrame, int(comX), int(comY))
                centerX = comX + xSlice.start
                centerY = comY + ySlice.start
                return GenericFrameInformation(self.timeHandler.getTime(), centerX, centerY,
                                               flux, maxAdc, fwhm, objectSize, None)
            else:
                msg = 'Full frame rejected: flux = {}, maxAdc = {}, centroid = ({}, {})'.format(flux,
                                                                                                maxAdc,
                                                                                                comX,
                                                                                                comY)
                raise FrameRejected(msg)
        except IndexError:
            raise FrameRejected("Failed to find object in frame.")
