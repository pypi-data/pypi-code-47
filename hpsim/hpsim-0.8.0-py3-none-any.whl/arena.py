#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:02:19 2019

@author: hogbobson
"""

import numpy as np

def make_arena_inf():
    cells = np.empty(1, dtype = object)
    lims = np.array([[np.inf, -np.inf], [np.inf, -np.inf], [np.inf, -np.inf]])
    return (cells, lims, np.inf)

def make_arena(cell_size, arena_limits):
    if type(arena_limits) == type(np.array(1)):
        arena_dims = np.size(arena_limits)//2
        arena_size = np.empty(arena_dims)
        for i in range(arena_dims):
            arena_size[i] = arena_limits[1 + 2*i] - arena_limits[0 + 2*i]
    else:
        arena_size = 2*arena_limits
    
    num_cells = int(round(arena_size / cell_size))
    if np.size(num_cells) > 1:
        cells = np.empty(num_cells, dtype = object)
    else:
        cells = np.empty((num_cells, num_cells, num_cells), dtype = object)
    
    lims = arena_limits
    print(cells)
    return (cells, lims, cell_size)