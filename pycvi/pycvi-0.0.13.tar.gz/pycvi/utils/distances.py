import logging
import numpy as np

from .parse import preprocess

logger = logging.getLogger(__name__)


def mean_mahalanobis(data, mu, sigma):
    """
    Args:
        data: ndarray
            T_i * D array contaning the T_i D-dimensional data points in the cluster
        mu: ndarray
            D-dimensional array representing the mean of the component
        sigma: ndarray
            D*D array representing the covariance matrix of the component.

    Returns:
        S: float
            The mean distance between data points and mu, with covariance matrix sigma.
    """

    logger.info("Computing mean mahalanobis distance")
    print()
    print("Computing mean mahalanobis distance\n")
    print("received data:{}\n".format(data))

    if data.ndim == 1:
        data = data.reshape(1, -1)

    assert sigma.size == data.shape[1] ** 2, \
        "Wrong number of values for sigma, should have {}, got {}".format(data.shape[1] ** 2, sigma.size)

    sigma = sigma.reshape(data.shape[1], -1)

    # print("data: {}".format(data))
    x_minus_mu = data - mu
    inv_sigma = np.linalg.pinv(sigma)
    # print("x_minus_mu.shape: {}".format(x_minus_mu.shape))
    # print("inv_sigma.shape: {}".format(inv_sigma.shape))

    left_term = np.matmul(x_minus_mu, inv_sigma)
    # print("left_term.shape: {}".format(left_term.shape))
    tmp = np.matmul(left_term, x_minus_mu.T).diagonal()
    tmp = tmp ** (1/2)

    # print("tmp: {}".format(tmp))

    return tmp.mean()
