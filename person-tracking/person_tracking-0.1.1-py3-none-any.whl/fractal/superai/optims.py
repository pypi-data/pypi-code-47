""" Optimizers to train deep neural networks
"""
__author__ = ["PrakashJay"]

import torch

def get_optim(optim_type, model, kwargs):
    if optim_type == "sgd":
        print("Using sgd optim")
        return sgd(optim_type, model, kwargs)
        
    else:
        raise NotImplementedError("We haven't implemented these anchor boxes yet. Please raise a pull request if it is useful")


def sgd(optim_type, model, kwargs):
    if kwargs is None:
        print("Using Default values for optimizer")
        kwargs = {"lr": 0.001, 
        "momentum": 0.9,
        "weight_decay": 0.0005,
        "nesterov": True}
    return torch.optim.SGD(model.parameters(),
                           lr = kwargs["lr"], 
                           momentum = kwargs["momentum"],
                           weight_decay= kwargs["weight_decay"],
                           nesterov=kwargs["nesterov"])