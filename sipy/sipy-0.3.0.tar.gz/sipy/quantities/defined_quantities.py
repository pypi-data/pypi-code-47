# -*- coding: utf-8 -*-
"""Function for auto-generating all physical quantities from sipy config

`sipy.config.sipy.toml` defines all quantities which can be retrieved
using `sipy.config.quantity_info`. This module provides a method to
extract the quantities and their create corresponding types.
"""
# Standard Library
from typing import TYPE_CHECKING, Dict, Type

# SIpy
from sipy.config import quantity_info
from sipy.quantities.base_quantity import quantity_factory

if TYPE_CHECKING:
    from sipy.quantities.base_quantity import Quantity  # noqa


def defined_quantities() -> Dict[str, Type["Quantity"]]:
    """Generate a dictionary mapping quantity names to their object type"""
    my_quantities = {}
    for quantity in quantity_info():
        my_quantities[quantity.name] = quantity_factory(quantity.unit_counter)
    return my_quantities
