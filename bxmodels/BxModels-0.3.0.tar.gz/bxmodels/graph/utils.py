#
#  graph/utils.py
#  bxmodels
#
#  Created by Oliver Borchert on June 16, 2019.
#  Copyright (c) 2019 Oliver Borchert. All rights reserved.
#

import torch
import numpy as np
import scipy.sparse as sp

def normalized_adjacency_matrix(A):
    """
    Build the normalized adjacency matrix for a graph convolutional network
    as PyTorch sparse tensor.
    
    Parameters:
    -----------
    - A: scipy.sparse.csr_matrix
        A sparse matrix with binary entries.
        
    Returns:
    --------
    - torch.sparse.FloatTensor
        A sparse PyTorch tensor preprocessed to be used with a GCN. The
        returned matrix is symmetric.
    """
    assert A.shape[0] == A.shape[1]
    assert all(A.data == 1)
    
    # 1) Preprocess
    n = A.shape[0]
    
    # 1.1) Ensure A = A^T and set A = A + 1
    A = A + A.T
    A = A + sp.eye(n)
    A[A > 1] = 1
    
    # 1.2) Compute D^(-1/2) A D^(-1/2) for degree matrix D
    degrees = A.sum(axis=1).A1
    inv_degrees = 1 / np.sqrt(degrees)
    inv_degrees[np.isinf(inv_degrees)] = 0
    D = sp.diags(inv_degrees)
    A = D.dot(A).dot(D)
    
    return torch.sparse.FloatTensor(
        torch.LongTensor(A.nonzero()),
        torch.from_numpy(A.data).float(),
        torch.Size(A.shape)
    ).coalesce()


def normalized_feature_matrix(X):
    """
    Build the normalized feature matrix for a graph convolutional network
    as PyTorch dense tensor.
    
    Parameters:
    -----------
    - X: numpy.ndarray
        A dense matrix with arbitrary entries.
        
    Returns:
    --------
    - torch.FloatTensor
        A PyTorch tensor preprocessed to be used with a GCN.
    """
    # 1) Row-normalize X
    inv_rowsum = 1 / X.sum(axis=1)
    inv_rowsum[np.isinf(inv_rowsum)] = 0
    M = sp.diags(inv_rowsum)
    X = M.dot(X)
    
    # 2) Build tensor
    return torch.tensor(X, dtype=torch.float)
    