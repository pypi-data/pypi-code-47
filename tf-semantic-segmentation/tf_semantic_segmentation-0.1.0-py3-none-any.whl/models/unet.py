from ..layers import get_norm_by_name

from tensorflow.keras import layers, Model, Input
from tensorflow.keras import backend as K

import tensorflow as tf
import math


def conv(x, filters, kernel_size=(3, 3), norm='batch', activation='relu', l2=None, padding='SAME'):
    # print(locals())
    y = layers.Conv2D(filters, kernel_size=kernel_size, activation=activation, padding=padding)(x)
    if norm:
        y = get_norm_by_name(norm)(y)
    return y


def upsample(x):
    return layers.UpSampling2D(size=(2, 2))(x)


def upsample_conv(x, kernel_size=(3, 3), padding='SAME'):
    num_filters = x.shape[-1]
    return layers.Conv2DTranspose(num_filters, kernel_size=kernel_size, strides=(2, 2), padding=padding)(x)


"""
def upsample(x):
    shape = K.shape(x)
    size = (shape[0] / 2, shape[1] / 2)
    print("upsample to %s" % str(size))

    return tf.image.resize(x, size, method=tf.image.ResizeMethod.BILINEAR)
"""


def downsample(x, f=2):
    return layers.MaxPool2D(pool_size=(2, 2))(x)


def unet(input_shape=(256, 256, 1), num_classes=3, depth=5, num_first_filters=64):
    """ 
        https://arxiv.org/pdf/1505.04597.pdf
    """
    inputs = Input(input_shape)

    y = inputs
    layers = []

    features = [int(pow(2, math.log2(num_first_filters) + i)) for i in range(depth)]

    for k, num_filters in enumerate(features):
        y = conv(y, num_filters)
        y = conv(y, num_filters)
        layers.append(y)

        if k != (len(features) - 1):
            y = downsample(y)
        print("encoder - features: %d, shape: %s" % (num_filters, str(y.shape)))

    for k, num_filters in enumerate(reversed(features[:-1])):
        y = upsample_conv(y)
        y = K.concatenate([y, layers[-(k + 2)]])
        y = conv(y, num_filters)
        y = conv(y, num_filters)
        print("decoder - features: %d, shape: %s" % (num_filters, str(y.shape)))

    base_model = Model(inputs, y)
    y = conv(y, num_classes, kernel_size=(1, 1), activation=None, norm=None)
    return Model(inputs, y), base_model


def unet_v2(input_shape=(256, 256, 1), num_classes=2, depth=5, num_first_filters=32):
    """
    Modified version of the original unet with more convolutions and bilinear upsampling
    """
    inputs = Input(input_shape)

    y = inputs
    layers = []

    features = [pow(2, math.log2(num_first_filters)) for i in range(depth)]

    for k, f in enumerate(features):
        print("encoder k=%d, features=%d" % (k, f))
        y = conv(y, f)
        y = conv(y, f)
        layers.append(y)
        if k != (len(features) - 1):
            y = downsample(y)

    for k, f in enumerate(reversed(features[:-1])):
        print(k, f)
        y = upsample(y)
        y = conv(y, f, kernel_size=(1, 1), norm=None)
        y = K.concatenate([layers[-(k + 2)], y])
        y = conv(y, f, norm=None)
        y = conv(y, f)

    y = conv(y, features[0], norm=False)
    y = conv(y, features[0], norm=False)

    base_model = Model(inputs, y)
    y = conv(y, num_classes, kernel_size=(1, 1), activation=None, norm=None)
    return Model(inputs, y), base_model
