import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    dir = __file__.replace('main_test.py', '')
    suite = loader.discover(dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)