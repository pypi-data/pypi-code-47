import cv2 as cv
import numpy as np


def resize(img, size, interpolation=cv.INTER_LINEAR):
    '''
    Args:
        size: (h, w)
    '''

    if isinstance(size, int):
        h, w, _ = img.shape
        if w < h:
            ow = size
            oh = (ow / w) * h
        else:
            oh = size
            ow = (oh / h) * w
    else:
        oh, ow = size
    oh, ow = int(oh), int(ow)
    return cv.resize(img, (ow, oh), interpolation=interpolation)


def rotate(img, degree, interpolation=cv.INTER_LINEAR, expand=False, center=None):
    h, w, _ = img.shape
    if center is None:
        center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, degree, 1)

    if expand:
        cos, sin = abs(M[0, 0]), abs(M[0, 1])
        w, h = int(h * sin + w * cos), int(h * cos + w * sin)
        M[0, 2] += w/2 - center[0]
        M[1, 2] += h/2 - center[1]
    img = cv.warpAffine(img, M, (w, h), flags=interpolation)
    return img


# flipCode, horizontal: >0, vertical:0, horizaontal-vertical:<0
def hflip(img):
    return cv.flip(img, 1)


def vflip(img):
    return cv.flip(img, 0)


def crop(img, i, j, h, w):
    return img[i:(i+h), j:(j+w)]


def pad(img):
    pass


def center_crop(img, size):
    h, w, _ = img.shape
    if isinstance(size, int):
        size = (size, size)

    oh, ow = size
    i = int((h - oh) / 2)
    j = int((w - ow) / 2)
    return crop(img, i, j, oh, ow)


def resized_crop(img, i, j, h, w, size, interpolation=cv.INTER_LINEAR):
    img = crop(img, i, j, h, w)
    img = resize(img, size, interpolation)
    return img


def resized_center_crop(img, size, interpolation=cv.INTER_LINEAR):
    h, w, _ = img.shape
    img = center_crop(img, size)
    img = resize(img, (h, w), interpolation)
    return img


def adjust_brightness(img, scale):
    img = img * scale
    np.clip(img, 0, 255, out=img)
    return np.uint8(img)


def adjust_gamma(img, gamma, gain=1):
    gamma_map = np.array([255 * gain * pow(ele / 255., 1. / gamma)
                          for ele in range(256)]).astype(np.uint8)
    cv.LUT(img, gamma_map, img)
    return img

def to_gray(img, keep_dim=False):
    r, g, b = cv.split(img)
    gray = r * 299/1000 + g * 587/1000 + b * 114/1000
    if keep_dim:
        return cv.merge([gray] * 3)
    return gray

def adjust_saturation(img, scale):
    gray = to_gray(img, keep_dim=True)
    img = np.int32(img)
    img = img * scale + gray * (1.0 - scale) 
    np.clip(img, 0, 255, out=img)
    return np.uint8(img)

def adjust_contrast(img, scale):
    mean = round(to_gray(img).mean())
    gray = np.ones_like(img, dtype=np.uint8) * int(mean)
    img = img * scale + gray * (1.0 - scale) 
    np.clip(img, 0, 255, out=img)
    return np.uint8(img)

def adjust_hue(img, scale):

    if not(-0.5 <= scale <= 0.5):
        raise ValueError('hue_factor is not in [-0.5, 0.5].'.format(scale))
    img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    h, s, v = cv.split(img)

    h = np.int32(h)
    h = np.uint8((h + (scale * 180) % 181) % 181)

    img = cv.merge([h, s, v])
    img = cv.cvtColor(img, cv.COLOR_HSV2RGB)
    return img


def is_gray(img):
    if img.ndim == 2 or img.shape[-1] == 1:
        return True
    r, g, b = cv.split(img)
    if np.all(r == g) and np.all(r == b):
        return True
    return False


def clahe(img, clip_limit=2, tile_grid_size=(10, 10)):
    clahe = cv.createCLAHE(clip_limit, tile_grid_size)
    if is_gray(img):
        if img.ndim == 2 or img.shape[-1] == 1:
            img = clahe.apply(img)
        else:
            img = clahe.apply(img[..., 0])
            img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
    else:
        img = cv.cvtColor(img, cv.COLOR_RGB2LAB)
        img[..., 0] = clahe.apply(img[..., 0])
        img = cv.cvtColor(img, cv.COLOR_LAB2RGB)
    return img


def jpeg_quality(img, quality):
    _, im_code = cv.imencode('.jpg', img, (cv.IMWRITE_JPEG_QUALITY, quality))
    img = cv.imdecode(im_code, cv.IMREAD_UNCHANGED)
    return img


def perspective(img, startpoints, endpoints, interpolation=cv.INTER_LINEAR):
    M = cv.getPerspectiveTransform(startpoints, endpoints)
    img = cv.warpPerspective(img, M, img.shape[:2], interpolation)
    return img


def gaussian_noise(img, mean=0, var=0.01):
    noise = np.random.randn(*img.shape) * np.sqrt(var) + mean
    img = img * (1 + noise)
    np.clip(img, 0, 255, img)
    img = np.int8(img)
    return img

def poisson_noise(img, mean):
    noise = np.random.poisson(lam=mean, size=img.shape)
    np.sum(img, noise, out=img)
    np.clip(img, 0, 255, out=img)
    return np.uint8(img)


def speckle_noise(img):
    low = mean - np.sqrt(var)
    high = mean+ np.sqrt(var)
    J = np.random.uniform(low=low, high=high, size=size)
    return img

def imnoise(img, noise_type, mean=None, var=None, local_var=None, d=None):
    assert noise_type in ['gaussian', 'localvar', 'poisson', 'speckle']
    if noise_type == 'gaussian':
        img = gaussian_noise(img)
    elif noise_type == 'poisson':
        img = poisson_noise(img)
    elif  noise_type == 'speckle':
        img = speckle_noise(img)


    img  = img * (1 + J) * 255
    np.clip(img, 0, 255, out=img)
    return np.uint8(img)


def label_map(img, table, value=0):
    table = np.uint8([table.get(x, value) for x in range(256)])
    cv.LUT(img, table, img)
    return img