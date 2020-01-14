import torch.nn as nn
from . import functions as F

def get_metric(cfg):
    metrics = []
    for name in cfg.metrics:
        if name == "accuracy":
            metrics.append(Accuracy(activation=cfg.activation, thresh=cfg.threshold))
        elif name == "f1_score":
            metrics.append(FscoreMetric(eps=1., beta=1))
        else:
            raise NotImplementedError("This metric is not implemented")
    return metrics

class IoUMetric(nn.Module):

    __name__ = 'iou'

    def __init__(self, eps=1e-7, threshold=0.5, activation='sigmoid'):
        super().__init__()
        self.activation = activation
        self.eps = eps
        self.threshold = threshold

    def forward(self, y_pr, y_gt):
        return F.iou(y_pr, y_gt, self.eps, self.threshold, self.activation)


class FscoreMetric(nn.Module):

    __name__ = 'f1_score'

    def __init__(self, beta=1, eps=1e-7, threshold=0.5, activation='sigmoid'):
        super().__init__()
        self.activation = activation
        self.eps = eps
        self.threshold = threshold
        self.beta = beta

    def forward(self, y_pr, y_gt):
        return F.f_score(y_pr, y_gt, self.beta, self.eps, self.threshold, self.activation)

class Accuracy(nn.Module):
    __name__ = "accuracy"

    def __init__(self, thresh=0.5, activation="sigmoid"):
        super().__init__()
        self.activation = activation
        self.thresh = thresh
    
    def forward(self, y_pr, y_gt):
        if self.activation == "softmax":
            accuracy = F.accuracy(y_pr, y_gt)
        elif self.activation == "sigmoid":
            accuracy = F.accuracy_thresh(y_pr, y_gt, thresh=self.thresh)
        else:
            raise NotImplementedError("The activation function accuracy is not implemented")
        return accuracy