#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 NetEase.com, Inc. All Rights Reserved.
# Copyright 2019, The NSH Recommendation Project, The User Persona Group, The Fuxi AI Lab.
"""
FeatureUtil

Authors: zouzhene(zouzhene@corp.netease.com)
Phone: 132****2788
Date: 2019/9/11
"""

import abc
import six
import tensorflow as tf
from tensorflow.python.distribute import distribution_strategy_context
from tensorflow.python.framework import ops
from tensorflow.python.framework import smart_cond
from tensorflow.python.framework import tensor_util
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.utils import losses_utils
from tensorflow.python.keras.utils import tf_utils
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object
from tensorflow.python.keras.utils.generic_utils import serialize_keras_object
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn
from tensorflow.python.ops.losses import losses_impl
from tensorflow.python.ops.losses import util as tf_losses_util
from tensorflow.python.util.tf_export import keras_export
from tensorflow.tools.docs import doc_controls

def masked_categorical_crossentropy(y_true,
                             y_pred,
                             from_logits=False,
                             label_smoothing=0,
                             mask_value=-1):
    '''

    :param y_true: tensor of true targets.
    :param y_pred: tensor of predicted targets.
    :param from_logits: Whether `y_pred` is expected to be a logits tensor. By default,
      we assume that `y_pred` encodes a probability distribution.
    :param label_smoothing: Float in [0, 1]. If > `0` then smooth the labels.
    :param mask_value: if some value in y_true is equal to 'mask_value', the loss of this value is 0.
    :return: loss: Categorical crossentropy loss value.
    '''
    y_true = math_ops.cast(y_true, y_pred.dtype)
    y_pred = ops.convert_to_tensor(y_pred)
    mask = K.cast(K.not_equal(y_true, mask_value), K.floatx())

    label_smoothing = ops.convert_to_tensor(label_smoothing, dtype=K.floatx())

    def _smooth_labels():
        num_classes = math_ops.cast(array_ops.shape(y_true)[1], y_pred.dtype)
        return y_true * (1.0 - label_smoothing) + (label_smoothing / num_classes)

    y_true = smart_cond.smart_cond(label_smoothing, _smooth_labels, lambda: y_true)

    cross_entropy = K.categorical_crossentropy(y_true, y_pred, from_logits=from_logits)
    loss = tf.reduce_mean(tf.multiply(cross_entropy, mask)) / tf.reduce_mean(mask)

    return loss
