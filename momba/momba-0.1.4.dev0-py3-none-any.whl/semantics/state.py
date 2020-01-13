# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import dataclasses

from .. import model
from ..kit import dbm


class Value:
    pass


class Valuation:
    variable_valuation: t.Mapping[str, Value]

    parent: t.Optional[Valuation] = None


@dataclasses.dataclass(frozen=True)
class AutomatonState:
    location: model.Location
    valuation: Valuation


@dataclasses.dataclass(frozen=True)
class NetworkState:
    automata_states: t.Mapping[model.Instance, AutomatonState]

    # we represent all the values of all clocks with a single DBM
    # (to capture relations between global and local clocks)
    clock_valuation: dbm.DBM

    global_valuation: Valuation
