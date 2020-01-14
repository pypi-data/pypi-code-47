import json
from typing import Dict, List
import os


def _load_json(path: str) -> Dict:
    with open(path, "r") as f:
        return json.load(f)


def _load_data(file_name: str) -> Dict:
    pwd = os.path.dirname(os.path.abspath(__file__))
    return _load_json("{pwd}/../data/{file_name}.json".format(
        pwd=pwd,
        file_name=file_name
    ))


def load_columns() -> List:
    return _load_data("columns")


def load_urls() -> Dict:
    return _load_data("urls")


def load_paths() -> Dict:
    return _load_data("paths")
