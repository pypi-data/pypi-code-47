
# Unit test execution instructions
# $ pwd
# ~/dnspy/
#
# $ python -m unittest test/test_dnspy.py
# ......
# ----------------------------------------------------------------------
# Ran 6 tests in 0.301s
#
# OK

import unittest

from dnspy.dnspy import Dnspy


class DnspyTestCase(unittest.TestCase):

    def setUp(self):
        self.dno = Dnspy()

    def tearDown(self):
        pass

    def test_subdoms(self):
        expected = ['co.uk', 'google.co.uk', 'www.google.co.uk']
        result = self.dno.subdoms('1.2.3.www.google.co.uk')
        self.assertEqual(expected, result)

    def test_subdoms_n(self):
        expected = ['co.uk', 'google.co.uk', 'www.google.co.uk', '3.www.google.co.uk', '2.3.www.google.co.uk']
        result = self.dno.subdoms('1.2.3.www.google.co.uk', n=5)
        self.assertEqual(expected, result)

    def test_domlabels(self):
        expected = ['co.uk', 'google', 'www']
        result = self.dno.domlabels('1.2.3.www.google.co.uk')
        self.assertEqual(expected, result)

    def test_subdom_count(self):
        expected = ('google.co.uk', 4)
        result = self.dno.subdom_count('1.2.3.www.google.co.uk')
        self.assertEqual(expected, result)

    def test_idna_dom(self):
        expected = ['xn--h2brj9c', 'google.xn--h2brj9c']
        result = self.dno.subdoms('google.xn--h2brj9c')
        self.assertEqual(expected, result)

    def test_etld_only(self):
        expected = ['co.uk']
        result = self.dno.subdoms('co.uk')
        self.assertEqual(expected, result)

    def test_platform_sh_1(self):
        expected = ['bar.platform.sh', 'foo.bar.platform.sh']
        result = self.dno.subdoms('foo.bar.platform.sh')
        self.assertEqual(expected, result)

    def test_platform_sh_2(self):
        expected = ['platform.sh']
        result = self.dno.subdoms('platform.sh')
        self.assertEqual(expected, result)

    def test_com(self):
        expected = ['com']
        result = self.dno.subdoms('com')
        self.assertEqual(expected, result)

    def test_mm_1(self):
        expected = ['foo.mm']
        result = self.dno.subdoms('foo.mm')
        self.assertEqual(expected, result)

    def test_mm_2(self):
        expected = ['mm']
        result = self.dno.subdoms('mm')
        self.assertEqual(expected, result)
