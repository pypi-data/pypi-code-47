import os

import cv2
import numpy as np
import seaborn as sns

from msk_seg_util.util.io_util import mkdirs


class MultiClassOverlay(object):
    """This class overlays masks on volumes.

    Args:
        num_classes (int): Number of classes, including background.
        color_palette: Sequence of ``(r,g,b)`` colors. Defaults to ``sns.color_palette('bright')``.
            For example, ``[(0.5, 0, 0), (0.11, 0.45, 0.67)]``.
        background_label (int): Voxels with this value will be designated as background. Either ``0`` or ``None``.
            To include color for background, set to ``None``. Defaults to ``0``.
        opacity (float): Color overlay opacity. Must be in interval ``[0, 1]``. Defaults to ``0.7``.

    Attributes:
        num_classes (int): Number of classes, including background.
        background_label (int): Voxels with this value will be designated as background. Either ``0`` or ``None``.
        opacity (float): Color overlay opacity.
    """

    def __init__(self, num_classes,
                 color_palette=None,
                 background_label=0,
                 opacity=0.7):
        effective_num_classes = num_classes - 1 if background_label is not None else num_classes
        color_palette = sns.color_palette("bright") if color_palette is None else color_palette

        if len(color_palette) < effective_num_classes:
            raise ValueError("Must provide at least {} colors".format(effective_num_classes))

        if opacity < 0 or opacity > 1:
            raise ValueError("`opacity` must be in range [0, 1]")

        self.num_classes = num_classes
        self.background_label = background_label
        self.opacity = opacity

        # set colormap
        color_palette = color_palette
        colormap = dict()
        cp_ind = 0
        for i in range(num_classes):
            if i == background_label:
                continue
            cp_ind += 1
            colormap[i] = color_palette[cp_ind]
        self.colormap = colormap

    def overlay(self, volume: np.ndarray, masks: np.ndarray, save_path: str = None):
        """Overlay volume with labels.

        Voxels labeled as multiple classes will be colored with the last corresponding class in the ``masks`` array.
        To avoid this, make sure voxels are one-hot-encoded and have no overlap between masks.

        Args:
            volume (:obj:`np.ndarray`): 3D volume that will be colored. Must be grayscale.
            masks (:obj:`np.ndarray`): 4D binary mask with shape ``[Y, X, Z, # classes]``.
            save_path (:obj:`str`, optional): If specified, 2D images will be saved to directory.

        Returns:
            :obj:`np.ndarray`: 3D colored volume.
        """
        if volume.ndim != 3:
            raise ValueError("Volume must be 3D array with shape [Y, X, Z].")
        if masks.ndim != 4:
            raise ValueError("Masks must be 4D binary array with shape [Y, X, Z, classes].")

        # Labels are argmax(masks) in the class dimension.
        labels = self._masks_to_labels(masks)
        labels_colored = self._apply_colormap(labels)

        vol_rgb = np.zeros(volume.shape + (3,))
        for z in range(volume.shape[-1]):
            x_im = volume[..., z]
            label_overlay = labels_colored[..., z, :]

            slice_name = '%03d.png' % (z + 1)

            filepath = os.path.join(mkdirs(save_path), slice_name) if save_path is not None else None
            im_rgb = self._im_overlay(x_im, label_overlay, filepath)
            vol_rgb[..., z, :] = im_rgb

        return vol_rgb

    def _masks_to_labels(self, masks: np.ndarray):
        """Convert 4D masks to 3D label array.

        Args:
            masks (:obj:`np.ndarray`): 4D binary mask with shape ``(Y, X, Z, N)``.
                ``N`` corresponds to number of classes.

        Returns:
            np.ndarray: 3D array of class ids.

            Voxels values corresponding to class id. Non-background classes are 1-indexed. ``0`` corresponds to
            background voxel.
        """
        assert masks.ndim == 4, "Masks must be 4D binary array with shape (Y, X, Z, # classes)"
        masks = np.array(masks)
        for i in range(0, masks.shape[-1]):
            masks[..., i] *= (i + 1)

        return np.max(masks, axis=-1)

    def _apply_colormap(self, labels: np.ndarray):
        """Converts labels into color array.

        Args:
            labels (:obj:`np.ndarray`): 3D array of class ids.
        """
        colormap = self.colormap
        background_label = self.background_label

        labels_colored = np.zeros(labels.shape + (3,))

        for c in np.unique(labels):
            if c == background_label:
                continue

            labels_colored[labels == c, :] = colormap[c]

        return (labels_colored * 255).astype(np.uint8)

    def _im_overlay(self, x: np.ndarray, c_label: np.ndarray, out_file: str=None):
        """Color 2D grayscale image with labels.

        Args:
            x (:obj:`np.ndarray`): 2D grayscale image with shape ``(Y, X)``.
            c_label (:obj:`np.ndarray`): 2D rgb image with shape ``(Y, X, C)``.
            out_file (:obj:`str`, optional): If specified, image written to file.

        Returns:
            np.ndarray: 2D rgb image. Type: uint8.
        """
        x_o = scale_img(np.squeeze(x))
        x_rgb = np.stack([x_o, x_o, x_o], axis=-1).astype(np.uint8)
        overlap_img = cv2.addWeighted(x_rgb, 1, c_label, self.opacity, 0)

        if out_file:
            cv2.imwrite(out_file, cv2.cvtColor(overlap_img, cv2.COLOR_RGB2BGR))

        return overlap_img.astype(np.uint8)


def write_sep_im_overlay(dir_path, xs, y_true, y_pred):
    """Overlap input (xs) with mask (im_overlap) and save to directory.

    :param dir_path: path to directory to save images
    :param xs: inputs
    :param im_overlay: overlay images
    """
    correct_dir_path = mkdirs(os.path.join(dir_path, 'true_pos'))
    error_dir_path = mkdirs(os.path.join(dir_path, 'error'))
    num_slices = xs.shape[0]
    for i in range(num_slices):
        x = scale_img(np.squeeze(xs[i, ...]))
        x = np.stack([x, x, x], axis=-1).astype(np.uint8)
        im_correct, im_error = generate_sep_ovlp_image(y_true[i, ...], y_pred[i, ...])

        slice_name = '%03d.png' % i

        overlap_img_correct = cv2.addWeighted(x, 1, im_correct, 1.0, 0)
        cv2.imwrite(os.path.join(correct_dir_path, slice_name), overlap_img_correct)

        overlap_img_error = cv2.addWeighted(x, 1, im_error, 1.0, 0)
        cv2.imwrite(os.path.join(error_dir_path, slice_name), overlap_img_error)


def generate_sep_ovlp_image(y_true, y_pred):
    """
    TODO: write comment
    :param y_true: numpy array of ground truth labels
    :param y_pred: numpy array of predicted labels
    :return: a BGR image
    """
    assert (y_true.shape == y_pred.shape)
    assert len(y_true.shape) == 2, "shape should be 2d, but is " + y_true.shape

    y_true = y_true.astype(np.bool)
    y_pred = y_pred.astype(np.bool)

    TP = y_true * y_pred
    FN = y_true * (~y_pred)
    FP = (~y_true) * y_pred

    # BGR format
    img_corr = np.stack([np.zeros(TP.shape), TP, np.zeros(TP.shape)], axis=-1).astype(np.uint8) * 255
    img_err = np.stack([FP, np.zeros(TP.shape), FN], axis=-1).astype(np.uint8) * 255

    return (img_corr, img_err)


def write_ovlp_masks(dir_path, y_true, y_pred):
    """
    Overlap ground truth with prediction and save to directory
    Red - false negative
    Green - true positive
    Blue - false negative
    :param dir_path: path to directory
    :param y_true: numpy array of ground truth labels
    :param y_pred: numpy array of predicted labels
    """
    dir_path = mkdirs(dir_path)
    y_true = np.squeeze(y_true)
    y_pred = np.squeeze(y_pred)

    assert (y_true.shape == y_pred.shape)
    ims = []
    num_slices = y_true.shape[0]
    for i in range(num_slices):
        slice_true = y_true[i, :, :]
        slice_pred = y_pred[i, :, :]
        img = make_accuracy_map(slice_true, slice_pred)
        ims.append(img)

        slice_name = '%03d.png' % i
        cv2.imwrite(os.path.join(dir_path, slice_name), img)

    return ims


def write_mask(dir_path, y_true):
    """
    Save ground truth mask to directory
    :param dir_path: path to directory
    :param y_true: numpy array of ground truth labels
    """
    dir_path = mkdirs(dir_path)
    y_true = np.squeeze(y_true) * 255
    num_slices = y_true.shape[0]
    for i in range(num_slices):
        slice_name = '%03d.png' % i
        cv2.imwrite(os.path.join(dir_path, slice_name), y_true[i, :, :])


def write_prob_map(dir_path, y_probs):
    """
    Write probablity map for prediction as image (colormap jet)
    :param dir_path: path to directory
    :param y_probs: numpy array of prediction probabilities
    """
    dir_path = mkdirs(dir_path)
    y_probs = np.squeeze(y_probs)
    num_slices = y_probs.shape[0]
    for i in range(num_slices):
        slice_name = '%03d.png' % i
        im = y_probs[i, :, :] * 255
        im = im[..., np.newaxis].astype(np.uint8)
        imC = cv2.applyColorMap(im, cv2.COLORMAP_HOT)
        cv2.imwrite(os.path.join(dir_path, slice_name), imC)


def scale_img(im, scale=255):
    """
    Scale image from 0-scale
    :param im: input image
    :param scale: max value
    :return:
    """
    im = im.astype(np.float32)
    im = im - np.min(im)
    im = im / np.max(im)
    im *= scale

    return im


def make_accuracy_map(y_true: np.ndarray, y_pred: np.ndarray, only_err: bool = False):
    """Make rgb map of true positives, false positives, and false negatives.

    True positives are green, false positives are red, false negatives are blue.

    Args:
        y_true (:obj:`np.ndarray`): Ground truth binary mask(s).
        y_pred (:obj:`np.ndarray`): Prediction binary mask(s).
        only_err (:obj:`bool`, optional): Only map errors - false positives and false negatives.
            Defaults to ``False``.

    Returns:
        :obj:`np.ndarray`: A rgb array. Will have extra channel dimension.
    """
    if y_true.shape != y_pred.shape:
        raise ValueError("`y_true` and `y_pred` must have same shapes")
    assert len(y_true.shape) == 2, "shape should be 2d, but is {}".format(y_true.shape)

    y_true = y_true.astype(np.bool)
    y_pred = y_pred.astype(np.bool)

    TP = np.zeros(y_true.shape) if only_err else y_true & y_pred
    FN = y_true & (~y_pred)
    FP = (~y_true) & y_pred

    # RGB format.
    img = np.stack([FP, TP, FN], axis=-1).astype(np.uint8)

    return img
