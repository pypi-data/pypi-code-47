# -*- coding: utf-8 -*-
"""Function for auto-generating all physical constants from sipy config

`sipy.config.sipy.toml` defines all physical constants which can be retrieved
using `sipy.config.constants`. This module provides a method to
extract the constants and create the constants.
"""
# Standard Library
from typing import TYPE_CHECKING, Dict

# SIpy
from sipy.config import constants
from sipy.definitions import unit_counter_from_string
from sipy.quantities.base_quantity import quantity_factory

if TYPE_CHECKING:
    from sipy.quantities.base_quantity import Quantity  # noqa


def generate_constants() -> Dict[str, "Quantity"]:
    """Create physical quantities representing the defined constants"""
    constant_dict = {}
    for constant_name, [value, unit_string] in constants().items():
        quantity = quantity_factory(unit_counter_from_string(unit_string))()
        quantity.value = float(value)
        constant_dict[constant_name] = quantity
    return constant_dict
