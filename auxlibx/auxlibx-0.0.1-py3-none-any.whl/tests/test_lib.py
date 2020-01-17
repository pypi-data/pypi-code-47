"""
Docstring.
"""

from unittest import TestCase
import numpy as np
from auxlibx import np_utils


class UnitTestNoParams(TestCase):
    """
    Non-Parameterized tests simulate specific situations.
    """

    @staticmethod
    def test_np_utils():
        """
        Basic tests of the get_sampling_rate definition.
        """

        # Test 1:
        scalar = 5
        array1 = np.ones(5)
        array2 = np_utils.multiply_array(array1, scalar)
        assert np.array_equal(array1, np.ones(5))
        assert np.array_equal(array2, scalar*np.ones(5))
