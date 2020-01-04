from typing import Any

import birdjson
import birdyaml
from birdjson import JsonObject
from birdyaml import YamlObject


class ParseException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


def load_file(filename) -> Any:
    if filename.endswith('.yml') or filename.endswith('.yaml'):
        return birdyaml.load_file(filename)
    elif filename.endswith('.json'):
        return birdjson.load_file(filename)
    else:
        raise ParseException('unknown file format')


def write_yaml(obj: Any, filename: str) -> None:
    obj = to_yaml(obj)
    with open(filename, 'w') as f:
        f.write(str(obj))


def write_json(obj: Any, filename: str) -> None:
    obj = to_json(obj)
    with open(filename, 'w') as f:
        f.write(str(obj))


def load_file_to_json(filename: str) -> Any:
    return to_json(load_file(filename))


def load_file_to_yaml(filename) -> Any:
    return to_yaml(load_file(filename))


def to_yaml(obj: Any) -> Any:
    if type(obj) is YamlObject:
        return obj
    if type(obj) is JsonObject:
        return YamlObject(**obj.__dict__)
    return birdyaml.load_obj(obj)


def to_json(obj: Any) -> Any:
    if type(obj) is JsonObject:
        return obj
    if type(obj) is YamlObject:
        return JsonObject(**obj.__dict__)
    return birdjson.load_obj(obj)


def to_dict(obj: Any) -> Any:
    if type(obj) is JsonObject or type(obj) is YamlObject:
        return obj.to_obj_()
    if type(obj) is dict:
        return obj
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    raise ValueError('invalid type')
