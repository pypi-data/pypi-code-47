"""Support for loading/getting configuration dictionaries.
"""

import toml


class Config(dict):
    """Dict subclass with a root-path attribute.
    """

    def __init__(self, root_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._root_path = root_path

    @property
    def root_path(self):
        return self._root_path


def deserialize_config(config_string, root_path):
    config = toml.loads(config_string)
    return Config(root_path, config.get('godkjenn', {}))


def load_config(path):
    return deserialize_config(
        path.read_text(encoding='utf-8'),
        path.parent)


def serialize_config(config):
    return toml.dumps({'godkjenn': dict(config)})


def save_config(config, path):
    config_string = serialize_config(config)
    path.write_text(config_string, encoding='utf-8')
