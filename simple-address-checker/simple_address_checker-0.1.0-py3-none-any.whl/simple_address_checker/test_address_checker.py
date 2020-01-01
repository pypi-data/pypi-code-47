from .address_checker import AddressChecker, SubdistrictPayload
import unittest


class TestAddressChecker(unittest.TestCase):

    def setUp(self):
        self.subdistrict = SubdistrictPayload.load_subdistricts('id')
        self.address_checker = AddressChecker()

    def test_get_sim_subdistrict(self):
        result = self.address_checker.get_sim_subdistrict('pameungpek', self.subdistrict)
        expected = [
            {
                "score": 1,
                "subdistrict_code": "32.04.14",
                "subdistrict_name": "PAMEUNGPEUK".lower(),
                "city_name": "KAB. BANDUNG".lower(),
            },
            {
                "score": 1,
                "subdistrict_code": "32.05.27",
                "subdistrict_name": "PAMEUNGPEUK".lower(),
                "city_name": "KAB. GARUT".lower(),
            }
        ]
        self.assertEqual(result, expected)

    def test_get_sim_city(self):
        result = self.address_checker.get_sim_city('kota cimhi', self.subdistrict, 1)
        expected = [
            {
                "score": 1,
                "subdistrict_code": "32.77.01",
                "subdistrict_name": "CIMAHI SELATAN".lower(),
                "city_name": "KOTA CIMAHI".lower(),
            }
        ]
        self.assertEqual(result, expected)

    def test_suggest(self):
        result = self.address_checker.suggest('pameungpek', 'bandung', self.subdistrict)
        expected = [{'score': 5, 'city_name': 'kab. bandung', 'subdistrict_name': 'pameungpeuk',
                     'subdistrict_code': '32.04.14'}]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
