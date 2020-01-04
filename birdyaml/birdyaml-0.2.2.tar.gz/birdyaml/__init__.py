import re
from typing import Any, Union

import yaml
import yaml.resolver

_DEFAULT_LOADER = yaml.FullLoader


class YamlObject:
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

    def keys_(self):
        return self.__dict__.keys()

    def items_(self):
        return self.__dict__.items()

    def values_(self):
        return self.__dict__.values()

    def dumps_(self, **kwargs) -> str:
        return dumps(self, **kwargs)

    def to_obj_(self, loader=_DEFAULT_LOADER) -> Union[Any, dict]:
        return yaml.load(str(self), Loader=loader)

    def get_(self, key: str, default_value: Any = None) -> Any:
        return self[key] if key in self else default_value


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


def _load(yml) -> Union[Any, YamlObject]:
    if type(yml) is list:
        return _load_list(yml)
    elif type(yml) is dict:
        return _load_dict(yml)
    return yml


def _load_list(yml) -> list:
    lst = []
    for v in yml:
        _append_value(lst, v)
    return lst


def _load_dict(yml) -> Union[Any, YamlObject]:
    g = YamlObject()
    for key in yml:
        _inject_value(g, key, yml[key])
    return g


def _append_value(parent, value):
    if type(value) is list:
        lst = []
        for v in value:
            _append_value(lst, v)
        parent.append(lst)
    elif type(value) is dict:
        d = YamlObject()
        for k, v in value.items():
            _inject_value(d, k, v)
        parent.append(d)
    else:
        parent.append(value)


def _inject_value(parent, key, value):
    if type(value) is list:
        lst = []
        for v in value:
            _append_value(lst, v)
        parent.__dict__[_sanitize_key(key)] = lst
    elif type(value) is dict:
        d = YamlObject()
        for k, v in value.items():
            _inject_value(d, k, v)
        parent.__dict__[_sanitize_key(key)] = d
    else:
        parent.__dict__[_sanitize_key(key)] = value


def _sanitize_key(key, safe_mode=False) -> str:
    k = str(key)
    if safe_mode:
        if re.match(r'^([0-9])', k):
            k = '_' + k
        k = k.replace(' ', '_').replace('-', '_')
    return k


def _yaml_obj_representer(dumper, data):
    return dumper.represent_mapping(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        data.items_()
    )


yaml.add_representer(YamlObject, _yaml_obj_representer)
