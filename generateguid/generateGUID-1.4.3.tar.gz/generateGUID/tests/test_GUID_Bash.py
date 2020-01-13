# coding: utf-8

from guid_core.generate_GUID import generate_GUID
import unittest

GUID = generate_GUID("Jean-Michel"+"Frégnac"+"22/03/1949"+"M")


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_guid(self):
        key = "Jean-Michel"+"Frégnac"+"22/03/1949"+"M"

        self.assertEqual(generate_GUID(key), GUID)

    def test_guid1(self):

        key = "Jean-michel"+"Frégnac"+"22/03/1949"+"M"
        self.assertEqual(generate_GUID(key), GUID)

    def test_guid2(self):

        key = "Jean-michel"+"Fregnac"+"22/03/1949"+"M"
        self.assertEqual(generate_GUID(key), GUID)

    def test_guid3(self):

        key = "Jean michel"+"Frégnac"+"22/03/1949"+"M"
        self.assertEqual(generate_GUID(key), GUID)

    def test_guid4(self):

        key = "Jean-Michel"+"Frégnac"+r"22\03\1949"+"M"
        self.assertEqual(generate_GUID(key), GUID)

    def test_guid5(self):

        key = "Jean-michel"+"Fregnac"+"22-03-1949"+"M"

        self.assertEqual(generate_GUID(key), GUID)

    def test_guid6(self):

        key = "Jean michel"+"Frégnac"+"22 03 1949"+"M"
        self.assertEqual(generate_GUID(key), GUID)

    def test_guid7(self):

        key = "jean-michel"+"frégnac"+"22/03/1949"+"M"
        self.assertEqual(generate_GUID(key), GUID)

    def test_guid8(self):

        key = "Jean michel"+"Frégnac"+"22031949"+"M"
        self.assertEqual(generate_GUID(key), GUID)


if __name__ == '__main__':

    unittest.main()
