# at least four instances of $16, acting as synchronisation bytes;
# an instance of $24, acting to signal the end of the synchronisation bytes;


#
# two reserved bytes;
#
# a single byte specifying the data type of the upcoming file, one of:
# $00: the file is BASIC;
# $80: the file is machine code;
# a single byte specifying how to execute the upcoming file:
# $80: RUN as BASIC;
# $C7: execute as machine code;
#
# the ending address of the data stored, two bytes in big-endian form;
# the starting address of the data stored, two bytes in big-endian form;
#
# a reserved byte;
#
# the file's name — ASCII format, 16 characters at most, NULL terminated;
#
# the body of the file.

"""
Unit test for prg2tap
"""
import unittest

from prg2tap import sync_bytes, code_type, address_range, reserved, filename, body, process

class TestPrg2tap(unittest.TestCase):
    """Standard issues test case class"""
    def test_sync_bytes(self):
        # at least four instances of $16, acting as synchronisation bytes;
        # an instance of $24, acting to signal the end of the synchronisation bytes;
        expected = bytearray(b'\x16\x16\x16\x16\x24')
        actual = sync_bytes()

        self.assertEqual(actual, expected)


    def test_code_type(self):
        # $80: the file is machine code;
        # a single byte specifying how to execute the upcoming file:
        # $80: RUN as BASIC;
        # $C7: execute as machine code;
        expected = bytearray(b'\x80\xc7')
        actual = code_type()

        self.assertEqual(actual, expected)

    def test_address_range(self):
        # the ending address of the data stored, two bytes in big-endian form;
        # the starting address of the data stored, two bytes in big-endian form;
        expected = bytearray(b'\x08\x05\x08\x00')
        prg = bytearray(b'\x00\x08\xa9\x00\x8d\x02\xa9')
        actual = address_range(prg)

        self.assertEqual(actual, expected)

    def test_reserved(self):
        expected = bytearray(b'\x00\x00')
        actual = reserved(2)

        self.assertEqual(actual, expected)

    def test_filename(self):
        expected = bytearray(b'\x48\x45\x4c\x4c\x4f\x00')
        actual = filename('HELLO')

        self.assertEqual(actual, expected)

    def test_body(self):
        prg = bytearray(b'\x00\x08\xa9\x00\x8d\x02\xa9')
        expected = bytearray(b'\xa9\x00\x8d\x02\xa9')
        actual = body(prg)

        self.assertEqual(actual, expected)

    def test_header(self):
        prg = bytearray(b'\x00\x08\xa9\x00\x8d\x02\xa9')
        expected = bytearray(b'\x16\x16\x16\x16\x24\x00\x00\x80\xc7\x08\x05\x08\x00\x00\x48\x45\x4c\x4c\x4f\x00\xa9\x00\x8d\x02\xa9')
        actual = process(prg, 'HELLO')

        self.assertEqual(len(actual), len(expected))
        for i in range(0, len(expected)):
            self.assertEqual(actual[i], expected[i], 'at index:{0}'.format(i))

