import json
import os

from jsonschema import Draft7Validator, validators, exceptions

import yaml

with open(os.path.join(os.path.dirname(__file__), "schema.yaml"), "r") as f:
    schema = yaml.load(f, Loader=yaml.FullLoader)


def get(name):
    return schema['definitions'][name]


class MyDraft7Validator(Draft7Validator):
    def validate(self, *args, **kwargs):
        errors = self.iter_errors(*args, **kwargs)
        error = exceptions.best_match(errors)
        if error:
            message = f'Failed validating following key(s) {list(error.path)}: {error.message}'
            raise ValueError(message)


def extend_with_default(validator_class):
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for property, subschema in properties.items():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

        for error in validate_properties(validator, properties, instance, schema):
            yield error

    return validators.extend(
        validator_class, {"properties": set_defaults},
    )


DefaultValidatingDraft7Validator = extend_with_default(
    MyDraft7Validator)


def _init_schema(direction, definition):
    s = dict(get(definition))
    s['$schema'] = schema['$schema']
    s['definitions'] = schema['definitions']
    if direction == 'in':
        s = DefaultValidatingDraft7Validator(s)
    else:
        s = MyDraft7Validator(s)

    def validate(data):
        try:
            s.validate(data)
            return data
        except Exception:
            print("---")
            print(json.dumps(data, indent=2))
            print("---")
            raise
    return validate


validators = {
    'models': {
        'addon': _init_schema('out', 'Addon'),
        'item': {
            'directory': _init_schema('out', 'DirectoryItem'),
            'movie': _init_schema('out', 'MovieItem'),
            'series': _init_schema('out', 'SeriesItem'),
            'episode': _init_schema('out', 'EpisodeItem'),
            'channel': _init_schema('out', 'ChannelItem'),
            'iptv': _init_schema('out', 'IptvItem'),
            'basic': _init_schema('out', 'Item'),
        },
        'source': _init_schema('out', 'Source'),
        'subtitle': _init_schema('out', 'Subtitle'),
        'apiError': _init_schema('out', 'ApiError'),
    },
    'actions': {
        'addon': {
            'addonType': None,
            'request': _init_schema('in', 'ApiAddonRequest'),
            'response': _init_schema('out', 'ApiAddonResponse'),
        },
        'repository': {
            'addonType': 'repository',
            'request': _init_schema('in', 'ApiRepositoryRequest'),
            'response': _init_schema('out', 'ApiRepositoryResponse'),
        },
        'directory': {
            'addonType': 'worker',
            'request': _init_schema('in', 'ApiDirectoryRequest'),
            'response': _init_schema('out', 'ApiDirectoryResponse'),
        },
        'item': {
            'addonType': 'worker',
            'request': _init_schema('in', 'ApiItemRequest'),
            'response': _init_schema('out', 'ApiItemResponse'),
        },
        'source': {
            'addonType': 'worker',
            'request': _init_schema('in', 'ApiSourceRequest'),
            'response': _init_schema('out', 'ApiSourceResponse'),
        },
        'subtitle': {
            'addonType': 'worker',
            'request': _init_schema('in', 'ApiSubtitleRequest'),
            'response': _init_schema('out', 'ApiSubtitleResponse'),
        },
        'resolve': {
            'addonType': 'worker',
            'request': _init_schema('in', 'ApiResolveRequest'),
            'response': _init_schema('out', 'ApiResolveResponse'),
        },
    },
    'task': {
        'task': _init_schema('out', 'ApiTask'),
        'result': _init_schema('in', 'ApiTaskResult'),
    },


}

for key in ['resolveVideo', 'resolveSource', 'resolveSubtitle']:
    validators['actions'][key] = validators['actions']['resolve']
