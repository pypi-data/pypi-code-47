import cupy as cp
from autogradgpu.tensor import Tensor
from autogradgpu.parameter import Parameter
from metal.module import Module
from autogradgpu.dependency import Dependency
import math
import copy
from metal.layers.layer import Layer

class Flatten(Layer):
    __slots__ =( 'prev_shape', 'trainable','type' )

    """ Turns a multidimensional matrix into two-dimensional """
    def __init__(self, icput_shape=None):
        self.prev_shape = None
        self.trainable = True
        self.icput_shape = icput_shape

    def forward_pass(self, x_, training=True):
        self.prev_shape = x_.shape
        X = x_.data
        self.type = type(x_)
        requires_grad = x_.requires_grad
        if training:
            if requires_grad:
                depends_on = [Dependency(x_, self.gardflatten)]
            else:
                depends_on = []
        else:
            depends_on = []
        return self.type(data=X.reshape((X.shape[0], -1)),requires_grad=requires_grad,depends_on=depends_on)

    def gardflatten(self, accum_grad):
        return accum_grad.reshape(self.prev_shape)

    def update_pass(self):
        pass

    def output_shape(self):
        return (cp.prod(self.icput_shape),)
