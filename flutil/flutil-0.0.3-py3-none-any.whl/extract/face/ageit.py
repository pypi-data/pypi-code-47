"""A wrapper around the face_recognition from ageitgey."""

from .. import Extractor
from face_recognition import api
import numpy as np
import logging
from ...shape import Box


class GeitgeyFaceExtractor(Extractor):
    """Adam Geitgey implementation of face recognition."""

    def _get_descriptor(self, img: np.array) -> np.array:
        # Bounding box in CSS order (top, right, bottom, left)
        box = Box.from_width_height(*img.shape[::-1])
        encodings = api.face_encodings(img, [box.css])
        try:
            return encodings[0]
        except IndexError as e:
            logging.error(f'It was impossible to encode detection '
                          f'with shape {img.shape}.')
