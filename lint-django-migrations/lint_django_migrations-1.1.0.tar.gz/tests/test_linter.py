import unittest
from lint_django_migrations.migration_linter import MigrationLinter
from io import StringIO


class LinterFunctionsTestCase(unittest.TestCase):
    def app_is_valid(self, app):
        linter = MigrationLinter(
            include_apps=[app],
            state_path=None,
            std_out=StringIO()
        )
        return linter.lint_all_migrations()["valid"]

    def test_all_success(self):
        self.assertTrue(self.app_is_valid("app_correct"))

    def test_not_null(self):
        self.assertFalse(self.app_is_valid("app_add_not_null_column"))

    def test_not_null_followed_by_default(self):
        self.assertFalse(self.app_is_valid("app_add_not_null_column_followed_by_default"))

    def test_alter_column(self):
        self.assertFalse(self.app_is_valid("app_alter_column"))

    def test_alter_column_make_null(self):
        self.assertFalse(self.app_is_valid("app_alter_column_make_null"))

    def test_add_column_with_default(self):
        self.assertFalse(self.app_is_valid("app_add_column_with_default"))

    def test_create_table_with_not_null_column(self):
        self.assertTrue(self.app_is_valid("app_create_table_with_not_null_column"))

    def test_drop_column(self):
        self.assertFalse(self.app_is_valid("app_drop_column"))

    def test_rename_column(self):
        self.assertFalse(self.app_is_valid("app_rename_column"))

    def test_rename_table(self):
        self.assertFalse(self.app_is_valid("app_rename_table"))
