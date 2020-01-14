import torch.nn as nn 

def get_losses(config):
    if config.loss_name == "bce_loss":
        loss = BCELoss()
    if config.loss_name == "cce_loss":
        loss = CCELoss()
    else:
        raise NotImplementedError("The following loss function is ")
    return loss 


class CCELoss(nn.Module):
    __name__ = "cce_loss"

    def __init__(self):
        super().__init__()
        self.loss = nn.CrossEntropyLoss(reduction="mean")
    def forward(self, y_pr, y_gt):
        y_gt = y_gt.view(-1)
        return self.loss(y_pr, y_gt)

class BCELoss(nn.Module):
    __name__ = "bce_loss"

    def __init__(self):
        super().__init__() 
        self.loss = nn.BCEWithLogitsLoss(reduction="mean")
    
    def forward(self, y_pr, y_gt):
        return self.loss(y_pr, y_gt)