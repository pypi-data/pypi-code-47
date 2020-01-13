# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

"""
Implements an evaluation engine for automata networks.

We support an abstract evaluation of clocks with DBMs. This allows building
a region graph using the evaluation engine where everything expect clocks
are evaluated concretely. The usage of DBMs imposes various restrictions
on the model.
"""

from __future__ import annotations
