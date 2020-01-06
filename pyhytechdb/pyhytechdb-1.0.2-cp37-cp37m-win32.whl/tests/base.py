import unittest
import pyhytechdb


import logging
logging.basicConfig(level=logging.DEBUG)

class TestBase(unittest.TestCase):
    user = 'test'
    passwd = 'test'
    server = 'tcpip:/localhost:1000'


    def setUp(self):
        self.connection = pyhytechdb.connect(self.server, self.user, self.passwd)

    def tearDown(self):
        self.connection.close()

