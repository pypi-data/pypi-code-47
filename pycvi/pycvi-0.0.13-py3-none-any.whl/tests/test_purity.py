import logging
import unittest


from pycvi.external.purity import Purity


y_true0 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

y_pred0 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred1 = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0]


class TestPurity(unittest.TestCase):
    def test_0(self):
        print("Starting test_0")
        p = Purity(y_true0, y_pred0).purity
        self.assertEqual(1, p)
        p = Purity(y_true0, y_pred1).purity
        self.assertEqual(.6, p)
