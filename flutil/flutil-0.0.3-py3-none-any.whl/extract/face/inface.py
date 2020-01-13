import os.path
import numpy as np
import mxnet as mx
from ..mx import MxModExtractor
import logging
from ...detect import BoxShapeDetection
from ...detect import ShapeDetection, Detection
from sklearn.preprocessing import normalize
from skimage import transform
import cv2
from copy import deepcopy
from typing import List
import pandas as pd
from PIL import Image

IMAGE_INPUT_SIZE = (112, 112)

# DOWNLOAD MODEL FILES FROM HERE:
# https://github.com/deepinsight/insightface/wiki/Model-Zoo
MODEL_PREFIX = os.path.join(os.path.dirname(__file__),
                            'etc',
                            'model-r100-ii/model')


class InfaceExtractor(MxModExtractor):
    """Facial feature extrator based on InsightFace.

    See: https://github.com/deepinsight/insightface
    """
    def __init__(self, imgs, dets=None,
                 bs=1, model: str = None,
                 **kwargs):
        """
        :param Iterable[Union[str, Path, Image, np.ndarray]] imgs: an iterable
        of paths (type `str` or `pathlib.Path`) pointing to image files or an
        iterable of image objects (type `PIL.Image` or `np.ndarray`). When
        using a numpy array, The different color bands/channels should be
        stored in the third dimension, such that a gray-image is MxN, an
        RGB-image MxNx3 and an RGBA-image MxNx4.
        :param Iterable[Iterable[Box]] dets: the detections per image. More
        generally, the regions for which features will be extracted.
        :param int bs: (optional) batch size to process the images
        :param str model: (optional) mxnet model prefix
        :param kwargs: kwargs for MxModExtractor
        """
        if model is None:
            prefix = MODEL_PREFIX
        else:
            prefix = model

        epoch = 0
        ctx = mx.gpu(0)
        sym, arg_params, aux_params = mx.model.load_checkpoint(prefix, epoch)
        all_layers = sym.get_internals()
        sym = all_layers['fc1_output']
        mod = mx.mod.Module(symbol=sym, context=ctx, label_names=None)
        mod.bind(data_shapes=[('data', (bs, 3, 112, 112))])
        mod.set_params(arg_params, aux_params)

        def transform(img):
            img = mx.image.imresize(img, w=112, h=112)  # resize
            img = img.transpose((2,   # Channel
                                 0,   # Height
                                 1))  # Width
            return img
        super().__init__(imgs=imgs, dets=dets, model=mod, transform=transform,
                         bs=bs, **kwargs)

    @staticmethod
    def _landmark_warp(img, det: ShapeDetection):
        src = np.array([[30.2946, 51.6963],
                        [65.5318, 51.5014],
                        [48.0252, 71.7366],
                        [33.5493, 92.3655],
                        [62.7299, 92.2041]],
                       dtype=np.float32)
        src[:, 0] += 8.0

        dst = np.array([list(p) for p in det.points],
                       dtype=np.float32)
        tform = transform.SimilarityTransform()
        tform.estimate(dst, src)
        M = tform.params[0:2, :]
        warped = cv2.warpAffine(img, M, IMAGE_INPUT_SIZE)
        return warped

    @staticmethod
    def _crop_box(img, det: Detection, margin=44):
        det = deepcopy(det)
        height, width, _ = img.shape
        det.x_min = max(det.x_min - margin/2, 0)
        det.y_min = max(det.y_min - margin/2, 0)
        det.x_max = min(det.x_max + margin/2, width)
        det.y_max = min(det.y_max + margin/2, height)
        det = det.to_int()

        return img[det.y_min:det.y_max, det.x_min:det.x_max, :]

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
        imgs = []
        for index, row in batch.iterrows():
            detection = row['detection']
            img = np.array(Image.open(row['image']))
            if img.ndim != 3:
                logging.warning('Image has ndim != 3')
                return None

            if isinstance(detection, BoxShapeDetection):
                img = self._landmark_warp(img, detection.points)
            elif isinstance(detection, ShapeDetection):
                img = self._landmark_warp(img, detection)
            else:
                img = self._crop_box(img, detection)

            imgs.append(img)

        batch['nd_img'] = imgs

        # Get descriptor for the face and the flipped version of the face
        descrs_normal = super()._get_batch_descrs(batch)
        batch['nd_img'] = batch['nd_img'].apply(lambda img:
                                                img[:, ::-1, :])
        descrs_flipped = super()._get_batch_descrs(batch)

        # Combine and normalize the descriptors
        descrs = [norm + flip
                  for norm, flip in zip(descrs_normal, descrs_flipped)]
        return [normalize(descr[np.newaxis, :]).flatten()
                for descr in descrs]
