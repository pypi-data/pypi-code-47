#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     January 2019                                                                    #
#                                                                                           #
#############################################################################################

from __future__ import absolute_import, division, print_function

__all__ = ['font', 'color', 'line', 'marker',
           'image', 'video', 'player', 'viewer3d',
           'messager']

import os, sys
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
#
from cognitivegeo.src.vis.font import font as font
from cognitivegeo.src.vis.color import color as color
from cognitivegeo.src.vis.line import line as line
from cognitivegeo.src.vis.marker import marker as marker
from cognitivegeo.src.vis.colormap import colormap as cmap
from cognitivegeo.src.vis.image import image as image
from cognitivegeo.src.vis.video import video as video
from cognitivegeo.src.vis.player import player as player
from cognitivegeo.src.vis.viewer3d import viewer3d as viewer3d
from cognitivegeo.src.vis.messager import messager as messager