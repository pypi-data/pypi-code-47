from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import math
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
from ..backend.pytorch_backend import to_numpy,to_tensor,Layer,Sequential
from .pytorch_layers import *
from .pytorch_activations import  get_activation
from .pytorch_normalizations import get_normalization

__all__ = ['Conv2d_Block','GcdConv2d_Block','TransConv2d_Block','GcdConv2d_Block_1','Classifier1d','ShortCut2d']

_session = get_session()
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_epsilon=_session.epsilon


def _ntuple(n):
    def parse(x):
        if isinstance(x, container_abcs.Iterable):
            return x
        return tuple(repeat(x, n))

    return parse


_single = _ntuple(1)
_pair = _ntuple(2)
_triple = _ntuple(3)
_quadruple = _ntuple(4)

class Conv2d_Block(Layer):
    def __init__(self, kernel_size=(3,3), num_filters=32, strides=1, auto_pad=True,activation='relu6',
                 normalization='instance',  use_bias=False,dilation=1, groups=1,add_noise=False,noise_intensity=0.005,dropout_rate=0):
        super(Conv2d_Block, self).__init__()
        self.kernel_size = kernel_size
        self.num_filters = num_filters
        self.strides = strides
        self.auto_pad = auto_pad
        self.padding=0
        # if self.auto_pad == False:
        #     self.padding = 0
        # else:
        #     self.padding= tuple([n-2 for n in  list(self.kernel_size)]) if hasattr(self.kernel_size,'__len__') else self.kernel_size-2

        self.use_bias = use_bias
        self.dilation = dilation
        self.groups = groups

        self.add_noise = False
        self.noise_intensity=noise_intensity
        self.dropout_rate=dropout_rate
        self.conv=None
        self.norm = get_normalization(normalization)
        self.activation=get_activation(activation)
        self.droupout = None
    def build(self, input_shape):
        if self._built == False or self.conv is None:
            self.conv =Conv2d(kernel_size=self.kernel_size, num_filters=self.num_filters, strides=self.strides,auto_pad=self.auto_pad, padding=self.padding,activation=None, use_bias=self.use_bias,dilation=self.dilation, groups=self.groups).to(_device)
            self.conv.input_shape = input_shape
            #self._modules['conv'] = conv
            output_shape = self._input_shape.clone().tolist()
            output_shape[0] = self.num_filters
            if self.norm != None:
                self.norm.input_shape=output_shape
            self.to(self.device)
    def forward(self, *x):
        x=enforce_singleton(x)
        if self.add_noise==True and self.training == True:
            noise = self.noise_intensity * torch.randn_like(x, dtype=torch.float32)
            x=x+noise
        x = self.conv(x)
        if self.norm is not None:
            x = self.norm(x)
        if self.activation is not None:
            x = self.activation(x)
        if self.dropout_rate > 0:
            x = F.dropout(x, p=self.dropout_rate, training=self.training)
        return x



    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {num_filters}, strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], nn.Module):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        return s.format(**self.__dict__)

class TransConv2d_Block(Layer):
    def __init__(self, kernel_size=(3,3), num_filters=32, strides=1, auto_pad=True,activation='relu6',
                 normalization='instance',  use_bias=False, dilation=1, groups=1,add_noise=False,noise_intensity=0.005,dropout_rate=0):
        super(TransConv2d_Block, self).__init__()
        self.kernel_size = kernel_size
        self.num_filters = num_filters
        self.strides = strides
        self.auto_pad = auto_pad
        self.padding=0
        self.use_bias = use_bias
        self.dilation = dilation
        self.groups = groups
        self.add_noise = False
        self.noise_intensity = noise_intensity
        self.dropout_rate=dropout_rate
        self.conv =None
        self.norm = get_normalization(normalization)
        self.activation=get_activation(activation)
        self.droupout = None
    def build(self, input_shape):
        if self._built == False or self.conv is None:
            self.conv = TransConv2d(kernel_size=self.kernel_size, num_filters=self.num_filters, strides=self.strides,
                               auto_pad=self.auto_pad, padding=self.padding, activation=None, use_bias=self.use_bias,
                               dilation=self.dilation, groups=self.groups).to(_device)
            self.conv.input_shape = input_shape
            # self._modules['conv'] = conv
            # self.conv = conv
            output_shape = self._input_shape.clone().tolist()
            output_shape[0] = self.num_filters
            if self.norm != None:
                self.norm.input_shape=output_shape
            self._built=True
            self.to(self.device)
    def forward(self, *x):
        x=enforce_singleton(x)
        if self.add_noise==True and self.training == True:
            noise = self.noise_intensity * torch.randn_like(x, dtype=torch.float32)
            x=x+noise
        x=self.conv(x)
        if self.norm!=None:
            x = self.norm(x)
        if self.activation != None:
            x = self.activation(x)

        if self.dropout_rate > 0:
            x = F.dropout(x, p=self.dropout_rate, training=self.training)
        return x
    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {num_filters}, strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], nn.Module):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()

        return s.format(**self.__dict__)



class GcdConv2d_Block(Layer):
    def __init__(self, kernel_size=(3,3), num_filters=32, strides=1, auto_pad=True,divisor_rank=0,activation='relu6',normalization=None,init=None, use_bias=False, init_bias=0, dilation=1, groups=1,add_noise=False,noise_intensity=0.005,dropout_rate=0,
                 weights_contraint=None):
        super(GcdConv2d_Block, self).__init__()
        self.kernel_size = kernel_size
        self.num_filters = num_filters
        self.strides = _pair(strides)
        self.auto_pad = auto_pad

        self.init = init
        self.use_bias = use_bias
        self.init_bias = init_bias
        self.dilation = dilation
        self.groups = groups
        self.weights_contraint = weights_contraint
        self.add_noise = False
        self.noise_intensity = noise_intensity
        self.dropout_rate=dropout_rate
        self.conv =None
        self.droupout=None
        self.divisor_rank=divisor_rank

        self.activation = get_activation(activation)
        self.norm = get_normalization(normalization)
    def build(self, input_shape):
        if self._built == False or self.conv is None:
            conv= GcdConv2d(self.kernel_size, input_filters=self.input_filters, num_filters=self.num_filters, strides=self.strides,
                           auto_pad=self.auto_pad, activation=None, init=None, use_bias=self.use_bias, init_bias=0,divisor_rank=self.divisor_rank,
                           dilation=self.dilation).to(self.device)
            conv.input_shape = input_shape
            self._modules['conv'] = conv
            self.conv = conv
            output_shape = self._input_shape.clone().tolist()
            output_shape[0] = self.num_filters
            if self.norm != None:
                self.norm.input_shape=output_shape
            self._built = True
            self.to(self.device)
    def forward(self, *x):
        x=enforce_singleton(x)
        if self.add_noise==True and self.training == True:
            noise = self.noise_intensity * torch.randn_like(x, dtype=torch.float32)
            x=x+noise
        #dynamic generation
        x = self.conv(x)
        if self.activation is not None:
            x = self.activation()(x)

        if self.dropout_rate > 0:
            x = F.dropout(x, p=self.dropout_rate, training=self.training)
        if torch.isnan(x).any():
            print(self._get_name() + '  nan detected!!')
        return x

    def extra_repr(self):
        s = ('{input_filters}, {num_filters}, kernel_size={kernel_size}'
             ', stride={stride}')

        return s.format(**self.__dict__)

class GcdConv2d_Block_1(Layer):
    def __init__(self, kernel_size=(3,3), num_filters=32, strides=1, auto_pad=True,divisor_rank=0,activation='relu6', normalization=None, self_norm=True,is_shuffle=False,init=None, use_bias=False, init_bias=0, dilation=1, groups=1,add_noise=False,noise_intensity=0.005,dropout_rate=0,
                 weights_contraint=None):
        super(GcdConv2d_Block_1, self).__init__()
        self.kernel_size = kernel_size
        self.num_filters = num_filters
        self.strides = _pair(strides)
        self.auto_pad = auto_pad

        self.init = init
        self.use_bias = use_bias
        self.init_bias = init_bias
        self.dilation = dilation
        self.groups = groups
        self.weights_contraint = weights_contraint
        self.add_noise = False
        self.noise_intensity = noise_intensity
        self.dropout_rate=dropout_rate
        self.activation = get_activation(activation)
        self.self_norm=self_norm
        self.is_shuffle=is_shuffle
        self.norm = get_normalization(normalization)
        self.normalization =normalization
        self.conv =None
        self.droupout=None
        self.divisor_rank=divisor_rank
    def build(self, input_shape):
        if self._built == False or self.conv is None:

            conv = GcdConv2d_1(self.kernel_size, input_filters=self.input_filters, num_filters=self.num_filters,
                                    strides=self.strides, auto_pad=self.auto_pad, activation=None, init=None,
                                    use_bias=self.use_bias, init_bias=0, divisor_rank=self.divisor_rank,
                                    self_norm=self.self_norm, is_shuffle=self.is_shuffle, dilation=self.dilation).to(self.device)
            conv.input_shape = input_shape
            self._modules['conv'] = conv
            self.conv = conv
            output_shape = self._input_shape.clone().tolist()
            output_shape[0] = self.num_filters
            if self.norm != None:
                self.norm.input_shape=output_shape
            self._built = True
            self.to(self.device)
    def forward(self, *x):
        x=enforce_singleton(x)
        if self.add_noise == True and self.training == True:
            noise = self.noise_intensity * torch.randn_like(x, dtype=torch.float32)
            x = x + noise
        x = self.conv(x)

        if self.normalization is not None:
            x =self.norm(x)

        if self.activation is not None:
            x = self.activation(x)
        if self.dropout_rate > 0:
            x = F.dropout(x, p=self.dropout_rate, training=self.training)

        return x

    def extra_repr(self):
        s = ('kernel_size={kernel_size}, {num_filters}, strides={strides},activation={activation} ')

        return s.format(**self.__dict__)



class Highway(Layer):

    """Highway module.
    In highway network, two gates are added to the ordinal non-linear
    transformation (:math:`H(x) = activate(W_h x + b_h)`).
    One gate is the transform gate :math:`T(x) = \\sigma(W_t x + b_t)`, and the
    other is the carry gate :math:`C(x)`.
    For simplicity, the author defined :math:`C = 1 - T`.
    Highway module returns :math:`y` defined as
    .. math::
        y = activate(W_h x + b_h) \\odot \\sigma(W_t x + b_t) +
        x \\odot(1 - \\sigma(W_t x + b_t))
    The output array has the same spatial size as the input. In order to
    satisfy this, :math:`W_h` and :math:`W_t` must be square matrices.
    Args:
        in_out_features (int): Dimension of input and output vectors.
        bias (bool): If ``True``, then this function does use the bias.
        activate: Activation function of plain array. :math:`tanh` is also
            available.
    See:
        `Highway Networks <https://arxiv.org/abs/1505.00387>`_.
    """

    def __init__(self, in_out_features, bias=True, activate=F.relu):
        super(Highway, self).__init__()
        self.in_out_features = in_out_features
        self.bias = bias
        self.activate = activate

        self.plain = nn.Linear(self.in_out_features, self.in_out_features, bias=bias)
        self.transform = nn.Linear(self.in_out_features, self.in_out_features, bias=bias)


    def forward(self, *x):
        """Computes the output of the Highway module.
        Args:
            x (~torch.Tensor): Input variable.
        Returns:
            Variable: Output variable. Its array has the same spatial size and
            the same minibatch size as the input array.
        """
        x=enforce_singleton(x)
        out_plain = self.activate(self.plain(x))
        out_transform = torch.sigmoid(self.transform(x))
        x = out_plain * out_transform + x * (1 - out_transform)
        return x


class Classifier1d(Layer):
    def __init__(self, num_classes=10, is_multilable=False, classifier_type=ClassfierType.dense, **kwargs):
        super(Classifier1d, self).__init__()
        self.classifier_type = classifier_type
        self.num_classes = num_classes
        self.is_multilable = is_multilable
        self.dense=None
        self.global_avgpool=None
        self.conv1x1=None
    def build(self, input_shape):
        if self._built == False or self.conv1x1 is None:
            if self.classifier_type == 'global_avgpool':
                if self.input_filters != self.num_classes:
                    if self.conv1x1 is None:
                        self.conv1x1 = Conv2d((1, 1),  num_filters=self.num_classes, strides=1,padding=0, activation=None, use_bias=False).to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))
                        self.conv1x1.input_shape=input_shape
            self._built = True
    def forward(self, *x):
        x = enforce_singleton(x)
        if self.classifier_type == 'dense' :
            x = x.view(x.size(0),x.size(1), -1)
            x =torch.mean(x, -1, False)
            if self.dense is None:
                self.dense = nn.Linear(x.size(1), self.num_classes).to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))
            x=self.dense(x)

        elif self.classifier_type == 'global_avgpool':
            if len(self._input_shape)!=3:
                raise  ValueError("GlobalAvgPool2d only accept BCHW shape")
            if self.conv1x1 is not None:
                x=self.conv1x1(x)
            if self.global_avgpool is None:
                self.global_avgpool = nn.AdaptiveAvgPool2d(output_size=1)
            x=self.global_avgpool(x)
            x = x.view(x.size(0), x.size(1))
        x = torch.sigmoid(x)
        return torch.softmax(x,dim=1)

    def extra_repr(self):
        s = ('{num_classes}, classifier_type={classifier_type}')
        return s.format(**self.__dict__)
class ShortCut2d(Layer):
    def __init__(self, layer_defs:OrderedDict):
        """

        Parameters
        ----------
        layer_defs : object
        """
        super(ShortCut2d, self).__init__()
        self.layer_defs = layer_defs
        self.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

    def forward(self, *x):
        x = enforce_singleton(x)
        idx = 0
        branches = OrderedDict()
        for k, v in self.layer_defs.items():
            if hasattr(v, '__iter__'):
                out = x
                for f in v:
                    if callable(f):
                        f.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))
                        out = f(out)
                branches[idx] = out
                idx += 1
        branch_aggregate=None
        for k, v in branches.items():
            if branch_aggregate is None:
                branch_aggregate=v
            else :
                branch_aggregate=torch.add(branch_aggregate, v)
        if x.size()==branch_aggregate.size():
            x = torch.add(x, branch_aggregate)
        return branch_aggregate




    def extra_repr(self):
        s = ('{num_classes}, classifier_type={classifier_type}')
        return s.format(**self.__dict__)


