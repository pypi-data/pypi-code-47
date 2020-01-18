# -*- coding: utf-8 -*-
"""Populate the UNIT_MAP dictionary used when generating new quantities.

 The `sipy.quantities.quantity.quantity_factory` looks up new quantities in
 the UNIT_MAP to determine what units they should have.
"""
# Standard Library
from collections import defaultdict
from typing import Counter, DefaultDict, List, Tuple, Type

# SIpy
from sipy.config import quantity_info
from sipy.definitions import unit_reference, unit_string
from sipy.units import PUBLIC_PREFIXES, PUBLIC_UNITS, DerivedSIUnit

# A mapping from SI measures to supported prefixes
UNIT_MAP: DefaultDict[str, List[Tuple[str, Type[DerivedSIUnit]]]] = defaultdict(list)


def add_unit_mapping(
    quantity_units: Counter,
    unit_class: Type[DerivedSIUnit] = DerivedSIUnit,
    name: str = None,
):
    """Register a new type of unit in the UNIT_MAP

    Args:
        quantity_units: The SI Units associated with the unit
        unit_class: The `sipy.units.si.SIBaseUnit` to register
        name: The name of fundamental unit
    """
    name = name or unit_reference(quantity_units)
    UNIT_MAP[unit_string(quantity_units)] += [(name, unit_class)]


def add_unit_mappings(
    quantity_units: Counter, unit_classes: List[Type[DerivedSIUnit]], name: str = None,
):
    """Register multiple units for a single quantity in the UNIT_MAP

    Args:
        quantity_units: The SI Units associated with the unit
        unit_classes: A list of `sipy.units.si.SIBaseUnit` to register
        name: The name of fundamental unit
    """
    for unit_class in unit_classes:
        add_unit_mapping(quantity_units, unit_class, name)


def populate_map():
    """Populate UNIT_MAP with new units by reading from the packates config

    The function can be called multiple times in order to re-populate the
    UNIT_MAP. This will cause us to re-read the packages config, which
    might have changed.
    """
    UNIT_MAP.clear()
    for quantity in quantity_info():
        unit_count = quantity.unit_counter

        # Some units have custom prefixies defined. A custom prefix is specified
        # by the quantity as a string that we lookup in the public dictionary
        # of prefixes.
        prefixes = PUBLIC_PREFIXES[quantity.prefixes]

        # Add the basic unit names (ones that refer to the quantities fundamental
        # unit) and all the prefixes associated with quantity, e.g. Kilo, Mega, ...
        for unit_name in quantity.unit_names:
            add_unit_mapping(unit_count, DerivedSIUnit, unit_name)
            add_unit_mappings(unit_count, prefixes, unit_name)

        # Add in all the custom units, the units type is specified as a string that
        # is looked up in the dictionary of public unit types.
        for extra_unit_name, unit_info in quantity.extra_units.items():
            unit_base_type, *args = unit_info
            unit_type = PUBLIC_UNITS[unit_base_type].factory(extra_unit_name, *args)
            add_unit_mapping(unit_count, unit_type, extra_unit_name)


populate_map()
