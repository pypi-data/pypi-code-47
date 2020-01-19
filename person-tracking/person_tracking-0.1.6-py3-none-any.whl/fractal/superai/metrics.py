import torch
import numpy as np
import torch.nn.functional as F
from sklearn.metrics import fbeta_score, f1_score

def get_metric(opt, outputs, targets):
    """ Metric to evaluate

    outputs = [network outputs]
    targets = [network targets]
    """
    if opt.metric == "accuracy":
        outputs = F.softmax(outputs, dim =1)
        _, pred = outputs.topk(1)
        accuracy = float(torch.sum(pred == targets).cpu().numpy())/pred.shape[0]
        
        if opt.metric_n:
            _, pred = outputs.topk(opt.metric_n)
            images, _ = targets.size()
            targets = targets.expand(images, opt.metric_n)
            accuracy_n = float(torch.sum(pred == targets).cpu().numpy())/pred.shape[0]
            
        return accuracy, accuracy_n
        
    elif opt.metric == "logloss":
        return float(F.cross_entropy(outputs, targets.view(-1), weight=opt.class_weight).cpu().numpy()), _

    elif opt.metric == "mean_f2_score":
        out = torch.sigmoid(outputs)
        out = out.detach().cpu().numpy()
        #print(targets)
        #print(out)
        out = out>0.5
        return fbeta_score(targets, out, average='weighted', beta=2), 0
    
    elif opt.metric == "f1_macro":
        out = torch.sigmoid(outputs)
        out = out.detach().cpu().numpy()
        out = out > 0.5
        return f1_score(targets.cpu().numpy(), out, average="macro"), 0

    else:
        raise NotImplementedError
