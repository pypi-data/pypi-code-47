import argparse
import os

import numpy as np
import tensorflow as tf
from pymongo import MongoClient
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.layers import (Activation, BatchNormalization,
                                            Dense)
from tensorflow.python.keras.models import Input, Model
from tensorflow.python.keras.utils import to_categorical

from .tf_config import config
from pubsub_ncs import Publisher


def check(input_data, label_data, vector_size):
    from sklearn.model_selection import train_test_split

    if isinstance(label_data, np.ndarray):
        _y = label_data.tolist()
    elif isinstance(label_data, (list, tuple)):
        _y = label_data
    if isinstance(input_data, (list, tuple)):
        input_data = np.asarray(input_data)
    _num_class = sorted(set(_y), key=_y.index)
    label2index = {k: i for i, k in enumerate(_num_class)}
    index2label = {i: k for i, k in enumerate(_num_class)}
    _class = [label2index[k] for k in label_data]
    num_class = len(_num_class)
    _class = to_categorical(_class, num_classes=num_class)
    x_train, x_test, y_train, y_test = train_test_split(
        input_data, _class, test_size=0.2, shuffle=True)

    def modelCreate():
        inputs = Input((vector_size,), name="input1")

        def hidden_layer(cnt, layer):
            x = Dense(30, name=f"dense{cnt}")(layer)
            x = BatchNormalization(name=f"batch{cnt}")(x)
            x = Activation("relu", name=f"activation{cnt}")(x)
            return x
        for i in range(2):
            layer = hidden_layer(i+1, inputs if i == 0 else layer)
        outputs = Dense(num_class, name="output1")(layer)
        outputs = Activation("softmax")(outputs)
        model = Model(inputs, outputs)
        model.compile(loss="categorical_crossentropy",
                      optimizer="adam", metrics=['accuracy'])
        model._make_predict_function()
        return model
    g = tf.Graph()
    with g.as_default():
        with tf.compat.v1.Session(graph=g, config=config) as sess:
            K.set_session(sess)
            model = modelCreate()
            model.fit(input_data, _class, batch_size=32,
                      epochs=300, validation_data=(x_train, y_train), verbose=0)
            score = model.evaluate(x_test, y_test, verbose=0)
    return score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gensim_id', help="gensimマスタの識別ID")
    args = parser.parse_args()
    mongo_connection_string = os.getenv(
        'MONGO_CONNECT_STR', 'mongodb://root:example@localhost:27017')
    client = MongoClient(mongo_connection_string)
    assistant = client.assistant
    gensim_master = assistant.geinsim_master
    gensim_data = gensim_master.find_one(filter={'id': args.gensim_id})
    score = check(gensim_data['input_data'], gensim_data['label_data'],
                  gensim_data['vector_size'])
    loss = float(score[0]) * 100
    accuracy = float(score[1]) * 100
    pub = Publisher(args.gensim_id)
    pub.send({
        'message': '学習モデルの評価終了',
        'loss': f'loss:{loss}',
        'accuracy': f'accuracy:{accuracy}'
    })
