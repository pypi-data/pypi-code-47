import unittest

__dt__ = __import__("dynamodb-traverse")


class TestBaseObject(unittest.TestCase):
    def test_log_file_generation(self):
        obj = __dt__.Base()
        obj.info("test msg")

    def test_log_silence(self):
        obj = __dt__.Base(silence=True)
        obj.info("test msg")

    def test_log_not_to_screen(self):
        obj = __dt__.Base(log_to_screen=False)
        obj.info("test msg")
