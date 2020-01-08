#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:21:59 2019

@author: hogbobson
"""
import numpy as np


### BOUNDARIES
def periodic_boundaries(ensemble, cells_and_limits):
    limits = cells_and_limits[1]
    org_shape = ensemble['affectee position'].shape
    afcte_pos = ensemble['affectee position'].flatten()
    afctr_pos = ensemble['affector position'].flatten()
    for i in range(afcte_pos.size):
        afcte_pos[i][afcte_pos[i] > limits] = \
        afcte_pos[i][afcte_pos[i] > limits]%(limits) - limits 
        afctr_pos[i][afctr_pos[i] > limits] = \
        afctr_pos[i][afctr_pos[i] > limits]%(limits) - limits
        afcte_pos[i][afcte_pos[i] < -limits] = \
        -afcte_pos[i][afcte_pos[i] < -limits]%(limits) + limits
        afctr_pos[i][afctr_pos[i] < -limits] = \
        -afctr_pos[i][afctr_pos[i] < -limits]%(limits) + limits
            
    
    ensemble['affectee position'] = afcte_pos.reshape(org_shape)
    ensemble['affector position'] = afctr_pos.reshape(org_shape)
    return ensemble


def oblivion_boundaries(ensemble, cells_and_limits):
    limits     = cells_and_limits[1]
    org_shape  = ensemble['affectee position'].shape
    afcte_pos  = ensemble['affectee position'].flatten()
    afctr_pos  = ensemble['affector position'].flatten()
    afcte_mass = ensemble['affectee mass'].flatten()
    afctr_mass = ensemble['affector mass'].flatten()
    afcte_vel  = ensemble['velocity'].flatten()
    afct_stat  = ensemble['affect_status'].flatten()
    

def edge(ensemble, edge_axes = [0], 
         edge_values_lower = [0], edge_values_upper = [np.inf]):
    org_shape = ensemble['affectee position'].shape
    afcte_pos = ensemble['affectee position'].flatten()
    afctr_pos = ensemble['affector position'].flatten()
    
    for i in range(afcte_pos.size):
        for ax, val in zip(edge_axes, edge_values_lower):
            afcte_pos[i][:,ax][afcte_pos[i][:,ax] < val] = val
            afctr_pos[i][:,ax][afctr_pos[i][:,ax] < val] = val
        for ax, val in zip(edge_axes, edge_values_upper):
            afcte_pos[i][:,ax][afcte_pos[i][:,ax] > val] = val
            afctr_pos[i][:,ax][afctr_pos[i][:,ax] > val] = val
            
    ensemble['affectee position'] = afcte_pos.reshape(org_shape)
    ensemble['affector position'] = afctr_pos.reshape(org_shape)
    return ensemble


def edge_elastic(ensemble, elasticity = 1, 
                 edge_axes = [0], 
                 edge_values_lower = [0], edge_values_upper = [np.inf]):
    org_shape = ensemble['affectee position'].shape
    afcte_pos = ensemble['affectee position'].flatten()
    afcte_vel = ensemble['velocity'].flatten()
    
    for i in range(afcte_pos.size):
        for ax, val in zip(edge_axes, edge_values_lower):
            drctn = np.sign(afcte_vel[i][:,ax][afcte_pos[i][:,ax] < val])
            afcte_vel[i][:,ax][afcte_pos[i][:,ax] < val] *= -elasticity*-drctn
        for ax, val in zip(edge_axes, edge_values_upper):
            drctn = np.sign(afcte_vel[i][:,ax][afcte_pos[i][:,ax] > val])
            afcte_vel[i][:,ax][afcte_pos[i][:,ax] > val] *= -elasticity*drctn
    
    ensemble['velocity'] = afcte_vel.reshape(org_shape)
    return ensemble