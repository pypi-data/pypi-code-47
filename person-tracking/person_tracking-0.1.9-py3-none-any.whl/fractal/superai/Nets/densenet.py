import torchvision
import torch.nn as nn

__models__ = ["densnet121", "densenet161", "densenet169", "densenet201"]


def densnet121(num_classes=1000, pretrained='imagenet'):
    if pretrained == "imagenet":
        model = torchvision.model.densnet121(pretrained=True)
        if num_classes != 1000:
            model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    else:
        model = torchvision.models.densnet121(pretrained=False, num_classes=num_classes)
    return model

def densnet161(num_classes=1000, pretrained='imagenet'):
    if pretrained == "imagenet":
        model = torchvision.model.densnet161(pretrained=True)
        if num_classes != 1000:
            model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    else:
        model = torchvision.models.densnet161(pretrained=False, num_classes=num_classes)
    return model

def densnet169(num_classes=1000, pretrained='imagenet'):
    if pretrained == "imagenet":
        model = torchvision.model.densnet169(pretrained=True)
        if num_classes != 1000:
            model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    else:
        model = torchvision.models.densnet169(pretrained=False, num_classes=num_classes)
    return model

def densnet201(num_classes=1000, pretrained='imagenet'):
    if pretrained == "imagenet":
        model = torchvision.model.densnet201(pretrained=True)
        if num_classes != 1000:
            model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    else:
        model = torchvision.models.densnet201(pretrained=False, num_classes=num_classes)
    return model
