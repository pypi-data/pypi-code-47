# -*- coding: utf-8 -*-
"""The API for working with units"""


# SIpy
# flake8: noqa
from sipy.units import prefixes
from sipy.units.base_unit import DerivedSIUnit
from sipy.units.defined_units import generate_units_from_quantities

PUBLIC_UNITS = {"Multiplier": prefixes.UnitMultiple}
PUBLIC_PREFIXES = {
    "Prefix": prefixes.PREFIXES,
    "MassPrefix": prefixes.MASS_PREFIXES,
    "NoPrefix": [],
}
