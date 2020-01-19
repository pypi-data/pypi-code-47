import torch
import torchvision
import math
import torch.nn as nn

def resnet18(num_classes, pretrained=True, imbalance=False, prior=0.01):
    model = torchvision.models.resnet18(pretrained=pretrained)
    num_fltrs = model.fc.in_features
    model.avgpool = nn.AdaptiveAvgPool2d(1)
    model.fc = torch.nn.Linear(num_fltrs, num_classes)
    if imbalance:
        model.fc.weight.data.fill_(0)
        model.fc.bias.data.fill_(-math.log((1.0-prior)/prior))
    return model
def resnet50(num_classes, pretrained=True, imbalance=False, prior=0.01):
    model = torchvision.models.resnet50(pretrained=pretrained)
    num_fltrs = model.fc.in_features
    model.avgpool = nn.AdaptiveAvgPool2d(1)
    model.fc = torch.nn.Linear(num_fltrs, num_classes)
    if imbalance:
        model.fc.weight.data.fill_(0)
        model.fc.bias.data.fill_(-math.log((1.0-prior)/prior))
    return model

def resnet101(num_classes, pretrained=True, imbalance=False, prior=0.01):
    model = torchvision.models.resnet101(pretrained=pretrained)
    num_fltrs = model.fc.in_features
    model.avgpool = nn.AdaptiveAvgPool2d(1)
    model.fc = torch.nn.Linear(num_fltrs, num_classes)
    if imbalance:
        model.fc.weight.data.fill_(0)
        model.fc.bias.data.fill_(-math.log((1.0-prior)/prior))
    return model
