#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 NetEase.com, Inc. All Rights Reserved.
# Copyright 2019, The NSH Recommendation Project, The User Persona Group, The Fuxi AI Lab.
"""
keras_lstm

Authors: wangkai02(wangkai02@corp.netease.com)
Phone: 17816029211
Date: 2019/9/11
"""

import tensorflow as tf

from tensorflow_core.python.keras import layers
from tensorflow_core.python.keras.models import Model
from tensorflow_core.python.keras import backend as K

from rslib.algo.layers.interaction import BiInteractionPooling
from ..sparse_dnn.DenseLayerForSparse import DenseLayerForSparse


def get_model(config):

    maxlen = config['maxlen']
    class_num = config['class_num']
    hidden_unit = config['lstm_hidden_units']
    emb_size = config['lstm_emb_size']

    user_size = config['user_size']
    cross_feature_num = config['cross_feature_num']
    user_feature_num = config['user_feature_num']
    user_feature_size = config['user_feature_size']
    output_unit = config['output_unit']
    seq_num = config['seq_num']
    # seq_group_index = config['atrank_seq_group']
    # target_seq = config['atrank_target_seq']
    is_amp = config['is_amp']

    role_id_input = layers.Input(shape=(), dtype='int32')
    seq_id_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    seq_time_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    seq_time_gaps_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    cross_feature_input = layers.Input(shape=(cross_feature_num,), dtype='float32', sparse=True)
    user_feature_input = layers.Input(shape=(user_feature_num,), dtype='int32')
    label_week_id_input = layers.Input(shape=(maxlen,), dtype='int32')

    seq_index_layer = layers.Lambda(lambda x: x[0][:, x[1]])

    seqs_lstm = []
    for i in range(seq_num):
        seq_i = seq_index_layer([seq_id_input, i])
        seq_i_embeddings = layers.Embedding(class_num, emb_size, mask_zero=True)(seq_i)
        seq_i_lstm = layers.LSTM(units=64)(seq_i_embeddings)
        seqs_lstm.append(seq_i_lstm)

    seqs_embeddings = layers.Concatenate(axis=-1)(seqs_lstm)

    cross_feature = DenseLayerForSparse(cross_feature_num, 64, 'relu')(cross_feature_input)

    layers_emb_fm1_user_feature = layers.Embedding(input_dim=user_feature_size, output_dim=1)
    layers_emb_fm2_user_feature = layers.Embedding(input_dim=user_feature_size, output_dim=emb_size)
    layers_FM = BiInteractionPooling()
    user_feature_1 = layers.Flatten()(layers_emb_fm1_user_feature(user_feature_input))
    user_feature_2 = layers.Flatten()(layers_FM(layers_emb_fm2_user_feature(user_feature_input)))
    user_feature = layers.Concatenate(axis=1)([user_feature_1, user_feature_2])

    all_feature = layers.Concatenate(axis=-1)([seqs_embeddings, cross_feature, user_feature])
    output = layers.Dense(output_unit, activation='softmax')(all_feature)
    model = Model(inputs=[role_id_input, seq_id_input, seq_time_input, seq_time_gaps_input, cross_feature_input,
                          user_feature_input, label_week_id_input], outputs=[output])

    opt = tf.keras.optimizers.Adam()
    if is_amp:
        opt = tf.train.experimental.enable_mixed_precision_graph_rewrite(opt)
    loss_dict = {'1': 'mean_squared_error'}
    model.compile(loss=loss_dict.get(str(output_unit), 'categorical_crossentropy'),
                  optimizer=opt,
                  metrics=['accuracy'])

    sess = K.get_session()
    sess.run(tf.compat.v1.local_variables_initializer())
    sess.run(tf.compat.v1.global_variables_initializer())
    sess.run(tf.compat.v1.tables_initializer())
    print(model.summary())
    return model
