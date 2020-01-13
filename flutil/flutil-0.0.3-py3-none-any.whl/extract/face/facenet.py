"""A wrapper around facenet"""
from .. import Extractor
from ...shape import Box
from ...detect import Detection
from typing import List
import numpy as np
from scipy import misc
from .etc.facenet.contributed import face


class FacenetExtractor(Extractor):
    """Facenet implementation of a face Descriptor."""

    def __init__(self, imgs: List[str],
                 dets: List[List[Detection]],
                 aois: List[List[Box]], **kwargs):
        super().__init__(imgs=imgs, dets=dets, aois=aois, **kwargs)
        self._encoder = face.Encoder()

    def _get_descriptor(self, img: np.array) -> np.array:
        # Make sure it is RGB
        if img.ndim != 3:
            return None

        img_face = face.Face()
        img_face.container_image = img
        img_face.bounding_box = np.zeros(4, dtype=np.int32)

        box = Box.from_width_height(*img.shape[::-1])
        img_face.bounding_box[0] = int(box.x_min)
        img_face.bounding_box[1] = int(box.y_min)
        img_face.bounding_box[2] = int(box.x_max)
        img_face.bounding_box[3] = int(box.y_max)

        cropped = img[box.y_min:box.y_max,
                      box.x_min:box.x_max]
        img_face.image = misc.imresize(cropped,
                                       (self.detect.face_crop_size,
                                        self.detect.face_crop_size),
                                       interp='bilinear')

        return self._encoder.generate_embedding(img_face)
