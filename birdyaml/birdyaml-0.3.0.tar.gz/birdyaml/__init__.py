import re
from typing import Any, Union

import yaml
import yaml.resolver

_DEFAULT_LOADER = yaml.FullLoader


class YamlObject:
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

    def yaml_(self, **kwargs) -> str:
        return dumps(self, **kwargs)

    def dumps_(self, **kwargs) -> str:
        return dumps(self, **kwargs)

    def obj_(self, loader=_DEFAULT_LOADER) -> Union[Any, dict]:
        return yaml.load(str(self), Loader=loader)

    def dict_(self, loader=_DEFAULT_LOADER) -> Union[Any, dict]:
        return yaml.load(str(self), Loader=loader)

    def get_(self, key: str, default_value: Any = None) -> Any:
        return self.__dict__[key] if key in self else default_value


def _load(js) -> Union[YamlObject, list]:
    if isinstance(js, dict):
        return YamlObject(js)
    elif hasattr(js, '__dict__'):
        return YamlObject(js.__dict__)
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
        parent.append(YamlObject(value))
    elif hasattr(value, '__dict__'):
        parent.append(YamlObject(value.__dict__))
    elif isinstance(value, (list, tuple)):
        parent.append(_load_list(value))
    else:
        parent.append(value)


def _inject_value(parent, key, value):
    if isinstance(value, dict):
        parent.__dict__[str(key)] = YamlObject(value)
    elif hasattr(value, '__dict__'):
        parent.__dict__[str(key)] = YamlObject(value.__dict__)
    elif isinstance(value, (list, tuple)):
        parent.__dict__[str(key)] = _load_list(value)
    else:
        parent.__dict__[str(key)] = value


def load_file(filename, loader=_DEFAULT_LOADER) -> Union[Any, YamlObject]:
    with open(filename) as f:
        return load(f, loader=loader)


def load(fp, loader=_DEFAULT_LOADER) -> Union[Any, YamlObject]:
    return _load(yaml.load(fp, Loader=loader))


def loads(s, loader=_DEFAULT_LOADER) -> Union[Any, YamlObject]:
    return _load(yaml.load(s, Loader=loader))


def load_obj(obj) -> Union[Any, YamlObject]:
    return _load(obj)


def dumps(obj, **kwargs) -> str:
    return yaml.dump(obj, default_flow_style=False, **kwargs)


def _yaml_obj_representer(dumper, data):
    return dumper.represent_mapping(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        data.items_()
    )


yaml.add_representer(YamlObject, _yaml_obj_representer)
