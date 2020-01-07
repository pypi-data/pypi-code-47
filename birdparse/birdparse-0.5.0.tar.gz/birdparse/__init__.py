from typing import Any, Union

import birdjson
import birdyaml
from birdjson import JsonObject
from birdyaml import YamlObject


class ParseException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


def load_file(filename) -> Union[YamlObject, JsonObject, list]:
    if filename.endswith('.yml') or filename.endswith('.yaml'):
        return birdyaml.load_file(filename)
    elif filename.endswith('.json'):
        return birdjson.load_file(filename)
    else:
        raise ParseException('unknown file format')


def write_yaml(obj: Any, filename: str):
    obj = to_yaml(obj)
    with open(filename, 'w') as f:
        f.write(str(obj))


def write_json(obj: Any, filename: str):
    obj = to_json(obj)
    with open(filename, 'w') as f:
        f.write(str(obj))


def load_file_to_json(filename: str) -> Union[JsonObject, list]:
    return to_json(load_file(filename))


def load_file_to_yaml(filename) -> Union[YamlObject, list]:
    return to_yaml(load_file(filename))


def to_yaml(obj: Any) -> Union[YamlObject, list]:
    if isinstance(obj, YamlObject):
        return obj
    if isinstance(obj, JsonObject):
        return YamlObject(**obj.__dict__)
    return birdyaml.load_obj(obj)


def to_json(obj: Any) -> Union[JsonObject, list]:
    if isinstance(obj, JsonObject):
        return obj
    if isinstance(obj, YamlObject):
        return JsonObject(**obj.__dict__)
    return birdjson.load_obj(obj)


def to_dict(obj: Any) -> Union[Any, dict]:
    if isinstance(obj, (JsonObject, YamlObject)):
        return obj.obj_()
    if isinstance(obj, dict):
        return obj
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    raise ValueError('invalid type')
