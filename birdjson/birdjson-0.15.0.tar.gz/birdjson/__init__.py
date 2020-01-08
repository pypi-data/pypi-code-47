from datetime import datetime
from typing import Any, Union

try:
    import simplejson as json
except ImportError:
    import json


__all__ = ['JsonObject']


class JsonObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
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

    def __getattr__(self, attr):
        # This method is called ONLY when an attribute does NOT exist
        return None

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __delattr__(self, key):
        if key in self.__dict__:
            del self.__dict__[key]

    def keys_(self):
        return self.__dict__.keys()

    def items_(self):
        return self.__dict__.items()

    def values_(self):
        return self.__dict__.values()

    def str_(self, **kwargs) -> str:
        return dumps(self, **kwargs)

    def json_(self, **kwargs) -> str:
        return dumps(self, **kwargs)

    def dumps_(self, **kwargs) -> str:
        return dumps(self, **kwargs)

    def obj_(self) -> Union[Any, dict]:
        return json.loads(str(self))

    def dict_(self) -> Union[Any, dict]:
        return json.loads(str(self))

    def get_(self, key: str, default_value: Any = None) -> Any:
        return self[key] if key in self else default_value

    def to_yaml_object_(self) -> 'YamlObject':
        import birdyaml
        return birdyaml.load_obj(self.obj_())

    def to_yaml_(self, **kwargs) -> str:
        return self.to_yaml_object_().dumps_(**kwargs)

    def write_json_(self, filename: str, **kwargs):
        with open(filename, 'w') as f:
            f.write(self.dumps_(**kwargs))

    def write_yaml_(self, filename: str, **kwargs):
        with open(filename, 'w') as f:
            f.write(self.to_yaml_(**kwargs))

    @staticmethod
    def loads(s: str) -> 'JsonObject':
        return loads(s)

    @staticmethod
    def load_file(filename: str) -> 'JsonObject':
        return load_file(filename)

    @staticmethod
    def load(fp) -> 'JsonObject':
        return load(fp)

    @staticmethod
    def load_dict(obj: dict) -> 'JsonObject':
        return _load(obj)

    @staticmethod
    def load_obj(obj: dict) -> 'JsonObject':
        return _load(obj)

    @staticmethod
    def makes(**kwargs) -> str:
        return dumps(JsonObject(**kwargs))


def load_file(filename: str) -> JsonObject:
    with open(filename) as f:
        return load(f)


def load(fp) -> JsonObject:
    return _load(json.load(fp))


def loads(s: str) -> JsonObject:
    return _load(json.loads(s))


def load_dict(obj: dict) -> JsonObject:
    return _load(obj)


def load_obj(obj: dict) -> JsonObject:
    return _load(obj)


def dumps(obj: Any, **kwargs) -> str:
    return json.dumps(obj, default=lambda o: _json_default(o), **kwargs)


def makes(**kwargs) -> str:
    """Create a json string from arguments"""
    return dumps(JsonObject(**kwargs))


def make(**kwargs) -> JsonObject:
    """Create a json object from arguments"""
    return JsonObject(**kwargs)


def _load(js) -> Union[JsonObject, list]:
    if type(js) is list:
        return _load_list(js)
    elif type(js) is dict:
        return _load_dict(js)
    return js


def _load_list(js) -> list:
    lst = []
    for v in js:
        _append_value(lst, v)
    return lst


def _load_dict(js) -> JsonObject:
    g = JsonObject()
    for key in js:
        _inject_value(g, key, js[key])
    return g


def _append_value(parent, value):
    if type(value) is list:
        lst = []
        for v in value:
            _append_value(lst, v)
        parent.append(lst)
    elif type(value) is dict:
        d = JsonObject()
        for k, v in value.items():
            _inject_value(d, k, v)
        parent.append(d)
    else:
        parent.append(value)


def _inject_value(parent, key, value):
    if isinstance(value, list):
        lst = []
        for v in value:
            _append_value(lst, v)
        parent.__dict__[str(key)] = lst
    elif isinstance(value, dict):
        d = JsonObject()
        for k, v in value.items():
            _inject_value(d, k, v)
        parent.__dict__[str(key)] = d
    else:
        parent.__dict__[str(key)] = value


def _json_default(o) -> Union[str, dict]:
    if isinstance(o, datetime):
        return str(o)
    else:
        return o.__dict__
