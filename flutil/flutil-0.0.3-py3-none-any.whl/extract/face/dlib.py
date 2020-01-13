"""A wrapper around the dlib face recognition."""
import dlib
from .. import Extractor
from ...detect import Detection
from ...shape import Box
import os
import numpy as np
import logging
from typing import List

# DOWNLOAD THE FILES FROM
# http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2
# http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2
SHAPE_PRED_PATH = os.path.join(os.path.dirname(__file__),
                               'etc',
                               'shape_predictor_5_face_landmarks.dat')
FACE_MODEL_PATH = os.path.join(os.path.dirname(__file__),
                               'etc',
                               'face_recognition_resnet_model_v1.dat')


class DlibFaceExtractor(Extractor):
    """DLIB implementation of face Descriptor."""
    def __init__(self, imgs: List[str]=[], dets: List[List[Detection]]=None,
                 aois=None, **kwargs):
        super().__init__(imgs=imgs, dets=dets, aois=aois, **kwargs)
        self._face_rec = dlib.face_recognition_model_v1(FACE_MODEL_PATH)
        self._shape_pred = dlib.shape_predictor(SHAPE_PRED_PATH)

    def _get_descriptor(self, img: np.array) -> np.array:
        if img.ndim != 3:
            logging.warning('Image has ndim != 3')
            return None

        box = Box.from_width_height(width=img.shape[1], height=img.shape[0])
        rect = dlib.rectangle(left=box.left,
                              right=box.right,
                              top=box.top,
                              bottom=box.bottom)
        shape = self._shape_pred(img, rect)
        return np.array(self._face_rec.compute_face_descriptor(img, shape))
