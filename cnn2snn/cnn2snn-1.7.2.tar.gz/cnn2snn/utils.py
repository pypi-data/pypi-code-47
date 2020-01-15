#!/usr/bin/env python
# ******************************************************************************
# Copyright 2019 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
"""
A set of functions to convert a Keras (tf.keras) model to a new
equivalent model with different characteristics. Then, the new model
can be quantized.

"""
import numpy as np
from tensorflow.keras.layers import MaxPooling2D, AveragePooling2D, \
    BatchNormalization, GlobalAveragePooling2D, InputLayer
from tensorflow.keras.models import Model
from .quantization_layers import QuantizedConv2D, QuantizedDense, \
    QuantizedDepthwiseConv2D, QuantizedSeparableConv2D

def invert_batchnorm_pooling(model):
    """Returns a new model where pooling and batchnorm layers are inverted.

    From a Keras model where pooling layers precede batch normalization
    layers, this function places the BN layers before pooling layers. This
    is the first step before folding BN layers into neural layers.

    Note: inversion of layers is equivalent only if the gammas of BN layers
    are positive. The function raises an error if not.

    Args:
        model (:obj:`tf.keras.Model`): a tf.keras model.

    Returns:
        :obj:`tf.keras.Model`: a keras.Model.

    """
    x = model.layers[0].output
    i = 1
    while i < len(model.layers) - 1:
        layer = model.layers[i]
        next_layer = model.layers[i+1]
        supported_pool = (MaxPooling2D,
                          AveragePooling2D,
                          GlobalAveragePooling2D)
        is_pool = isinstance(layer, supported_pool)
        if is_pool and isinstance(next_layer, BatchNormalization):
            gammas = next_layer.get_weights()[0]
            if np.sum(gammas <= 0) > 0:
                # NB: negative gammas are only a problem for max pooling, not
                # for avg pooling
                raise RuntimeError(f"There are {np.sum(gammas <= 0)} negative "
                                   "gammas in the batch norm layer "
                                   "{next_layer.name}. Negative gammas are "
                                   "not supported.")
            next_layer_config = next_layer.get_config()
            # GlobalAveragePooling2D brings a change on axis for the batch norm.
            if isinstance(layer, GlobalAveragePooling2D):
                next_layer_config['axis'] = [-1]
            bn_layer = BatchNormalization.from_config(next_layer_config)
            x = bn_layer(x)
            x = layer(x)
            bn_layer.set_weights(next_layer.get_weights())
            i = i + 2
        else:
            x = layer(x)
            i = i + 1

    x = model.layers[-1](x)
    return Model(inputs=model.input, outputs=[x], name='model_BN_MP')


def fold_batch_norms(model):
    """Returns a new model where batchnorm layers are folded into
    previous neural layers.

    From a Keras model where BN layers follow neural layers, this
    function removes the BN layers and updates weights and bias
    accordingly of the preceding neural layers. The new model is
    strictly equivalent to the previous one.

    Args:
        model (:obj:`tf.keras.Model`): a Keras model.

    Returns:
        :obj:`tf.keras.Model`: a tf.keras.Model.

    """
    x = model.layers[0].output
    i = 1
    while i < len(model.layers) - 1:
        layer = model.layers[i]
        next_layer = model.layers[i+1]

        if isinstance(next_layer, BatchNormalization):
            if not isinstance(layer, (QuantizedConv2D,
                                      QuantizedDepthwiseConv2D,
                                      QuantizedDense)):
                raise AttributeError("The layer preceding a batch norm "
                                     "layer must be QuantizedDense, "
                                     "QuantizedConv2D or "
                                     "QuantizedDepthwiseConv2D.")

            # Get weights and BN parameters
            gamma, beta, mean, var = next_layer.get_weights()
            epsilon = next_layer.epsilon
            weights = layer.get_weights()[0]
            bias = layer.get_weights()[1] if len(
                layer.get_weights()) > 1 else 0

            # Compute new weights for folded layer
            scale_BN = gamma / np.sqrt(var + epsilon)
            new_weights = [weights * scale_BN]
            new_weights.append(beta + (bias-mean) * scale_BN)

            # Create new layer

            if isinstance(layer, QuantizedDepthwiseConv2D):
                new_layer = QuantizedDepthwiseConv2D(layer.kernel_size,
                                                     quantizer=layer.quantizer,
                                                     use_bias=True,
                                                     padding=layer.padding,
                                                     name=layer.name + '_foldBN')
            elif isinstance(layer, QuantizedConv2D):
                new_layer = QuantizedConv2D(layer.filters, layer.kernel_size,
                                            quantizer=layer.quantizer,
                                            strides=layer.strides,
                                            use_bias=True,
                                            padding=layer.padding,
                                            name=layer.name + '_foldBN')
            elif isinstance(layer, QuantizedDense):
                new_layer = QuantizedDense(layer.units,
                                           quantizer=layer.quantizer,
                                           use_bias=True,
                                           name=layer.name + '_foldBN')

            x = new_layer(x)
            new_layer.set_weights(new_weights)
            i = i + 2

        else:
            x = layer(x)
            i = i + 1

    if not isinstance(model.layers[-1], BatchNormalization):
        x = model.layers[-1](x)

    return Model(inputs=model.input, outputs=[x], name='model_foldBN')


def merge_separable_conv(model):
    """Returns a new model where all depthwise conv2d layers followed by conv2d
    layers are merged into single separable conv layers.

    The new model is strictly equivalent to the previous one.

    Args:
        model (:obj:`tf.keras.Model`): a Keras model.

    Returns:
        :obj:`tf.keras.Model`: a tf.keras.Model.

    """
    # If no layers are Depthwise, there is nothing to be done, return.
    if not any([isinstance(l, QuantizedDepthwiseConv2D) for l in model.layers]):
        return model

    if isinstance(model.layers[0], InputLayer):
        x = model.layers[0].output
        i = 1
    else:
        x = model.layers[0].input
        i = 0
    while i < len(model.layers) - 1:
        layer = model.layers[i]
        next_layer = model.layers[i+1]

        if isinstance(layer, QuantizedDepthwiseConv2D):
            # Check layers expected order
            if not isinstance(next_layer, QuantizedConv2D):
                raise AttributeError(f"Layer {layer.name} "
                                     "QuantizedDepthwiseConv2D should be "
                                     "followed by QuantizedConv2D layers.")

            if layer.bias is not None:
                raise AttributeError(f"Unsupported bias in "
                                     "QuantizedDepthwiseConv2D Layer "
                                     "{layer.name} ")

            # Get weights and prepare new ones
            dw_weights = layer.get_weights()[0]
            pw_weights = next_layer.get_weights()[0]
            new_weights = [dw_weights, pw_weights]
            if next_layer.use_bias:
                bias = next_layer.get_weights()[1]
                new_weights.append(bias)

            # Create new layer
            new_name = f'{layer.name}_{next_layer.name}'
            new_layer = QuantizedSeparableConv2D(next_layer.filters,
                                                 layer.kernel_size,
                                                 quantizer=layer.quantizer,
                                                 padding=layer.padding,
                                                 use_bias=next_layer.use_bias,
                                                 name=new_name)
            x = new_layer(x)
            new_layer.set_weights(new_weights)
            i = i + 2

        else:
            x = layer(x)
            i = i + 1

    # Add last layer if not done already
    if i == (len(model.layers) - 1):
        if isinstance(model.layers[-1], QuantizedDepthwiseConv2D):
            raise AttributeError(f"Layer {layer.name} "
                                 "QuantizedDepthwiseConv2D should be followed "
                                 "by QuantizedConv2D layers.")
        x = model.layers[-1](x)

    return Model(inputs=model.input, outputs=[x], name=model.name)
