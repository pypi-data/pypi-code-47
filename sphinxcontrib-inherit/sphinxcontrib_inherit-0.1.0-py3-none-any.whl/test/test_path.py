# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from sphinxcontrib.inherit.path import (
    Path, path_contains, path_subdir_contains)
from unittest import TestCase

abs_path = Path('/abs/path')
abs_path_to = abs_path / 'to'
abs_path_to_somewhere = abs_path_to / 'somewhere'
abs_path_to_nowhere = abs_path_to / 'nowhere'

rel_path = Path('rel/path')
rel_path_to = rel_path / 'to'
rel_path_to_somewhere = rel_path_to / 'somewhere'
rel_path_to_nowhere = rel_path_to / 'nowhere'

other_abs_path = Path('/other/abs/path')
other_rel_path = Path('other/rel/path')


class TestInheritPath(TestCase):

    def test_absolute_path_contains(self):
        "Test absolute path contains another path."
        self.assertTrue(path_contains(abs_path, abs_path_to))
        self.assertTrue(path_contains(abs_path, abs_path_to_somewhere))

    def test_absolute_path_contains_str(self):
        "Test absolute path contains another string path."
        self.assertTrue(path_contains(abs_path, str(abs_path_to)))
        self.assertTrue(path_contains(abs_path, str(abs_path_to_somewhere)))

    def test_absolute_path_does_not_contain(self):
        "Test absolute path does not contain different path."
        self.assertFalse(path_contains(other_abs_path, abs_path))
        self.assertFalse(path_contains(other_abs_path, abs_path_to))
        self.assertFalse(path_contains(other_abs_path, abs_path_to_somewhere))

        self.assertFalse(path_contains(abs_path, other_abs_path))
        self.assertFalse(path_contains(abs_path_to, other_abs_path))
        self.assertFalse(path_contains(abs_path_to_somewhere, other_abs_path))

    def test_absolute_path_does_not_contain_relative(self):
        "Test absolute path does not contain relative path."
        self.assertFalse(path_contains(abs_path, rel_path_to))
        self.assertFalse(path_contains(abs_path, str(abs_path_to)[1:]))

    def test_relative_path_contains(self):
        "Test relative path contains another path."
        self.assertTrue(path_contains(rel_path, rel_path_to))
        self.assertTrue(path_contains(rel_path, rel_path_to_somewhere))

    def test_relative_path_contains_str(self):
        "Test relative path contains another string path."
        self.assertTrue(path_contains(rel_path, str(rel_path_to)))
        self.assertTrue(path_contains(rel_path, str(rel_path_to_somewhere)))

    def test_relative_path_does_not_contain(self):
        "Test relative path does not contain different path."
        self.assertFalse(path_contains(other_rel_path, rel_path))
        self.assertFalse(path_contains(other_rel_path, rel_path_to))
        self.assertFalse(path_contains(other_rel_path, rel_path_to_somewhere))

        self.assertFalse(path_contains(rel_path, other_rel_path))
        self.assertFalse(path_contains(rel_path_to, other_rel_path))
        self.assertFalse(path_contains(rel_path_to_somewhere, other_rel_path))

    def test_relative_path_does_not_contain_absolute(self):
        "Test relative path does not contain absolute path."
        self.assertFalse(path_contains(rel_path, abs_path_to))
        self.assertFalse(path_contains(rel_path, Path('/') / rel_path_to))

    def test_absolute_path_subdir_contains(self):
        "Test absolute path subdir contains another path."
        self.assertTrue(path_subdir_contains(abs_path, abs_path_to_somewhere))
        self.assertTrue(path_subdir_contains(abs_path, abs_path_to_nowhere))

    def test_absolute_path_subdir_contains_str(self):
        "Test absolute path subdir contains another string path."
        self.assertTrue(path_subdir_contains(
            abs_path, str(abs_path_to_somewhere)))
        self.assertTrue(path_subdir_contains(
            abs_path, str(abs_path_to_nowhere)))

    def test_absolute_path_item_in_dir_not_in_subdir(self):
        "Test absolute path item in directory but not in subdirectory."
        self.assertFalse(path_subdir_contains(abs_path, abs_path_to))
        self.assertFalse(path_subdir_contains(abs_path, str(abs_path_to)))

    def test_absolute_path_subdir_does_not_contain(self):
        "Test absolute path subdir does not contain different path."
        self.assertFalse(path_subdir_contains(other_abs_path, abs_path))
        self.assertFalse(path_subdir_contains(other_abs_path, abs_path_to))
        self.assertFalse(path_subdir_contains(
            other_abs_path, abs_path_to_somewhere))

        self.assertFalse(path_subdir_contains(abs_path, other_abs_path))
        self.assertFalse(path_subdir_contains(abs_path_to, other_abs_path))
        self.assertFalse(path_subdir_contains(
            abs_path_to_somewhere, other_abs_path))

    def test_absolute_path_subdir_does_not_contain_relative(self):
        "Test absolute path subdir does not contain relative path."
        self.assertFalse(path_subdir_contains(abs_path, rel_path_to_somewhere))
        self.assertFalse(path_subdir_contains(
            abs_path, str(abs_path_to_somewhere)[1:]))

    def test_relative_path_subdir_contains(self):
        "Test relative path subdir contains another path."
        self.assertTrue(path_subdir_contains(rel_path, rel_path_to_somewhere))
        self.assertTrue(path_subdir_contains(rel_path, rel_path_to_nowhere))

    def test_relative_path_subdir_contains_str(self):
        "Test relative path subdir contains another string path."
        self.assertTrue(path_subdir_contains(
            rel_path, str(rel_path_to_somewhere)))
        self.assertTrue(path_subdir_contains(
            rel_path, str(rel_path_to_nowhere)))

    def test_relative_path_item_in_dir_not_in_subdir(self):
        "Test relative path item in directory but not in subdirectory."
        self.assertFalse(path_subdir_contains(rel_path, rel_path_to))
        self.assertFalse(path_subdir_contains(rel_path, str(rel_path_to)))

    def test_relative_path_subdir_does_not_contain(self):
        "Test relative path subdir does not contain different path."
        self.assertFalse(path_subdir_contains(other_rel_path, rel_path))
        self.assertFalse(path_subdir_contains(other_rel_path, rel_path_to))
        self.assertFalse(path_subdir_contains(
            other_rel_path, rel_path_to_somewhere))

        self.assertFalse(path_subdir_contains(rel_path, other_rel_path))
        self.assertFalse(path_subdir_contains(rel_path_to, other_rel_path))
        self.assertFalse(path_subdir_contains(
            rel_path_to_somewhere, other_rel_path))

    def test_relative_path_subdir_does_not_contain_absolute(self):
        "Test relative path subdir does not contain absolute path."
        self.assertFalse(path_subdir_contains(rel_path, abs_path_to_somewhere))
        self.assertFalse(path_subdir_contains(
            rel_path, Path('/') / rel_path_to_somewhere))
