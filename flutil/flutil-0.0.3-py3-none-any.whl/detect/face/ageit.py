from face_recognition import api
from .. import Detector, Detection
import numpy as np


class AgeitFaceDetector(Detector):
    def _desc2det(self, desc: np.ndarray) -> Detection:
        return Detection(x_min=desc[3],  # left
                         x_max=desc[1],  # right
                         y_min=desc[0],  # top
                         y_max=desc[2])  # bottom

    def _get_descriptor(self, im: np.array) -> np.array:
        return api.face_locations(im)
