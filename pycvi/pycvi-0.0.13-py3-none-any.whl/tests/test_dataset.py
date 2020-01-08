import unittest

import numpy as np
import pandas as pd

from pycvi.utils import dataset

##########################################
#             Test cases                 #
##########################################

VALID = {
    0: {
        "X": pd.DataFrame([[0, 1], [1, 2]]),
        "y": [1, 2],
        "XX": np.array([[0, 1], [1, 2]]),
        "yy": np.array([1, 2])
    }
}

INVALID = {
    0: {
        "X": pd.DataFrame([0, 1], [1, 2]),
        "y": [1, 2, 3],
        "raises": AssertionError
    }
}


class TestDataSet(unittest.TestCase):
    def test_valid(self):
        for key, value in VALID.items():
            data = dataset.DataSet(value["X"], value["y"])
            self.assertEqual(list(data.X.ravel()), list(value["XX"].ravel()))
            self.assertEqual(list(data.labels.ravel()), list(value["yy"].ravel()))

    def test_invalid(self):
        for key, value in INVALID.items():
            self.assertRaises(value["raises"], dataset.DataSet, *(value["X"], value["y"]))
