import numpy as np 
import torch

def xyxy_xywh(boxes, offset=0.5):
    """xyxy to xywh format  
    """
    height = boxes[:, 3] - boxes[:, 1]
    width = boxes[:, 2] - boxes[:, 0]
    ctr_y = boxes[:, 1] + offset * height
    ctr_x = boxes[:, 0] + offset * width 
    return torch.stack((ctr_x, ctr_y, width, height), dim=1)

def clamper(bbox, size):
    """bbox takes xyxy values
    """
    h, w = size
    bbox[:, 0] = torch.clamp(bbox[:, 0], 0, w)
    bbox[:, 1] = torch.clamp(bbox[:, 1], 0, h)
    bbox[:, 2] = torch.clamp(bbox[:, 2], 0, w)
    bbox[:, 3] = torch.clamp(bbox[:, 3], 0, h)
    return bbox
    
def xywh_xyxy(boxes):
    """xyhw_xyxy ----> we are using h,w and not w, h format .. Please be careful
    """
    bbox = torch.zeros(boxes.shape)
    bbox[:, 0] = boxes[:, 0] - 0.5 * boxes[:, 2]
    bbox[:, 1] = boxes[:, 1] - 0.5 * boxes[:, 3]
    bbox[:, 2] = boxes[:, 0] + 0.5 * boxes[:, 2]
    bbox[:, 3] = boxes[:, 1] + 0.5 * boxes[:, 3]
    return bbox

def bbox_iou(bbox_a, bbox_b, intersection=True):
    """Calculate the Intersection of Unions (IoUs) between
    bounding boxes.
    IoU is calculated as a ratio of area of the intersection
    and area of the union.

    bbox_a: numpy array
    bbox_b: numpy array

    Returns the area between two numpy array's. (yxyx format)
    
    
    """
    #ToDo :Convert to Pytorch
    if bbox_a.shape[1] != 4 or bbox_b.shape[1] != 4:
        raise IndexError

    # top left
    tl = np.maximum(bbox_a[:, None, :2], bbox_b[:, :2])
    # bottom right
    br = np.minimum(bbox_a[:, None, 2:], bbox_b[:, 2:])

    area_i = np.prod(br - tl, axis=2) * (tl < br).all(axis=2)
    area_a = np.prod(bbox_a[:, 2:] - bbox_a[:, :2], axis=1)
    area_b = np.prod(bbox_b[:, 2:] - bbox_b[:, :2], axis=1)
    if intersection:
        iou = area_i / (area_a[:, None] + area_b - area_i)
    else:
        iou = area_i 
    return iou
