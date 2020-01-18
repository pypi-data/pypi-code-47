# -*- coding: utf-8 -*-
"""Function for auto-generating all physical units from sipy config

`sipy.config.sipy.toml` defines all units which can be retrieved
using `sipy.config.quantity_info`. This module provides a method to
extract the units and create corresponding unit objects.
"""
# Standard Library
from typing import TYPE_CHECKING, Dict, Type

# SIpy
from sipy.config import quantity_info

if TYPE_CHECKING:
    from sipy.quantities.base_quantity import Quantity  # noqa


def generate_units_from_quantities(
    all_quantities: Dict[str, Type["Quantity"]],
) -> Dict[str, "Quantity"]:
    """Generate a dictionary mapping unit names to their corresponding object"""
    my_units = {}
    for quantity in quantity_info():
        for unit_name in quantity.unit_names:
            new_quantity = all_quantities[quantity.name]()
            new_quantity.value = 1
            my_units[unit_name] = new_quantity

        base_unit = new_quantity
        for extra_unit_name in quantity.extra_units:
            new_quantity = all_quantities[quantity.name]()
            new_quantity.value = 1 / getattr(base_unit, extra_unit_name)
            my_units[extra_unit_name] = new_quantity
    return my_units
