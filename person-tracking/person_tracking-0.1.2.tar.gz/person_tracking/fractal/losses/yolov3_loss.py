import torch
import torch.nn as nn

import math
import sys
import numpy as np

from ..anchors.encoder import process_yolo_output, encode_targets
from ..vis_lib.visdom_vis import VisdomLinePlotter
from ..anchors.anchors_generator import generate_anchors


class Yolov3_loss(nn.Module):
    def __init__(self, num_classes = 80, use_gpu=True, use_visdom=True, exp_name="yolo"):
        super(Yolov3_loss, self).__init__()
        self.num_classes=num_classes
        self.use_gpu = use_gpu
        self.use_visdom = use_visdom 
        
        if self.use_visdom:
            print("Using visdom: run visdom.server somewhere")
            self.plot = VisdomLinePlotter(env_name = exp_name)
        self.iterations = 1

    
    def forward(self, cls_preds, cls_targets, scales, stride, nW, nH, pyramids=3):
        #cls_preds = cls_preds.cpu()
        #cls_targets = cls_targets.cpu()
        #print(stride, nW, nH, scales)
        anchors = generate_anchors(stride, nW, nH, scales)
        if self.use_gpu:
            anchors = anchors.cuda()
        outs, scores = process_yolo_output(cls_preds, stride, scales, anchors.clone(), nW, nH, self.num_classes)
        coord_mask, conf_mask, cls_mask, tcoord, tconf, tcls, nRecall, nRecall75, nGT = encode_targets(outs.cpu().clone(),
                                                                                                    cls_targets.cpu().detach(), 
                                                                                                    scales,
                                                                                                    anchors.cpu().clone(),
                                                                                                    nW, 
                                                                                                    nH, 
                                                                                                    self.num_classes,
                                                                                                    stride)
        cls = scores[:,:, 5:].clone()
        coord = scores[:,:, :4].clone()
        conf = scores[:,:,  4].clone()
        
        #print("conf", conf.cpu().unique())
        #print("tconf", tconf.sum())
        
        if self.use_gpu:
            coord_mask = coord_mask.cuda()
            conf_mask = conf_mask.cuda()
            cls_mask = cls_mask.cuda()
            tcoord = tcoord.cuda()
            tconf = tconf.cuda()
            tcls = tcls.cuda()
        nProposals = int((conf > 0.25).float().sum())
        
        ## cls score 
        #cls = cls[(cls_mask == 1)]
        #tcls = tcls[(cls_mask == 1)].long().view(-1) - 1 ## 0-79 rathere than 1-80
        #loss_cls = torch.nn.CrossEntropyLoss(size_average=False)(cls, tcls) if cls.size(0) > 0 else 0
        summed = tcls.sum()
        loss_cls = torch.nn.BCELoss(size_average=False)(cls[(tcls ==1)], cls_mask[(tcls==1)] )/(summed)
        
        ## coord_loss
        #coord_mask = coord_mask.unsqueeze(2)
        loss_coord = 4*(torch.nn.MSELoss(size_average=False)(coord[(tcls==1)], tcoord[(tcls==1)])/(summed))
        
        ## conf_loss 
        #loss_conf = torch.nn.BCELoss(size_average=False)(conf[(conf_mask ==1)], tconf[(conf_mask == 1)])/ (summed)
        loss_conf = torch.nn.MSELoss(size_average=False)(conf*conf_mask, tconf*conf_mask)/(summed)
        total_loss = loss_conf + loss_coord + loss_cls
        print("Iter: {}, nProposals: {}, nRecall: {}, nRecall75: {}, nGT: {}, loss_conf: {}, loss_coord: {}, loss_cls: {}, total_loss: {}".format(int(self.iterations/pyramids), nProposals, nRecall, nRecall75, nGT, loss_conf, loss_coord, loss_cls, total_loss))
        
        if self.iterations%10 == 0: 
            if self.use_visdom:
                self.plot.plot("loss_coord", "training", self.iterations, np.array(float(loss_coord)))
                self.plot.plot("loss_conf", "training", self.iterations, np.array(float(loss_conf)))
                self.plot.plot("loss_cls", "training", self.iterations, np.array(float(loss_cls)))

        self.iterations +=1
        return loss_conf, loss_coord, loss_cls