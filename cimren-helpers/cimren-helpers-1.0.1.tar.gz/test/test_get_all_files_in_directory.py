import sys
sys.path.insert(0, '/helpers')

import unittest
from helpers import files


class TestAllFileInDirectory(unittest.TestCase):

    def test_all_files_in_directory(self):
        file_list = files.get_all_files_in_directory('.')
        print(file_list)
        self.assertEqual(2, len(file_list))


if __name__ == '__main__':
    unittest.main()
