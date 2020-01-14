import unittest
import sys
sys.path.append('../')
from Spitzer.config import config

class test_config(unittest.TestCase):

    def test_get(self):
        result = config.get_dynamic('unittest')
        self.assertEqual('ignore me', result)

    def test_set(self):
        config.set_dynamic('unittest', 'test value')
        self.assertEqual('test value', config.dynamic['unittest'])

    def test_set_value(self):
        config.set_value(['unittest', 'different text'])
        self.assertEqual('different text', config.dynamic['unittest'])

if __name__ == '__main__':
    unittest.main()