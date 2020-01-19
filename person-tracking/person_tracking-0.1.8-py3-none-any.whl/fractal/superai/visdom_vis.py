import torch
from torchvision.transforms import transforms
import numpy as np
import visdom

import matplotlib.pyplot as plt 
from PIL import Image


class VisdomLinePlotter(object):
    """Plots to Visdom
    """
    def __init__(self, env_name='main'):
        self.viz = visdom.Visdom()
        self.env = env_name
        self.plots = {}
    def plot(self, var_name, split_name, x, y):
        """ Plot all the metrics available as named tuple
        
        var_name: named tuple 
        """
        if var_name not in self.plots:
            self.plots[var_name] = self.viz.line(X=np.array([x,x]), Y=np.array([y,y]), env=self.env, opts=dict(
                legend=[split_name],
                title=var_name,
                xlabel='Iterations',
                ylabel=var_name
            ))
        else:
            self.viz.line(X=np.array([x]), Y=np.array([y]), env=self.env, win=self.plots[var_name], name=split_name, update = 'append')

    def plot_tuple(self, ntuple, name, iteration):

        for field, value in ntuple._asdict().items():
            self.plot(field, name, iteration, value.data.cpu().numpy()[0])