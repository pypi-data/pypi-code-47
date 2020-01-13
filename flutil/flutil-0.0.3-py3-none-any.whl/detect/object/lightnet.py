from .. import Detector
from .. import ObjectDetection, Detection
from torchvision import transforms as tf
import lightnet as ln
from lightnet.data import transform as lntf
import torch
import numpy as np
from typing import List
from skimage import img_as_ubyte


class YoloV3(Detector):
    def __init__(self, imgs, weights, bs=1, conf_thresh=0.5, class_label_map=None,
                 network_size=[416, 416], **kwargs):
        super().__init__(imgs=imgs, bs=bs)
        self._net = ln.models.YoloV3(**kwargs)
        self._net.eval()
        self._conf_thresh = conf_thresh
        self._cl_map = class_label_map
        self.network_size = network_size

        if torch.cuda.is_available():
            self._net = self._net.to('cuda')

        self._net.load(weights)
        self._post = lntf.Compose([
            lntf.GetMultiScaleBoundingBoxes(anchors=self._net.anchors,
                                            num_classes=self._net.num_classes,
                                            conf_thresh=self._conf_thresh),
            lntf.NonMaxSupression(nms_thresh=0.5),
            lntf.TensorToBrambox(network_size=self.network_size,
                                 class_label_map=self._cl_map)])

    def _get_descriptor(self, im: np.array) -> np.array:
        """Return the descriptor for an image.

        :param np.array im: the image array obtained by calling
        ``skimage.io.imread()`` with the image file path as an argument.
        """
        img = img_as_ubyte(im)
        im_h, im_w = img.shape[:2]
        img_tf = lntf.Letterbox.apply(img, dimension=self.network_size)
        img_tf = tf.ToTensor()(img_tf)
        img_tf.unsqueeze_(0)

        if torch.cuda.is_available():
            img_tf = img_tf.to('cuda')

        # Run detector
        with torch.no_grad():
            out = self._net(img_tf)
            out = [o.to('cpu') for o in out]

        out = self._post(out)

        # Resize bb to true image dimensions
        out = lntf.ReverseLetterbox.apply(out,
                                          network_size=self.network_size,
                                          image_size=(im_w, im_h))
        return out

    def _desc2dets(self, desc: np.ndarray) -> List[Detection]:
        """Return the `Detection`s that correspond to the given descriptor.

        :param np.ndarray desc: the descriptor
        :rtype: List[Detection]
        :returns: the `Detection`s that correspond to the given descriptor
        """
        return [ObjectDetection(x_min=obj.x_top_left,
                                x_max=obj.x_top_left + obj.width,
                                y_min=obj.y_top_left,
                                y_max=obj.y_top_left + obj.height,
                                confidence=obj.confidence,
                                label=obj.class_label)
                for obj in desc[0]]
