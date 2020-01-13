from typing import List
import tensorflow as tf
import numpy as np
from .. import Detector
from .. import BoxShapeDetection, Detection, ShapeDetection
from .etc.align import detect_face
import logging


class MTCNN(Detector):
    def __init__(self,
                 imgs=[], bs=1,
                 det_minsize=50,
                 det_threshold=[0.4, 0.6, 0.6],
                 det_factor=0.9, **kwargs):
        """MTCNN detector for face detection.

        :param Iterable[Union[str, Path, Image, np.ndarray]] imgs: the image
        paths
        :param int bs: the batch size
        :param int det_minsize: the minimum size of faces to detect
        :param List[float] det_threshold: the thresholds for the proposal net
        (pnet), refinement net (rnet) and further refinement / landmark
        positions net (onet)
        :param float det_factor: factor for creating the image pyramid
        :param kwargs: kwargs to pass to `Detector`
        """
        super().__init__(imgs=imgs, bs=bs, **kwargs)
        with tf.Graph().as_default():
            config = tf.ConfigProto()
            config.gpu_options.per_process_gpu_memory_fraction = 0.2
            sess = tf.Session(config=config)

            with sess.as_default():
                pnet, rnet, onet = detect_face.create_mtcnn(sess, None)

        self.pnet = pnet
        self.rnet = rnet
        self.onet = onet
        self.det_minsize = det_minsize
        self.det_threshold = det_threshold
        self.det_factor = det_factor

    def _desc2dets(self, desc: np.ndarray) -> List[Detection]:
        """Return the `Detection`s that correspond to the given descriptor.

        :param np.ndarray desc: the descriptor
        :rtype: List[Detection]
        :returns: the `Detection`s that correspond to the given descriptor
        """
        if not desc:
            return []

        raw_boxes, raw_points = desc
        if len(raw_boxes) != 0 and len(raw_points) != 0:
            points = [p for p in zip(raw_points[:5].T, raw_points[5:].T)]
            return [BoxShapeDetection(box_x_min=b[0],
                                      box_y_min=b[1],
                                      box_x_max=b[2],
                                      box_y_max=b[3],
                                      box_confidence=b[4],
                                      points_x=p[0],
                                      points_y=p[1])
                    for b, p in zip(raw_boxes, points)]
        elif len(raw_boxes) != 0:
            return [Detection(x_min, y_min, x_max, y_max, conf)
                    for (x_min, y_min, x_max, y_max, conf)
                    in raw_boxes]
        elif len(raw_points) != 0:
            return [ShapeDetection(xs=face_xs, ys=face_ys)
                    for face_xs, face_ys in zip(raw_points[:5].T,
                                                raw_points[5:].T)]
        else:
            return []

    def _get_batch_descrs(self, batch: List[np.array]) -> List[np.array]:
        """Return the descriptors for a batch of images.

        :param List[np.array] batch: a batch of images
        :returns: a list of descriptors for all the images in the batch
        """
        if not len(batch) > 0:
            return []

        first_im = batch.iloc[0]['nd_img']
        if len(first_im.shape) == 3:
            h, w, _ = batch.iloc[0]['nd_img'].shape
        else:
            logging.warning('Dropped batch because number of channels '
                            'in image != 3')
            return []
        det_win_ratio = self.det_minsize / min(w, h)
        descrs = detect_face.bulk_detect_face(batch['nd_img'],
                                              det_win_ratio,
                                              self.pnet,
                                              self.rnet,
                                              self.onet,
                                              self.det_threshold,
                                              self.det_factor)
        return descrs
