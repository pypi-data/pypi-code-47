"""Library functions for YamlTable."""


from typing import Any, Iterable, List

import yaml
from yamltable.typing import Path, Row


def read(file_path: Path) -> List[Row]:
    """Read data from YAML file.

    :param file_path: YAML file path
    :return: YAML data
    :raise TypeError: if file is not organized as a list
    """

    with open(file_path, "r") as handle:
        rows = yaml.safe_load(handle)

    if isinstance(rows, list):
        return rows
    else:
        raise TypeError("YAML file does not contain a list")


def search(key: str, val: Any, rows: Iterable[Row]) -> List[Row]:
    """Search dictionaries by key and value.

    :param key: search key
    :param val: key comparison value
    :param rows: dictionaries to search
    :return: matching dictionaries
    """

    return [row for row in rows if key in row and row[key] == val]


def sort(key: str, rows: Iterable[Row]) -> List[Row]:
    """Sort dictionaries based on value for supplied key name.

    :param key: search key
    :param rows: dictionaries to sort
    :return: list of sorted dictionaries
    """

    return sorted(rows, key=lambda row: row[key])


def write(file_path: Path, rows: List[Row], sort_keys: bool = False) -> None:
    """Write data to YAML file.

    Additional sorts dictionary keys.

    :param file_path: YAML file path
    :param rows: list of dictionaries to write
    """

    with open(file_path, "w") as handle:
        yaml.dump(rows, handle, sort_keys=sort_keys)
