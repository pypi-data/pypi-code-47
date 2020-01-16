# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from collections import namedtuple

__all__ = ["FullFrameInformation", "GenericFrameInformation", "RoiFrameInformation"]

"""Frame information named tuples

Attributes
----------
FullFrameInformation : namedtuple
    Information describing a full CCD frame
    * centerX (int) - The calculated x pixel value of the frame centroid
    * centerY (int) - The calculated y pixel value of the frame centroid
    * flux (float) - The sum total ADC count for the frame
    * maxAdc (float) - The maximum ADC in the frame
    * fwhm (float) - The FHWM of the spot in pixels
GenericFrameInformation : namedtuple
    Information describing a generic CCD frame
    * timestamp (datetime.datetime) - The date/time when measurement was made
    * centerX (float) - The calculated x pixel value of the frame centroid
    * centerY (float) - The calculated y pixel value of the frame centroid
    * flux (float) - The sum total ADC count for the frame
    * maxAdc (float) - The maximum ADC in the frame
    * fwhm (float) - The FHWM of the spot in pixels
    * objectSize (int) - The number of pixels in an identified object (pixels above threshold)
    * stdNoObjects (float) - The standard deviation of the frame with no object pixels
RoiFrameInformation : namedtuple
    Information describing a ROI CCD frame
    * centerX (float) - The calculated x pixel value of the frame centroid
    * centerY (float) - The calculated y pixel value of the frame centroid
    * flux (float) - The sum total ADC count for the frame
    * maxAdc (float) - The maximum ADC in the frame
    * fwhm (float) - The FHWM of the spot in pixels
    * rmsX (float) - The standard deviation of the centerX values in arcseconds
    * rmsY (float) - The standard deviation of the centerY values in arcseconds
    * validFrames (tuple(int, float)) - The number and time of valid frames
"""

FullFrameInformation = namedtuple('FullFrameInformation', 'centerX centerY flux maxAdc fwhm')

GenericFrameInformation = namedtuple('GenericFrameInformation',
                                     'timestamp centerX centerY flux maxAdc fwhm objectSize stdNoObjects')

RoiFrameInformation = namedtuple('RoiFrameInformation',
                                 'centerX centerY flux maxAdc fwhm rmsX rmsY validFrames')
