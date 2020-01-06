import cupy as cp
from autograd.tensor import Tensor
from autograd.parameter import Parameter
from autograd.dependency import Dependency
import math
import copy
from metal.layers.layer import Layer
from metal.utils.layer_data_manipulations import *

class Conv2D(Layer):
    __slots__ =('n_filters','filter_shape','padding','stride','trainable','seed','w','b','w_opt','b_opt','type','layer_icput','X_col','W_col')

    """A 2D Convolution Layer.
    Parameters:
    -----------
    n_filters: int
        The number of filters that will convolve over the icput matrix. The number of channels
        of the output shape.
    filter_shape: tuple
        A tuple (filter_height, filter_width).
    icput_shape: tuple
        The shape of the expected icput of the layer. (batch_size, channels, height, width)
        Only needs to be specified for first layer in the network.
    padding: string
        Either 'same' or 'valid'. 'same' results in padding being added so that the output height and width
        matches the icput height and width. For 'valid' no padding is added.
    stride: int
        The stride length of the filters during the convolution over the icput.
    """
    def __init__(self, n_filters, filter_shape, icput_shape=None, padding='same', stride=1, seed=None):
        self.n_filters = n_filters
        self.filter_shape = filter_shape
        self.padding = padding
        self.stride = stride
        self.icput_shape = icput_shape
        self.trainable = True
        self.seed = seed
        self.load_params_ = False

    def load_params(self, weights, bias, trainable=False):
        self.load_params_ = True
        self.trainable = trainable

        if self.trainable == False:
            self.w = Parameter(data = weights,requires_grad=False)
            self.b = Parameter(data = bias.reshape(-1,1),requires_grad=False)
        elif self.trainable == True:
            self.w = Parameter(data = weights)
            self.b = Parameter(data = bias.reshape(-1,1))


    def load_optimzer(self,optimizer=None):
        # Weight optimizers
        if optimizer is not None:
            self.w_opt  = copy.copy(optimizer)
            self.b_opt = copy.copy(optimizer)

    def initialize(self, optimizer=None):
        cp.random.seed(self.seed)
        # Initialize the weights
        filter_height, filter_width = self.filter_shape
        channels = self.icput_shape[0]
        limit = 1 / math.sqrt(cp.prod(self.filter_shape))
        # create filter
        # grad would be zeros instead of None :bugfix
        if self.trainable == False:
            self.w = Parameter(data = cp.random.uniform(-limit, limit, size=(self.n_filters, channels, filter_height, filter_width)),requires_grad=False)
            self.b = Parameter(data = cp.zeros((self.n_filters, 1)),requires_grad=False)
        elif self.trainable == True:
            self.w = Parameter(data = cp.random.uniform(-limit, limit, size=(self.n_filters, channels, filter_height, filter_width)))
            self.b = Parameter(data = cp.zeros((self.n_filters, 1)))
        # Weight optimizers
        if optimizer is not None:
            self.w_opt  = copy.copy(optimizer)
            self.b_opt = copy.copy(optimizer)

    def parameters_(self):
        return cp.prod(self.w.shape) + cp.prod(self.b.shape)

    def forward_pass(self, x, training):

        X = x.data
        self.type = type(x)
        requires_grad = x.requires_grad or self.w.requires_grad or self.b.requires_grad
        depends_on: List[Dependency] = []

        batch_size, channels, height, width = X.shape
        self.layer_icput = X
        # Turn image shape into column shape
        # (enables dot product between icput and weights)
        self.X_col = image_to_column(X, self.filter_shape, stride=self.stride, output_shape=self.padding)
        # Turn weights into column shape
        self.W_col = self.w.data.reshape((self.n_filters, -1))
        # Calculate output
        output = self.W_col.dot(self.X_col) + self.b.data
        # Reshape into (n_filters, out_height, out_width, batch_size)
        output = output.reshape(self.output_shape() + (batch_size, ))
        # Redistribute axises so that batch size comes first
        if training:
            if requires_grad:
                if self.w.requires_grad:
                    depends_on.append(Dependency(self.w, self.grad_w_conv2D))
                if self.b.requires_grad:
                    depends_on.append(Dependency(self.b, self.grad_b_conv2D))
                if x.requires_grad:
                    depends_on.append(Dependency(x, self.grad_a_conv2D))
            else:
                depends_on = []
        return self.type(data=output.transpose(3,0,1,2),requires_grad=requires_grad,depends_on=depends_on)


    def grad_w_conv2D(self, accum_grad):
        # Reshape accumulated gradient into column shape
        accum_grad = accum_grad.transpose(1, 2, 3, 0).reshape(self.n_filters, -1)
        # Take dot product between column shaped accum. gradient and column shape
        # layer icput to determine the gradient at the layer with respect to layer weights
        grad_w = accum_grad.dot(self.X_col.T).reshape(self.w.shape)

        return grad_w

    def grad_b_conv2D(self, accum_grad):
        # Reshape accumulated gradient into column shape
        accum_grad = accum_grad.transpose(1, 2, 3, 0).reshape(self.n_filters, -1)
        # The gradient with respect to bias terms is the sum similarly to in Dense layer
        grad_w0 = cp.sum(accum_grad, axis=1, keepdims=True)

        return grad_w0

    def grad_a_conv2D(self, accum_grad):
        # Reshape accumulated gradient into column shape
        accum_grad = accum_grad.transpose(1, 2, 3, 0).reshape(self.n_filters, -1)
        # Recalculate the gradient which will be propogated back to prev. layer
        accum_grad = self.W_col.T.dot(accum_grad)
        # Reshape from column shape to image shape
        accum_grad = column_to_image(accum_grad,
                                self.layer_icput.shape,
                                self.filter_shape,
                                stride=self.stride,
                                output_shape=self.padding)

        return accum_grad

    def update_pass(self):
        # Update the layer weights
        if self.trainable:
            self.w = self.w_opt.update(self.w)
            self.b = self.b_opt.update(self.b)
        # clear the gradients
        self.zero_grad()




    def output_shape(self):
        channels, height, width = self.icput_shape
        pad_h, pad_w = determine_padding(self.filter_shape, output_shape=self.padding)
        output_height = (height + cp.sum(pad_h) - self.filter_shape[0]) / self.stride + 1
        output_width = (width + cp.sum(pad_w) - self.filter_shape[1]) / self.stride + 1
        return self.n_filters, int(output_height), int(output_width)
