import unittest
from src.ssdp import SimpleServiceDiscoveryProtocol, ST_ROKU, DiscoveryMessage, HTTPResponse

class TestSimpleServiceDiscoveryProtocol(unittest.TestCase):

    def setUp(self):
        self.ssdp = SimpleServiceDiscoveryProtocol(ST_ROKU)

    def tearDown(self):
        pass
    
    def test_default_timout(self):
        self.assertEqual(self.ssdp.timeout, 1)

    def test_timeout(self):
        SimpleServiceDiscoveryProtocol.settimeout(3)
        ssdp = SimpleServiceDiscoveryProtocol(ST_ROKU)
        self.assertEqual(ssdp.timeout, 3)
        with self.assertRaises(ValueError):
            SimpleServiceDiscoveryProtocol.settimeout('string')
    
    def test_broadcast(self):
        result = self.ssdp.broadcast()
        self.assertIsInstance(result, list)
        if len(result) > 0:
            self.assertIsInstance(result[0], HTTPResponse)
        else:
            print('No response from broadcast.')
    
    def test_message(self):
        self.assertIsInstance(self.ssdp.message, DiscoveryMessage)