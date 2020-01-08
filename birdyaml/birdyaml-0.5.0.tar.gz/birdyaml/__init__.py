from typing import Any, Union

import yaml
import yaml.resolver


__all__ = ['YamlObject']
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
        return self[key] if key in self else default_value

    def to_json_object_(self) -> 'JsonObject':
        import birdjson
        return birdjson.load_obj(self.obj_())

    def to_json_(self, **kwargs) -> str:
        return self.to_json_object_().dumps_(**kwargs)

    def write_yaml_(self, filename: str, **kwargs):
        with open(filename, 'w') as f:
            f.write(self.dumps_(**kwargs))

    def write_json_(self, filename: str, **kwargs):
        with open(filename, 'w') as f:
            f.write(self.to_json_(**kwargs))

    @staticmethod
    def loads(s: str) -> 'YamlObject':
        return loads(s)

    @staticmethod
    def load_file(filename: str) -> 'YamlObject':
        return load_file(filename)

    @staticmethod
    def load(fp) -> 'YamlObject':
        return load(fp)

    @staticmethod
    def load_dict(obj: dict) -> 'YamlObject':
        return _load(obj)

    @staticmethod
    def load_obj(obj: dict) -> 'YamlObject':
        return _load(obj)

    @staticmethod
    def makes(**kwargs) -> str:
        return dumps(YamlObject(**kwargs))


def _load(js) -> Union[YamlObject, list]:
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


def _load_dict(js) -> YamlObject:
    g = YamlObject()
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
        d = YamlObject()
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
        d = YamlObject()
        for k, v in value.items():
            _inject_value(d, k, v)
        parent.__dict__[str(key)] = d
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


def makes(**kwargs) -> str:
    """Create a yaml string from arguments"""
    return dumps(YamlObject(**kwargs))


def make(**kwargs) -> YamlObject:
    """Create a yaml object from arguments"""
    return YamlObject(**kwargs)


def _yaml_obj_representer(dumper, data):
    return dumper.represent_mapping(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        data.items_()
    )


yaml.add_representer(YamlObject, _yaml_obj_representer)
