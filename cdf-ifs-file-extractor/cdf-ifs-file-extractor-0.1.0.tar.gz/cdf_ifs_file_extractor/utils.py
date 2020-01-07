from typing import Dict

import yaml


def read_yaml(file_path) -> Dict:
    with open(file_path, "r") as yaml_file:
        return yaml.full_load(yaml_file.read())
