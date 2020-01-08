import unittest

import numpy as np
import pandas as pd

from pycvi.utils import labels

##########################################
#             Test cases                 #
##########################################

VALID = {
    0: (pd.DataFrame([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        np.array([0, 1, 2])),
    1: (np.array([[1, 0], [0, 1], [0, 1], [0, 1]]),
        np.array([0, 1, 1, 1])),
    2: ([[0, 1], [1, 0]],
        np.array([1, 0])),
    3: (((0, 1), (1, 0)),
        np.array([1, 0])),
    4: ([1, 2, 3, 4],
        np.array([1, 2, 3, 4]))
}

INVALID = {
    0: ([[], []], ValueError),  # trying to get argmax on an empty sequence
    1: ({1, 0, 2}, TypeError),
    2: ([[1, 0, 0], [1, 0, 0], [1, 0, 0]], AssertionError),  # no two distinct labels
    3: ([1, 1, 1, 1], AssertionError)
}


class TestLabels(unittest.TestCase):
    def test_valid(self):
        for key, value in sorted(VALID.items(), key=lambda x: x[0]):
            self.assertEqual(list(labels.Labels(value[0]).labels.ravel()),
                             list(value[1].ravel()),
                             "{} != {}".format(labels.Labels(value[0]).labels, value[1]))

    def test_invalid(self):
        for key, value in sorted(INVALID.items(), key=lambda x: x[0]):
            self.assertRaises(value[1], labels.Labels, value[0])
