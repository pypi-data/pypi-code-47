import unittest

__dt__ = __import__("dynamodb-traverse")


class TestBaseObject(unittest.TestCase):
    def setUp(self) -> None:
        self.test_subject = __dt__.Base()

    def test_logger(self):
        self.test_subject.info("test message")
