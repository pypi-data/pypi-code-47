import math
import numbers
import random
from abc import ABCMeta, abstractmethod
from collections import Iterable
from functools import partial
from typing import List

import numpy as np
import torch

from . import functional as F


class Sequence:
    def __init__(self, transforms):
        if not isinstance(transforms, List):
            transforms = [transforms]
        self.transforms = transforms

    def __call__(self, data):
        for t in self.transforms:
            data = t(data)
        return data
    
    def __repr__(self):
        format_string = self.__class__.__name__ + '('
        for t in self.transforms:
            format_string += '\n'
            format_string += '    {0}'.format(t)
        format_string += '\n)'
        return format_string

class Shuffle:
    def __init__(self, transforms):
        if not isinstance(transforms, List):
            transforms = [transforms]
        self.transforms = transforms

    def __call__(self, data):
        random.shuffle(self.transforms)
        for t in self.transforms:
            data = t(data)
        return data

    def __repr__(self):
        format_string = self.__class__.__name__ + '('
        for t in self.transforms:
            format_string += '\n'
            format_string += '    {0}'.format(t)
        format_string += '\n)'
        return format_string

class Sample:
    def __init__(self, transforms, k=1):
        if not isinstance(transforms, List):
            transforms = [transforms]
        assert len(transforms) >= k
        self.transforms = transforms
        self.k = k

    def __call__(self, data):
        transforms = random.sample(self.transforms, k=self.k)
        for t in transforms:
            data = t(data)
        return data

    def __repr__(self):
        format_string = self.__class__.__name__ + '('
        for t in self.transforms:
            format_string += '\n'
            format_string += '    {0}'.format(t)
        format_string += '\n)'
        return format_string

class Transform(metaclass=ABCMeta):
    @abstractmethod
    def apply_image(self, img):
        pass

    def apply_mask(self, mask):
        raise NotImplementedError

    def apply_box(self, box):
        raise NotImplementedError

    def apply_kp(self, kp):
        raise NotImplementedError

    def __repr__(self):
        format_string = self.__class__.__name__
        return format_string

class ToTensor(Transform):
    def __call__(self, data):
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v)
        else:
            data = self.apply_image(data)
        return data

    def apply_image(self, img):
        return F.to_tensor(img)

    def apply_mask(self, mask):
        if isinstance(mask, List):
            return torch.stack([torch.as_tensor(np.asarray(m), dtype=torch.int64) for m in mask])
        return torch.as_tensor(np.asarray(mask), dtype=torch.int64)


class Normalize(Transform):
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, data):
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v)
        else:
            data = self.apply_image(data)
        return data
    
    def apply_image(self, img):
        return F.normalize(img, self.mean, self.std)

    def apply_mask(self, mask):
        return mask


class LabelMap(Transform):
    def __init__(self, table):
        table = {int(k):int(v) for k,v in table.items()}
        self.label_map = table

    def __call__(self, data):
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v)
        else:
            data = self.apply_image(data)
        return data
    
    def apply_image(self, img):
        return img

    def apply_mask(self, mask):
        if isinstance(mask, List):
            return mask
        return F.label_map(mask, self.label_map)

class Identity(Transform):
    def __call__(self, data):
        return data

    def apply_image(self, img):
        return img

class RandomHorizontalFlip(Transform):
    def __init__(self, p=0.5):
        self.p = p

    def __call__(self, data):
        if random.random() < self.p:
            if isinstance(data, dict):
                for k, v in data.items():
                    if v is not None:
                        data[k] = getattr(self, f'apply_{k}')(v)
            else:
                data = self.apply_image(data)
        return data

    def apply_image(self, img):
        return F.hflip(img)

    def apply_mask(self, mask):
        if isinstance(mask, List):
            return [F.hflip(m) for m in mask]
        return F.hflip(mask)


class RandomVerticalFlip(Transform):
    def __init__(self, p=0.5):
        self.p = p

    def __call__(self, data):
        if random.random() < self.p:
            if isinstance(data, dict):
                for k, v in data.items():
                    if v is not None:
                        data[k] = getattr(self, f'apply_{k}')(v)
            else:
                data = self.apply_image(data)
        return data

    def apply_image(self, img):
        return F.vflip(img)

    def apply_mask(self, mask):
        if isinstance(mask, List):
            return [F.vflip(m) for m in mask]
        return F.vflip(mask)


class RandomRotation(Transform):
    def __init__(self, degrees, interpolation='nearest', expand=False, center=None, fill=0):
        if isinstance(degrees, numbers.Number):
            if degrees < 0:
                raise ValueError(
                    "If degrees is a single number, it must be positive.")
            self.degrees = (-degrees, degrees)
        else:
            if len(degrees) != 2:
                raise ValueError(
                    "If degrees is a sequence, it must be of len 2.")
            self.degrees = degrees

        self.interpolation = interpolation
        self.expand = expand
        self.center = center
        self.fill = fill

    def __call__(self, data):
        degree = self.get_params(self.degrees)
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v, degree)
        else:
            data = self.apply_image(data, degree)
        return data

    @staticmethod
    def get_params(degrees):
        degree = random.uniform(degrees[0], degrees[1])
        return degree

    def apply_image(self, img, degree):
        return F.rotate(img, degree, self.interpolation, self.expand, self.center)

    def apply_mask(self, mask, degree):
        rotate = partial(F.rotate, degree=degree, interpolation='nearest',
                         expand=self.expand, center=self.center)
        if isinstance(mask, List):
            return [rotate(m) for m in mask]
        return rotate(mask)


class Resize(Transform):
    def __init__(self, size, interpolation='bilinear'):
        assert isinstance(size, int) or (
            isinstance(size, Iterable) and len(size) == 2)
        self.size = size
        self.interpolation = interpolation

    def __call__(self, data):
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v)
        else:
            data = self.apply_image(data)
        return data

    def apply_image(self, img):
        return F.resize(img, self.size, self.interpolation)

    def apply_mask(self, mask):
        resize = partial(F.resize, size=self.size, interpolation='nearest')
        if isinstance(mask, List):
            return [resize(m) for m in mask]
        return resize(mask)


class RandomResizedCrop(Transform):
    def __init__(self, size, scale=(0.08, 1.0), ratio=(3. / 4., 4. / 3.), interpolation='bilinear'):
        self.size = size
        self.scale = scale
        self.ratio = ratio
        self.interpolation = interpolation

    def __call__(self, data):
        if isinstance(data, dict):
            params = self.get_params(data['image'], self.scale, self.ratio)
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v, *params)
        else:
            params = self.get_params(data, self.scale, self.ratio)
            data = self.apply_image(data, *params)
        return data

    @staticmethod
    def get_params(img, scale, ratio):

        width, height = F.get_image_size(img)
        area = height * width

        for attempt in range(10):
            target_area = random.uniform(*scale) * area
            log_ratio = (math.log(ratio[0]), math.log(ratio[1]))
            aspect_ratio = math.exp(random.uniform(*log_ratio))

            w = int(round(math.sqrt(target_area * aspect_ratio)))
            h = int(round(math.sqrt(target_area / aspect_ratio)))

            if 0 < w <= width and 0 < h <= height:
                i = random.randint(0, height - h)
                j = random.randint(0, width - w)
                return i, j, h, w

        # Fallback to central crop
        in_ratio = float(width) / float(height)
        if (in_ratio < min(ratio)):
            w = width
            h = int(round(w / min(ratio)))
        elif (in_ratio > max(ratio)):
            h = height
            w = int(round(h * max(ratio)))
        else:  # whole image
            w = width
            h = height
        i = (height - h) // 2
        j = (width - w) // 2
        return i, j, h, w

    def apply_image(self, img, i, j, h, w):
        return F.resized_crop(img, i, j, h, w, self.size, self.interpolation)

    def apply_mask(self, mask, i, j, h, w):
        if isinstance(mask, List):
            return [F.resized_crop(m, i, j, h, w, self.size, 'nearest') for m in mask]
        return F.resized_crop(mask, i, j, h, w, self.size, 'nearest')


class RandomBright(Transform):
    def __init__(self, scale):
        if isinstance(scale, numbers.Number):
            scale = (1-scale, 1+scale)
        self.scale = scale

    def __call__(self, data):
        scale = random.uniform(*self.scale)
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v, scale)
        else:
            data = self.apply_image(data, scale)
        return data

    def apply_image(self, img, scale):
        return F.adjust_brightness(img, scale)

    def apply_mask(self, mask, scale):
        return mask


class RandomContrast(Transform):
    def __init__(self, scale):
        if isinstance(scale, numbers.Number):
            scale = (1-scale, 1+scale)
        self.scale = scale

    def __call__(self, data):
        scale = random.uniform(*self.scale)
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v, scale)
        else:
            data = self.apply_image(data, scale)
        return data

    def apply_image(self, img, scale):
        return F.adjust_contrast(img, scale)

    def apply_mask(self, mask, scale):
        return mask


class RandomSaturation(Transform):
    def __init__(self, scale):
        if isinstance(scale, numbers.Number):
            scale = (1-scale, 1+scale)
        self.scale = scale

    def __call__(self, data):
        scale = random.uniform(*self.scale)
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v, scale)
        else:
            data = self.apply_image(data, scale)
        return data

    def apply_image(self, img, scale):
        return F.adjust_saturation(img, scale)

    def apply_mask(self, mask, scale):
        return mask


class RandomHue(Transform):
    def __init__(self, scale):
        if isinstance(scale, numbers.Number):
            assert abs(scale) <= 0.5
            scale = (-scale, scale)
        self.scale = scale

    def __call__(self, data):
        scale = random.uniform(*self.scale)
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v, scale)
        else:
            data = self.apply_image(data, scale)
        return data

    def apply_image(self, img, scale):
        return F.adjust_hue(img, scale)

    def apply_mask(self, mask, scale):
        return mask


class RandomGamma(Transform):
    def __init__(self, scale, gain=1):
        if isinstance(scale, numbers.Number):
            scale = (1-scale, 1+scale)
        self.scale = scale
        self.gain = gain

    def __call__(self, data):
        scale = random.uniform(*self.scale)
        if isinstance(data, dict):
            for k, v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v, scale)
        else:
            data = self.apply_image(data, scale)
        return data

    def apply_image(self, img, scale):
        return F.adjust_gamma(img, scale, self.gain)

    def apply_mask(self, mask, scale):
        return mask


class RandomPerspective(object):
    def __init__(self, distortion_scale=0.5, p=0.5, interpolation='bicubic'):
        self.p = p
        self.interpolation = interpolation
        self.distortion_scale = distortion_scale

    def __call__(self, data):
        if isinstance(data, dict):
            height, width = F.get_image_size(data['image'])
            startpoints, endpoints = self.get_params(width, height, self.distortion_scale)
            for k,v in data.items():
                if v is not None:
                    data[k] = getattr(self, f'apply_{k}')(v, startpoints, endpoints)
        else:
            height, width = F.get_image_size(data)
            startpoints, endpoints = self.get_params(width, height, self.distortion_scale)
            data = self.apply_image(data, startpoints, endpoints)
        return data

    def apply_image(self, img, startpoints, endpoints):
        return F.perspective(img, startpoints, endpoints, self.interpolation)

    def apply_mask(self, mask, startpoints, endpoints):
        distort = partial(F.perspective, startpoints, endpoints, self.interpolation)
        if isinstance(mask, List):
            return [distort(m) for m in mask]
        return distort(mask)

    @staticmethod
    def get_params(width, height, distortion_scale):

        half_height = int(height / 2)
        half_width = int(width / 2)
        topleft = (random.randint(0, int(distortion_scale * half_width)),
                   random.randint(0, int(distortion_scale * half_height)))
        topright = (random.randint(width - int(distortion_scale * half_width) - 1, width - 1),
                    random.randint(0, int(distortion_scale * half_height)))
        botright = (random.randint(width - int(distortion_scale * half_width) - 1, width - 1),
                    random.randint(height - int(distortion_scale * half_height) - 1, height - 1))
        botleft = (random.randint(0, int(distortion_scale * half_width)),
                   random.randint(height - int(distortion_scale * half_height) - 1, height - 1))
        startpoints = [(0, 0), (width - 1, 0), (width - 1, height - 1), (0, height - 1)]
        endpoints = [topleft, topright, botright, botleft]
        return startpoints, endpoints

    def __repr__(self):
        return self.__class__.__name__
