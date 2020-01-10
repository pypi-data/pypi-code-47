"""
Name : Graphics.py
Author  : Cash
Contact : tkggpdc2007@163.com
Time    : 2020-01-08 10:52
Desc:
"""

import cv2
import numpy as np

__all__ = ['alpha_compose', 'add_border', 'erase_border', 'alpha_nonzero']


def alpha_compose(image, src, x, y):
    """
    图像alpha通道融合
    :param image: numpy data with 3/4 channels
    :param src: numpy data with 4 channels
    :param x: col
    :param y: row
    :return: numpy data with 4 channels
    """
    try:
        if len(image.shape) < 3:
            return image

        if len(src.shape) < 3 or src.shape[-1] < 4:
            return src

        if image.shape[-1] == 3:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
        width, height = image.shape[:2][::-1]
        w, h = src.shape[:2][::-1]

        x1, y1 = max(-x, 0), max(-y, 0)
        x2, y2 = min(width - x, w), min(height - y, h)
        src = src[y1:y2, x1:x2]
        alpha = np.expand_dims(src[:, :, 3] / 255.0, -1)

        x, y = max(x, 0), max(y, 0)
        w, h = src.shape[:2][::-1]
        image[y:y + h, x:x + w] = src * alpha + image[y:y + h, x:x + w] * (1 - alpha)

    except ValueError:
        pass

    return image


def add_border(image, border, color):
    """
    添加边框
    :param image: numpy data with 3 channers
    :param border: [up, down, left, right]
    :param color: (r, g, b)
    :return:
    """
    if len(image.shape) < 3:
        return image

    h, w, c = image.shape
    up, down, left, right = border
    if up < 0 or down < 0 or left < 0 or right < 0:
        return image
    height, width, channel = h + up + down, w + left + right, 3
    new = np.empty((height, width, channel))
    new[:, :] = color
    new[up:height - down, left:width - right] = image
    return new


def erase_border(image, border, color):
    """
    添加边框
    :param image: numpy data with 3 channels
    :param border: [up, down, left, right]
    :param color: (r, g, b)
    :return:
    """
    if len(image.shape) < 3:
        return image

    height, width, _ = image.shape
    up, down, left, right = border
    if up < 0 or down < 0 or left < 0 or right < 0:
        return image
    new = np.empty((height, width, 3))
    new[:, :] = color
    new[up:height - down, left:width - right] = image[up:height - down, left:width - right]
    return new.astype(np.uint8)


def alpha_nonzero(image):
    """
    处理图层图像，裁剪空白区域，保留最小凸包
    :param image:
    :return:
    """
    if len(image.shape) != 3 and image.shape[-1] != 4:
        return image
    x = np.nonzero(image[:, :, 3])
    c_min = min(x[1])
    c_max = max(x[1])
    r_min = min(x[0])
    r_max = max(x[0])
    return image[r_min:r_max + 1, c_min:c_max + 1]
