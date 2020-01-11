import inspect
from types import MappingProxyType
from typing import Any, Union

import yaml
import yaml.resolver

__all__ = ['YamlObject']
_DEFAULT_LOADER = yaml.FullLoader


def _attr_is_function(cls, attr):
    return hasattr(cls, attr) and inspect.isfunction(getattr(cls, attr))


class YamlObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = _load(v)

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

    def json(self, indent=None, **kwargs) -> str:
        import birdjson
        return birdjson.dumps(self, indent=indent, **kwargs)

    def dumps(self, indent=None, **kwargs) -> str:
        return dumps(self, indent=indent, **kwargs)

    def pretty(self, indent=2, separators=(', ', ': '), **kwargs) -> str:
        return dumps(self, indent=indent, separators=separators, **kwargs)

    def minify(self, **kwargs):
        return dumps(self, separators=(',', ':'), **kwargs)

    def convert_to(self, cls) -> Any:
        return _load(self, cls=cls)

    def obj(self, cls=dict) -> Union[Any, dict]:
        return self.convert_to(cls)

    def dict(self) -> Union[Any, dict]:
        return self.convert_to(dict)

    def get(self, key: str, default=None) -> Any:
        return self[key] if key in self else default

    def yaml(self, **kwargs) -> str:
        return dumps(self, **kwargs)

    def write_json(self, filename: str, **kwargs):
        with open(filename, 'w') as f:
            f.write(self.json(**kwargs))

    def write_yaml(self, filename: str, **kwargs):
        with open(filename, 'w') as f:
            f.write(self.yaml(**kwargs))


def load_file(filename, loader=_DEFAULT_LOADER) -> Union[Any, YamlObject]:
    with open(filename) as f:
        return load(f, loader=loader)


def load(fp, loader=_DEFAULT_LOADER) -> Union[Any, YamlObject]:
    return _load(yaml.load(fp, Loader=loader))


def loads(s, loader=_DEFAULT_LOADER) -> Union[Any, YamlObject]:
    return _load(yaml.load(s, Loader=loader))


def load_obj(obj: Any, cls=YamlObject) -> YamlObject:
    return _load(obj, cls=cls)


def dumps(obj: Any, **kwargs) -> str:
    return yaml.dump(obj, default_flow_style=False, **kwargs)


def makes(**kwargs) -> str:
    """Create a yaml string from arguments"""
    return dumps(_load(kwargs, cls=dict))


def make(cls=YamlObject, **kwargs) -> YamlObject:
    """Create a yaml object from arguments"""
    return _load(kwargs, cls=cls)


def make_obj(cls, **kwargs) -> Any:
    return _load(kwargs, cls=cls)


def make_dict(**kwargs) -> dict:
    return _load(kwargs, cls=dict)


def _load(js, cls: Any = YamlObject) -> Union[YamlObject, Any]:
    if isinstance(js, (list, tuple)):
        return [_load(v, cls=cls) for v in js]
    elif isinstance(js, MappingProxyType):
        return _load_dict(js.copy(), cls=cls)
    elif isinstance(js, dict):
        return _load_dict(js, cls=cls)
    elif hasattr(js, '__dict__'):
        return _load_dict(js.__dict__, cls=cls)
    return js


def _load_dict(d, cls=YamlObject) -> Union[YamlObject, Any]:
    obj = cls()
    for key in d:
        obj[str(key)] = _load(d[key], cls=cls)
    return obj


def _yaml_obj_representer(dumper, data):
    return dumper.represent_mapping(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        data.__dict__
    )


yaml.add_representer(YamlObject, _yaml_obj_representer)

if __name__ == '__main__':
    print(YamlObject(x=1, y=2, z=3).json())
