from parser import Parser
from service import Service
from status import Status
from unittest import TestCase


class TestResult(TestCase):
    def setUp(self):
        self.parser = Parser()

    def tearDown(self):
        pass

    def test_parse_search(self):
        with open('resources/search.xml', 'r') as f:
            xml_result = f.read()
        ret = self.parser.parse(xml_result.encode('utf-8'))
        self.assertEqual(ret.status, Status.OK.value)
        self.assertEqual(ret.servicecd, Service.SEARCH.value)
        self.assertTrue(ret.message is None)
        self.assertTrue(ret.total_results > 0)
        self.assertEqual(ret.start_index, 1)
        self.assertEqual(ret.items_per_page, 3)
        self.assertEqual(len(ret.entries), 3)

    def test_parse_list(self):
        with open('resources/list.xml', 'r') as f:
            xml_result = f.read()
        ret = self.parser.parse(xml_result.encode('utf-8'))
        self.assertEqual(ret.status, Status.OK.value)
        self.assertEqual(ret.servicecd, Service.LIST.value)
        self.assertTrue(ret.message is None)
        self.assertTrue(ret.total_results > 0)
        self.assertEqual(ret.start_index, 1)
        self.assertEqual(ret.items_per_page, 1)
        self.assertEqual(len(ret.entries), 1)
