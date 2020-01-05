import os

from fuga.config.experiment import get_experiment_config
from fuga.config.environment import get_environment_config


def get_config(name):
    env_name = 'FUGA_' + name.upper()
    # Prioritize env var over ~/.fuga/config.yml file
    # (It allows users to use multiple configurations)
    return os.getenv(
        env_name,
        get_experiment_config(name) or get_environment_config(name))
