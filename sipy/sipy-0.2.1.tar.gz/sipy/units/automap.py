# -*- coding: utf-8 -*-
# Standard Library
from collections import defaultdict
from typing import Counter, DefaultDict, List, Tuple, Type, Union

# SIpy
from sipy.config import quantities
from sipy.definitions import unit_reference, unit_string
from sipy.units.prefixes import PUBLIC_PREFIXES
from sipy.units.public import UNIT_TYPES
from sipy.units.si import DerivedSIUnit, SIBaseUnit

# A mapping from SI measures to supported prefixes
Unit = Union[SIBaseUnit, DerivedSIUnit]
UNIT_MAP: DefaultDict[str, List[Tuple[str, Type[Unit]]]] = defaultdict(list)


def add_unit_mapping(
    quantity_units: Counter, unit_class: Type[SIBaseUnit] = SIBaseUnit, name: str = None
):
    name = name or unit_reference(quantity_units)
    UNIT_MAP[unit_string(quantity_units)] += [(name, unit_class)]


def add_unit_mappings(
    quantity_units: Counter, unit_classes: List[Type[SIBaseUnit]], name: str = None,
):
    for unit_class in unit_classes:
        add_unit_mapping(quantity_units, unit_class, name)


def populate_map():
    UNIT_MAP.clear()
    for quantity in quantities():
        unit_count = quantity.unit_counter
        prefixes = PUBLIC_PREFIXES[quantity.prefixes]

        for unit_name in quantity.unit_names:
            add_unit_mapping(unit_count, SIBaseUnit, unit_name)
            add_unit_mappings(unit_count, prefixes, unit_name)

        for extra_unit_name, unit_info in quantity.extra_units.items():
            unit_base_type, *args = unit_info
            unit_type = UNIT_TYPES[unit_base_type].factory(extra_unit_name, *args)
            add_unit_mapping(unit_count, unit_type, extra_unit_name)


populate_map()
