# -*- coding: utf-8 -*-
# Standard Library
import os
import pathlib
from enum import Enum
from typing import Dict

# Third Party
import toml

# SIpy
from sipy.definitions import unit_counter_from_string

CONFIG_FILE = pathlib.Path(__file__).parent / "sipy.toml"
KEYS = Enum(
    "Keys",
    {
        "prefixes": "Prefixes",
        "quantity": "Quantity",
        "sipy": "Sipy",
        "constants": "Constants",
    },
)
CONFIG_KEYS = Enum(
    "QuantityKey",
    {"si_units": "si_units", "unit_names": "unit_names", "prefix": "prefix"},
)
CONFIG_KEY = "config"
CUSTOM_FILE_ENV_VAR = "SIPY_CFG_FILE"


class SipyConfigError(Exception):
    pass


class Quantity:
    def __init__(self, name, config, extra_units):
        self.name = name
        self.extra_units = extra_units

        self.unit_names = config.get(CONFIG_KEYS.unit_names.value, [])
        self.prefixes = config.get(CONFIG_KEYS.prefix.value, "Prefix")

        if CONFIG_KEYS.si_units.value not in config:
            raise SipyConfigError(
                "Quantities must define 'si_units' in [Quantity.*.config]"
            )
        self.si_units = config[CONFIG_KEYS.si_units.value]

        if self.prefixes and not self.unit_names:
            raise SipyConfigError(
                f"Must specify 'unit_names' for {self.name} if prefix=true"
            )

    @property
    def unit_counter(self):
        return unit_counter_from_string(self.si_units)

    @classmethod
    def from_toml_dict(cls, name, toml_dict):
        config = toml_dict.pop(CONFIG_KEY)
        return cls(name, config, toml_dict)


def _load_config(file_name=CONFIG_FILE):
    cfg = toml.load(file_name)
    validate_config(cfg)
    return cfg


def validate_config(cfg: Dict):
    if KEYS.sipy.value not in cfg:
        raise SipyConfigError(f"[{KEYS.sipy.value}] must be present in config file")

    version = cfg[KEYS.sipy.value].get("version")
    if version != "1.0.0":
        raise SipyConfigError(f"Unsupported config file version: {version}")

    all_keys = [k.value for k in KEYS]
    for key in cfg.keys():
        if key not in all_keys:
            raise SipyConfigError(f"[{key}] is not a valid section name")


def prefixes():
    app_config = _load_config().get(KEYS.prefixes.value, {})

    env_file = os.getenv(CUSTOM_FILE_ENV_VAR)
    if env_file:
        env_config = _load_config(env_file).get(KEYS.prefixes.value, {})
        app_config.update(env_config)

    return app_config


def _extract_quantities(quantities_dict):
    return [
        Quantity.from_toml_dict(name, toml_dict)
        for name, toml_dict in quantities_dict.items()
    ]


def quantities():
    app_config = _load_config()[KEYS.quantity.value]
    my_quantities = _extract_quantities(app_config)

    env_file = os.getenv(CUSTOM_FILE_ENV_VAR)
    if env_file:
        env_config = _load_config(env_file).get(KEYS.quantity.value, {})
        my_quantities += _extract_quantities(env_config)

    return my_quantities


def constants():
    app_config = _load_config()[KEYS.constants.value]

    env_file = os.getenv(CUSTOM_FILE_ENV_VAR)
    if env_file:
        env_config = _load_config(env_file).get(KEYS.constants.value, {})
        app_config.update(env_config)

    return app_config
