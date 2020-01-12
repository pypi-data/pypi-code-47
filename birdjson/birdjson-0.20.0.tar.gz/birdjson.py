import inspect
import json
import re
from datetime import datetime
from types import MappingProxyType
from typing import Any, Union

import inflection

__all__ = ['JsonObject', 'KeyConverter', 'GenericObject']


def _attr_is_function(cls, attr):
    return hasattr(cls, attr) and inspect.isfunction(getattr(cls, attr))


class KeyConverter:
    @staticmethod
    def camel(key):
        return inflection.camelize(key, uppercase_first_letter=False)

    @staticmethod
    def Camel(key):
        return inflection.camelize(key, uppercase_first_letter=True)

    @staticmethod
    def snake(key):
        return inflection.underscore(key)

    @staticmethod
    def mongo(key):
        """
        sanitize keys for mongo databases
        - periods become underscores
        - prefix underscore if key starts with $
        """
        if key[0] == '$':
            key = '_' + key
        return re.sub(r'[.$ ]', '_', key)

    @staticmethod
    def sanitize_attr(key):
        """
        sanitize keys to be used as python attributes
        - do not start with a number
        - spaces, dashes, and periods become underscores
        """
        if '0' <= key[0] <= '9':
            key = '_' + key
        return re.sub(r'[^_a-zA-Z0-9]', '_', key)

    @staticmethod
    def all(*converters):
        """Combine multiple converters into one ordered converter"""
        return lambda key: map(lambda conv: conv(key), converters)


class GenericObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = _load(v, cls=self.__class__)

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        if type(key) is int and key < len(self):
            # assuming insertion order, which should be guaranteed in py 3.6/3.7+ (PEP 520)
            return self.__dict__[list(self.__dict__.keys())[key]]
        return None

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __setattr__(self, key, value):
        if _attr_is_function(self.__class__, key):
            # preserve class methods if an attribute would overwrite it
            # such that if a user sets obj.items = 5, obj.items() will still
            # be callable under the new attribute obj._items(), and obj.items will equal 5
            setattr(self.__class__, f'_{key}', getattr(self.__class__, key))
        self.__dict__[key] = value

    def __getattr__(self, attr):
        # This method is called ONLY when an attribute does NOT exist
        if (
            attr.startswith('_')
            and not attr.startswith('__')
            and _attr_is_function(self.__class__, attr[1:])
        ):
            return getattr(self, attr[1:])

        return None

    def __delitem__(self, key):
        if key in self.__dict__:
            del self.__dict__[key]

    def __contains__(self, key):
        return key in self.__dict__

    def __repr__(self):
        return dumps(self)

    def __str__(self):
        return dumps(self)

    def __iter__(self):
        for k, v in self.__dict__.items():
            yield k, v

    def __len__(self):
        return len(self.__dict__.keys())

    def __delattr__(self, key):
        if key in self.__dict__:
            del self.__dict__[key]

    def __eq__(self, o: object) -> bool:
        # todo: implement equals better
        return str(self) == str(o)

    def keys(self):
        return self.__dict__.keys()

    def keylist(self):
        return list(self.__dict__.keys())

    def items(self):
        return self.__dict__.items()

    def values(self):
        return self.__dict__.values()

    def valuelist(self):
        return list(self.__dict__.values())

    def convert_to(self, cls, key_conv=None) -> Any:
        return _load(self, cls=cls, key_conv=key_conv)

    def obj(self, cls=dict, key_conv=None) -> Union[Any, dict]:
        return self.convert_to(cls, key_conv=key_conv)

    def dict(self, key_conv=None) -> Union[Any, dict]:
        return self.convert_to(dict, key_conv=key_conv)

    def get(self, key: str, default=None) -> Any:
        return self[key] if key in self else default


class JsonObject(GenericObject):
    def json(self, indent=None, separators=None, key_conv=None, **kwargs) -> str:
        return self.dumps(indent=indent, separators=separators, key_conv=key_conv, **kwargs)

    def dumps(self, indent=None, separators=None, key_conv=None, **kwargs) -> str:
        return dumps(self, indent=indent, separators=separators, key_conv=key_conv, **kwargs)

    def pretty(self, indent=2, separators=None, key_conv=None, **kwargs) -> str:
        return self.dumps(indent=indent, separators=separators, key_conv=key_conv, **kwargs)

    def minify(self, key_conv=None, **kwargs):
        return self.dumps(separators=(',', ':'), key_conv=key_conv, **kwargs)

    def camel(self, **kwargs):
        return self.dumps(key_conv=KeyConvertor.camel, **kwargs)

    def yaml(self, **kwargs) -> str:
        import birdyaml
        import yaml
        yaml.add_representer(JsonObject, birdyaml._yaml_obj_representer)
        return birdyaml.dumps(self, **kwargs)

    def write_json(self, filename: str, **kwargs):
        with open(filename, 'w') as f:
            f.write(self.json(**kwargs))

    def write_yaml(self, filename: str, **kwargs):
        with open(filename, 'w') as f:
            f.write(self.yaml(**kwargs))


def load_file(filename: str, key_conv=None) -> JsonObject:
    with open(filename) as f:
        return load(f, key_conv=key_conv)


def load(fp, key_conv=None) -> JsonObject:
    return _load(json.load(fp), key_conv=key_conv)


def loads(s: str, key_conv=None) -> JsonObject:
    return _load(json.loads(s), key_conv=key_conv)


def load_obj(obj: Any, cls=JsonObject, key_conv=None) -> JsonObject:
    return _load(obj, cls=cls, key_conv=key_conv)


def dumps(obj: Any, indent=None, key_conv=None, **kwargs) -> str:
    if key_conv is not None and type(key_conv) is not str:
        obj = _load(obj, cls=dict, key_conv=key_conv)
    return json.dumps(obj, indent=indent, default=_json_default_encoder, **kwargs)


def makes(key_conv=None, **kwargs) -> str:
    """Create a json string from arguments"""
    return dumps(_load(kwargs, cls=dict, key_conv=key_conv))


def make(cls=JsonObject, key_conv=None, **kwargs) -> JsonObject:
    """Create a json object from arguments"""
    return _load(kwargs, cls=cls, key_conv=key_conv)


def make_obj(cls, key_conv=None, **kwargs) -> Any:
    return _load(kwargs, cls=cls, key_conv=key_conv)


def make_dict(key_conv=None, **kwargs) -> dict:
    return _load(kwargs, cls=dict, key_conv=key_conv)


def _load(js, cls: Any = JsonObject, key_conv=None) -> Union[JsonObject, Any]:
    if isinstance(js, (list, tuple)):
        return [_load(v, cls=cls, key_conv=key_conv) for v in js]
    elif isinstance(js, MappingProxyType):
        return _load_dict(js.copy(), cls=cls, key_conv=key_conv)
    elif isinstance(js, dict):
        return _load_dict(js, cls=cls, key_conv=key_conv)
    elif hasattr(js, '__dict__'):
        return _load_dict(js.__dict__, cls=cls, key_conv=key_conv)
    return js


def _load_dict(d, cls=JsonObject, key_conv=None) -> Union[JsonObject, Any]:
    if key_conv is None:
        key_conv = str
    obj = cls()
    for key in d:
        obj[key_conv(key)] = _load(d[key], cls=cls, key_conv=key_conv)
    return obj


def _json_default_encoder(o) -> Any:
    if isinstance(o, datetime):
        return str(o)
    elif isinstance(o, MappingProxyType):
        return o.copy()
    elif hasattr(o, '__dict__'):
        return o.__dict__
    return str(o)


if __name__ == '__main__':
    x = make(y=2, json=3)

    # make sure __setitem__ preserves built-in functions when something overwrites it
    print(x.json)
    print(x._json())
    x['minify'] = 10
    print(x.minify)
    print(x._minify())

    # make sure __setattr__ preserves built-in functions when something overwrites it
    assert callable(x.items)
    x.items = [1, 2, 3, 4]
    assert not callable(x.items)
    print(x._items())
    assert callable(x._items)

    assert not callable(x.z)
    x.z = 5
    # Make sure it does not preserve non-callables
    assert x._z is None

    print(x.yaml())
    assert x.yaml() == x._yaml()

    js = load_file('../tests/config.json')
    print(js)
    print(js.dumps(key_conv=KeyConvertor.snake))
    print(js.dumps(key_conv=KeyConvertor.mongo))

    print(KeyConvertor.sanitize_attr('0.this.is.a-test'))
