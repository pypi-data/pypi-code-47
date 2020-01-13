"""Module providing an implementation with an mxnet backend."""
from typing import List
import mxnet as mx
from mxnet.module.base_module import BaseModule
import numpy as np
from .. import Extractor
import pandas as pd


class MxModExtractor(Extractor):
    """An ``Extractor`` using trained mxnet models.

    :param Module model: the mxnet model to use.
    :param transform: callable that tranforms an image into the desired format
    to feed into the module.
    :param kwargs: kwargs for `Extractor` class
    """
    def __init__(self, model: BaseModule, transform=None, **kwargs):
        super().__init__(**kwargs)

        self.model = model
        self.transform = transform

    def _get_batch_descrs(self, batch: pd.DataFrame) -> List[np.array]:
        """Return the descriptors for a batch of images.

        Either `_get_descriptor` or `_get_batch_descrs` should be implemented
        by child classes.

        :param pd.DataFrame batch: a `DataFrame` representing a batch. Its
        images as nd arrays are in a column named `nd_img`. The column `image`
        contains the path to the original image. Optionally the batch
        `DataFrame` can also contain columns `detection` and `aoi`.
        :returns: a list of descriptors for all the images in the batch
        """
        imgs = [mx.nd.array(img) for img in batch['nd_img']]

        if self.transform:
            imgs = [self.transform(img) for img in imgs]

        if len(imgs) == 0:
            return []
        imgs = mx.nd.stack(*imgs)
        self.model.forward(mx.io.DataBatch(data=[imgs]), is_train=False)
        return list(self.model.get_outputs()[0].asnumpy())
