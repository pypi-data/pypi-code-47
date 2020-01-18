from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
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
from .tensorflow_activations import get_activation
from itertools import repeat
import inspect


from ..backend.common import *
from ..backend.tensorflow_backend import *

_tf_data_format= 'channels_last'

__all__ = ['InputLayer','Dense', 'Flatten', 'Concatenate','Concate','Add','Subtract', 'Conv1d', 'Conv2d', 'Conv3d',  'TransConv2d', 'TransConv3d','Reshape','Dropout','Lambda','SoftMax']


_session = get_session()

_device='CPU'
for device in device_lib.list_local_devices():
      if tf.DeviceSpec.from_string(device.name).device_type == 'GPU':
          _device='GPU'
          break

_epsilon = _session.epsilon


def _ntuple(n):
    def parse(x):
        if isinstance(x, collections.Iterable):
            return x
        return tuple(repeat(x, n))

    return parse


_single = _ntuple(1)
_pair = _ntuple(2)
_triple = _ntuple(3)
_quadruple = _ntuple(4)

def get_layer_repr(layer):
    # We treat the extra repr like the sub-module, one item per line
    extra_lines = []
    if hasattr( layer, 'extra_repr' ) and callable( layer.extra_repr ):
        extra_repr = layer.extra_repr()
        # empty string will be split into list ['']
        if extra_repr:
            extra_lines = extra_repr.split('\n')
    child_lines = []
    if isinstance(layer,(tf.keras.Model,tf.keras.Sequential)) and layer.layers is not None:
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

class InputLayer(tf.keras.layers.InputLayer):
    def __init__(self, input_shape: (list, tuple,int) = None,batch_size=None,name='',**kwargs):
        if isinstance(input_shape, int):
            input_shape = (input_shape),
        elif isinstance(input_shape, list):
            input_shape = tuple(input_shape)
        super(InputLayer, self).__init__(input_shape=input_shape, batch_size=batch_size,  name=name, **kwargs)

    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        s = 'input_shape={input_shape},batch_size= {batch_size},name={name}'
        return s.format(**self.__dict__)


class Dense(tf.keras.layers.Dense):
    def __init__(self, output_filters, use_bias=True, activation=None,input_shape=None, **kwargs ):
        super(Dense, self).__init__(units=output_filters,use_bias=use_bias,activation=get_activation(activation),**kwargs)
        inp_shape = kwargs.get('input_shape')
        if inp_shape is not None:
            self.input_spec = inp_shape

    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'output_shape={units}, use_bias={use_bias},'+'activation={0}'.format(None if self.activation is None else self.activation.__name__)
        return s.format(**self.__dict__)


class Flatten(tf.keras.layers.Flatten):
    def __init__(self ):
        super(Flatten, self).__init__()
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        return ''



class Concate(tf.keras.layers.Concatenate):
    def __init__(self, axis=-1 ):
        super(Concate, self).__init__(axis=axis)
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        return ''

Concatenate=Concate


class Add(tf.keras.layers.Add):
    def __init__(self ):
        super(Add, self).__init__()
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        return ''


class Subtract(tf.keras.layers.Subtract):
    def __init__(self ):
        super(Subtract, self).__init__()
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        return ''



class SoftMax(tf.keras.layers.Softmax):
    def __init__(self ,axis=-1, **kwargs):
        super(SoftMax, self).__init__(axis=-1, **kwargs)
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repe(self):
        return 'axis={0}'.format(self.axis)





class Conv1d(tf.keras.layers.Conv1D):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None ,auto_pad=True,padding_mode=PaddingMode.replicate, activation=None, use_bias=False, dilation=1,
                 groups=1, name=None, **kwargs):
        kernel_size = _single(kernel_size)
        strides = _single(strides)
        dilation = _single(dilation)
        activation = get_activation(activation)
        super(Conv1d, self).__init__(self,filters=num_filters, kernel_size=kernel_size, strides=strides,
                                     padding='same'if auto_pad else 'valid', dilation_rate=dilation, activation=activation, use_bias=use_bias,data_format='channels_last',name=name,**kwargs)
        self.groups=groups
        inp_shape = kwargs.get('input_shape')
        if inp_shape is not None:
            self.input_spec = inp_shape
    @property
    def num_filters(self):
        return super().filters

    @num_filters.setter
    def num_filters(self,value):
        self.filters=_single(value)

    @property
    def auto_pad(self):
        return super().padding=='same'

    @auto_pad.setter
    def auto_pad(self, value):
        self.padding ='same'if value else 'valid'

    @property
    def dilation(self):
        return super().dilation_rate

    @dilation.setter
    def dilation(self, value):
        self.dilation_rate =_single(value)


    def __repr__(self):
        return get_layer_repr(self)


    def extra_repr(self):
        s = 'kernel_size={kernel_size}, num_filters={num_filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)




class Conv2d(tf.keras.layers.Conv2D):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, name=None,**kwargs):
        kernel_size = _pair(kernel_size)
        strides = _pair(strides)
        dilation = _pair(dilation)
        activation = get_activation(activation)
        super(Conv2d, self).__init__(filters=num_filters, kernel_size=kernel_size, strides=strides,  padding='same'if auto_pad else 'valid', dilation_rate=dilation, activation=activation, use_bias=use_bias,data_format='channels_last',name=name,**kwargs)
        self.groups=groups
        inp_shape=kwargs.get('input_shape')
        if inp_shape is not None:
            self.input_spec=inp_shape
    @property
    def num_filters(self):
        return super().filters

    @num_filters.setter
    def num_filters(self,value):
        self.filters=_pair(value)

    @property
    def auto_pad(self):
        return super().padding=='same'

    @auto_pad.setter
    def auto_pad(self, value):
        self.padding ='same'if value else 'valid'

    @property
    def dilation(self):
        return super().dilation_rate

    @dilation.setter
    def dilation(self, value):
        self.dilation_rate =_pair(value)
    def __repr__(self):
        return get_layer_repr(self)


    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)




class Conv3d(tf.keras.layers.Conv3D):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, name=None, **kwargs):
        kernel_size = _triple(kernel_size)
        strides = _triple(strides)
        dilation = _triple(dilation)
        activation = get_activation(activation)
        super(Conv3d, self).__init__(filters=num_filters, kernel_size=kernel_size, strides=strides,
                                     padding='same' if auto_pad else 'valid', dilation_rate=dilation,
                                     activation=activation, use_bias=use_bias, data_format='channels_last',name=name, **kwargs)
        self.groups=groups

        inp_shape = kwargs.get('input_shape')
        if inp_shape is not None:
            self.input_spec = inp_shape
    @property
    def num_filters(self):
        return super().filters

    @num_filters.setter
    def num_filters(self, value):
        self.filters = _triple(value)

    @property
    def auto_pad(self):
        return super().padding == 'same'

    @auto_pad.setter
    def auto_pad(self, value):
        self.padding = 'same' if value else 'valid'

    @property
    def dilation(self):
        return super().dilation_rate

    @dilation.setter
    def dilation(self, value):
        self.dilation_rate = _triple(value)

    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)




class TransConv2d(tf.keras.layers.Conv2DTranspose):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1,  name=None,**kwargs):
        kernel_size = _pair(kernel_size)
        strides = _pair(strides)
        dilation = _pair(dilation)
        activation = get_activation(activation)
        super(TransConv2d, self).__init__( filters=num_filters, kernel_size=kernel_size, strides=strides,input_shape=input_shape,
                                     padding='same' if auto_pad else 'valid', dilation_rate=dilation,
                                     activation=activation, use_bias=use_bias,data_format='channels_last',name=name, **kwargs)
        self.groups = groups


        @property
        def num_filters(self):
            return super().filters

        @num_filters.setter
        def num_filters(self, value):
            self.filters = _pair(value)

        @property
        def auto_pad(self):
            return super().padding == 'same'

        @auto_pad.setter
        def auto_pad(self, value):
            self.padding = 'same' if value else 'valid'

        @property
        def dilation(self):
            return super().dilation_rate

        @dilation.setter
        def dilation(self, value):
            self.dilation_rate = _pair(value)
    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)



class TransConv3d(tf.keras.layers.Conv3DTranspose):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, name=None, **kwargs):
        kernel_size = _triple(kernel_size)
        strides = _triple(strides)
        dilation = _triple(dilation)
        activation = get_activation(activation)
        super(TransConv3d, self).__init__( filters=num_filters, kernel_size=kernel_size, strides=strides,input_shape=input_shape,
                                     padding='same' if auto_pad else 'valid', dilation_rate=dilation,
                                     activation=activation, use_bias=use_bias,data_format='channels_last',name=name, **kwargs)
        self.groups = groups

        @property
        def num_filters(self):
            return super().filters

        @num_filters.setter
        def num_filters(self, value):
            self.filters = _triple(value)

        @property
        def auto_pad(self):
            return super().padding == 'same'

        @auto_pad.setter
        def auto_pad(self, value):
            self.padding = 'same' if value else 'valid'

        @property
        def dilation(self):
            return super().dilation_rate

        @dilation.setter
        def dilation(self, value):
            self.dilation_rate = _triple(value)
    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)




class Lambda(tf.keras.layers.Lambda):
    """
    Applies a lambda function on forward()
    Args:
        lamb (fn): the lambda function
    """

    def __init__(self, function):
        super(Lambda, self).__init__(function=function, output_shape=None, arguments={})
        self.function = function

    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'function={0}'.format("".join(inspect.getsourcelines(self.function)[0]))



class Reshape(tf.keras.layers.Reshape):
    def __init__(self, target_shape, **kwargs ):
        super(Reshape, self).__init__(target_shape, **kwargs)
    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'target_shape={0}'.format(self.target_shape)


class Dropout(tf.keras.layers.Dropout):
    def __init__(self, dropout_rate=0 ):
        super(Dropout, self).__init__(dropout_rate)
    @property
    def dropout_rate(self):
        return self.rate
    @dropout_rate.setter
    def dropout_rate(self,value):
        self.rate=value

    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'dropout_rate={0}'.format(self.dropout_rate)




