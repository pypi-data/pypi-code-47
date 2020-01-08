#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:50:32 2019

@author: hogbobson
"""
import numpy as np
import fnmatch as fn
import time

from . import acceleration
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
from . import boundaries

class hpsim:
    def __init__(cls, preload = True):
        # TODO: Documentation
        cls.functions     = {}
        cls.input_str     = ' input keys'
        cls.ens_str       = ' ensemble keys'
        cls.output_str    = ' output key'
        cls.order_str     = ' order'
        cls.loop_str      = ' loop status'
        cls.prio_str      = ' priority'
        
        cls.definite_ensemble_keys = ['affectee position',
                                      'affectee position data',
                                      'affector position',
                                      'affectee velocity',
                                      'affectee mass',
                                      'affector mass',
                                      'velocity',
                                      'energy',
                                      'energy data',
                                      'number of objects',
                                      'label',
                                      'affect status',
                                      'remaining',
                                      'charge',
                                      'sigma',
                                      'epsilon']
        
        cls.data             = {}
        cls.data['steps']    = 0
        
        cls.verbose = True
        
        if preload:
            cls.preload_solar_system()
        # TODO: Various toggles and shit
        
        
    
    def _loop(cls):
        st = time.time()
        while cls._time_now < cls.time_end and cls.data['steps'] < cls.step_max:
            cls._step()
            cls._time_now += cls.time_step/cls.order
            cls.data['steps'] += 1
            print("FUCK YEAH!")
            print(str(cls.data['steps']) + ' / ' + str(cls.step_max))
        en = time.time()
        cls.data['loop time'] = en - st
    
    def _loop_functions(cls, num_funcs, offset):
        for i in range(num_funcs):
            i += offset
            if not cls.data['steps']%cls.priority[i]:
                key_out = cls.output_keys[i]
                dynamic_input = [cls.data[k] for k in cls.input_keys[i]]
                for k in cls.ensemble_keys[i]:
                    dynamic_input.append(cls.data['ensemble'][k])
                cls.data[key_out] = cls.funcs[i](*dynamic_input)
                cls.data['Previous Key'] = key_out
    
    def _step(cls):
        cls._loop_functions(cls.funcs_in_loop, cls.funcs_b4_loop)
    
    def _preamble(cls):
        cls._loop_functions(cls.funcs_b4_loop, 0)
    
    def _postprocessing(cls):
        cls._loop_functions(cls.funcs_in_end, cls.funcs_b4_end)
    
    
    def _update(cls, func, params):
        def do(*data):
            return func(*data, *params)
        if func:
            return do
        return
    
    def clear_func_dict(cls):
        cls.functions = {}
        cls.funcs = None
        cls.output_keys = None
        cls.input_keys = None
        cls.ensemble_keys = None
        cls.loop = None
        cls.funcs_b4_loop = None
        cls.funcs_in_loop = None
        cls.funcs_b4_end  = None
        cls.funcs_in_end  = None
        
    
    
    def preload_solar_system(cls):
        """
        Method for preloading the solar system. Includes the following:
            TODO: write what it includes.
        """
        # func, name, input_keys, static_params, output_key, 
        # order, pre_loop = False, post_loop = False):
        cls.set_time(0, timestep.constant_dt(2e6), timegen.time_years(1000))
        cls.set_function(arena.make_arena_inf, 'arena generator', 
                         [], (), 
                         'cells and limits', 1, 
                         pre_loop = True)
        cls.set_function(ensgen.solar_system, 'ensemble generator', 
                         ['cells and limits'], (), 
                         'ensemble', 2, 
                         pre_loop = True)
        cls.set_function(solver.sym_solver_init, 'pre-solver',
                         [], (1,),
                         'solver object', 3,
                         pre_loop = True)
        cls.set_function(integrator.n_body_nice, 'integrator', 
                         ['ensemble'], (), 
                         'ensemble', 4)
        cls.set_function(force.gravity, 'force 1', 
                         ['affector position', 'affectee position',
                          'affector mass', 'affectee mass'], (), 
                         'force 1', 5)
        cls.set_function(acceleration.single_force_acceleration, 
                         'acceleration',
                         ['ensemble', 'force 1'], (), 
                         'acceleration', 6)
        cls.set_function(solver.sym1, 'solver', 
                         ['ensemble', 'acceleration'], (cls.time_step,), 
                         'ensemble', 7)
        cls.set_function(cls.save_data, 'saver', 
                         ['ensemble'], (),
                         'ensemble', 8)
        cls.set_function(visual.simple_2d_anim, 'plotter', 
                         ['ensemble', 'steps'], (), 
                         'garbage', 9, post_loop = True)
        cls.sort_functions()
        if cls.verbose:
            print('The Solar System has been preloaded. Please run the \
              appropriate preload-function to load something else instead.')
    
    
    def preload_n_body_nice(cls):
        # TODO: FIX THIS
        cls.set_time(0, timestep.constant_dt(2e6), timegen.time_years(200))
        cls.set_function(arena.make_arena_inf, 'arena generator',
                         [], (), 
                         'cells and limits', 1,
                         pre_loop = True)
        cls.set_function(ensgen.n_body_nice, 'ensemble generator',
                         ['cells and limits'], (),
                         'ensemble', 2, 
                         pre_loop = True)
        cls.set_function(solver.sym_solver_init, 'pre-solver',
                         [], (1,),
                         'solver object', 3,
                         pre_loop = True)
        cls.set_function(integrator.n_body_nice, 'integrator',
                         ['ensemble'], (),
                         'ensemble', 4)
        cls.set_function(force.gravity, 'force 1', 
                         ['affector position', 'affectee position', 
                          'affector mass', 'affectee mass'], (),
                          'force', 5)
        cls.set_function(acceleration.single_force_acceleration, 'accelerator',
                         ['ensemble', 'force'], (),
                         'acceleration', 6)
        cls.set_function(solver.sym, 'solver',
                         ['solver object', 'steps', 
                          'ensemble', 'acceleration'], (cls.time_step,),
                          'ensemble', 7)
        cls.set_function(cls.save_data, 'saver', 
                         ['ensemble'], (),
                         'ensemble', 8, priority = 5)
        cls.set_function(visual.simple_2d_anim, 'plotter', 
                         ['ensemble', 'steps'], (), 
                         'garbage', 9, post_loop = True)
        cls.sort_functions()
        if cls.verbose:
            print('The Solar System has been preloaded. Please run the \
              appropriate preload-function to load something else instead.')
    
    
    def preload_lennard_jones(cls):
        # func, name, input_keys, static_params, output_key, 
        # order, pre_loop = False, post_loop = False):
        cls.set_time(0, timestep.constant_dt(0.01), timegen.time_seconds(10))
        cls.set_function(arena.make_arena, 'arena generator',
                         [], (0.4, 0.6), 
                         'cells and limits', 1,
                         pre_loop = True)
        cls.set_function(ensgen.lennard_jones_example, 'ensemble generator', 
                         ['cells and limits'], (),
                         'ensemble', 2,
                         pre_loop = True)
        cls.set_function(integrator.PIC_make_local_choords_once, 'integrator0',
                         ['cells and limits'], (),
                         'local cell choords', 3,
                         pre_loop = True)
        cls.set_function(integrator.PIC_get_non_periodic_box_indices,
                         'integrator1', ['cells and limits'], (),
                         'PIC cell indices', 4,
                         pre_loop = True)
        cls.set_function(solver.sym_solver_init, 'pre-solver',
                         [], (1,),
                         'solver object', 5,
                         pre_loop = True)
        cls.set_function(integrator.PIC_force_non_periodic, 'integrator',
                         ['PIC cell indices', 'ensemble'], 
                         (force.lennard_jones, ),
                         'force', 6)
        cls.set_function(acceleration.single_force_acceleration, 'accelerator',
                         ['ensemble', 'force'], (),
                         'acceleration', 7)
        cls.set_function(solver.sym, 'solver', 
                         ['solver object', 'steps', 
                          'ensemble', 'acceleration'], (cls.time_step,), 
                         'ensemble', 8)
        cls.set_function(integrator.PIC_organize, 'integrator2',
                         ['ensemble', 'cells and limits',
                          'local cell choords'], (),
                          'ensemble', 9)
        cls.set_function(integrator.update_affector, 'affector update',
                         ['ensemble'], (),
                         'ensemble', 10)
        cls.set_function(boundaries.edge_elastic, 'boundary',
                         ['ensemble'], (1, [0,1,2], [-0.6, -0.6, -0.6], 
                         [0.6, 0.6, 0.6]),
                         'ensemble', 11)
        cls.set_function(cls.save_data, 'saver', 
                         ['ensemble'], (),
                         'ensemble', 12, priority = 20)
        cls.set_function(visual.simple_2d_anim, 'plotter', 
                         ['ensemble', 'steps'], (), 
                         'garbage', 13, post_loop = True)
        cls.sort_functions()
        if cls.verbose:
            print('The Solar System has been preloaded. Please run the \
              appropriate preload-function to load something else instead.')
        
        print('Ready to go!')
        
    def preload_lennard_jones_old(cls):
        # func, name, input_keys, static_params, output_key, 
        # order, pre_loop = False, post_loop = False):
        cls.set_time(0, timestep.constant_dt(0.1), timegen.time_seconds(100))
        cls.set_function(arena.make_arena, 'arena generator',
                         [], (0.4, 0.6), 
                         'cells and limits', 1,
                         pre_loop = True)
        cls.set_function(ensgen.lennard_jones_example, 'ensemble generator', 
                         ['cells and limits'], (),
                         'ensemble', 2,
                         pre_loop = True)
        cls.set_function(integrator.PIC_make_local_choords_once, 'integrator0',
                         ['cells and limits'], (),
                         'local cell choords', 3,
                         pre_loop = True)
        cls.set_function(solver.sym_solver_init, 'pre-solver',
                         [], (1,),
                         'solver object', 4,
                         pre_loop = True)
        cls.set_function(integrator.PIC_force, 'integrator',
                         ['ensemble'], (force.lennard_jones, ),
                         'force', 5)
        cls.set_function(acceleration.single_force_acceleration, 'accelerator',
                         ['ensemble', 'force'], (),
                         'acceleration', 6)
        cls.set_function(solver.sym, 'solver', 
                         ['solver object', 'steps', 
                          'ensemble', 'acceleration'], (cls.time_step,), 
                         'ensemble', 7)
        cls.set_function(integrator.PIC_organize, 'integrator1',
                         ['ensemble', 'cells and limits',
                          'local cell choords'], (),
                          'ensemble', 8)
        cls.set_function(integrator.update_affector, 'affector update',
                         ['ensemble'], (),
                         'ensemble', 9)
        cls.set_function(boundaries.edge_elastic, 'boundary',
                         ['ensemble'], (1, [0,1,2], [-0.6, -0.6, -0.6], 
                         [0.6, 0.6, 0.6]),
                         'ensemble', 10)
        cls.set_function(cls.save_data, 'saver', 
                         ['ensemble'], (),
                         'ensemble', 11, priority = 5)
        cls.set_function(visual.simple_2d_anim, 'plotter', 
                         ['ensemble', 'steps'], (), 
                         'garbage', 12, post_loop = True)
        cls.sort_functions()
        if cls.verbose:
            print('The Solar System has been preloaded. Please run the \
              appropriate preload-function to load something else instead.')
        
        print('Ready to go!')
        
    
    
    def preload_particle_in_B_field(cls):
        cls.set_time(0, timestep.constant_dt(0.001), 
                     time_end = timegen.time_seconds(20))
        cls.set_function(arena.make_arena_inf, 'arena generator',
                         [], (),
                         'cells and limits', 1,
                         pre_loop = True)
        cls.set_function(ensgen.particle_in_B, 'ensemble generator',
                         ['cells and limits'], (),
                         'ensemble', 2,
                         pre_loop = True)
        cls.set_function(force.uniform_B, 'field generator 1',
                         [], (1, 2),
                         'B-field', 3,
                         pre_loop = True)
        cls.set_function(force.uniform_E, 'field generator 2',
                         [], (0, 0),
                         'E-field', 4,
                         pre_loop = True)
        cls.set_function(solver.sym_solver_init, 'pre-solver',
                         [], (1,),
                         'solver object', 5,
                         pre_loop = True)
        cls.set_function(force.lorentz_force, 'force function',
                         ['E-field', 'B-field', 'charge', 'velocity'], (),
                         'force', 6,
                         priority = 1)
        cls.set_function(acceleration.single_force_acceleration, 'accelerator',
                         ['ensemble', 'force'], (),
                         'acceleration', 7,
                         priority = 1)
        cls.set_function(solver.sym, 'solver',
                         ['solver object', 'steps', 
                          'ensemble', 'acceleration'], (cls.time_step, ),
                         'ensemble', 8,
                         priority = 1)
        cls.set_function(cls.save_data, 'saver',
                         ['ensemble'], (),
                         'ensemble', 9,
                         priority = 100)
        cls.set_function(visual.simple_2d_anim, 'plotter',
                         ['ensemble', 'steps'], (),
                         'garbage', 10, post_loop = True)
        cls.sort_functions()
    
    
    def preload_two_body_problem(cls):
        cls.set_time(0, timestep.constant_dt(0.001), timegen.time_seconds(20))
        cls.set_function(arena.make_arena_inf, 'arena generator',
                         [], (),
                         'cells and limits', 1,
                         pre_loop = True)
        cls.set_function(ensgen.two_body_problem, 'ensemble generator',
                         ['cells and limits'], (),
                         'ensemble', 2,
                         pre_loop = True)
        cls.set_function(solver.sym_solver_init, 'pre-solver',
                         [], (1,),
                         'solver object', 5,
                         pre_loop = True)
        cls.set_function(force.gravity, 'force function',
                         ['E-field', 'B-field', 'charge', 'velocity'], (),
                         'force', 6,
                         priority = 1)
        cls.set_function(acceleration.single_force_acceleration, 'accelerator',
                         ['ensemble', 'force'], (),
                         'acceleration', 7,
                         priority = 1)
        cls.set_function(solver.sym, 'solver',
                         ['solver object', 'steps', 
                          'ensemble', 'acceleration'], (cls.time_step,),
                         'ensemble', 8,
                         priority = 1)
        cls.set_function(cls.save_data, 'saver',
                         ['ensemble'], (),
                         'ensemble', 9,
                         priority = 100)
        cls.set_function(visual.simple_2d_anim, 'plotter',
                         ['ensemble', 'steps'], (),
                         'garbage', 10, post_loop = True)
        cls.sort_functions()
        
    
    
    def run(cls):
        cls._preamble()
        cls._loop()
        cls._postprocessing()
        return cls.data
    
    
    def set_function(cls, func, name, input_keys, static_params, output_key, 
                     order, priority = 1, pre_loop = False, post_loop = False):
        if pre_loop and post_loop:
            raise('wtf')
        
        ensemble_keys = []
        data_keys = []
        for k in input_keys:
            if k in cls.definite_ensemble_keys:
                ensemble_keys.append(k)
            else:
                data_keys.append(k)
        
        
        cls.functions[name]                  = cls._update(func, static_params)
        cls.functions[name + cls.input_str]  = data_keys
        cls.functions[name + cls.ens_str]    = ensemble_keys
        cls.functions[name + cls.output_str] = output_key
        cls.functions[name + cls.order_str]  = order
        cls.functions[name + cls.loop_str]   = -pre_loop + post_loop
        cls.functions[name + cls.prio_str]   = priority
        
        if name == 'pre-solver':
            cls.order = static_params[0]
        
        
    def set_time(cls, time_start, time_step, time_end, max_steps = 100000):
        cls.time_start = time_start
        cls.time_step  = time_step
        cls.time_end   = time_end
        cls._time_now  = time_start
        cls.step_max   = max_steps
    
    
    def save_data(cls, ensemble,
                  key_ensemble = 'affectee position',
                  key_save = 'affectee position data'):
        data_temp = np.empty((0,3), float)
        cnt = 0
        for i in ensemble[key_ensemble].flatten():
            #print(cnt)
            cnt += 1
            data_temp = np.append(data_temp, i, axis=0)
        ensemble[key_save] = np.append(ensemble[key_save],
                                np.reshape(data_temp,
                                          (ensemble['number of objects'],
                                           3,1)), axis = 2)
        return ensemble
        
    
    
    def sort_functions(cls):
        funcs         = [cls.functions[k] for k in cls.functions.keys() \
                         if cls.input_str not in k\
                         if cls.output_str not in k\
                         if cls.order_str not in k\
                         if cls.loop_str not in k\
                         if cls.ens_str not in k\
                         if cls.prio_str not in k]
        input_keys    = [cls.functions[k] for k in cls.functions.keys() \
                         if cls.input_str in k]
        ensemble_keys = [cls.functions[k] for k in cls.functions.keys() \
                         if cls.ens_str in k]
        output_keys   = [cls.functions[k] for k in cls.functions.keys() \
                         if cls.output_str in k]
        loop_status   = [cls.functions[k] for k in cls.functions.keys() \
                         if cls.loop_str in k]
        order         = [cls.functions[k] for k in cls.functions.keys() \
                         if cls.order_str in k]
        priority      = [cls.functions[k] for k in cls.functions.keys() \
                         if cls.prio_str in k]
        
        indx = np.array(order).argsort()
        cls.funcs = np.empty(indx.size, object)
        cls.output_keys = np.empty(indx.size, object)
        cls.input_keys = np.empty(indx.size, object)
        cls.ensemble_keys = np.empty(indx.size, object)
        cls.priority = np.array(priority)[indx]
        for srt_in, cnt_in in zip(indx, range(indx.size)):
            cls.funcs[cnt_in] = funcs[srt_in]
            cls.output_keys[cnt_in] = output_keys[srt_in]
            cls.input_keys[cnt_in] = input_keys[srt_in]
            cls.ensemble_keys[cnt_in] = ensemble_keys[srt_in]
        cls.loop = np.array(loop_status)[indx]
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
            
    
    
    