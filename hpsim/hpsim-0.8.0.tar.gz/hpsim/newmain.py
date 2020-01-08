#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:50:32 2019

@author: hogbobson
"""

import numpy as np
import fnmatch as fn
import time

from hpsim import acceleration
from . import force
from . import miscfuncs
from . import solver
from . import integrator
from . import ensgen
from . import timestep
from . import timegen
from . import visual
from . import energy
from . import arena

class hpsim:
    def __init__(cls, preload = True):
        cls.functions     = {}
        cls.output_str    = ' output key'
        cls.order_str     = ' order'
        cls.loop_str      = ' loop status'
        
        
        cls.data             = {}
        cls._iteration_steps = 0
        
        
        if preload:
            cls.preload_solar_system()
        # Various toggles and shit
        cls.verbose = True
        
    
    def _loop(cls):
        while cls._current_time < cls.time_end:
            cls._step()
    
    def _loop_functions(cls, num_funcs, offset):
        for i in (range(num_funcs) + offset):
            key_out = cls.output_keys[i]
            cls.data[key_out] = cls.funcs[i]
    
    def _step(cls):
        cls._loop_functions(cls.funcs_in_loop, cls.funcs_b4_loop)
    
    def _preamble(cls):
        cls._loop_functions(cls.funcs_b4_loop, 0)
    
    def _postprocessing(cls):
        cls._loop_functions(cls.funcs_in_end, cls.funcs_b4_end)

    
    def _update(cls, func, params):
        def do(data):
            return func(data, *params)
        if func:
            return do
        return
    
    def preload_solar_system(cls):
        """
        Method for preloading the solar system. Includes the following:
            TODO: write what it includes.
        """
        cls.set_time(0, timestep.constant_dt(2e6), timegen.time_years(100))
        cls.set_function(arena.make_arena_inf, (), 'arena', 'cells and limits',
                         1, pre_loop = True)
        cls.set_function(ensgen.solar_system, (), 'ensemble generator',
                         'ensemble', 2, pre_loop = True)
        cls.set_function(integrator.n_body_nice, (), 'integrator',
                         'integrator ouput', 3)
        cls.set_function(force.gravity, (), 'force 1', 'force 1',
                         4)
        cls.set_function(acceleration.classic_acceleration, (), 'acceleration',
                         'acceleration', 5)
        cls.set_function(solver.sym1, (cls.time_step,), 'solver', 'ensemble',
                         6)
        cls.set_function(visual.simple_2d_anim, (), 'plotter', 'garbage', 7,
                         post_loop = True)
        if cls.verbose:
            print('The Solar System has been preloaded. Please run the \
              appropriate preload-function to load something else instead.')
    
    def run(cls):
        cls._preamble()
        cls._loop()
        cls._postprocessing()
        return cls.data
    
    
    def set_function(cls, func, params, name, output_key, order, 
                     pre_loop = False, post_loop = False):
        if pre_loop and post_loop:
            raise('wtf')
        
        cls.functions[name]                  = cls._update(cls, func, params)
        cls.functions[name + cls.output_str] = output_key
        cls.functions[name + cls.order_str]  = order
        cls.functions[name + cls.loop_str]   = -pre_loop + post_loop
        
        
    def set_time(cls, time_start, time_step, time_end):
        cls.time_start = time_start
        cls.time_step  = time_step
        cls.time_end   = time_end
        cls._time_now  = time_start
    
    
    def sort_functions(cls):
        funcs       = [cls.functions[k] for k in cls.functions.keys() \
                 if cls.output_str or cls.order_str or cls.loop_str not in k]
        output_keys = [cls.functions[k] for k in cls.functions.keys() \
                       if cls.output_str in k]
        loop_status = [cls.functions[k] for k in cls.functions.keys() \
                       if cls.loop_str in k]
        order       = [cls.functions[k] for k in cls.functions.keys() \
                       if cls.order_str in k]
        
        indx = np.array(order).argsort()
        cls.funcs = funcs[indx]
        cls.output_keys = output_keys[indx]
        cls.loop = np.array(loop_status[indx])
        cls.funcs_b4_loop = sum(cls.loop == -1)
        cls.funcs_in_loop = sum(cls.loop == 0)
        cls.funcs_b4_end  = cls.funcs_in_loop + cls.funcs_b4_loop
        cls.funcs_in_end  = sum(cls.loop == 1)
    
    
# =============================================================================
#     def set_num_functions(cls, num):
#         cls.functions         = np.resize(cls.functions, num)
#         cls.func_designations = np.resize(cls.func_designations, num)
#         cls.output_keys       = np.resize(cls.outer_keys, num)
#         
#         if cls.verbose:
#             print('Your functions now are as follows:')
#             print('functions:')
#             print(cls.functions)
#             print()
#             print('designations:')
#             print(cls.func_designations)
#             print()
#             print("Please be aware that there are duplicates if the array is \
#                   longer than before, and deletions if it is shorter.")
# =============================================================================
            
    
    
    