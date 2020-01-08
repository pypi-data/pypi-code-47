import unittest

import numpy as np
import pandas as pd

from pycvi.utils import parse


def arr(value, t='arr'):
    """

    Args:
        value: list
            list to use in order to create the object
        t: str
            'arr' to create an np.array and 'df' to create a pd.DataFrame
    Returns: the array of the appropriate type

    """

    if t == 'df':
        return pd.DataFrame(value)
    return np.array(value)


df_empty1d, df_empty2d, df_empty3d = arr([], t='df'), arr([[], []], t='df'),\
                                     arr([[[], []], [[], []], [[], []]], t='df')
df_scalar = arr([42], 'df')
df_1d = arr([0, 1, 2], 'df')
df_2d = arr([[0, 1], [2, 3]], 'df')
df_3d = arr([[[ 0,  1,  2], [ 3,  4,  5]],
             [[ 6,  7,  8], [ 9, 10, 11]],
             [[12, 13, 14], [15, 16, 17]]], 'df')

arr_empty1d, arr_empty2d, arr_empty3d = [np.zeros((0,)*i) for i in range(1, 4)]
arr_scalar, arr_1d, arr_2d, arr_3d = \
    arr([42]), arr([0, 1, 2]), arr([[0, 1], [2, 3]]),\
    arr([[[ 0,  1,  2], [ 3,  4,  5]],
         [[ 6,  7,  8], [ 9, 10, 11]],
         [[12, 13, 14], [15, 16, 17]]])

one_data_point_2d = [
    arr([[42, 52]], 'df'),
    arr([[42, 52]]),
    [[42, 52]]
]


empty_arrays = [
                df_empty1d, df_empty2d, df_empty3d,
                arr_empty1d, arr_empty2d, arr_empty3d,
                [], [[], []], [[[], []], [[], []]]
               ]

scalar_arrays = [df_scalar, arr_scalar, [42]]

one_d_arrays = [
                df_1d, arr_1d, [0, 1, 2]
               ]

two_d_arrays = [
                df_2d, arr_2d, [[0, 1], [2, 3]]
               ]

three_d_arrays = [
    df_3d, arr_3d, [[[ 0,  1,  2], [ 3,  4,  5]],
                    [[ 6,  7,  8], [ 9, 10, 11]],
                    [[12, 13, 14], [15, 16, 17]]]
]

incorrect_type = [
    42,
    'Bonjour',
    50.7,
    {1, 2, 3},
    {'a': 0, 'b': 1}
]


class TestPreprocess(unittest.TestCase):
    def test_empty_arrays(self):
        for e in empty_arrays:
            self.assertRaises(AssertionError, parse.preprocess, e)

    def test_1d_arrays(self):
        for e in one_d_arrays:
            self.assertSequenceEqual(list(parse.preprocess(e)),
                                     list(np.array([[0], [1], [2]])),
                                     "fail test 1d")

    def test_2d_arrays(self):
        for e in two_d_arrays:
            self.assertSequenceEqual(list(parse.preprocess(e).ravel()),
                                     list(np.array([[0, 1], [2, 3]]).ravel()),
                                     "fail test 2d")

    def test_3d_arrays(self):
        for e in three_d_arrays:
            self.assertRaises(AssertionError, parse.preprocess, e)

    def test_incorrect_type(self):
        for e in incorrect_type:
            self.assertRaises(TypeError, parse.preprocess, e)
