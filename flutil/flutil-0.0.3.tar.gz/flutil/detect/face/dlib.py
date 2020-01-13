from .. import Detector
from .. import Detection, ShapeDetection
import dlib
import numpy as np
from typing import List
from pathlib import Path

FACE_MODEL = str(Path(__file__).parent / 'etc/mmod_human_face_detector.dat')
SHAPE_PRED_PATH = str(Path(__file__).parent
                      / 'etc/shape_predictor_5_face_landmarks.dat')


class DlibCnnDetector(Detector):
    """DLIB CNN implementation of a face detector."""

    def __init__(self, imgs=[]):
        super().__init__(imgs)
        self._detector = dlib.cnn_face_detection_model_v1(FACE_MODEL)

    def _desc2dets(self, desc: np.ndarray) -> List[Detection]:
        """Return the `Detection`s that correspond to the given descriptor.

        :param np.ndarray desc: the descriptor
        :rtype: List[Detection]
        :returns: the `Detection`s that correspond to the given descriptor
        """
        return [Detection(*det) for det in desc]

    def _get_descriptor(self, im: np.array) -> np.array:
        """Return the descriptor for an image.

        :param np.array im: the image array obtained by calling
        ``skimage.io.imread()`` with the image file path as an argument.
        """
        faces = self._detector(im, 1)
        return np.array([[face.rect.left(),
                          face.rect.right(),
                          face.rect.top(),
                          face.rect.bottom()]
                         for face in faces])


class DlibFrontDetector(Detector):
    """DLIB implementation of a frontal face detector."""

    def __init__(self, imgs=[]):
        super().__init__(imgs)
        self._detector = dlib.get_frontal_face_detector()

    def _desc2dets(self, desc: np.ndarray) -> List[Detection]:
        """Return the `Detection`s that correspond to the given descriptor.

        :param np.ndarray desc: the descriptor
        :rtype: List[Detection]
        :returns: the `Detection`s that correspond to the given descriptor
        """
        return [Detection(*det) for det in desc]

    def _get_descriptor(self, im: np.array) -> np.array:
        """Return the descriptor for an image.

        Either `_get_descriptor` or `_get_batch_descrs` should be implemented
        by child classes.

        :param np.array im: the image array obtained by calling
        ``skimage.io.imread()`` with the image file path as an argument.
        """
        faces = self._detector(im, 1)
        return np.array([[face.left(),
                          face.right(),
                          face.top(),
                          face.bottom()]
                         for face in faces])


class DlibFacePointsDetector(Detector):
    """DLIB implementation of a facial landmark detector."""

    def __init__(self, imgs=[]):
        super().__init__(imgs)
        self._shape_pred = dlib.shape_predictor(SHAPE_PRED_PATH)
        self._detector = DlibCnnDetector(imgs)

    def _desc2dets(self, desc: np.ndarray) -> List[Detection]:
        """Return the `Detection`s that correspond to the given descriptor.

        :param np.ndarray desc: the descriptor
        :rtype: List[Detection]
        :returns: the `Detection`s that correspond to the given descriptor
        """
        return [ShapeDetection(*det) for det in desc]

    def _get_descriptor(self, im: np.array) -> np.array:
        """Return the descriptor for an image.

        Either `_get_descriptor` or `_get_batch_descrs` should be implemented
        by child classes.

        :param np.array im: the image array obtained by calling
        ``skimage.io.imread()`` with the image file path as an argument.
        """
        dets = self._detector.get_detections()['detections']
        detections = []
        for det in dets:
            dlibdet = dlib.rectangle(left=det.left, right=det.right,
                                     top=det.top, bottom=det.bottom)
            shape = self._shape_pred(im, dlibdet)
            detections.append([[p.x, p.y]
                               for p in shape.parts()])
        return np.array(detections)
