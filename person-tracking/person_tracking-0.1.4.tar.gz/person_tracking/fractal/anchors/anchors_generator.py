""" For now write individual anchor boxes generator
"""
import torch
import numpy as np 

from person_tracking.fractal.anchors.utils import bbox_iou, xywh_xyxy, clamper, xyxy_xywh
# from fractal.anchors.utils import bbox_iou, xywh_xyxy, clamper, xyxy_xywh


def get_inside_index(bbox, H, W):
    """ index of the elements whose co-ordinates are bound inside the image
    """
    index = torch.where((bbox[:, 0] >= 0) &
        (bbox[:, 1] >= 0) &
        (bbox[:, 2] <= H) &
        (bbox[:, 3] <= W), torch.ones(bbox.shape[0]), torch.zeros(bbox.shape[0])).nonzero()
    return index.squeeze(1)

def _unmap(data, count, index, fill=-1):
    if len(data.shape) == 1:
        t = torch.zeros(count)
        t.fill_(fill)
        t[index] = data
    else:
        t = torch.zeros((count, data.shape[1:][0]))
        t.fill_(fill)
        t[index, :] = data
    return t 


def generate_grid(grid_size, offset=0.5):
    """
    :param grid_size:
    :param offset: offset from left top corner
    :return:
    """
    grid = np.arange(grid_size)
    x_offset, y_offset = np.meshgrid(grid, grid)
    x_offset, y_offset = torch.FloatTensor(x_offset) + offset, torch.FloatTensor(y_offset) + offset
    grid_cells = torch.cat((x_offset.unsqueeze(2), y_offset.unsqueeze(2)), 2)
    grid_cells = grid_cells.view(-1, 2)
    return grid_cells


def generate_anchors(stride, nW, nH, anchors_scales):
    grid_size_x = nW/stride
    grid_size_y = nH/stride
    grid = generate_grid(grid_size_x, 0)
    wh_anchors = anchors_scales /stride
    all_grid_xy = grid.repeat(1, 3).view(-1, 2)
    all_grid_wh = wh_anchors.repeat(int(grid_size_x*grid_size_y), 1)
    return torch.cat((all_grid_xy, all_grid_wh), 1)


class Yolov3:
    
    def __init__(self, strides, anchor_centroids, img_size):
        """

        :param strides: [32, 16, 8]
        :param anchor_centroids:  [[[10, 13], [16, 30], [33, 23]],
                                   [[30, 61], [62, 45], [59, 119]],
                                   [[116, 90], [156, 198], [373, 326]]]
                                   Anchor box attr per centroid (here shape is 3X3X2)
        :param img_size: 416
        """
        self.strides = strides
        self.anchor_centroids = anchor_centroids
        self.img_size = img_size
        self.anchors_attr_list, self.anchor_strides_list = self.generate_anchors() # cx,cy,w,h format
        self.all_anchors = torch.cat(self.anchors_attr_list)
        self.all_anchors_xy = xywh_xyxy(self.all_anchors)
        self.all_anchors_strides = torch.cat(self.anchor_strides_list)
        self.all_anchors_ft_scale = self.get_anchors_ft_scale()
        self.valid_anchors_index = self.valid_index()
        self.anchor_tiles = self.anchor_tiles()
        self.valid_anchor_tiles = self.anchor_tiles[self.valid_anchors_index]
    
    def anchor_tiles(self):
        all_anchors_ft_scale = self.all_anchors_ft_scale
        all_anchors_ft_scale[:, 0] = torch.floor(all_anchors_ft_scale[:, 0])
        all_anchors_ft_scale[:, 1] = torch.floor(all_anchors_ft_scale[:, 1])
        return torch.cat([all_anchors_ft_scale[:, :2], 1+all_anchors_ft_scale[:, :2]], 1)
    
    def valid_index(self):
        all_anchors_xyxy = xywh_xyxy(self.all_anchors)
        valid_index = get_inside_index(all_anchors_xyxy, self.img_size, self.img_size)
        return valid_index
        
    def get_anchors_ft_scale(self):
        return self.all_anchors / self.all_anchors_strides.view(-1, 1).repeat(1, 4)
    
    @staticmethod
    def generate_grid(grid_size, offset=0.5):
        """
        :param grid_size:
        :param offset: offset from left top corner
        :return:
        """
        grid = np.arange(grid_size)
        x_offset, y_offset = np.meshgrid(grid, grid)
        x_offset, y_offset = torch.FloatTensor(x_offset) + offset, torch.FloatTensor(y_offset) + offset
        grid_cells = torch.cat((x_offset.unsqueeze(2), y_offset.unsqueeze(2)), 2)
        grid_cells = grid_cells.view(-1, 2)
        return grid_cells


    def generate_anchors(self):
        anchor_attrs_list = []
        anchor_strides = []
        for num, stride in enumerate(self.strides):
            grid_size = self.img_size // stride #13
            grid_cells = Yolov3.generate_grid(grid_size) # 13*13 X 2
            anchors_for_stride = self.anchor_centroids[num] #[[10, 13], [16, 30], [33, 23]]
            grid_cells_r = grid_cells.repeat(1, len(anchors_for_stride)).view(-1, 2) # 13*13*3 X2                             
            grid_cells_r *= stride # cordinates on  image_scale                                 
            anchors_r = torch.Tensor(anchors_for_stride).repeat(grid_size*grid_size, 1) # 3*13*13X2
            anchors_attrs_iscale = torch.cat((grid_cells_r, anchors_r),1) #13*13*3 X 4
            anchor_attrs_list.append(anchors_attrs_iscale)
            anchor_strides.append((torch.ones(anchors_attrs_iscale.shape[0])).fill_(stride))
            
        return anchor_attrs_list, anchor_strides
    
    def generate_pos_anchor_boxes_mask(self, bbox):
        """bbox will be in xywh format
        """
        total_gt = bbox.shape[0]
        strides = self.all_anchors_strides.view(-1, 1).repeat(total_gt, 1, 4)
        bbox_re = bbox.unsqueeze(1).repeat(1, 1, self.all_anchors.shape[0]).view(total_gt, -1, 4)
        bbox_re_strides = bbox_re/strides
        
        where = ((bbox_re_strides[:, :, 0] > self.anchor_tiles[:, 0]) &
                 (bbox_re_strides[:, :, 0] < self.anchor_tiles[:, 2]) &
                 (bbox_re_strides[:, :, 1] > self.anchor_tiles[:, 1]) &
                 (bbox_re_strides[:, :, 1] < self.anchor_tiles[:, 3]))
        where = where.permute(1, 0)
        where = where[self.valid_anchors_index]
        return where
    
    def encoder(self, bbox, labels):
        """ bbox is in xywh mode
        """
        ##Objectness score
        bbox_xywh = bbox 
        bbox = xywh_xyxy(bbox_xywh)
        assigned_anchors = self.generate_pos_anchor_boxes_mask(bbox_xywh) #[valid_anchors, gt_boxes]
        ious = bbox_iou(self.all_anchors_xy[self.valid_anchors_index][:, [1, 0, 3, 2]].numpy(), bbox[:, [1, 0, 3, 2]].numpy())
        
        single_pos = np.multiply(ious, assigned_anchors.float().numpy()).argmax(0)
        ignore_pos= np.where(ious > 0.5)[0]
        
        #if len(ignore_pos) == 0:
        #    ious_max = 0
        #    single_pos =0 
            
        #else:
        #    single_pos = ignore_pos[assigned_anchors[ignore_pos].argmax(0).numpy()]
        #    which_bbox = which_bbox[assigned_anchors[ignore_pos].argmax(0).numpy()] ## Will give in that order
        
        os_score = torch.zeros(self.valid_anchors_index.shape[0])
        os_score.fill_(0)
        if len(ignore_pos) > 0:
            os_score[ignore_pos] = -1 
        os_score[single_pos] = 1 
        
        f_os_score = _unmap(os_score, self.all_anchors.shape[0], self.valid_anchors_index, -1)
        
        ## xyhw 
        
        xy_anchors = self.all_anchors[self.valid_anchors_index][single_pos]
        strides = self.all_anchors_strides[self.valid_anchors_index][single_pos].view(-1, 1).repeat(1, 2)
        #xy_bboxes = bbox[which_bbox] #IF which_bbox is [2, 1, 0] incase of 3 boxes . this will change the order
        
        xy_anchors_tile = torch.floor(xy_anchors[:, :2]/strides)
        xy_bboxes_tile = bbox_xywh[:, :2]/strides
        
        xy_score = xy_bboxes_tile - xy_anchors_tile
        wh_score = torch.log(bbox_xywh[:, 2:]/xy_anchors[:, 2:])
        
        xywh_score = torch.cat([xy_score, wh_score], 1)
        
        coord_score = torch.zeros(self.valid_anchors_index.shape[0], 4)
        coord_score.fill_(-1) 
        coord_score[single_pos] = xywh_score 
        
        f_coord_score = _unmap(coord_score, self.all_anchors.shape[0], self.valid_anchors_index, -1)
        
        ## labels 
        l_score = torch.zeros(self.valid_anchors_index.shape[0])
        l_score.fill_(-1)
        l_score[single_pos] = labels.float()
        
        f_l_score = _unmap(l_score, self.all_anchors.shape[0], self.valid_anchors_index, -1)
        return torch.cat([f_coord_score, f_os_score.view(-1, 1), f_l_score.view(-1, 1)], 1)
        
            
            
            
        