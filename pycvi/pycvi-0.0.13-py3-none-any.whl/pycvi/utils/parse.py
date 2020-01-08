import numpy as np
import pandas as pd


def reshape(array):
    """

    Args:
        array: np.ndarray
            N-dimensional array

    Returns: np.ndarray
        2D array if at least 2 elements

    """
    assert array.ndim in [1, 2],\
        "Expected 1D or 2D array, got {}D".format(array.ndim)

    # If array is 1D, reshape it to be 2D. If 2D, do nothing
    ret = array.reshape(-1, 1) if array.ndim == 1 else array

    # Check that we have at least two lines
    assert ret.shape[0] and ret.shape[1],\
        "Expected at least 2 data points, got {}".format(array.shape[0])

    return ret


def array_from_ndarray(array):
    """

    Args:
        array: np.ndarray

    Returns:

    """
    assert array.dtype in [float, int],\
        "Expected array of int or float, got {}".format(array.dtype)
    return reshape(array)


def preprocess(X):
    """
    Args:
        X: iterable
            Array containing the features

    Return:
        np.ndarray: 2D array
    """

    if isinstance(X, pd.DataFrame):
        res = array_from_ndarray(X.values)
    elif isinstance(X, np.ndarray):
        res = array_from_ndarray(X)
    elif isinstance(X, (list, tuple)):
        res = array_from_ndarray(np.array(X))
    else:
        raise TypeError("Expected an np.array, a pd.Dataframe, or a list.\
                                Got: {}".format(type(X)))

    return res
