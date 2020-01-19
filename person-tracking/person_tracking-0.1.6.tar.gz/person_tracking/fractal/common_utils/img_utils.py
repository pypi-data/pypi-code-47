__author__ = ["Not me"]

import torch
import numpy as np 
import torch.nn as nn


def bbox_iou(box1, box2):
    """ Returns the IoU of two bounding boxes 
    """
    #Get the coordinates of bounding boxes
    b1_x1, b1_y1, b1_x2, b1_y2 = box1[:,0], box1[:,1], box1[:,2], box1[:,3]
    b2_x1, b2_y1, b2_x2, b2_y2 = box2[:,0], box2[:,1], box2[:,2], box2[:,3]
    
    #get the corrdinates of the intersection rectangle
    inter_rect_x1 =  torch.max(b1_x1, b2_x1)
    inter_rect_y1 =  torch.max(b1_y1, b2_y1)
    inter_rect_x2 =  torch.min(b1_x2, b2_x2)
    inter_rect_y2 =  torch.min(b1_y2, b2_y2)
    
    #Intersection area
    inter_area = torch.clamp(inter_rect_x2 - inter_rect_x1 + 1, min=0) * torch.clamp(inter_rect_y2 - inter_rect_y1 + 1, min=0)
    
    #Union Area
    b1_area = (b1_x2 - b1_x1 + 1)*(b1_y2 - b1_y1 + 1)
    b2_area = (b2_x2 - b2_x1 + 1)*(b2_y2 - b2_y1 + 1)
    
    iou = inter_area / (b1_area + b2_area - inter_area)
    
    return iou

def unique(tensor):
    tensor_np = tensor.cpu().numpy()
    unique_np = np.unique(tensor_np)
    unique_tensor = torch.from_numpy(unique_np)
    
    tensor_res = tensor.new(unique_tensor.shape)
    tensor_res.copy_(unique_tensor)
    return tensor_res


def write_results(prediction, confidence, num_classes, nms = True, nms_conf = 0.4):
    conf_mask = (prediction[:,:,4] > confidence).float().unsqueeze(2)
    prediction = prediction*conf_mask
    

    try:
        ind_nz = torch.nonzero(prediction[:,:,4]).transpose(0,1).contiguous()
    except:
        return 0
    
    
    box_a = prediction.new(prediction.shape)
    box_a[:,:,0] = (prediction[:,:,0] - prediction[:,:,2]/2)
    box_a[:,:,1] = (prediction[:,:,1] - prediction[:,:,3]/2)
    box_a[:,:,2] = (prediction[:,:,0] + prediction[:,:,2]/2) 
    box_a[:,:,3] = (prediction[:,:,1] + prediction[:,:,3]/2)
    prediction[:,:,:4] = box_a[:,:,:4]
    

    
    batch_size = prediction.size(0)
    
    output = prediction.new(1, prediction.size(2) + 1)
    write = False


    for ind in range(batch_size):
        #select the image from the batch
        image_pred = prediction[ind]
        

        
        #Get the class having maximum score, and the index of that class
        #Get rid of num_classes softmax scores 
        #Add the class index and the class score of class having maximum score
        max_conf, max_conf_score = torch.max(image_pred[:,5:5+ num_classes], 1)
        max_conf = max_conf.float().unsqueeze(1)
        max_conf_score = max_conf_score.float().unsqueeze(1)
        seq = (image_pred[:,:5], max_conf, max_conf_score)
        image_pred = torch.cat(seq, 1)
        

        
        #Get rid of the zero entries
        non_zero_ind =  (torch.nonzero(image_pred[:,4]))

        
        image_pred_ = image_pred[non_zero_ind.squeeze(),:].view(-1,7)
        
        #Get the various classes detected in the image
        try:
            img_classes = unique(image_pred_[:,-1])
        except:
             continue
        #WE will do NMS classwise
        for cls in img_classes:
            #get the detections with one particular class
            cls_mask = image_pred_*(image_pred_[:,-1] == cls).float().unsqueeze(1)
            class_mask_ind = torch.nonzero(cls_mask[:,-2]).squeeze()
            

            image_pred_class = image_pred_[class_mask_ind].view(-1,7)

		
        
             #sort the detections such that the entry with the maximum objectness
             #confidence is at the top
            conf_sort_index = torch.sort(image_pred_class[:,4], descending = True )[1]
            image_pred_class = image_pred_class[conf_sort_index]
            idx = image_pred_class.size(0)
            
            #if nms has to be done
            if nms:
                #For each detection
                for i in range(idx):
                    #Get the IOUs of all boxes that come after the one we are looking at 
                    #in the loop
                    try:
                        ious = bbox_iou(image_pred_class[i].unsqueeze(0), image_pred_class[i+1:])
                    except ValueError:
                        break
        
                    except IndexError:
                        break
                    
                    #Zero out all the detections that have IoU > treshhold
                    iou_mask = (ious < nms_conf).float().unsqueeze(1)
                    image_pred_class[i+1:] *= iou_mask       
                    
                    #Remove the non-zero entries
                    non_zero_ind = torch.nonzero(image_pred_class[:,4]).squeeze()
                    image_pred_class = image_pred_class[non_zero_ind].view(-1,7)
                    
                    

            #Concatenate the batch_id of the image to the detection
            #this helps us identify which image does the detection correspond to 
            #We use a linear straucture to hold ALL the detections from the batch
            #the batch_dim is flattened
            #batch is identified by extra batch column
            
            
            batch_ind = image_pred_class.new(image_pred_class.size(0), 1).fill_(ind)
            seq = batch_ind, image_pred_class
            if not write:
                output = torch.cat(seq,1)
                write = True
            else:
                out = torch.cat(seq,1)
                output = torch.cat((output,out))
    
    return output


def xyxy_xywh(boxes, offset=0.5):
    """xyxy to xywh format  
    """
    height = boxes[:, 3] - boxes[:, 1]
    width = boxes[:, 2] - boxes[:, 0]
    ctr_y = boxes[:, 1] + offset * height
    ctr_x = boxes[:, 0] + offset * width 
    return torch.stack((ctr_x, ctr_y, width, height), dim=1)
        
#def xyxy_xyhw(boxes, offset=0.5):
#    """xyxy
#    """
#    height = boxes[:, 3] - boxes[:, 1]
#    width = boxes[:, 2] - boxes[:, 0]
#    ctr_y = boxes[:, 1] + offset * height
#    ctr_x = boxes[:, 0] + offset * width 
#    return torch.stack((ctr_x, ctr_y, height, width), dim=1)

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

    
#def xyhw_xyxy(boxes):
#    """xyhw_xyxy
#    """
#    bbox = torch.zeros(boxes.shape)
#    bbox[:, 0] = boxes[:, 0] - 0.5 * boxes[:, 3]
#    bbox[:, 1] = boxes[:, 1] - 0.5 * boxes[:, 2]
#    bbox[:, 2] = boxes[:, 0] + 0.5 * boxes[:, 3]
#    bbox[:, 3] = boxes[:, 1] + 0.5 * boxes[:, 2]
#    return bbox

def reframe_bboxes_for_actual_image(img_size, resized_img_size, bboxes):
    h, w = img_size
    oh, ow = resized_img_size

    sw = w/ float(ow) 
    sh = h/ float(oh)
    
    xywh = xyxy_xywh(bboxes)
    xywh[:, 2] = (w/float(ow)) * xywh[:, 2]
    xywh[:, 3] = (h/float(oh)) * xywh[:, 3]
    xywh[:, 1] = (h/float(oh)) * xywh[:, 1]
    xywh[:, 0] = (w/float(ow)) * xywh[:, 0]
    
    bbox = xywh_xyxy(xywh)
    return bbox