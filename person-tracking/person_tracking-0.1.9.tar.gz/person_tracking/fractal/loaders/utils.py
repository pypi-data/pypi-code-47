import torch

def xyxy_xywh(boxes, offset=0.5):
    """xyxy
    """
    height = boxes[:, 3] - boxes[:, 1]
    width = boxes[:, 2] - boxes[:, 0]
    ctr_y = boxes[:, 1] + offset * height
    ctr_x = boxes[:, 0] + offset * width 
    return torch.stack((ctr_x, ctr_y, width, height), dim=1)