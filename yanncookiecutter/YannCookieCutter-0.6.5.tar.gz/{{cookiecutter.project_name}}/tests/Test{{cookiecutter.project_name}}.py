import unittest

from {{ cookiecutter.project_name }}.{{cookiecutter.project_slug}} import fct


class Test{{ cookiecutter.project_name }} (unittest.TestCase):
    def test_01(self):
        pass


if __name__ == '__main__':
    unittest.main()
