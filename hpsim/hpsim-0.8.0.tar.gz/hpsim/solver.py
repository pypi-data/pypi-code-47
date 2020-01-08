#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
solver.py contains everything related to solvers, that is, integrators... they
make time move forward, okay!
"""
import numpy as np
from numpy import linalg as LA

class Solvers:
    def __init__(self, order):
        sym1_c = [1]
        sym1_d = [1]
        
        sym2_c = [0, 1]
        sym2_d = [0.5, 0.5]
        
        sym3_c = [1, -2/3, 2/3]
        sym3_d = [-1/24, 3/4, 7/24]
        
        a = 2**(1/3)        
        sym4_c = [1/(2*(2-a)), (1-a)/(2*(2 - a)), 
                       (1-a)/(2*(2 - a)), 1/(2*(2-a))]
        sym4_d = [1/(2-a), -a/(2-a), 1/(2-a), 0]
        
        sym_c = np.array([sym1_c, sym2_c, sym3_c, sym4_c])
        sym_d = np.array([sym1_d, sym2_d, sym3_d, sym4_d])
        
        self.order = order-1
        
        self.sym_c_use = sym_c[self.order]
        self.sym_d_use = sym_d[self.order]
        self.reset_len = len(sym_c[self.order])
    
        



def sym_solver_init(order):
    solver_obj = Solvers(order)
    return solver_obj
    

def sym4(solver_obj, stps, ensemble, acceleration, dt):
    so = solver_obj
    ensemble['acceleration'] = acceleration
    indx = stps%so.reset_len
    print(indx)
    ensemble = sym_kick(ensemble, dt, so.sym_d_use[indx])
    ensemble = sym_drift(ensemble, dt, so.sym_c_use[indx])
    return ensemble


def sym(solver_obj, stps, ensemble, acceleration, dt):
    so = solver_obj
    ensemble['acceleration'] = acceleration
    indx = stps%so.reset_len
    ensemble = sym_kick(ensemble, dt, so.sym_d_use[indx])
    ensemble = sym_drift(ensemble, dt, so.sym_c_use[indx])
    return ensemble


def sym1(ensemble, acceleration, dt):
    #a = LA.norm(ensemble['velocity'][0])
    ensemble['acceleration'] = acceleration
    ensemble = sym_kick(ensemble, dt, 1)
    ensemble = sym_drift(ensemble, dt, 1)
    #b = LA.norm(ensemble['velocity'][0])
    #print(a)
    #print(b)
    return ensemble

#TODO: INDEN ALLE HASTIGHEDSOPDATERINGER SKAL KRAFTEN UDREGNES VED DEN NYE POSITION

def sym2(ensemble, acceleration, dt):
    a = LA.norm(ensemble['velocity'][0])
    ensemble['acceleration'] = acceleration
    ensemble = sym_kick(ensemble, dt, 0.5)
    ensemble = sym_drift(ensemble, dt, 1)
    ensemble = sym_kick(ensemble, dt, 0.5)
    b = LA.norm(ensemble['velocity'][0])
    print(a)
    print(b)
    return ensemble

def sym3(ensemble, acceleration, dt):
    ensemble['acceleration'] = acceleration
    
    a = LA.norm(ensemble['velocity'][0])
    
    ensemble = sym_drift(ensemble, dt, 1)
    ensemble = sym_kick(ensemble, dt, -1/24)
    ensemble = sym_drift(ensemble, dt, -2/3)
    ensemble = sym_kick(ensemble, dt, 3/4)
    ensemble = sym_drift(ensemble, dt, 2/3)
    ensemble = sym_kick(ensemble, dt, 7/24)
    
    b = LA.norm(ensemble['velocity'][0])
    print(a)
    print(b)
    
    
    return ensemble
    


# TODO: SYM3
# TODO: SYM4
# TODO: RK





def sym_kick(ensemble, dt, d):
    vel = ensemble['velocity'].flatten()
    acc = ensemble['acceleration'].flatten()
    for i in range(vel.size):
        vel[i] += d * dt * acc[i]
    ensemble['velocity'] = vel.reshape(ensemble['velocity'].shape)
    return ensemble

def sym_drift(ensemble, dt, c):
    pos = ensemble['affectee position'].flatten()
    vel = ensemble['velocity'].flatten()
    for i in range(vel.size):
        pos[i] += c * dt * vel[i]
    ensemble['affectee position'] = pos.reshape(
                                ensemble['affectee position'].shape)
    return ensemble
# =============================================================================
# def sym_kick(ensemble, dt, d):
#     ensemble['velocity'] += d * dt * ensemble['acceleration']
#     return ensemble
# 
# 
# def sym_drift(ensemble, dt, c):
#     ensemble['affectee position'] += c * dt * ensemble['velocity']
#     return ensemble
# =============================================================================





