"""
各种模型评价指标
"""
import numpy as np
import pandas as pd


def mape_matrix(X: np.ndarray, W: np.ndarray, Y: np.ndarray):
    """
    MAPE of each line of matrix
    """
    try:
        m = np.abs(Y - np.matmul(X, W)) * 1.0 / Y
        return m
    except Exception as e:
        print("X shape: {} ".format(X.shape))
        print("W shape: {} ".format(W.shape))
        print("Y shape: {} ".format(Y.shape))
        raise e


def mape_value(x, w, y):
    return abs(y-w*x)*1.0/y


def mape_dataframe(df:pd.DataFrame, xcols:list, ycols:list, W):
    """
    对pandas数据集进行计算
    :param df:
    :param xcols:
    :param ycols:
    :param w:
    :return:
    """
    X = np.array(df[xcols].values)
    Y = np.array(df[ycols].values)
    if isinstance(W, (pd.DataFrame, pd.Series)):
        W = np.array(W.values).reshape((-1,1))
    elif isinstance(W, list):
        W = np.array(W).reshape((-1,1))
    return mape_matrix(X,W,Y)


if __name__ == '__main__':
    dataset = pd.DataFrame({
        "X": [1.0,2.0,3.0],
        "Y": [4.0,5.0,6.0]
    })
    W = [[3]]
    print(mape_dataframe(dataset, ["X"], ["Y"], W))