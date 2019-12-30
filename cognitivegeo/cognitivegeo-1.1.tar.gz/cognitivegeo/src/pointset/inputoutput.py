#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     January 2019                                                                    #
#                                                                                           #
#############################################################################################

# pointset data IO

import numpy as np
import os, sys
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.vis.messager import messager as vis_msg


__all__ = ['inputoutput']

def readPointFromAscii(asciifile, comment='#', delimiter=None,
                       inlcol=0, xlcol=1, zcol=2):
    """
    Read points from an ASCII file (by numpy.loadtxt)

    Args:
        asciifile:  An ASCII file for reading
        comment:    Comments. Default is '#'
        delimiter:  Delimiter. Default is None
        inlcol:     Index of the inline column. Default is 0
        xlcol:      Index of the crossline column. Default is 1
        zcol:       Index of the z column. Default is 2

    Return:
        2D array of the points from the ASCII file, with inline at column 0, crossline at column 1, and z at column 2
    """

    if os.path.exists(asciifile) is False:
        vis_msg.print("ERROR in readPointFromAscii: Pointset file not found", type='error')
        sys.exit()
    #
    data = np.loadtxt(asciifile, comments=comment, delimiter=delimiter)
    #
    npt, ncol = np.shape(data)
    #
    if inlcol >= ncol or inlcol < 0:
        vis_msg.print("ERROR in readPointFromAscii: Inline column index not found", type='error')
        sys.exit()
    if xlcol >= ncol or xlcol < 0:
        vis_msg.print("ERROR in readPointFromAscii: Crossline column index not found", type='error')
        sys.exit()
    if zcol >= ncol or zcol < 0:
        vis_msg.print("ERROR in readPointFromAscii: Z column index not found", type='error')
        sys.exit()
    #
    point = np.zeros([npt, ncol])
    point[:, 0:1] = data[:, inlcol:inlcol+1]
    point[:, 1:2] = data[:, xlcol:xlcol+1]
    point[:, 2:3] = data[:, zcol:zcol+1]
    # more columns
    idx = 3
    for i in range(ncol):
        if i != inlcol and i != xlcol and i != zcol:
            point[:, idx:idx+1] = data[:, i:i+1]
            idx = idx + 1
    #
    return point


class inputoutput:
    # group all functions as a single class
    readPointFromAscii = readPointFromAscii