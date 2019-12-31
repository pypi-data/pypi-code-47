import io
import unittest

from ppci.arch.jvm import read_class_file, class_to_ir


class JavaTestCase(unittest.TestCase):
    def test_class_file_loading(self):
        f = io.BytesIO(simple_class_file)
        class_file = read_class_file(f)
        class_to_ir(class_file)


simple_class_file = b'\xca\xfe\xba\xbe\x00\x00\x004\x00\x0f\n\x00' + \
    b'\x03\x00\x0c\x07\x00\r\x07\x00\x0e\x01\x00\x06<init>\x01\x00' + \
    b'\x03()V\x01\x00\x04Code\x01\x00\x0fLineNumberTable\x01\x00\x06' + \
    b'my_add\x01\x00\x05(II)I\x01\x00\nSourceFile\x01\x00\x0bTest14' + \
    b'.java\x0c\x00\x04\x00\x05\x01\x00\x06Test14\x01\x00\x10java/lan' + \
    b'g/Object\x00 \x00\x02\x00\x03\x00\x00\x00\x00\x00\x02\x00\x00' + \
    b'\x00\x04\x00\x05\x00\x01\x00\x06\x00\x00\x00\x1d\x00\x01\x00' + \
    b'\x01\x00\x00\x00\x05*\xb7\x00\x01\xb1\x00\x00\x00\x01\x00\x07' + \
    b'\x00\x00\x00\x06\x00\x01\x00\x00\x00\x02\x00\x08\x00\x08\x00\t' + \
    b'\x00\x01\x00\x06\x00\x00\x00\x1e\x00\x02\x00\x02\x00\x00\x00' + \
    b'\x06\x1a\x1b`\x04`\xac\x00\x00\x00\x01\x00\x07\x00\x00\x00\x06' + \
    b'\x00\x01\x00\x00\x00\x04\x00\x01\x00\n\x00\x00\x00\x02\x00\x0b'


if __name__ == '__main__':
    unittest.main()
