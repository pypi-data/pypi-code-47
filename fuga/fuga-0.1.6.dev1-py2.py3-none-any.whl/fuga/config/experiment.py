import os
import copy

import yaml

from fuga.utils import find_experiment_root_dir
from fuga.exceptions import MissingExperimentContextError

DEFAULT_CONFIG = {
}

_config = copy.deepcopy(DEFAULT_CONFIG)

_experiment_root_dir = find_experiment_root_dir()
if _experiment_root_dir:
    _config_path = os.path.join(_experiment_root_dir, 'fuga.yml')

    if os.path.exists(_config_path):
        _config_path = os.path.join(_experiment_root_dir, 'fuga.yml')
        try:
            with open(_config_path) as f:
                _config = yaml.load(f)
        except ValueError:
            _config = {}


def get_experiment_config(name):
    return _config.get(name, None)


def write_experiment_config(key, value):
    _experiment_root_dir = find_experiment_root_dir()
    if _experiment_root_dir:
        raise MissingExperimentContextError()

    _config_path = os.path.join(_experiment_root_dir, 'fuga.yml')

    if _config_path is None:
        raise MissingExperimentContextError
    _config[key] = value

    with open(_config_path, 'w') as f:
        f.write(yaml.dump(_config, default_flow_style=False))
