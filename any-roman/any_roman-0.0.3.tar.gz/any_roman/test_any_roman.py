#!/usr/bin/env python3

import unittest
import doctest 
import any_roman


def load_tests(loader, suite, ignore):
    suite.addTests(doctest.DocTestSuite(any_roman))
    suite.addTest(doctest.DocFileSuite('test_any_roman.txt'))
    return suite


def test():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    test()
