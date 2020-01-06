#
#  graph/gcn.py
#  bxmodels
#
#  Created by Oliver Borchert on June 16, 2019.
#  Copyright (c) 2019 Oliver Borchert. All rights reserved.
#

import math
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.jit as jit
import bxtorch.nn as xnn

class GCNConfig(xnn.Config):

    # The number of features attached to each node.
    num_features: int

    # The number of classes to use for a classification task.
    num_classes: int

    # The size(s) of the hidden layer(s).
    hidden_layers: list = []

    # The dropout rate to use in between any layers (apart from the output
    # layer).
    dropout: float = 0.5

    # Whether to use ReLU acitvation after every layer (apart from the output
    # layer).
    use_relu: bool = True


class GCN(xnn.Configurable, xnn.Estimator, nn.Module):
    """
    Implementation of the graph convolutional network as presented in 
    "Semi-Supervised Classification with Graph Convolutional Networks" (Kipf & 
    Welling, 2017).
    """

    __config__ = GCNConfig
    __engine__ = xnn.SupervisedEngine

    # MARK: Initialization
    def __init__(self, config):
        super().__init__(config)
        
        convs = []
        sizes = [self.num_features] + self.hidden_layers + [self.num_classes]
        for in_size, out_size in zip(sizes, sizes[1:]):
            convs.append(GraphConvolution(in_size, out_size))

        self.convolutions = nn.ModuleList(convs)

    # MARK: Instance Methods
    def forward(self, A, X):
        """
        Computes the forward pass of the GCN.

        Parameters:
        -----------
        - A: torch.sparse.FloatTensor [N, N]
            The normalized adjacency matrix of the graph with N nodes.
        - X: torch.FloatTensor [N, D]
            The normalized feature matrix where each node has D features.

        Returns:
        --------
        - torch.FloatTensor [N, C]
            Class probabilities for all C classes for each node of the graph.
        """
        H = self.convolutions[0](A, X)

        for conv in self.convolutions[1:]:
            if self.use_relu:
                H = F.relu(H)
            H = F.dropout(H, self.dropout, training=self.training)
            H = conv(A, H)

        if self.num_classes == 1:
            return torch.sigmoid(H).view(-1)
        else:
            return F.softmax(H, dim=-1)


class GraphConvolution(nn.Module):
    """
    Graph convolution layer for the graph convolutional network.
    """

    use_bias: jit.Final[bool]

    # MARK: Initialization
    def __init__(self, in_dim, out_dim, use_bias=True):
        """
        Initializes a new graph convolution layer.

        Parameters:
        -----------
        - in_dim: int
            The dimension of the inputs.
        - out_dim: int
            The dimension of the outputs.
        """
        super().__init__()

        self.use_bias = use_bias

        self.weight = nn.Parameter(torch.FloatTensor(in_dim, out_dim))
        if use_bias:
            self.bias = nn.Parameter(torch.FloatTensor(out_dim))

        self.reset_parameters()


    # MARK: Instance Methods
    def reset_parameters(self):
        std = 1 / math.sqrt(self.weight.size(1))
        nn.init.uniform_(self.weight, -std, std)
        if self.use_bias:
            nn.init.uniform_(self.bias, -std, std)

    def forward(self, A, H):
        """
        Computes the forward pass of the graph convolution layer.

        Parameters:
        -----------
        - A: torch.sparse.Tensor [N, N]
            The normalized adjacency matrix of the graph with N nodes.
        - H: torch.Tensor [N, K]
            The hidden node representations of the preceding layer with K
            dimensions.

        Returns:
        --------
        - torch.Tensor [N, D]
            The hidden representation of this layer with D dimensions.
        """
        H = H.matmul(self.weight)
        H = torch.spmm(A, H)
        if self.use_bias:
            return H + self.bias
        else:
            return H
