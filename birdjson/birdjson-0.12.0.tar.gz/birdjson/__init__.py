from datetime import datetime
from typing import Any, Union

try:
    import simplejson as json
except ImportError:
    import json


class JsonObject:
    def __init__(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, dict):
                kwargs.update(arg)
            elif hasattr(arg, '__dict__'):
                kwargs.update(arg.__dict__)
            else:
                raise AttributeError(f'invalid positional argument: {arg}')

        for k, v in kwargs.items():
            _inject_value(self, k, v)

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
        _inject_value(self, key, value)

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
        return self.__dict__[key] if key in self else default_value


def load_file(filename) -> JsonObject:
    with open(filename) as f:
        return load(f)


def load(fp) -> JsonObject:
    return _load(json.load(fp))


def loads(s) -> JsonObject:
    return _load(json.loads(s))


def load_dict(obj) -> JsonObject:
    return _load(obj)


def load_obj(obj) -> JsonObject:
    return _load(obj)


def dumps(obj, **kwargs) -> str:
    return json.dumps(obj, default=lambda o: _json_default(o), **kwargs)


def makes(**kwargs) -> str:
    """Create a json string from arguments"""
    return dumps(JsonObject(**kwargs))


def make(**kwargs) -> JsonObject:
    """Create a json object from arguments"""
    return JsonObject(**kwargs)


def _load(js) -> Union[JsonObject, list]:
    if isinstance(js, dict):
        return JsonObject(js)
    elif hasattr(js, '__dict__'):
        return JsonObject(js.__dict__)
    elif isinstance(js, (list, tuple)):
        return _load_list(js)
    else:
        return js


def _load_list(js) -> list:
    lst = []
    for v in js:
        _append_value(lst, v)
    return lst


def _append_value(parent, value):
    if isinstance(value, dict):
        parent.append(JsonObject(value))
    elif hasattr(value, '__dict__'):
        parent.append(JsonObject(value.__dict__))
    elif isinstance(value, (list, tuple)):
        parent.append(_load_list(value))
    else:
        parent.append(value)


def _inject_value(parent, key, value):
    if isinstance(value, dict):
        parent.__dict__[str(key)] = JsonObject(value)
    elif hasattr(value, '__dict__'):
        parent.__dict__[str(key)] = JsonObject(value.__dict__)
    elif isinstance(value, (list, tuple)):
        parent.__dict__[str(key)] = _load_list(value)
    else:
        parent.__dict__[str(key)] = value


def _json_default(o) -> Union[str, dict]:
    if isinstance(o, datetime):
        return str(o)
    else:
        return o.__dict__
