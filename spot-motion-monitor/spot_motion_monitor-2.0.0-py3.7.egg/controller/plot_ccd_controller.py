# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import spot_motion_monitor.utils as smmUtils

__all__ = ['PlotCcdController']

class PlotCcdController():

    """This class manages the interactions between the all of the plot widgets
       and calculation data models.

    Attributes
    ----------
    cameraPlotWidget : .CameraPlotWidget
        An instance of the camera plot widget.
    updater : .InformationUpdater
        An instance of the status bar updater.
    """

    def __init__(self, cpw):
        """Initialize the class.

        Parameters
        ----------
        cpw : .CameraPlotWidget
            An instance of the camera plot widget.
        """
        self.cameraPlotWidget = cpw
        self.updater = smmUtils.InformationUpdater()

    def passFrame(self, frame, showFrames):
        """Receive and handle the camera CCD frame.

        Parameters
        ----------
        frame : numpy.array
            A frame from a camera CCD.
        showFrames : bool
            Flag to show camera CCD frames.
        """
        if frame is None:
            return
        if showFrames:
            self.cameraPlotWidget.image.setImage(frame)
