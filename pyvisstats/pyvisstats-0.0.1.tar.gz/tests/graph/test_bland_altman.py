import unittest

import numpy as np
import pandas as pd

from pyvisstats.graph import bland_altman as ba_graph


class BlandAltmanTest(unittest.TestCase):
    def test_ndarray(self):
        a = np.random.rand(1, 100)
        b = np.random.rand(1, 100)

        ba_graph.bland_altman(a, b)

    def test_dataframe_single_col(self):
        a = pd.DataFrame(np.random.rand(100, 1))
        b = pd.DataFrame(np.random.rand(100, 1))

        # if no value_col provided raise error
        with self.assertRaises(ValueError):
            ba_graph.bland_altman(a, b)

        ba_graph.bland_altman(a, b, value_col=0)

    def test_dataframe_groupby(self):
        a = pd.DataFrame(np.random.rand(100, 1), columns=['value'])
        str_vals = ['alpha' if np.random.random(1) > 0.5 else 'beta' for i in range(100)]
        a['Greek'] = str_vals
        b = a

        ba_graph.bland_altman(a, b, value_col='value')
        ba_graph.bland_altman(a, b, value_col='value', group_by='Greek')


if __name__ == '__main__':
    unittest.main()
