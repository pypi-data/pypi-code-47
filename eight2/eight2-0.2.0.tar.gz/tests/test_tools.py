#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eight2.tools import BZBaseTools


def test_combinations():
    li = [1, 6, 9, 4, 1]
    tools = BZBaseTools()
    assert tools.Combinations(li, 2)
