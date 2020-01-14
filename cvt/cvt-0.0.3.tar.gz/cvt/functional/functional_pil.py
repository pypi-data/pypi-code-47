from PIL import Image, ImageOps, ImageEnhance
import numpy as np

def hflip(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)


def vflip(img):
    return img.transpose(Image.FLIP_TOP_BOTTOM)


def crop(img, i, j, h, w):
    return img.crop((j, i, j + w, i + h))


def resize(img, size, interpolation=Image.BILINEAR):
    if isinstance(size, int):
        w, h = img.size
        if (w <= h and w == size) or (h <= w and h == size):
            return img
        if w < h:
            ow = size
            oh = int(size * h / w)
            return img.resize((ow, oh), interpolation)
        else:
            oh = size
            ow = int(size * w / h)
    else:
        oh, ow = size
    return img.resize((ow, oh), interpolation)


def rotate(img, degree, interpolation=Image.BILINEAR, expand=False, center=None, fill=0):
    return img.rotate(degree, interpolation, expand, center, fillcolor=fill)

def resized_crop(img, i, j, h, w, size, interpolation=Image.BILINEAR):
    img = crop(img, i, j, h, w)
    img = resize(img, size, interpolation)
    return img

def adjust_brightness(img, scale):
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(scale)
    return img

def adjust_contrast(img, scale):
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(scale)
    return img

def adjust_saturation(img, scale):
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(scale)
    return img


def adjust_hue(img, scale):

    if not(-0.5 <= scale <= 0.5):
        raise ValueError('hue_factor is not in [-0.5, 0.5].'.format(scale))

    input_mode = img.mode
    if input_mode in {'L', '1', 'I', 'F'}:
        return img

    h, s, v = img.convert('HSV').split()

    np_h = np.array(h, dtype=np.uint8)
    # uint8 addition take cares of rotation across boundaries
    with np.errstate(over='ignore'):
        np_h += np.uint8(scale * 255)
    h = Image.fromarray(np_h, 'L')

    img = Image.merge('HSV', (h, s, v)).convert(input_mode)
    return img


def adjust_gamma(img, gamma, gain=1):
    input_mode = img.mode
    img = img.convert('RGB')

    gamma_map = [255 * gain * pow(ele / 255., gamma) for ele in range(256)] * 3
    img = img.point(gamma_map) 
    img = img.convert(input_mode)
    return img

def _get_perspective_coeffs(startpoints, endpoints):
    matrix = []

    for p1, p2 in zip(endpoints, startpoints):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0] * p1[0], -p2[0] * p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1] * p1[0], -p2[1] * p1[1]])

    A = torch.tensor(matrix, dtype=torch.float)
    B = torch.tensor(startpoints, dtype=torch.float).view(8)
    res = torch.lstsq(B, A)[0]
    return res.squeeze_(1).tolist()


def perspective(img, startpoints, endpoints, interpolation=Image.BICUBIC):
    coeffs = _get_perspective_coeffs(startpoints, endpoints)
    return img.transform(img.size, Image.PERSPECTIVE, coeffs, interpolation)

def label_map(img, tabel, value=0):
    img = img.point(lambda x: tabel.get(x, value))
    return img

