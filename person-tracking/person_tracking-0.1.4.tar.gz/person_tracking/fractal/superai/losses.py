import torch
import torch.nn as nn
import torch.nn.functional as F

def get_loss_function(opt):
    if opt.loss_type == "cross_entropy_loss":
        return torch.nn.CrossEntropyLoss(weight=opt.class_weight)
    elif opt.loss_type == "focal_loss":
        return FocalLoss(opt.num_classes, opt.use_gpu)
    elif opt.loss_type == "multilabel_BCELoss":
        return torch.nn.BCEWithLogitsLoss(reduction="sum")
    else:
        raise NotImplementedError


        
class FocalLoss(nn.Module):
    def __init__(self,
                 classes,
                 use_gpu,
                 focusing_param=2.0,
                 balance_param=0.25):
        super().__init__()
        self.use_gpu = use_gpu
        self.focusing_param = focusing_param
        self.balance_param = balance_param
        self.classes = classes
        
    def forward(self, x, y):
        batch_size, next_best = y.size()[0], y.size()[1]
        sigmoid_p = torch.sigmoid(x)
        zeros = torch.zeros(sigmoid_p.shape)
        if self.use_gpu:
            zeros = zeros.cuda()
        y = y.float()
        
        pos_p_sub = ((y >= sigmoid_p).float() * (y-sigmoid_p)) + ((y < sigmoid_p).float() * zeros)
        neg_p_sub = ((y >= zeros).float() * zeros) + ((y <= zeros).float() * sigmoid_p)
        
        ce = (-1) * self.balance_param * (pos_p_sub ** self.focusing_param) * torch.log(torch.clamp(sigmoid_p, 1e-4, 1.0)) -(1-self.balance_param) * (neg_p_sub ** self.focusing_param) * torch.log(torch.clamp(1.0-sigmoid_p, 1e-4, 1.0))
        #pos_samples = float(batch_size * next_best)
        return ce.sum()/y.sum()
        