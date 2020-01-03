import math
import torch
from torch import nn
from torch._six import inf
from torch.optim.lr_scheduler import _LRScheduler,ReduceLROnPlateau,CosineAnnealingLR,LambdaLR
from torch.optim.optimizer import  Optimizer
import numpy as np
from ..backend.common import get_function,get_class,snake2camel
from ..optims.trainers import LRSchedulerMixin
__all__ = ['warmup_lr_scheduler','adjust_learning_rate','reduce_lr_on_plateau','cyclic_scheduler','get_lr_scheduler']


def warmup_lr_scheduler(func):
    def wrapper(*args, **kwargs):
        x = args[0]
        w = args[1]
        if x.ndim == 3:
            w = np.flipud(w)
            w = np.transpose(w, (1, 2, 0))
            if kwargs['data_format'] == 'channels_last':
                x = np.transpose(x, (0, 2, 1))
        elif x.ndim == 4:
            w = np.fliplr(np.flipud(w))
            w = np.transpose(w, (2, 3, 0, 1))
            if kwargs['data_format'] == 'channels_last':
                x = np.transpose(x, (0, 3, 1, 2))
        else:
            w = np.flip(np.fliplr(np.flipud(w)), axis=2)
            w = np.transpose(w, (3, 4, 0, 1, 2))
            if kwargs['data_format'] == 'channels_last':
                x = np.transpose(x, (0, 4, 1, 2, 3))
        dilation_rate = kwargs.pop('dilation_rate', 1)
        if isinstance(dilation_rate, int):
            dilation_rate = (dilation_rate,) * (x.ndim - 2)
        for (i, d) in enumerate(dilation_rate):
            if d > 1:
                for j in range(w.shape[2 + i] - 1):
                    w = np.insert(w, 2 * j + 1, 0, axis=2 + i)
        y = func(x, w, **kwargs)
        if kwargs['data_format'] == 'channels_last':
            if y.ndim == 3:
                y = np.transpose(y, (0, 2, 1))
            elif y.ndim == 4:
                y = np.transpose(y, (0, 2, 3, 1))
            else:
                y = np.transpose(y, (0, 2, 3, 4, 1))
        return y
    return wrapper



def adjust_learning_rate(optimizer,base_lr=0.001, current_epoch=0,num_epochs=3, power=0.8,warmup=5,verbose=True):
    """Sets the learning rate: milestone is a list/tuple"""

    # def lr_poly(base_lr, iter, max_iter, power):
    #     return base_lr * ((1 - float(iter) / max_iter) ** (power))
    def lr_poly(base_lr, iter, max_iter, power):
        return base_lr * pow(power,max(float(iter)-1,0))
    if current_epoch<warmup:
        lr=1e-5*(current_epoch+1)
    else:
        lr = lr_poly(base_lr, current_epoch, num_epochs, power)
    if verbose==True:
        print('learning rate : {0:.4e}'.format(lr))
    #optimizer.param_groups[0]['lr'] = lr
    optimizer.adjust_learning_rate(lr,True)

    return lr



def reduce_lr_on_plateau(optimizer,base_lr=0.001 ,verbose=True, mode='min', factor=0.5, patience=5, threshold=1e-4, threshold_mode='rel', cooldown=0, min_lr=1e-8, eps=1e-9):
   return ReduceLROnPlateau(optimizer,mode=mode,factor=factor,patience=patience,verbose=verbose,threshold=threshold,threshold_mode=threshold_mode,cooldown=cooldown,min_lr=min_lr,eps=eps)

def cosine_annealing_lr(optimizer,base_lr=0.001 ,total_epoch=100,  eta_min=0, last_epoch=-1):
    return CosineAnnealingLR(optimizer,total_epoch, eta_min, last_epoch=last_epoch)


def cyclic_scheduler(optimizer,base_lr=0.001, current_epoch=0,current_batch=0,total_epoch=100,total_batch=100,verbose=True,min_lr_factor=0.05, max_lr=1.0 ):
    half_epochs = total_epoch // 2
    decay_epochs = total_epoch * 0.05
    lr_grow = np.linspace(min_lr_factor, max_lr, half_epochs)
    lr_down = np.linspace(max_lr, min_lr_factor, half_epochs - decay_epochs)
    lr_decay = np.linspace(min_lr_factor, min_lr_factor * 0.01, decay_epochs)
    learning_rates = np.concatenate((lr_grow, lr_down, lr_decay)) / max_lr
   # lrs=[base_lr * learning_rates[last_epoch] for base_lr in base_lrs]




def get_lr_scheduler(lr_scheduler_name):
    if lr_scheduler_name is None:
        return None
    lr_scheduler_modules = ['trident.optims.pytorch_lr_schedulers','torch.optim']
    lr_scheduler_fn=None
    if isinstance(lr_scheduler_name,str):
        if lr_scheduler_name in __all__:
            lr_scheduler_fn=get_function(lr_scheduler_name,lr_scheduler_modules)
    else:
        try:
            lr_scheduler_fn = get_function(lr_scheduler_name, lr_scheduler_modules)
        except Exception :
            lr_scheduler_fn = get_function(snake2camel(lr_scheduler_name), lr_scheduler_modules)
    return lr_scheduler_fn





