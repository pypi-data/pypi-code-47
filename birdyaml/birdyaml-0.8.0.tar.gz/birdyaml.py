from typing import Any, Union

import birdjson
import yaml
import yaml.resolver

__all__ = ['YamlObject']
_DEFAULT_LOADER = yaml.FullLoader


class YamlObject(birdjson.GenericObject):
    def json(self, indent=None, **kwargs) -> str:
        return birdjson.dumps(self, indent=indent, **kwargs)

    def dumps(self, indent=None, **kwargs) -> str:
        return dumps(self, indent=indent, **kwargs)

    def pretty(self, indent=2, separators=(', ', ': '), **kwargs) -> str:
        return dumps(self, indent=indent, separators=separators, **kwargs)

    def minify(self, **kwargs):
        return dumps(self, separators=(',', ':'), **kwargs)

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
    return birdjson._load(yaml.load(fp, Loader=loader))


def loads(s, loader=_DEFAULT_LOADER) -> Union[Any, YamlObject]:
    return birdjson._load(yaml.load(s, Loader=loader))


def load_obj(obj: Any, cls=YamlObject) -> YamlObject:
    return birdjson._load(obj, cls=cls)


def dumps(obj: Any, **kwargs) -> str:
    return yaml.dump(obj, default_flow_style=False, **kwargs)


def makes(**kwargs) -> str:
    """Create a yaml string from arguments"""
    return dumps(birdjson._load(kwargs, cls=dict))


def make(cls=YamlObject, **kwargs) -> YamlObject:
    """Create a yaml object from arguments"""
    return birdjson._load(kwargs, cls=cls)


def make_obj(cls, **kwargs) -> Any:
    return birdjson._load(kwargs, cls=cls)


def make_dict(**kwargs) -> dict:
    return birdjson._load(kwargs, cls=dict)


def _load_dict(d, cls=YamlObject) -> Union[YamlObject, Any]:
    obj = cls()
    for key in d:
        obj[str(key)] = birdjson._load(d[key], cls=cls)
    return obj


def _yaml_obj_representer(dumper, data):
    return dumper.represent_mapping(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        data._items_
    )


yaml.add_representer(YamlObject, _yaml_obj_representer)

if __name__ == '__main__':
    print(YamlObject(x=1, y=2, z=3).json())
