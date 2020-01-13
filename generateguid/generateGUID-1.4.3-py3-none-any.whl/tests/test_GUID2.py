#!/usr/bin/python
# -*- coding: utf-8 -*-

from guid_core.generate_GUID import generate_GUID2

import unittest

GUID = generate_GUID2('Jean-Michel', "Frégnac", '1949-03-22', 'M')


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_guid(self):
        nom = 'Jean-Michel'
        prenom = "Frégnac"
        age = '22/03/1949'
        sexe = 'M'
        self.assertEqual(generate_GUID2(nom, prenom, age, sexe), GUID)

    def test_guid1(self):
        nom = 'Jean-michel'
        prenom = "Frégnac"
        age = '22/03/1949'
        sexe = 'M'

        self.assertEqual(generate_GUID2(nom, prenom, age, sexe), GUID)

    def test_guid2(self):
        nom = 'Jean-michel'
        prenom = 'Fregnac'
        age = '22/03/1949'
        sexe = 'M'

        self.assertEqual(generate_GUID2(nom, prenom, age, sexe), GUID)

    def test_guid3(self):
        nom = 'Jean michel'
        prenom = "Frégnac"
        age = '22/03/1949'
        sexe = 'M'

        self.assertEqual(generate_GUID2(nom, prenom, age, sexe), GUID)

    def test_guid4(self):
        nom = 'Jean-Michel'
        prenom = "Frégnac"
        age = r"22\03\1949"
        sexe = 'M'

        self.assertEqual(generate_GUID2(nom, prenom, age, sexe), GUID)

    def test_guid5(self):
        nom = 'Jean-Michel'
        prenom = 'Fregnac'
        age = '22-03-1949'
        sexe = 'M'

        self.assertEqual(generate_GUID2(nom, prenom, age, sexe), GUID)

    def test_guid6(self):
        nom = 'Jean michel'
        prenom = "Frégnac"
        age = '22 03 1949'
        sexe = 'M'

        self.assertEqual(generate_GUID2(nom, prenom, age, sexe), GUID)

    def test_guid7(self):
        nom = 'jean-michel'
        prenom = "frégnac"
        age = '22/03/1949'
        sexe = 'M'

        self.assertEqual(generate_GUID2(nom, prenom, age, sexe), GUID)

    def test_guid8(self):
        nom = 'Jean michel'
        prenom = "frégnac"
        age = '22031949'
        sexe = 'M'

        self.assertEqual(generate_GUID2(nom, prenom, age, sexe), GUID)


if __name__ == '__main__':

    unittest.main()
