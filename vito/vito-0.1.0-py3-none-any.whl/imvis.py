#!/usr/bin/env python
# coding=utf-8
"""Handy visualization tools."""

import numpy as np

from . import colormaps
from . import imutils

try:
    # Try to load OpenCV (in case you installed it in your workspace)
    import cv2

    def imshow(img_np, title="Image", flip_channels=False, wait_ms=10):
        """
        Convenience 1-liner to display image and wait for key input.

        :param img_np:    Should be provided as BGR, otherwise use flip_channels=True
        :param title:  Window title
        :param wait_ms: cv2.waitKey() input
        :param flip_channels: if you want to display an RGB image poperly, we need 
                            to flip the color channels
        :return: Pressed key or -1, i.e. cv2.waitKey() output
        """
        if flip_channels:
            disp = imutils.flip_layers(img_np)
        else:
            disp = img_np
        cv2.imshow(title, disp)
        return cv2.waitKey(wait_ms)
except:
    from PIL import Image

    def imshow(img_np, title="Image", flip_channels=False, **kwargs):
        """
        Convenience 1-liner to display image. This implementation uses
        PIL (which uses your OS default viewer).
        'kwargs' will silently be ignored and are only provided to be
        compatible with the OpenCV-based 'imshow' version (which will be
        loaded in case 'cv2' is installed in your python workspace).

        Note that the window usually doesn't block!

        :param img:    Should be provided as BGR, otherwise use flip_channels=True
        :param title:  Window title
        :param flip_channels: if you want to display an RGB image poperly, we need 
                            to flip the color channels
        :return: -1 for compatibility reasons (the same return value as if you
                        used the OpenCV-based version and there was no key press)
        """
        if flip_channels:
            disp = imutils.flip_layers(img_np)
        else:
            disp = img_np
        im = Image.fromarray(disp)
        im.show(title=title)
        return -1



# #TODO implement
# def color_by_id(id, flip_channels=False):
#     """Returns a color tuple (rgb) to colorize labels, identities, segments, etc."""
#     col = color_by_id__(id)
#     if flip_channels:
#         return (col[2], col[1], col[0])
#     return col


def pseudocolor(values, limits=[0.0, 1.0], color_map=colormaps.colormap_parula_rgb):
    """
    Return a HxWx3 pseudocolored representation of the input matrix.

    :param values: A single channel, HxW or HxWx1 numpy ndarray.
    :param limits: [min, max] to clip the input values. If limits is None or
        any of min/max is None, the corresponding limits will be computed from
        the input values.
    :param color_map: The color map to be used, see colormaps.py

    :return: a HxWx3 colorized representation.
    """
    # Sanity checks
    if len(values.shape) > 2:
        if values.shape[2] > 1:
            raise ValueError('Input to pseudocoloring must be a single channel data matrix, shaped (H,W) or (H,W,1)!')
        values = values.reshape((values.shape[0], values.shape[1]))

    if limits is None:
        limits = [np.min(values[:]), np.max(values[:])]
    if limits[0] is None:
        limits[0] = np.min(values[:])
    if limits[1] is None:
        limits[1] = np.max(values[:])

    values = values.astype(np.float64)
    lut = np.asarray(color_map)
    interval = (limits[1] - limits[0]) / 255.0
    # Clip values to desired limits
    values[values < limits[0]] = limits[0]
    values[values > limits[1]] = limits[1]
    # Compute lookup values
    if interval > 0:
        lookup_values = np.floor((values - limits[0]) / interval).astype(np.int32)
    else:
        lookup_values = np.zeros(values.shape, dtype=np.int32)
    colorized = lut[lookup_values].astype(np.uint8)
    return colorized


def overlay(img1, img2, weight1, mask1=None):
    """Overlay two images with alpha blending, s.t.
    out = img1 * weight1 + img2 * (1-weight2).
    Optionally, only overlays those parts of the image which are indicated by
    non-zero mask1 pixels: out = blended if mask1 > 0, else img2
    Output dtype will be the same as img2.dtype.
    Only float32, float64 and uint8 are supported.
    """
    if weight1 < 0.0 or weight1 > 1.0:
        raise ValueError('Weight factor must be in [0,1]')

    # Allow overlaying a grayscale image on top of a color image (and vice versa)
    if len(img1.shape) == 2:
        channels1 = 1
    else:
        channels1 = img1.shape[2]

    if len(img2.shape) == 2:
        channels2 = 1
    else:
        channels2 = img2.shape[2]

    if channels1 == channels2 and not (channels1 == 1 or channels1 == 3):
        raise ValueError('Can only extrapolate single channel image to the others dimension')

    if channels1 == 1 and channels2 > 1:
        img1 = np.repeat(img1[:,:,np.newaxis], channels2, axis=2)
    if channels2 == 1 and channels1 > 1:
        img2 = np.repeat(img2[:,:,np.newaxis], channels1, axis=2)

    num_channels = 1 if len(img1.shape) == 2 else img1.shape[2]

    # Convert to float64, [0,1]
    if img1.dtype == np.uint8:
        scale1 = 255.0
    elif img1.dtype in [np.float32, np.float64]:
        scale1 = 1.0
    else:
        raise ValueError('Datatype {} not yet supported'.format(img1.dtype))
    img1 = img1.astype(np.float64) / scale1

    target_dtype = img2.dtype
    if img2.dtype == np.uint8:
        scale2 = 255.0
    elif img2.dtype in [np.float32, np.float64]:
        scale2 = 1.0
    else:
        raise ValueError('Datatype {} not yet supported'.format(img2.dtype))
    img2 = img2.astype(np.float64) / scale2

    if mask1 is None:
        out = weight1 * img1 + (1. - weight1) * img2
    else:
        if num_channels == 1:
            img1 = np.where(np.repeat(mask1[:,:,np.newaxis], num_channels, axis=2) > 0, img1, img2)
        else:
            img1 = np.where(mask1 > 0, img1, img2)
        out = weight1 * img1 + (1. - weight1) * img2
        # out = img2
        # idx = np.where(mask1 > 0)
        # out[idx] = weight1 * img1[idx] + (1. - weight1) * img2[idx]
    return (scale2 * out).astype(target_dtype)
