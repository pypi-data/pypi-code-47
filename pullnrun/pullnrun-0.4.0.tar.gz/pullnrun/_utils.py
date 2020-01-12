import json
from time import time

try:
    import importlib.resources as resources
except ImportError: # pragma: no cover
    import importlib_resources as resources

from jsonschema import validate

def as_list(a):
    if isinstance(a, list):
        return a
    if a is None:
        return []
    return [a]

def create_meta(start, end, **kwargs):
    try:
        json.dumps(kwargs)
    except:
        raise ValueError('kwargs should be JSON serializable')

    return {
        'start': start,
        'end': end,
        **kwargs
    }

def filter_dict(dict_, keys):
    return {k: v for k, v in dict_.items() if k in keys}

def get_log_entry(type_, status, start=None, end=None, errors=None, **data):
    try:
        json.dumps(data)
    except:
        raise ValueError('data should be JSON serializable')

    entry = {
        'type': type_,
        'status': status,
        'data': data,
        'meta': create_meta(start, end)
    }

    if errors:
        entry['errors'] = errors

    validate_dict(entry, 'log_entry')
    return entry

def prefix_object(prefix, object_name, delimiter='/'):
    name_as_list = object_name.split(delimiter)
    folder = delimiter.join(name_as_list[:-1])
    return f'{folder}{folder and delimiter}{prefix}-{name_as_list[-1]}'

def timestamp():
    return int(time() * 1000)

def validate_dict(input_dict, schema_name):
    schema = json.loads(resources.read_text('pullnrun.schemas', f'{schema_name}.json'))
    validate(instance=input_dict, schema=schema)

def void_fn(*_args, **_kwargs):
    return None