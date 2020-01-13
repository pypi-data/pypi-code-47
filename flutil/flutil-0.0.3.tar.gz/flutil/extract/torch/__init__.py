from typing import List, Union, Iterable
from pathlib import Path
import torch
from torch.nn import Module
from torch.autograd import Variable
import numpy as np
from PIL import Image
from torchvision import transforms

from .. import Extractor


class TorchModuleExtractor(Extractor):
    """An ``Extractor`` using trained PyTorch ``nn.Module``s.

    :param Iterable[Union[str, Path, Image.Image, np.ndarray]] imgs: an
    iterable of paths (type `str` or `pathlib.Path`) pointing to image
    files or an iterable of image objects (type `PIL.Image.Image` or
    `np.ndarray`).  When using a numpy array, The different color
    bands/channels should be stored in the third dimension, such that a
    gray-image is MxN, an RGB-image MxNx3 and an RGBA-image MxNx4.

    :param Module model: the PyTorch ``nn.Module`` to use.
    :param int bs: (optional) batch size to process the images
    :param transform: (optional) callable that tranforms an image into the
    desired format to feed into the module.
    :param kwargs: kwargs for `Extractor` class
    """
    def __init__(self, imgs: Iterable[Union[str, Path, Image.Image,
                                            np.ndarray]],
                 model: Module, bs: int = 1, transform=None, **kwargs):
        super().__init__(imgs=imgs, bs=bs, **kwargs)

        if torch.cuda.is_available():
            self.model = model.cuda()

        self.model.train(False)

        for param in self.model.parameters():
            param.requires_grad = False
        self.transform = transform

    def _get_batch_descrs(self, batch: List[np.array]) -> List[np.array]:
        """Return the descriptors for a batch of images.

        Either `_get_descriptor` or `_get_batch_descrs` should be implemented
        by child classes.

        :param List[np.array] batch: a batch of images
        :returns: a list of descriptors for all the images in the batch
        """
        imgs = [Image.fromarray(img) for img in batch['nd_img']]

        if self.transform is not None:
            imgs = [self.transform(img) for img in imgs]

        inputs = torch.stack([transforms.ToTensor()(img) for img in imgs])

        if torch.cuda.is_available():
            inputs = Variable(inputs.cuda())
            return list(self.model(inputs).data.cpu().numpy())
        else:
            inputs = Variable(inputs)
            return list(self.model(inputs).data.numpy())
