"""Not a dummer any more 
"""
import torch
import numpy as np 

from person_tracking.fractal.anchors.utils import bbox_iou, xywh_xyxy, clamper, xyxy_xywh
from person_tracking.fractal.anchors.anchors_generator import generate_anchors
# from fractal.anchors.utils import bbox_iou, xywh_xyxy, clamper, xyxy_xywh
# from fractal.anchors.anchors_generator import generate_anchors



def bbox_iou(box1, box2, x1y1x2y2=True):
    if x1y1x2y2:
        x1_min = min(box1[0], box2[0])
        x2_max = max(box1[2], box2[2])
        y1_min = min(box1[1], box2[1])
        y2_max = max(box1[3], box2[3])
        w1, h1 = box1[2] - box1[0], box1[3] - box1[1]
        w2, h2 = box2[2] - box2[0], box2[3] - box2[1]
    else:
        w1, h1 = box1[2], box1[3]
        w2, h2 = box2[2], box2[3]
        x1_min = min(box1[0]-w1/2.0, box2[0]-w2/2.0)
        x2_max = max(box1[0]+w1/2.0, box2[0]+w2/2.0)
        y1_min = min(box1[1]-h1/2.0, box2[1]-h2/2.0)
        y2_max = max(box1[1]+h1/2.0, box2[1]+h2/2.0)

    w_union = x2_max - x1_min
    h_union = y2_max - y1_min
    w_cross = w1 + w2 - w_union
    h_cross = h1 + h2 - h_union
    carea = 0
    if w_cross <= 0 or h_cross <= 0:
        return 0.0

    area1 = w1 * h1
    area2 = w2 * h2
    carea = w_cross * h_cross
    uarea = area1 + area2 - carea
    return float(carea/uarea)

def multi_bbox_ious(boxes1, boxes2, x1y1x2y2=True):
    """ To find iou by 1to1 mapping
    (4, 507) * (4*507) --- > 507
    """
    if x1y1x2y2:
        x1_min = torch.min(boxes1[0], boxes2[0])
        x2_max = torch.max(boxes1[2], boxes2[2])
        y1_min = torch.min(boxes1[1], boxes2[1])
        y2_max = torch.max(boxes1[3], boxes2[3])
        w1, h1 = boxes1[2] - boxes1[0], boxes1[3] - boxes1[1]
        w2, h2 = boxes2[2] - boxes2[0], boxes2[3] - boxes2[1]
    else:
        w1, h1 = boxes1[2], boxes1[3]
        w2, h2 = boxes2[2], boxes2[3]
        x1_min = torch.min(boxes1[0]-w1/2.0, boxes2[0]-w2/2.0)
        x2_max = torch.max(boxes1[0]+w1/2.0, boxes2[0]+w2/2.0)
        y1_min = torch.min(boxes1[1]-h1/2.0, boxes2[1]-h2/2.0)
        y2_max = torch.max(boxes1[1]+h1/2.0, boxes2[1]+h2/2.0)

    w_union = x2_max - x1_min
    h_union = y2_max - y1_min
    w_cross = w1 + w2 - w_union
    h_cross = h1 + h2 - h_union
    mask = (((w_cross <= 0) + (h_cross <= 0)) > 0)
    area1 = w1 * h1
    area2 = w2 * h2
    carea = w_cross * h_cross
    carea[mask] = 0
    uarea = area1 + area2 - carea
    return carea/uarea

def process_yolo_output(output, stride, anchor_scales, anchors, nW, nH, nC):
    """ The most crazy function. Outputs the prediction for each box on feature scale
    """
    nB = output.shape[0]
    grid_size_x = int(nW/stride)
    grid_size_y = int(nH/stride)
    nAnchors = anchor_scales.shape[0]
    #print(nB, grid_size_x, grid_size_y, nAnchors)
    output = output.view(nB, (nC+5)*nAnchors, grid_size_x * grid_size_y).transpose(1, 2).contiguous()
    output = output.view(nB, grid_size_x * grid_size_y * nAnchors, nC+5)
    #print("before", output[:, :, 4].cpu().unique())
    
    output[:, :, :2] = torch.sigmoid(output[:, :, :2])
    output[:, :, 4] = torch.sigmoid(output[:, :, 4])
    output[:, :, 5:] = torch.sigmoid(output[:, :, 5:])
    #print("after", output[:, :, 4].cpu().unique())
    
    scores = output.clone()
    
    output[:, :, :2] += anchors[:, :2]
    output[:, :, 2]  = output[:, :, 2].exp() * anchors[:, 2]
    output[:, :, 3]  = output[:, :, 3].exp() * anchors[:, 3]
    return output, scores

def encode_targets(outputs, targets, anchor_scales, anchors, nW, nH, nC, strides, nthresh=0.7):
    eps = 0.00001
    nB = outputs.size(0)
    nA = outputs.size(1)
    nG = targets.shape[1]
    conf_mask = torch.ones(nB, nA)
    coord_mask = torch.zeros(nB, nA, 4)
    cls_mask = torch.zeros(nB, nA, nC)
    tcoord = torch.zeros(nB, nA , 4)
    tconf = torch.zeros(nB, nA)
    tcls = torch.zeros(nB, nA)
    twidth, theight = nW/strides, nH/strides
    anchors_xy = anchors.clone()
    anchors_xy[:, :2] += 0.5
    
    nGT=0
    nRecall = 0
    nRecall75 = 0
    
    for b in range(nB):
        label = targets[b]
        cur_pred_boxes = outputs[b]
        cur_ious = torch.zeros(nA)
        for la in label:
            if la[0] == 0:
                break
            gx, gy, gw, gh = la[1:]/strides
            cur_gt_boxes = torch.FloatTensor([gx, gy, gw, gh]).repeat(nA, 1)
            ious = multi_bbox_ious(cur_gt_boxes.t(), anchors_xy.t(), x1y1x2y2=False)
            cur_ious = torch.max(cur_ious, ious)
        ignore_ix = cur_ious > nthresh
        conf_mask[b, ignore_ix] = 0
        
        for la in label:
            if la[0] == 0:
                break
            nGT+=1
            gx, gy, gw, gh = la[1:]/strides
            tmp_gt_boxes = torch.FloatTensor([0, 0, gw, gh]).repeat(anchor_scales.shape[0], 1)
            bestn_start = ((anchors[:, 0] == int(gx)) & (anchors[:, 1] == int(gy))).nonzero()[0]
            k = anchors_xy[(anchors[:, 0] == int(gx)) & (anchors[:, 1] == int(gy))]
            k[:, :2] = 0
            values, bestn = torch.max(multi_bbox_ious(tmp_gt_boxes.t(), \
                                     k.t(), x1y1x2y2=False), 0)
            total_n = int(bestn+bestn_start)
            #assigned_anchor = anchors[total_n]
            gt_box = torch.FloatTensor([gx, gy, gw, gh])
            iou = bbox_iou(gt_box, outputs[b, total_n][:4].cpu(), x1y1x2y2=False)
            
            if iou > 0.5:
                nRecall +=1
                if iou > 0.75:
                    nRecall75 +=1
            
            coord_mask[b, total_n] = 1 
            cls_mask[b, total_n, int(la[0]) - 1] = 1
            conf_mask[b, total_n] = 5
            tcoord[b, total_n, 0] = float(gx - int(gx))
            tcoord[b, total_n, 1] = float(gy - int(gy))
            tcoord[b, total_n, 2] = float(torch.log((gw+eps)/anchors[total_n, 2]))
            tcoord[b, total_n, 3] = float(torch.log((gh+eps)/anchors[total_n, 3]))
            tcls[b, total_n] =  1
            tconf[b, total_n] = 1#iou if 0 else 1
    return coord_mask, conf_mask, cls_mask, tcoord, tconf, tcls, nRecall, nRecall75, nGT
            
            
    
    
    