import torch
import torchvision.transforms as transforms 
from PIL import Image

import numpy as np 

from ..anchors.utils import clamper, bbox_iou

def get_grid_xy(img_size, stride):
    """ Given img_size and stide, it extracts the xy locations (top, left) of all the image patches
    
    img_size: tuple: Size of the image (h, w)
    stride: int: stride to move along x and y axis 
    
    Returns:
    x_y_offset: [N, 2]: A image tensor
    """
    h = img_size[0]//stride
    w = img_size[1]//stride
    grid_x = np.arange(w)
    grid_y = np.arange(h)
    a, b = np.meshgrid(grid_x, grid_y)
    x_offset = torch.FloatTensor(a).view(-1, 1)
    y_offset = torch.FloatTensor(b).view(-1, 1)
    x_y_offset = torch.cat((x_offset, y_offset), 1)
    return x_y_offset

def patch_loc(stride, patch_size, img_size, pad=True):
    """ Extracts the patch locations from the image by using padding 
    
    stride: int: Stride to move along x and y axis of the image : Future scope is to move 3D 
    patch_size: int: Size of the image patch we need 
    img_size: tuple: Size of the image patch we need 
    pad: boolean: padding to convert image to extract all parts of the image with equal size
    
    Returns: 
    xywh: Tensor: [N, 4] Locations of the image patches (ctr_x, ctr_y, w, h)
    img_size: tuple: The transformed image size. use it to pad the image 
    """
    h, w = img_size 
    if pad:
        h_ = patch_size - (h%stride)
        w_ = patch_size - (w%stride)
        img_size = (h+h_, w+w_)
    x_y_offset = get_grid_xy(img_size, stride)
    xy = x_y_offset * stride 
    xy[:, 0] = xy[:, 0] + (patch_size/2)
    xy[:, 1] = xy[:, 1] + (patch_size/2)
    wh = torch.ones(xy.shape) * patch_size 
    xywh = torch.cat([xy, wh], 1)
    return xywh, img_size 

def read_img(loc, tensor=True):
    """ Read a image into python environment
    """
    img = Image.open(loc)
    if tensor:
        img = transforms.ToTensor()(img)
    return img 

def pil_2_tensor(pil_img):
    """convert a pil image to tensor
    """
    img = transforms.ToTensor()(pil_img)
    return img


def pad_img(img_pil, new_dim):
    """Pad the image so that the output image will have the dimensions of new dim. Always use "constant" mode only to pass
    """
    w, h = img_pil.size
    h_, w_ = new_dim 
    h_pad = h_ - h
    w_pad = w_ - w 
    padded_img = transforms.functional.pad(img_pil, padding=(w_pad//2, h_pad//2), padding_mode="constant")
    return padded_img 
    

def get_img_patches(img_tensor, grid_dim):
    """Gets image patches tensors according to the grid
    
    Inputs:
    --------
    img_tensor: (C, H, W) - Image tensor
    grid_dim: [y1, x1, y2, x2] [N, 4] - N patchces xyxy co-ordinates 

    Outputs:
    --------
    Lists of Tensors (Each tensor represents the part of a images)
    """
    return [img_tensor[:, int(i):int(k), int(j): int(l)] for i, j, k, l in grid_dim]

def tensors_2_pil(img_tensors_list):
    """ Converts a list of tensors to PIL images 
    
    img_tensors_list: List of tensors which are converted to images
    """
    pills = transforms.ToPILImage()
    pil_list = [pills(img_tensors_list[i]) for i in range(len(img_tensors_list))]
    return pil_list

def bbox_extractor(img_grid, bbox, labels, patch_size, iou_required=0.5):
    """ Assign bboxes to respective grids and change their co-ordinates with respect to that bbox 
    
    Inputs:
    -------
    img_grid: [N, 4]: yxyx format. The coord loc of grid for each image: torch.FloatTensor 
    bbox: [N, 4]: yxyx format. The coord loc of bboxes of a image: torch.FloatTensor
    
    Outputs:
    --------
    A dict: with each key has image patch index and its key as bboxes assoiciated with it.
    
    bboxes: [N, 6]: [y1, x1, y2, x2, label , iou]
    """
    bbox_xy = bbox[:, [1,0, 3, 2]].clone()
    ious_area = bbox_iou(img_grid.numpy(), bbox.numpy(), intersection=False) # numpy is bloating man, Change this quickly
    grids, boxes = ious_area.shape
    bbox_area = (bbox[:, 2] - bbox[:, 0]) * (bbox[:, 3] - bbox[:, 1])
    final_ious = ious_area/bbox_area.repeat(grids).view(-1, boxes)
    
    patch_index = {} # key as patch number and values as boxes assoiciated with it 
    for i in range(img_grid.shape[0]):
        mask = (final_ious[i, :] > iou_required)
        boxes_ = bbox[mask] #yxyx
        labels_ = labels[mask]
        ious_ = final_ious[i, :][mask]
        patch_ = img_grid[i, :]
        ## convertin yxyx to yxhw ---> yx is (top left)
        
        
        if len(boxes_) > 0:
            boxes_[:, 2] = boxes_[:, 2] - boxes_[:, 0] # h
            boxes_[:, 3] = boxes_[:, 3] - boxes_[:, 1] # w 
            #boxes_ = boxes_[:, [0, 1, 3, 2]] # y1x1wh 
            boxes_[:, :2] = boxes_[:, :2] - patch_[:2]
            boxes_[:, 2] = boxes_[:, 0] + boxes_[:, 2] # y2
            boxes_[:, 3] = boxes_[:, 1] + boxes_[:, 3]
            #boxes_[:, 2:] = boxes_[:, 2:] - patch_[2:] + patch_size 
            boxes_ = clamper(boxes_[:, [1, 0, 3, 2]], (patch_size, patch_size)) #converting yxyx format to xyxy
            boxes_ = torch.cat([boxes_, labels_.float().view(-1, 1), ious_.view(-1, 1)], 1)
        patch_index[i] = boxes_
    return patch_index