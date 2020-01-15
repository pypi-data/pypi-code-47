from .tensor import *
from . import functional_cv2 as F_cv2
from . import functional_pil as F_pil
from . import functional_tensor as F_tensor
import cv2 as cv


def im_type(img):
    if is_numpy(img):
        return 'cv2'
    if is_pil(img):
        return 'pil'
    if is_tensor(img):
        return 'tensor'

def call_by_name(func, img, *args, **kwargs):
    func_map = {
        'cv2': F_cv2,
        'pil': F_pil,
        'tensor': F_tensor
    }
    return getattr(func_map[im_type(img)], func)(img, *args, **kwargs)
    

def inter_code(mode, backend):
    interpolation = {
        'pil': {
            'nearest': Image.NEAREST,
            'bilinear': Image.BILINEAR,
            'bicubic': Image.BICUBIC,
        },
        'cv2': {
            'nearest': cv.INTER_NEAREST,
            'bilinear': cv.INTER_LINEAR,
            'bicubic': cv.INTER_CUBIC,
        },
        'tensor': {},
    }
    return interpolation[backend].get(mode, mode)


def get_image_size(img):
    if is_pil(img):
        w, h = img.size
    elif is_tensor(img) and img.dim() > 2:
        h, w = img.shape[-2:]
    elif is_numpy(img):
        h, w = img.shape[:2]
    else:
        raise TypeError("Unexpected type {}".format(type(img)))
    return h, w


def hflip(img):
    return call_by_name('hflip', img)


def vflip(img):
    return call_by_name('vflip', img)


def rotate(img, degree, interpolation='bilinear', expand=False, center=None):
    return call_by_name('rotate', img, degree=degree, interpolation=inter_code(interpolation, im_type(img)), expand=False, center=None)


def resize(img, size, interpolation):
    return call_by_name('resize', img, size=size, interpolation=inter_code(interpolation, im_type(img)))


def resized_crop(img, i, j, h, w, size, interpolation):
    return call_by_name('resized_crop', img, i, j, h, w, size, inter_code(interpolation, im_type(img)))


def adjust_brightness(img, scale):
    return call_by_name('adjust_brightness', img, scale)

def adjust_contrast(img, scale):
    return call_by_name('adjust_contrast', img, scale)

def adjust_saturation(img, scale):
    return call_by_name('adjust_saturation', img, scale)

def adjust_hue(img, scale):
    return call_by_name('adjust_hue', img, scale)

def adjust_gamma(img, gamma, gain):
    return call_by_name('adjust_gamma', img, gamma, gain)

def perspective(img, startpoints, endpoints, interpolation):
    return call_by_name('perspective', startpoints, endpoints, inter_code(interpolation, im_type(img)))

def label_map(img, table):
    return call_by_name('label_map', img, table)

def normalize(tensor, mean, std):
    return F_tensor.normalize(tensor, mean, std)

