import os

import pytest

from ..ymlConfiger import YmlConfiger


@pytest.fixture(scope='class')
def ymlConfiger():
    cwd = os.path.dirname(__file__)
    ordered_file_paths = [os.path.join(cwd, filename) for filename in ['pytestSample-1.yaml', 'pytestSample-2.yaml']]
    return YmlConfiger(ordered_file_paths)


class TestYmlConfiger:
    def test_get(self, ymlConfiger):
        assert ymlConfiger.get('ad') == 12

    def test_verbose_get(self, ymlConfiger):
        verbose_return = ymlConfiger.get('ad', verbose=True)
        assert verbose_return[0] == 12
        assert 'pytestSample-2.yaml' in verbose_return[1]
