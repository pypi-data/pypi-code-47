# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

__all__ = ["CameraNotFound", "FrameCaptureFailed", "FrameRejected"]

class CameraNotFound(Exception):
    """Exception for a camera startup failure.
    """

class FrameCaptureFailed(Exception):
    """Exception for a frame capture failure
    """

class FrameRejected(Exception):
    """Exception for rejected frames.
    """
    pass
