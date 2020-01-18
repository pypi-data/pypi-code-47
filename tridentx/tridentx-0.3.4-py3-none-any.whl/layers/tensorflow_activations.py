from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six
from ..backend.common import *
import inspect
import numpy as np
import six
import tensorflow as tf
from tensorflow.keras import backend as K


__all__ = ['Identity','Sigmoid','Tanh','Relu','Relu6','LeakyRelu','LeakyRelu6','SmoothRelu','PRelu','Swish','Elu','HardSigmoid','HardSwish','Selu','LecunTanh','SoftSign','SoftPlus','HardTanh','Logit','LogLog','Mish','Softmax','BertGELU','GPTGELU','identity','sigmoid','tanh','relu','relu6','leaky_relu','leaky_relu6','smooth_relu','p_relu','swish','elu','hard_sigmoid','hard_swish','selu','lecun_tanh','soft_sign','soft_plus','hard_tanh','logit','log_log','mish','softmax','bert_gelu','gpt_gelu','get_activation']


def identity(x):
    return x

Identity=tf.keras.layers.Lambda(identity)

def sigmoid(x):
    return tf.nn.sigmoid(x)

Sigmoid=tf.keras.layers.Lambda(sigmoid)

def tanh(x):
    return tf.nn.tanh(x)

Tanh=tf.keras.layers.Lambda(tanh)

def relu(x,upper_limit=None):
    if upper_limit is not None and upper_limit<=0:
        raise ValueError('Upper limit should greater than 0!')
    elif upper_limit is not None:
        return K.clip(tf.nn.relu(x),0,upper_limit)
    return tf.nn.relu(x)

def relu6(x):
    return K.clip(tf.nn.relu(x),0,6)


Relu=tf.keras.layers.ReLU
Relu6=tf.keras.layers.Lambda(relu6)

def leaky_relu(x,alpha=0.01,upper_limit=None):
    if upper_limit is not None:
        return K.clip(tf.nn.leaky_relu(x,alpha), -np.inf, upper_limit)
    return tf.nn.leaky_relu(x,alpha)

def leaky_relu6(x,alpha=0.01):
    return K.clip(tf.nn.leaky_relu(x,alpha), -6, 6)

LeakyRelu=tf.keras.layers.LeakyReLU
LeakyRelu6=tf.keras.layers.Lambda(leaky_relu6)

def elu(x,alpha=0.01,upper_limit=None):
    if upper_limit is not None:
        return K.clip(tf.nn.elu(x,alpha),-np.inf,upper_limit)
    return tf.nn.elu(x,alpha)

Elu=tf.keras.layers.ELU
lrelu=leaky_relu


def smooth_relu(x,upper_limit=None):
    if upper_limit is not None:
        return K.clip(tf.math.log(1 + tf.math.exp(x)),-np.inf,upper_limit)
    return tf.math.log(1 + tf.math.exp(x))
SmoothRelu=tf.keras.layers.Lambda(smooth_relu)

def p_relu(x,upper_limit=None):
    if upper_limit is not None:
        return K.clip(tf.keras.layers.PReLU()(x),-np.inf,upper_limit)
    return tf.keras.layers.PReLU()(x)
PRelu=tf.keras.layers.PReLU

def swish(x):
    return tf.nn.sigmoid(x) * x

Swish=tf.keras.layers.Lambda(swish)


def selu(x):
    return tf.nn.selu(x)

Selu=tf.keras.layers.Lambda(selu)



def lecun_tanh(x):
    return 1.7159 * tf.nn.tanh(2/3 * x)

LecunTanh=tf.keras.layers.Lambda(lecun_tanh)

def soft_sign(x):
    return tf.nn.softsign(x)
SoftSign=tf.keras.layers.Lambda(soft_sign)

def soft_plus(x):
    return tf.nn.softplus(x)
SoftPlus=tf.keras.layers.Lambda(soft_plus)

def hard_sigmoid(x):
    return relu6(x+3)/6
HardSigmoid=tf.keras.layers.Lambda(hard_sigmoid)


def hard_tanh(x):
    return tf.keras.backend.clip(x,-1,1)
HardTanh=tf.keras.layers.Lambda(hard_tanh)


def hard_swish(x):
    return  x * hard_sigmoid(x)
HardSwish=tf.keras.layers.Lambda(hard_swish)


def logit(x):
        return tf.math.log(x / (1 - x))

Logit=tf.keras.layers.Lambda(logit)

def log_log(x):
    return  1-tf.math.exp(-tf.math.exp(x))

LogLog=tf.keras.layers.Lambda(log_log)


def softmax(x):
    return tf.nn.softmax(x)

Softmax=tf.keras.layers.Softmax

def mish(x):
    return x*tf.nn.tanh(tf.nn.softplus(x))

Mish=tf.keras.layers.Lambda(mish)




def bert_gelu(x):

  """Gaussian Error Linear Unit.
  This is a smoother version of the RELU.
  Original paper: https://arxiv.org/abs/1606.08415
  Args:
    x: float Tensor to perform activation.
  Returns:
    `x` with the GELU activation applied.
  """
  return x *  0.5 * (1.0 + tf.nn.tanh((np.sqrt(2 / np.pi) * (x + 0.044715 * tf.pow(x, 3)))))

BertGELU=tf.keras.layers.Lambda(bert_gelu)


def gpt_gelu(x):
    return 0.5 * x * (1 + tf.math.tanh(tf.math.sqrt(2 /np.pi) * (x + 0.044715 * tf.math.pow(x, 3))))

GPTGELU=tf.keras.layers.Lambda(bert_gelu)

def get_activation(fn_name):
    if fn_name is None:
        return None
    fn_modules = ['trident.layers.tensorflow_activations']
    try:
        if isinstance(fn_name,str) and fn_name in __all__:
            if  fn_name.islower():
                 activation_fn = get_function(fn_name, fn_modules)
                 return activation_fn
            else:
                try:
                    activation_fn = get_class(fn_name,  fn_modules)
                    return activation_fn()
                except Exception:
                    activation_fn = get_function(camel2snake(fn_name), fn_modules)
                    return activation_fn
        if getattr(fn_name, '__module__', None) == 'trident.layers.tensorflow_activations':
            if inspect.isfunction(fn_name):
                return fn_name
            elif isinstance(fn_name, tf.keras.layers.Layer):
                return fn_name()
        else:
            if callable(fn_name) :
                result=inspect.getfullargspec(fn_name)
                if 1<=len(result.args)<=2:
                    return fn_name if inspect.isfunction(fn_name) else fn_name()
                else:
                    raise ValueError('Unknown activation function/ class')
    except Exception:
        return None

