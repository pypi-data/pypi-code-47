import datetime
import tkinter
import matplotlib
import platform
if platform.system() not in ['Linux', 'Darwin'] and not platform.system().startswith('CYGWIN'):
    matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from IPython import display,get_ipython

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib import colors as mcolors
import numpy as np


from scipy import ndimage
import pylab
import PIL
from PIL import Image
import cv2
import os
import pickle
import codecs
import glob
import math

from ..backend.common import get_time_suffix
from ..backend.image_common import *

__all__ = ['tile_rgb_images','loss_metric_curve','steps_histogram','is_notebook']

def is_notebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter

def tile_rgb_images(*imgs, row=3,save_path=None,imshow=False):
    fig = plt.gcf()
    fig.set_size_inches(len(imgs) * 2, row * 2)
    plt.clf()
    plt.ioff()  # is not None:
    suffix=get_time_suffix()

    for m in range(row * len(imgs)):
        plt.subplot(row, len(imgs), m + 1)
        img = array2image((imgs[int(m % len(imgs))][int(m // len(imgs))]))
        plt.imshow(img, interpolation="nearest", animated=True)
        plt.axis("off")
    filename =save_path.format(suffix)
    plt.savefig(filename, bbox_inches='tight')
    if imshow==True:
        plSize = fig.get_size_inches()
        fig.set_size_inches((int(round(plSize[0]*0.75,0)), int(round(plSize[1]*0.75,0))))
        if is_notebook():
            display.display(plt.gcf())
        else:
            plt.ion()
            plt.show()



def loss_metric_curve(losses,metrics,sample_collected=None, legend=None,calculate_base='epoch',max_iteration=None,save_path=None,imshow=False):
    fig = plt.gcf()
    fig.set_size_inches(18, 8)
    plt.clf()
    plt.ioff()  # is not None:
    collected_samples=[]
    if sample_collected is not None and len(sample_collected)>0:
        sample_collected=np.array(sample_collected)
        sample=np.arange(len(sample_collected))
        collected_samples=sample[sample_collected==1]


    plt.subplot(2, 2,1)
    if isinstance(losses,dict):
        if len(losses['total_losses']) == len(collected_samples) > 0:
            plt.plot(collected_samples, losses['total_losses'])
        else:
            plt.plot(losses['total_losses'])
        plt.legend(['loss'], loc='upper left')
    elif  isinstance(losses,list):
        for item in losses:
            if len(item['total_losses'])==len(collected_samples)>0 :
                plt.plot(collected_samples,np.array(item['total_losses']))
            else:
                plt.plot(np.array(item['total_losses']))
        if legend is not None:
            plt.legend([ 'loss {0}'.format(lg)for lg in legend], loc='upper left')
        else:
            plt.legend([ 'loss {0}'.format(i)for i in range(len(losses))], loc='upper left')

    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel(calculate_base)

    if max_iteration is not None:
        plt.xlim(0, max_iteration)


    plt.subplot(2, 2, 2)
    if isinstance(metrics,dict):
        for k, v in metrics.items():
            if len(metrics[k]) == len(collected_samples) > 0:
                plt.plot(collected_samples,metrics[k])
            else:
                plt.plot(metrics[k])
        plt.legend(list(metrics.keys()), loc='upper left')
    elif  isinstance(metrics,list):
        legend_list=[]
        for i in range(len(metrics)):
            item=metrics[i]
            for k, v in item.items():
                if len(item[k]) == len(collected_samples) > 0:
                    plt.plot(collected_samples,np.array(item[k]))
                else:
                    plt.plot(np.array(item[k]))
                if legend is not None:
                    legend_list.append([ 'metric {0} {1}'.format(k,legend[i])])
                else:
                    legend_list.append([ 'metric {0} {1}'.format(k,i)])
        plt.legend(legend_list, loc='upper left')


    plt.title('model metrics')
    plt.ylabel('metrics')
    plt.xlabel(calculate_base)

    if max_iteration is not None:
        plt.xlim(0, max_iteration)

    if save_path is not None:
        plt.savefig(save_path, bbox_inches='tight')
    if imshow == True:
        if is_notebook():
            display.display(plt.gcf())
        else:
            plt.ion()
            plt.show()


def polygon_under_graph(xlist, ylist):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (xlist, ylist) line graph.  Assumes the xs are in ascending order.
    """
    return [(xlist[0], 0.), *zip(xlist, ylist), (xlist[-1], 0.)]
default_bins=[]
default_bins.extend(np.arange(-0.02, 0.02, 0.002).tolist())
default_bins.extend(np.arange(-0.005, 0.005, 0.0005).tolist())
default_bins.extend(np.arange(-0.0002, 0.0002, 0.00002).tolist())
default_bins=sorted(list(set(default_bins)))

def steps_histogram(grads,weights,bins=None,size=(18, 8),inteval=1,save_path=None,imshow=False):
    global default_bins
    if bins is None:
        bins=default_bins
    fig = plt.figure(figsize=size)
    fig.patch.set_facecolor('white')
    ax= fig.add_subplot(1, 2, 1, projection = '3d')
    #ax = fig.gca(projection='3d')
    # Make verts a list, verts[i] will be a list of (x,y) pairs defining polygon i
    verts = []
    # The ith polygon will appear on the plane y = zs[i]
    zs = np.arange(len(grads))
    new_zs=[]
    max_frequency=0
    for i in range(len(grads)):
        if i%inteval==0:
            a, b = np.histogram(grads[i].reshape([-1]), bins)
            ys = a
            xs = b[:-1]
            new_zs.append(zs[i])
            max_frequency=max(ys.max(),max_frequency)
            verts.append(polygon_under_graph(xs, ys))

    poly = PolyCollection(verts, facecolors=['r', 'g', 'b', 'y'], alpha=.4)
    ax.add_collection3d(poly, zs=new_zs, zdir='y')
    override = {'fontsize': 'small', 'verticalalignment': 'top', 'horizontalalignment': 'center'}
    ax.set_xlabel('gradients', override)
    ax.set_ylabel('steps', override)
    ax.set_zlabel('frequency', override)
    ax.set_xlim(min(bins), max(bins))
    ax.set_ylim(0, int(max(new_zs)))
    ax.set_zlim(0,1000)
    plt.title('Gradients Histogram')

    ax = fig.add_subplot(1, 2, 2, projection='3d')

    bins=[b*10 for b in bins]
 
    # Make verts a list, verts[i] will be a list of (x,y) pairs defining polygon i
    verts = []
    # The ith polygon will appear on the plane y = zs[i]
    zs = np.arange(len(weights))
    new_zs=[]
    max_frequency = 0
    for i in range(len(weights)):
        if  i%inteval==0:
            a, b = np.histogram(weights[i].reshape([-1]), bins)
            ys = a
            xs = b[:-1] + 0.001
            new_zs.append(zs[i])
            max_frequency = max(ys.max(), max_frequency)
            verts.append(polygon_under_graph(xs, ys))

    poly = PolyCollection(verts, facecolors=['r', 'g', 'b', 'y'], alpha=.4)
    ax.add_collection3d(poly, zs=new_zs, zdir='y')
    override = {'fontsize': 'small', 'verticalalignment': 'top', 'horizontalalignment': 'center'}
    ax.set_xlabel('weights', override)
    ax.set_ylabel('steps', override)
    ax.set_zlabel('frequency', override)

    ax.set_xlim(min(bins), max(bins))
    ax.set_ylim(0, int(max(new_zs)))
    ax.set_zlim(0, int(max_frequency*1.1))
    plt.title('Weights Histogram')

    if save_path is not None:
        plt.savefig(save_path, bbox_inches='tight')
    if imshow == True:
        if is_notebook():
            display.display(plt.gcf())
        else:
            plt.ion()
            plt.show()



def centerloss_plot(feat, labels):
    plt.ion()
    c = ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff',
         '#ff00ff', '#990000', '#999900', '#009900', '#009999']
    plt.clf()
    for i in range(10):
        plt.plot(feat[labels == i, 0], feat[labels == i, 1], '.', c=c[i])
    plt.legend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], loc = 'upper right')
    plt.xlim(xmin=-8,xmax=8)
    plt.ylim(ymin=-8,ymax=8)
    plt.draw()
    plt.pause(0.001)



