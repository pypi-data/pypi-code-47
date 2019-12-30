#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

# basic functions for processing video

import sys, os
import numpy as np
from scipy import interpolate
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.vis.messager import messager as vis_msg


__all__ = ['video']


def changeVideoSize(video, video_height, video_width, video_depth,
                    video_height_new, video_width_new, video_depth_new, method='linear'):
    """
    Change video size through 3D interpolation (RegularGridInterpolator from scipy)

    Args:
        video:              2D matrix of videos [pixel 1, pixel 2, ..., pixel N]
                            Each row for all pixels in an video
        video_height:       Original height of video
        video_width:        Original width of video
        video_depth:        Original depth of video
        video_height_new:   New height of video
        video_width_new:    New width of video
        video_depth_new:    New depth of video
        method:             Interpolation kind, 'linear' or 'nearest'. Default is 'linear'

    Returns:
        2D matrix of videos after interpolation, with each row representing one video
    """

    if np.ndim(video) != 2:
        vis_msg.print('ERROR in changeVideoSize: 2D video matrix expected', type='error')
        sys.exit()
    if video_height <= 1 or video_width <= 1 or video_depth <= 1:
        vis_msg.print('ERROR in changeVideoSize: Original video height/width/depth be > 1', type='error')
        sys.exit()
    if video_height_new <= 0 or video_width_new <= 0 or video_depth_new <= 0:
        vis_msg.print('ERROR in changeVideoSize: New video height/width/depth be >= 1', type='error')
        sys.exit()

    nvideo, npixel = np.shape(video)

    if npixel != video_height * video_width * video_depth:
        vis_msg.print('ERROR in changeVideoSize: Original video height/width/depth not match', type='error')
        sys.exit()

    height = np.linspace(0.0, 1.0, video_height)
    width = np.linspace(0.0, 1.0, video_width)
    depth = np.linspace(0.0, 1.0, video_depth)
    height_new = np.linspace(0.0, 1.0, video_height_new)
    width_new = np.linspace(0.0, 1.0, video_width_new)
    depth_new = np.linspace(0.0, 1.0, video_depth_new)
    npixel_new = video_height_new * video_width_new * video_depth_new
    height_new, width_new, depth_new = np.meshgrid(height_new, width_new, depth_new, indexing='ij')
    height_new = np.reshape(height_new, [npixel_new, 1])
    width_new = np.reshape(width_new, [npixel_new, 1])
    depth_new = np.reshape(depth_new, [npixel_new, 1])

    video_new = np.zeros([nvideo, npixel_new])
    for i in range(nvideo):
        video_i = video[i, :]
        video_i = np.reshape(video_i, [video_height, video_width, video_depth])

        f = interpolate.RegularGridInterpolator((height, width, depth), video_i, method=method)
        video_i_new = f(np.concatenate((height_new, width_new, depth_new), axis=1))
        video_i_new = np.reshape(video_i_new, [video_height_new, video_width_new, video_depth_new])
        video_new[i, :] = np.reshape(video_i_new, [1, npixel_new])

    return video_new


class video:
    # Pack all functions as a class
    #
    changeVideoSize = changeVideoSize