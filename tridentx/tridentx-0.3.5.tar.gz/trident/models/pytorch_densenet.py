
from __future__ import division
from __future__ import print_function
import math
import os
import inspect
import numpy as np
from collections import *
from functools import partial
import uuid
from copy import copy, deepcopy
from collections import deque
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
from torch.nn.parameter import Parameter
from torch._six import container_abcs
from itertools import repeat


from ..backend.common import *
from ..backend.pytorch_backend import to_numpy,to_tensor,Layer,Sequential,Input
from ..layers.pytorch_layers import *
from ..layers.pytorch_activations import  get_activation,Identity,Relu
from ..layers.pytorch_normalizations import get_normalization,BatchNorm2d
from ..layers.pytorch_blocks import *
from ..layers.pytorch_pooling import *
from ..optims.pytorch_trainer import *
from ..data.image_common import *
from ..data.utils import download_file_from_google_drive

__all__ = ['DenseNet','DenseNet121']

_session = get_session()
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_epsilon=_session.epsilon
_trident_dir=_session.trident_dir

dirname = os.path.join(_trident_dir, 'models')
if not os.path.exists(dirname):
    try:
        os.makedirs(dirname)
    except OSError:
        # Except permission denied and potential race conditions
        # in multi-threaded environments.
        pass



def conv_block(growth_rate, name):
    return ConcateBlock(Identity(),
                 Sequential(
                     BatchNorm2d(name=name + '_0_bn'),
                     Relu(name=name + '_0_relu'),
                     Conv2d_Block((1,1),4 * growth_rate,strides=1,auto_pad=True,padding_mode=PaddingMode.zero,use_bias=False,  name=name + '_1_conv'),
                    Conv2d((3,3),growth_rate,strides=1,auto_pad=True,padding_mode=PaddingMode.zero,use_bias=False, name=name + '_2_conv')))

def dense_block(blocks,growth_rate=32,dropout_rate=0.2, name=''):
    """A dense block.
    # Arguments
        x: input tensor.
        blocks: integer, the number of building blocks.
        name: string, block label.
    # Returns
        output tensor for the block.
    """
    items = OrderedDict()
    for i in range(blocks):
        items[name + '_block' + str(i + 1)] = conv_block(growth_rate, name=name + '_block' + str(i + 1))
    items['dropout'] = Dropout(dropout_rate=dropout_rate)

    return Sequential(items)


def transition_block(reduction, name):
    items=OrderedDict()
    items[name + '_0_bn']=BatchNorm2d(name=name + '_0_bn')
    items[name + '_0_relu']=Relu(name=name + '_0_relu')
    items[name + '_conv']=Conv2d((1, 1),num_filters=None, filter_rate=reduction, strides=1, auto_pad=True,padding_mode=PaddingMode.zero,use_bias=False, name=name + '_conv')
    items[name + '_pool']=AvgPool2d(2,2, name=name + '_pool')
    return Sequential(items)



def DenseNet(blocks,
             growth_rate=32,
             include_top=True,
             pretrained=True,
             input_shape=(3,224,224),
             num_classes=1000,
             name='',
             **kwargs):
    """Instantiates the DenseNet architecture.
    Optionally loads weights pre-trained on ImageNet.
    Note that the data format convention used by the model is
    the one specified in your Keras config at `~/.keras/keras.json`.
    # Arguments
        blocks: numbers of building blocks for the four dense layers.
        include_top: whether to include the fully-connected
            layer at the top of the network.
        weights: one of `None` (random initialization),
              'imagenet' (pre-training on ImageNet),
              or the path to the weights file to be loaded.
        input_tensor: optional Keras tensor
            (i.e. output of `layers.Input()`)
            to use as image input for the model.
        input_shape: optional shape tuple, only to be specified
            if `include_top` is False (otherwise the input shape
            has to be `(224, 224, 3)` (with `'channels_last'` data format)
            or `(3, 224, 224)` (with `'channels_first'` data format).
            It should have exactly 3 inputs channels,
            and width and height should be no smaller than 32.
            E.g. `(200, 200, 3)` would be one valid value.
        pooling: optional pooling mode for feature extraction
            when `include_top` is `False`.
            - `None` means that the output of the model will be
                the 4D tensor output of the
                last convolutional block.
            - `avg` means that global average pooling
                will be applied to the output of the
                last convolutional block, and thus
                the output of the model will be a 2D tensor.
            - `max` means that global max pooling will
                be applied.
        classes: optional number of classes to classify images
            into, only to be specified if `include_top` is True, and
            if no `weights` argument is specified.
    # Returns
        A Keras model instance.
    # Raises
        ValueError: in case of invalid argument for `weights`,
            or invalid input shape.
    """


    densenet=Sequential()
    densenet.add_module('conv1/conv',Conv2d_Block((7,7),64,strides=2,use_bias=False,auto_pad=True,padding_mode=PaddingMode.zero,activation='relu',normalization='batch', name='conv1/conv'))
    densenet.add_module('maxpool', (MaxPool2d((3, 3), strides=2, auto_pad=True, padding_mode=PaddingMode.zero)))
    densenet.add_module('denseblock1', dense_block(blocks[0],growth_rate=growth_rate, name='denseblock1'))
    densenet.add_module('transitiondown2', transition_block(0.5, name='transitiondown2'))
    densenet.add_module('denseblock2', dense_block(blocks[1], growth_rate=growth_rate,name='denseblock2'))
    densenet.add_module('transitiondown3', transition_block(0.5, name='transitiondown3'))
    densenet.add_module('denseblock3', dense_block(blocks[2], growth_rate=growth_rate,name='denseblock3'))
    densenet.add_module('transitiondown4', transition_block(0.5, name='transitiondown4'))
    densenet.add_module('denseblock4', dense_block(blocks[3], growth_rate=growth_rate,name='denseblock4'))
    densenet.add_module('classifier_bn',BatchNorm2d(name='classifier_bn'))
    densenet.add_module('classifier_relu', Relu(name='classifier_relu'))
    densenet.add_module('avg_pool', GlobalAvgPool2d(name='avg_pool'))
    if include_top:
        densenet.add_module('classifier', Dense(num_classes, activation='softmax', name='classifier'))
    densenet.name = name
    model=ImageClassificationModel(input_shape=input_shape,output=densenet)
    model.model.to(_device)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagenet_labels1.txt'), 'r',encoding='utf-8-sig') as f:
        labels = [l.rstrip() for l in f]
        model.class_names = labels
    model.preprocess_flow = [resize((input_shape[2], input_shape[1]), keep_aspect=True), normalize(0, 255),  normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]
    # model.summary()
    return model





def DenseNet121(include_top=True,
             pretrained=True,
             input_shape=(3,224,224),
             classes=1000,
             **kwargs):
    if input_shape is not None and len(input_shape)==3:
        input_shape=tuple(input_shape)

    densenet121 =DenseNet([6, 12, 24, 16], include_top=include_top, pretrained=True,input_shape=input_shape, num_classes=classes,name='densenet121')
    if pretrained==True:
        download_file_from_google_drive('16N2BECErDMRTV5JqESEBWyylXbQmKAIk',dirname,'densenet121.pth')
        recovery_model=torch.load(os.path.join(dirname,'densenet121.pth'))
        recovery_model.to(_device)
        if include_top==False:
            recovery_model.__delitem__(-1)
        else:
            if classes!=1000:
                new_fc = Dense(classes, activation='softmax', name='classifier')
                new_fc.input_shape=recovery_model.classifier.input_shape
                recovery_model.classifier=new_fc
        densenet121.model=recovery_model
    return densenet121