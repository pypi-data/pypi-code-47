# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from pyqtgraph import GraphicsLayoutWidget, ImageItem

__all__ = ['CameraPlotWidget']

class CameraPlotWidget(GraphicsLayoutWidget):

    """This class manages and displays the camera CCD frame.

    Attributes
    ----------
    image : numpy.array
        The data frame to display.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        p1 = self.addPlot()
        p1.setAspectLocked(True)
        self.image = ImageItem()
        self.image.setOpts(axisOrder='row-major')
        p1.addItem(self.image)
