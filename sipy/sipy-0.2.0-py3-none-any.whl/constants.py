# -*- coding: utf-8 -*-
# SIpy
from sipy.config import constants
from sipy.definitions import unit_counter_from_string
from sipy.quantities import quantity_factory


def generate_constants():
    constant_dict = {}
    for constant_name, [value, unit_string] in constants().items():
        quantity = quantity_factory(unit_counter_from_string(unit_string))()
        quantity.value = float(value)
        constant_dict[constant_name] = quantity
    return constant_dict


locals().update(generate_constants())
