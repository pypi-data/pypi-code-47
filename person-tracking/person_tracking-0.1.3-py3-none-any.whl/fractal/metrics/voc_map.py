from collections import defaultdict 

import numpy as np 
import six
from ..anchors.utils import bbox_iou

class Voc_mAP:
    """ Extracts the ground truth objects and prediction objects from respective files and align them on per image basis. 
    """
    def __init__(self, actual_file_loc, predicted_file_loc, labels_loc):
        self.actual_file_loc = actual_file_loc
        self.predicted_file_loc = predicted_file_loc
        self.labels_loc = labels_loc
        #self.type= type #image wise or category wise
        
        self._gts= self.load_datasets(self.actual_file_loc)
        self._dts= self.load_datasets(self.predicted_file_loc, "dt")
        
        self.pred_bboxes = list()
        self.pred_labels = list()
        self.pred_scores = list()
        self.gt_bboxes = list()
        self.gt_labels = list()
        
        
    def load_datasets(self, loc, gt_or_dt ="gt"):
        if isinstance(loc, str):
            with open(loc) as f:
                lines = f.readlines()
        elif isinstance(loc,list):
            lines=loc
        else:
            print ("issue in mAP code.")
    
        data = {}
        for line in lines:
            splited = line.strip().split(' ')
            if gt_or_dt == "dt":
                num_boxes = (len(splited) - 1)//6
            else:
                num_boxes = (len(splited) - 1)//5
            box = []
            label = []
            if gt_or_dt == "dt":
                score = []
            for i in range(num_boxes):
                if gt_or_dt == "dt":
                    ymin = splited[1+6*i]
                    xmin = splited[2+6*i]
                    ymax = splited[3+6*i]
                    xmax = splited[4+6*i]
                    c = int(splited[5+6*i])
                    s = splited[6+6*i]
                else:
                    ymin = splited[1+5*i]
                    xmin = splited[2+5*i]
                    ymax = splited[3+5*i]
                    xmax = splited[4+5*i]
                    c = int(splited[5+5*i]) 
                box.append([float(ymin), float(xmin), float(ymax), float(xmax)])
                label.append(c)
                if gt_or_dt == "dt":
                    score.append(float(s))
            if gt_or_dt == "dt":
                data[splited[0]] = [np.asarray(box), np.asarray(label), np.asarray(score)]
            else:
                data[splited[0]] = [np.asarray(box), np.asarray(label)]
        return data
    
    def cal_mAP(self, iou_thresh=0.5, use_07_metric=False):
        imgs_list = list(self._dts.keys())
        
        for i in imgs_list:
            if i not in self._dts.keys():
                raise ValueError('Not all the images in the test are predicted. Please check once again.')
        
        if len(self.pred_bboxes) == 0:
            for i in imgs_list:
                pb, pl, ps = self._dts[i]
                gb, gl = self._gts[i]
                gl = gl-1
                self.pred_bboxes.append(pb)
                self.pred_labels.append(pl)
                self.pred_scores.append(ps)
                self.gt_bboxes.append(gb)
                self.gt_labels.append(gl)
        
        return eval_detection_voc(self.pred_bboxes,
                                 self.pred_labels,
                                 self.pred_scores,
                                 self.gt_bboxes,
                                 self.gt_labels,
                                 iou_thresh=iou_thresh,
                                 use_07_metric=use_07_metric)
    
def eval_detection_voc(pred_bboxes, 
                       pred_labels, 
                       pred_scores, 
                       gt_bboxes, 
                       gt_labels, 
                       iou_thresh=0.5, 
                       use_07_metric=False):
    """ Calculate the Average precision of each object class and the mean Average precision of all the cass
    Args:
        pred_bboxes: A list of arrays, where each array represents the bboxes predicted for each image
        pred_labels: A list of arrays, where each array represents the corresponding labels for the predicted pred_bboxes 
        pred_scores: A list of arrays, where each array represents the corresponding probability scores for the predicted labels
        gt_boxes: A list of arrays, where each array represents the ground truth bboxes for each image 
        gt_labels: A list of arrays, where each array represents the corresponing labels for the ground truth bboxes 
        iou_thresh: minimum threshold required to consider this as an image 
        use_07_metric: Weather to use the evaluation metric discussed in the VOC evaluation paper [1]. Default false.

    Returns:
            A dict:  AP: average precision of each object 
                    mAP: mean average precision of all the objects 
    """

    prec, rec = calc_detection_voc_prec_rec(
    pred_bboxes, pred_labels, pred_scores,
    gt_bboxes, gt_labels,
    iou_thresh=iou_thresh)

    ap = calc_detection_voc_ap(prec, rec, use_07_metric=use_07_metric)

    return {'ap': ap, 'map': np.nanmean(ap)}

    
    

def calc_detection_voc_prec_rec(
        pred_bboxes, pred_labels, pred_scores, gt_bboxes, gt_labels,
        iou_thresh=0.5):
    """Calculate precision and recall based on evaluation code of PASCAL VOC.
    This function calculates precision and recall of
    predicted bounding boxes obtained from a dataset which has :math:`N`
    images.
    The code is based on the evaluation code used in PASCAL VOC Challenge.
    Args:
        pred_bboxes (iterable of numpy.ndarray): An iterable of :math:`N`
            sets of bounding boxes.
            Its index corresponds to an index for the base dataset.
            Each element of :obj:`pred_bboxes` is a set of coordinates
            of bounding boxes. This is an array whose shape is :math:`(R, 4)`,
            where :math:`R` corresponds
            to the number of bounding boxes, which may vary among boxes.
            The second axis corresponds to
            :math:`y_{min}, x_{min}, y_{max}, x_{max}` of a bounding box.
        pred_labels (iterable of numpy.ndarray): An iterable of labels.
            Similar to :obj:`pred_bboxes`, its index corresponds to an
            index for the base dataset. Its length is :math:`N`.
        pred_scores (iterable of numpy.ndarray): An iterable of confidence
            scores for predicted bounding boxes. Similar to :obj:`pred_bboxes`,
            its index corresponds to an index for the base dataset.
            Its length is :math:`N`.
        gt_bboxes (iterable of numpy.ndarray): An iterable of ground truth
            bounding boxes
            whose length is :math:`N`. An element of :obj:`gt_bboxes` is a
            bounding box whose shape is :math:`(R, 4)`. Note that the number of
            bounding boxes in each image does not need to be same as the number
            of corresponding predicted boxes.
        gt_labels (iterable of numpy.ndarray): An iterable of ground truth
            labels which are organized similarly to :obj:`gt_bboxes`.
        gt_difficults (iterable of numpy.ndarray): An iterable of boolean
            arrays which is organized similarly to :obj:`gt_bboxes`.
            This tells whether the
            corresponding ground truth bounding box is difficult or not.
            By default, this is :obj:`None`. In that case, this function
            considers all bounding boxes to be not difficult.
        iou_thresh (float): A prediction is correct if its Intersection over
            Union with the ground truth is above this value..
    Returns:
        tuple of two lists:
        This function returns two lists: :obj:`prec` and :obj:`rec`.
        * :obj:`prec`: A list of arrays. :obj:`prec[l]` is precision \
            for class :math:`l`. If class :math:`l` does not exist in \
            either :obj:`pred_labels` or :obj:`gt_labels`, :obj:`prec[l]` is \
            set to :obj:`None`.
        * :obj:`rec`: A list of arrays. :obj:`rec[l]` is recall \
            for class :math:`l`. If class :math:`l` that is not marked as \
            difficult does not exist in \
            :obj:`gt_labels`, :obj:`rec[l]` is \
            set to :obj:`None`.
    """

    pred_bboxes = iter(pred_bboxes)
    pred_labels = iter(pred_labels)
    pred_scores = iter(pred_scores)
    gt_bboxes = iter(gt_bboxes)
    gt_labels = iter(gt_labels)

    n_pos = defaultdict(int)
    score = defaultdict(list)
    match = defaultdict(list)

    for pred_bbox, pred_label, pred_score, gt_bbox, gt_label in \
            six.moves.zip(
                pred_bboxes, pred_labels, pred_scores,
                gt_bboxes, gt_labels):


        for l in np.unique(np.concatenate((pred_label, gt_label)).astype(int)):
            pred_mask_l = pred_label == l
            pred_bbox_l = pred_bbox[pred_mask_l]
            pred_score_l = pred_score[pred_mask_l]
            # sort by score
            order = pred_score_l.argsort()[::-1]
            pred_bbox_l = pred_bbox_l[order]
            pred_score_l = pred_score_l[order]

            gt_mask_l = gt_label == l
            gt_bbox_l = gt_bbox[gt_mask_l]
            
            n_pos[l] += gt_bbox_l.shape[0]
            score[l].extend(pred_score_l)

            if len(pred_bbox_l) == 0:
                continue
            if len(gt_bbox_l) == 0:
                match[l].extend((0,) * pred_bbox_l.shape[0])
                continue

            # VOC evaluation follows integer typed bounding boxes.
            pred_bbox_l = pred_bbox_l.copy()
            pred_bbox_l[:, 2:] += 1
            gt_bbox_l = gt_bbox_l.copy()
            gt_bbox_l[:, 2:] += 1

            iou = bbox_iou(pred_bbox_l, gt_bbox_l)
            gt_index = iou.argmax(axis=1)
            # set -1 if there is no matching ground truth
            gt_index[iou.max(axis=1) < iou_thresh] = -1
            del iou

            selec = np.zeros(gt_bbox_l.shape[0], dtype=bool)
            
            for gt_idx in gt_index:
                if gt_idx >= 0:
                    if not selec[gt_idx]:
                        match[l].append(1)
                    else:
                        match[l].append(0)
                    selec[gt_idx] = True
                else:
                    match[l].append(0)
            
    for iter_ in (
            pred_bboxes, pred_labels, pred_scores,
            gt_bboxes, gt_labels):
        if next(iter_, None) is not None:
            raise ValueError('Length of input iterables need to be same.')

    n_fg_class = max(n_pos.keys()) + 1
    prec = [None] * n_fg_class
    rec = [None] * n_fg_class

    for l in n_pos.keys():
        score_l = np.array(score[l])
        match_l = np.array(match[l], dtype=np.int8)

        order = score_l.argsort()[::-1]
        match_l = match_l[order]

        tp = np.cumsum(match_l == 1)
        fp = np.cumsum(match_l == 0)

        # If an element of fp + tp is 0,
        # the corresponding element of prec[l] is nan.
        prec[l] = tp / (fp + tp)
        # If n_pos[l] is 0, rec[l] is None.
        if n_pos[l] > 0:
            rec[l] = tp / n_pos[l]

    return prec, rec


def calc_detection_voc_ap(prec, rec, use_07_metric=False):
    """Calculate average precisions based on evaluation code of PASCAL VOC.
    This function calculates average precisions
    from given precisions and recalls.
    The code is based on the evaluation code used in PASCAL VOC Challenge.
    Args:
        prec (list of numpy.array): A list of arrays.
            :obj:`prec[l]` indicates precision for class :math:`l`.
            If :obj:`prec[l]` is :obj:`None`, this function returns
            :obj:`numpy.nan` for class :math:`l`.
        rec (list of numpy.array): A list of arrays.
            :obj:`rec[l]` indicates recall for class :math:`l`.
            If :obj:`rec[l]` is :obj:`None`, this function returns
            :obj:`numpy.nan` for class :math:`l`.
        use_07_metric (bool): Whether to use PASCAL VOC 2007 evaluation metric
            for calculating average precision. The default value is
            :obj:`False`.
    Returns:
        ~numpy.ndarray:
        This function returns an array of average precisions.
        The :math:`l`-th value corresponds to the average precision
        for class :math:`l`. If :obj:`prec[l]` or :obj:`rec[l]` is
        :obj:`None`, the corresponding value is set to :obj:`numpy.nan`.
    """

    n_fg_class = len(prec)
    ap = np.empty(n_fg_class)
    for l in six.moves.range(n_fg_class):
        if prec[l] is None or rec[l] is None:
            ap[l] = np.nan
            continue

        if use_07_metric:
            # 11 point metric
            ap[l] = 0
            for t in np.arange(0., 1.1, 0.1):
                if np.sum(rec[l] >= t) == 0:
                    p = 0
                else:
                    p = np.max(np.nan_to_num(prec[l])[rec[l] >= t])
                ap[l] += p / 11
        else:
            # correct AP calculation
            # first append sentinel values at the end
            mpre = np.concatenate(([0], np.nan_to_num(prec[l]), [0]))
            mrec = np.concatenate(([0], rec[l], [1]))

            mpre = np.maximum.accumulate(mpre[::-1])[::-1]

            # to calculate area under PR curve, look for points
            # where X axis (recall) changes value
            i = np.where(mrec[1:] != mrec[:-1])[0]

            # and sum (\Delta recall) * prec
            ap[l] = np.sum((mrec[i + 1] - mrec[i]) * mpre[i + 1])
    return ap