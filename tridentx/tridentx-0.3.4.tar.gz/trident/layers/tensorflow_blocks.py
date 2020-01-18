from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from functools import reduce
from functools import wraps
import math
import collections
import itertools
import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow_core.python.keras.utils import conv_utils
from tensorflow.python.framework import tensor_shape
from tensorflow.python.keras.engine.input_spec import InputSpec
from tensorflow.python.ops import nn_ops
from tensorflow.python.client import device_lib
from tensorflow.python.keras import layers as layer_module

from tensorflow.python.keras.engine.base_layer import Layer
from tensorflow.python.keras.engine import base_layer_utils
from tensorflow.python.keras.engine import input_layer
from tensorflow.python.keras.engine import training
from tensorflow.python.keras.engine import training_utils
from tensorflow.python.keras.utils import layer_utils
from tensorflow.python.keras.utils import tf_utils

from tensorflow.python.training.tracking import layer_utils as trackable_layer_utils
from tensorflow.python.util import nest
from tensorflow.python.util import tf_inspect
from tensorflow.python.util.tf_export import keras_export

from .tensorflow_activations import get_activation, Identity
from .tensorflow_pooling import get_pooling, GlobalAvgPool2d
from .tensorflow_normalizations import get_normalization
from .tensorflow_layers import *

from itertools import repeat
import inspect

from ..backend.common import *
from ..backend.tensorflow_backend import *

_tf_data_format = 'channels_last'

__all__ = ['Conv2d_Block', 'TransConv2d_Block', 'ShortCut2d']

_session = get_session()


def get_layer_repr(layer):
    # We treat the extra repr like the sub-module, one item per line
    extra_lines = []
    if hasattr(layer, 'extra_repr') and callable(layer.extra_repr):
        extra_repr = layer.extra_repr()
        # empty string will be split into list ['']
        if extra_repr:
            extra_lines = extra_repr.split('\n')
    child_lines = []
    if isinstance(layer, (tf.keras.Model, tf.keras.Sequential)) and layer.layers is not None:
        for module in layer.layers:
            mod_str = repr(module)
            mod_str = addindent(mod_str, 2)
            child_lines.append('(' + module.name + '): ' + mod_str)
    lines = extra_lines + child_lines

    main_str = layer.__class__.__name__ + '('
    if lines:
        # simple one-liner info, which most builtin Modules will use
        if len(extra_lines) == 1 and not child_lines:
            main_str += extra_lines[0]
        else:
            main_str += '\n  ' + '\n  '.join(lines) + '\n'

    main_str += ')'
    return main_str


class Conv1d_Block(Sequential):
    def __init__(self, kernel_size=(3), num_filters=32, strides=1,input_shape=None,  auto_pad=True, activation='leaky_relu',
                 normalization=None, use_bias=False, dilation=1, groups=1, add_noise=False, noise_intensity=0.001,
                 dropout_rate=0, **kwargs):
        super(Conv1d_Block, self).__init__()
        if add_noise:
            noise = tf.keras.layers.GaussianNoise(noise_intensity)
            self.add(noise)
        self._conv = Conv1d(kernel_size=kernel_size, num_filters=num_filters, strides=strides,input_shape=input_shape, auto_pad=auto_pad,
                            activation=None, use_bias=use_bias, dilation=dilation, groups=groups)
        self.add(self._conv)

        self.norm = get_normalization(normalization)
        if self.norm is not None:
            self.add(self.norm)

        self.activation = get_activation(snake2camel(activation))
        if self.activation is not None:
            self.add(self.activation)
        if dropout_rate > 0:
            self.drop = Dropout(dropout_rate)
            self.add(self.drop)

    @property
    def conv(self):
        return self._conv

    @conv.setter
    def conv(self, value):
        self._conv = value


class Conv2d_Block(Sequential):
    def __init__(self, kernel_size=(3, 3), num_filters=32, strides=1, input_shape=None, auto_pad=True, activation='leaky_relu',
                 normalization=None, use_bias=False, dilation=1, groups=1, add_noise=False, noise_intensity=0.001,
                 dropout_rate=0, **kwargs):
        super(Conv2d_Block, self).__init__()
        if add_noise:
            self.add(tf.keras.layers.GaussianNoise(stddev=noise_intensity))
            #self.add(noise)
        self.add(Conv2d(kernel_size=kernel_size, num_filters=num_filters, strides=strides,input_shape=input_shape, auto_pad=auto_pad,
                            activation=None, use_bias=use_bias, dilation=dilation, groups=groups))
        # self.add(self._conv)

        norm = get_normalization(normalization)

        if norm is not None:
            self.add(norm)

        activation = get_activation(snake2camel(activation))
        if activation is not None:
            self.add(activation)
        if dropout_rate > 0:
            self.add(Dropout(dropout_rate))


            # self.add(self.drop)
    #
    # @property
    # def conv(self):
    #     return self._conv
    #
    # @conv.setter
    # def conv(self, value):
    #     self._conv = value

# class Conv2d_Block1(tf.keras.layers.Layer):
#     def __init__(self, k, exp, out, SE, NL, s, l2, name="Conv2d_Block1", **kwargs):
#         super(Conv2d_Block1, self).__init__(name=name, **kwargs)
#         self.k = k
#         self.exp = exp
#         self.out = out
#         self.se = SE
#         self.nl = NL
#         self.s = s
#         self.l2 = l2
#         self.conv2d = tf.keras.layers.Conv2D(filters=out, kernel_size=k, strides=s, activation=None, padding="same",
#                                              kernel_regularizer=tf.keras.regularizers.l2(l2), name="conv2d", **kwargs)
#         self.bn = tf.keras.layers.BatchNormalization(momentum=0.99, name="BatchNormalization", **kwargs)
#         self.act = _available_activation[NL]
#
#     def call(self, input):
#         output = self.conv2d(input)
#         output = self.bn(output)
#         output = self.act(output)
#         return output
#
#     def get_config(self):
#         config = {"k":self.k, "exp":self.exp, "out":self.out, "SE":self.se, "NL":self.nl, "s":self.s, "l2":self.l2}
#         base_config = super(Conv2d_Block1, self).get_config()
#         return dict(list(base_config.items()) + list(config.items()))

class Conv3d_Block(Sequential):
    def __init__(self, kernel_size=(3, 3, 3), num_filters=32, strides=1,input_shape=None, auto_pad=True, activation='leaky_relu',
                 normalization=None, use_bias=False, dilation=1, groups=1, add_noise=False, noise_intensity=0.001,
                 dropout_rate=0, **kwargs):
        super(Conv3d_Block, self).__init__()
        if add_noise:
            noise = tf.keras.layers.GaussianNoise(noise_intensity)
            self.add(noise)
        self._conv = Conv3d(kernel_size=kernel_size, num_filters=num_filters, strides=strides,input_shape=input_shape, auto_pad=auto_pad,
                            activation=None, use_bias=use_bias, dilation=dilation, groups=groups)
        self.add(self._conv)

        self.norm = get_normalization(normalization)
        if self.norm is not None:
            self.add(self.norm)

        self.activation = get_activation(snake2camel(activation))
        if self.activation is not None:
            self.add(self.activation)
        if dropout_rate > 0:
            self.drop = Dropout(dropout_rate)
            self.add(self.drop)

    @property
    def conv(self):
        return self._conv

    @conv.setter
    def conv(self, value):
        self._conv = value


#
# class TransConv1d_Block(Sequential):
#     def __init__(self, kernel_size=(3), num_filters=32, strides=1, auto_pad=True,activation='leaky_relu',normalization=None,  use_bias=False,dilation=1, groups=1,add_noise=False,noise_intensity=0.001,dropout_rate=0, **kwargs ):
#         super(TransConv1d_Block, self).__init__()
#         if add_noise:
#             noise = tf.keras.layers.GaussianNoise(noise_intensity)
#             self.add(noise)
#         self._conv = TransConv1d(kernel_size=kernel_size, num_filters=num_filters, strides=strides, auto_pad=auto_pad,
#                       activation=None, use_bias=use_bias, dilation=dilation, groups=groups)
#         self.add(self._conv)
#
#         self.norm = get_normalization(normalization)
#         if self.norm is not None:
#             self.add(self.norm)
#
#         self.activation = get_activation(activation)
#         if self.activation is not None:
#             self.add(activation)
#         if dropout_rate > 0:
#             self.drop = Dropout(dropout_rate)
#             self.add(self.drop)
#     @property
#     def conv(self):
#         return self._conv
#     @conv.setter
#     def conv(self,value):
#         self._conv=value
#
#
#     def __repr__(self):
#         return get_layer_repr(self)


class TransConv2d_Block(Sequential):
    def __init__(self, kernel_size=(3, 3), num_filters=32, strides=1,input_shape=None, auto_pad=True, activation='leaky_relu',
                 normalization=None, use_bias=False, dilation=1, groups=1, add_noise=False, noise_intensity=0.001,
                 dropout_rate=0, **kwargs):
        super(TransConv2d_Block, self).__init__()
        if add_noise:
            noise = tf.keras.layers.GaussianNoise(noise_intensity)
            self.add(noise)
        self._conv = TransConv2d(kernel_size=kernel_size, num_filters=num_filters, strides=strides,input_shape=input_shape, auto_pad=auto_pad,
                                 activation=None, use_bias=use_bias, dilation=dilation, groups=groups)
        self.add(self._conv)

        self.norm = get_normalization(normalization)
        if self.norm is not None:
            self.add(self.norm)

        self.activation = get_activation(snake2camel(activation))
        if self.activation is not None:
            self.add(self.activation)
        if dropout_rate > 0:
            self.drop = Dropout(dropout_rate)
            self.add(self.drop)

    @property
    def conv(self):
        return self._conv

    @conv.setter
    def conv(self, value):
        self._conv = value


class TransConv3d_Block(Sequential):
    def __init__(self, kernel_size=(3, 3, 3), num_filters=32, strides=1, input_shape=None,auto_pad=True, activation='leaky_relu',
                 normalization=None, use_bias=False, dilation=1, groups=1, add_noise=False, noise_intensity=0.001,
                 dropout_rate=0, **kwargs):
        super(TransConv3d_Block, self).__init__()
        if add_noise:
            noise = tf.keras.layers.GaussianNoise(noise_intensity)
            self.add(noise)
        self._conv = TransConv3d(kernel_size=kernel_size, num_filters=num_filters, strides=strides,input_shape=input_shape, auto_pad=auto_pad,
                                 activation=None, use_bias=use_bias, dilation=dilation, groups=groups)
        self.add(self._conv)

        self.norm = get_normalization(normalization)
        if self.norm is not None:
            self.add(self.norm)

        self.activation = get_activation(snake2camel(activation))
        if self.activation is not None:
            self.add(self.activation)
        if dropout_rate > 0:
            self.drop = Dropout(dropout_rate)
            self.add(self.drop)

    @property
    def conv(self):
        return self._conv

    @conv.setter
    def conv(self, value):
        self._conv = value


class Classifer1d(Sequential):
    def __init__(self, num_classes=10, is_multilable=False, classifier_type=ClassfierType.dense, **kwargs):
        super(Classifer1d, self).__init__()
        self.classifier_type = classifier_type
        self.num_classes = num_classes
        self.is_multilable = is_multilable
        if classifier_type == ClassfierType.dense:
            self.add(Flatten)
            self.add(Dense(num_classes, use_bias=False, activation='sigmoid'))
            if not is_multilable:
                self.add(SoftMax)
        elif classifier_type == ClassfierType.global_avgpool:
            self.add(Conv2d((1, 1), num_classes, strides=1, auto_pad=True, activation=None))
            self.add(GlobalAvgPool2d)
            if not is_multilable:
                self.add(SoftMax)

    def __repr__(self):
        return get_layer_repr(self)

#
# class ShortCut2d(Layer):
#     def __init__(self, *args, activation='relu', name="ShortCut2d", **kwargs):
#         """
#
#         Parameters
#         ----------
#         layer_defs : object
#         """
#         super(ShortCut2d, self).__init__(name=name, **kwargs)
#         self.activation = get_activation(activation)
#         self.has_identity = False
#         self.add_layer=Add()
#         for i in range(len(args)):
#             arg = args[i]
#             if isinstance(arg, (tf.keras.layers.Layer, list, dict)):
#                 if isinstance(arg, list):
#                     arg = Sequential(*arg)
#                     self.add(arg)
#                 elif isinstance(arg, dict) and len(args) == 1:
#                     for k, v in arg.items():
#                         if v is Identity:
#                             self.has_identity = True
#                         self.add(v)
#                 elif isinstance(arg, dict) and len(args) > 1:
#                     raise ValueError('more than one dict argument is not support.')
#                 elif arg is  Identity:
#                     self.has_identity = True
#                     self.add(arg)
#                 else:
#                     # arg.name='branch{0}'.format(i + 1)
#                     self.add(arg)
#         if len(self.layers) == 1 and self.has_identity == False:
#             self.add(Identity(name='Identity'))
#
#         # Add to the model any layers passed to the constructor.
#
#
#
#     @property
#     def layers(self):
#         return self._layers
#
#     def add(self, layer):
#         self._layers.append(layer)
#
#
#     def compute_output_shape(self, input_shape):
#         shape = input_shape
#         shape = self.layers[0].compute_output_shape(shape)
#         return shape
#
#     def call(self, inputs, training=None, mask=None):
#         x = enforce_singleton(inputs)
#         result=[]
#         if 'Identity' in self._layers:
#             result.append(x)
#         for layer in self._layers:
#             if layer is not Identity:
#                 out = layer(x)
#                 result.append(out)
#         result=self.add_layer(result)
#         if self.activation is not None:
#             result = self.activation(result)
#         return result
#
#     def __repr__(self):
#         return get_layer_repr(self)




class ShortCut2d(tf.keras.layers.Layer):
    def __init__(self, branch1,branch2, name="ShortCut2d", **kwargs):
        super(ShortCut2d, self).__init__(name=name, **kwargs)
        self.branch1=branch1
        self.branch2=branch2
        self.activation=get_activation('relu')

    def call(self, input):
      out1=self.branch1(input)
      out2 = self.branch2(input)
      out=self.activation(out1 + out2)
      return out

