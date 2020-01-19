import torch 
import torchvision.transforms as transforms
from torch.utils.data.sampler import Sampler

import numpy as np
import skimage
import random

class RectangularCropTfm(object):
    """ Rectangular Image transforms as told in fastai library
    """
    def __init__(self, idx2ar, target_size):
        self.idx2ar, self.target_size = idx2ar, target_size

    def __call__(self, img):
        target_ar = self.idx2ar[idx]
        if target_ar < 1: 
            w = int(self.target_size/target_ar)
            size = (w//8*8, self.target_size)
        else: 
            h = int(self.target_size*target_ar)
            size = (self.target_size, h//8*8)
        return transforms.functional.center_crop(img, size)
    
    
class MyResizer(object):
    """Convert ndarrays in sample to Tensors."""
    def __init__(self, min_side=224, max_side=512):
        self.min_side = min_side
        self.max_side = max_side

    def __call__(self, image):
        image= image['image']

        rows, cols, cns = image.shape

        smallest_side = min(rows, cols)

        # rescale the image so the smallest side is min_side
        scale = self.min_side / smallest_side

        # check if the largest side is now greater than max_side, which can happen
        # when images have a large aspect ratio
        largest_side = max(rows, cols)

        if largest_side * scale > self.max_side:
            scale = max_side / largest_side

        # resize the image with the computed scale
        image = skimage.transform.resize(image, (int(round(rows*scale)), int(round((cols*scale)))),
                                        anti_aliasing=True, mode="constant")#, mode='constant', anti_aliasing=False)
        rows, cols, cns = image.shape

        pad_w = 32 - rows%32
        pad_h = 32 - cols%32

        new_image = np.zeros((rows + pad_w, cols + pad_h, cns)).astype(np.float32)
        new_image[:rows, :cols, :] = image.astype(np.float32)

        return {"image": torch.from_numpy(new_image), "scale":scale} 
    
class Normalizer(object):

    def __init__(self, mean = [0.485, 0.456, 0.406],
                std = [0.229, 0.224, 0.225]):
        self.mean = np.array([[mean]])
        self.std = np.array([[std]])

    def __call__(self, image):

        image = image['image']
        return {'image':((image.astype(np.float32)-self.mean)/self.std)}
    

class UnNormalizer(object):
    def __init__(self, mean=None, std=None):
        if mean == None:
            self.mean = [0.485, 0.456, 0.406]
        else:
            self.mean = mean
        if std == None:
            self.std = [0.229, 0.224, 0.225]
        else:
            self.std = std

    def __call__(self, tensor):
        """
        Args:
            tensor (Tensor): Tensor image of size (C, H, W) to be normalized.
        Returns:
            Tensor: Normalized image.
        """
        for t, m, s in zip(tensor, self.mean, self.std):
            t.mul_(s).add_(m)
        return tensor

def collater(data):

    imgs = [s['img'] for s in data]
    scales = [s['scale'] for s in data]
    labels = [s["label"] for s in data]
        
    widths = [int(s.shape[0]) for s in imgs]
    heights = [int(s.shape[1]) for s in imgs]
    batch_size = len(imgs)

    max_width = np.array(widths).max()
    max_height = np.array(heights).max()

    padded_imgs = torch.zeros(batch_size, max_width, max_height, 3)

    for i in range(batch_size):
        img = imgs[i]
        padded_imgs[i, :int(img.shape[0]), :int(img.shape[1]), :] = img
    

    padded_imgs = padded_imgs.permute(0, 3, 1, 2)
    labels = torch.cat([i.view(1, -1) for i in labels])

    return {'img': padded_imgs, 'scale': scales, "label": labels}


class AspectRatioBasedSampler(Sampler):

    def __init__(self, data_source, batch_size, drop_last):
        self.data_source = data_source
        self.batch_size = batch_size
        self.drop_last = drop_last
        self.groups = self.group_images()

    def __iter__(self):
        random.shuffle(self.groups)
        for group in self.groups:
            yield group

    def __len__(self):
        if self.drop_last:
            return len(self.data_source) // self.batch_size
        else:
            return (len(self.data_source) + self.batch_size - 1) // self.batch_size

    def group_images(self):
        # determine the order of the images
        order = list(range(len(self.data_source)))
        order.sort(key=lambda x: self.data_source.image_aspect_ratio(x))

        # divide into groups, one group = one batch
        return [[order[x % len(order)] for x in range(i, i + self.batch_size)] for i in range(0, len(order), self.batch_size)]