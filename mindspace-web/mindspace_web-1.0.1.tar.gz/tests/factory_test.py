import os.path

from jinja2 import Environment, FileSystemLoader
from klein import Klein
from mindspace_web import MindspaceFactory, __file__ as mwf


def test_init(f):
    assert isinstance(f, MindspaceFactory)
    k = f.klein_app
    assert isinstance(k, Klein)
    assert isinstance(k.environment, Environment)
    assert k.environment.loader is k.loader
    assert isinstance(k.loader, FileSystemLoader)
    first, second = k.loader.searchpath
    assert first == os.path.join(os.path.dirname(mwf), 'templates')
    assert second == os.path.join(os.getcwd(), 'templates')
