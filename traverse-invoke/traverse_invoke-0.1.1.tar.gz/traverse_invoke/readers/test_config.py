import pytest
from traverse_invoke.readers import get_config

@pytest.fixture
def file(tmp_path):
    content ="""
[DEFAULT]
foo=1

[Module.submodule]
bar=2

[Module]
baz=3
    """
    p = tmp_path / 'config.ini'
    p.write_text(content)
    return p

def test_config(file):
    print(file)
    print(file.read_text())
    conf = get_config(str(file))
    assert conf['Module']['submodule']['bar'] == '2'
    assert conf['Module']['baz'] == '3'


