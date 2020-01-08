import unittest
from helpers import files


class TestAllFileInDirectory(unittest.TestCase):

    def test_all_files_in_directory(self):
        file_list = files.get_all_files_in_directory('.')
        self.assertEqual(1, len(file_list))


if __name__ == '__main__':
    unittest.main()
