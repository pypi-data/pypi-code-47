import os, sys, tensorflow as tf, numpy as np
'''
See Layer Subclassing Guide:
https://www.tensorflow.org/beta/guide/keras/custom_layers_and_models#layers_are_recursively_composable
'''

class MatrixFactorizationSlice(tf.keras.layers.Layer):
    def __init__(self, dim=8, **kwargs):
        '''
        dim (int): the  embedding size of the Matrix Factorization
            model. Defaults to `8`.
        '''
        super(MatrixFactorizationSlice, self).__init__()
        self.dim = dim

    def call(self, inputs):
        x = tf.squeeze(inputs, [1])
        x = x[:, :self.dim]
        return x

    def get_config(self):
        # config = super(tf.keras.layers.Layer, self).get_config()
        config = {}
        config.update({
            'dim': self.dim,
        })
        return config

class MultiLayerPerceptronSlice(tf.keras.layers.Layer):
    def __init__(self, dim, **kwargs):
        '''
        dim (int): the  embedding size of the Matrix Factorization
            model. Defaults to `8`.
        '''
        super(MultiLayerPerceptronSlice, self).__init__()
        self.dim = dim

    def call(self, inputs):
        x = tf.squeeze(inputs, [1])
        x = x[:, self.dim:]
        return x

    def get_config(self):
        # config = super(tf.keras.layers.Layer, self).get_config()
        config = {}
        config.update({
            'dim': self.dim,
        })
        return config
