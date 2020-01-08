#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
force.py is supposed to contain all of the pre-defined forces you can use.
You can make your own, of course, but it's good to have several.
"""
# External modules
import numpy as np
from numpy import linalg as LA
from scipy import constants as cnst

from .miscfuncs import distances as dist

# Internal modules
from hpsim.miscfuncs import distances

def gravity(affector_pos, affectee_pos, affector_mass, affectee_mass):
    ator_pos   = affector_pos.flatten()
    atee_pos   = affectee_pos.flatten()
    ator_mass  = affector_mass.flatten()
    atee_mass  = affectee_mass.flatten()
    F_temp     = np.empty_like(atee_pos)
    F          = np.empty_like(atee_pos)
    
    for i in range(atee_pos.size):
        n_atee    = atee_mass[i].size
        n_ator    = ator_mass[i].size
        d         = dist(atee_pos[i], ator_pos[i])
        d_mag     = LA.norm(d, axis = 2)
        d_mag_cub = d_mag*d_mag*d_mag
        F_temp[i] = -d * ator_mass[i].reshape((1,n_ator,1)) \
                      * atee_mass[i].reshape((n_atee,1,1)) \
                      * cnst.gravitational_constant \
                      / d_mag_cub.reshape(np.append(d_mag_cub.shape, 1))
        F_temp[i][np.isnan(F_temp[i])] = 0
        F[i]      = np.sum(F_temp[i], axis = 1)
        #print(F[i][5])
    
    F = F.reshape(affectee_pos.shape)
    return F
        

# =============================================================================
# def gravity(afctor_pos, afctee_pos, afctor_mass, afctee_mass):
#     """ gravity calculates - you guessed it - gravity. It works with the now
#     300-year-old equation F = GMm/r². """
#     
#     n_afctee  = np.shape(afctee_mass)[0]
#     
#     d         = np.empty(n_afctee, dtype=object)
#     d_mag_cub = np.empty(n_afctee, dtype=object)
#     F_temp    = np.empty(n_afctee, dtype=object)
#     
#     for i in range(n_afctee):
#         n_afctor = np.shape(afctor_pos[i])[0]
#         d[i] = afctor_pos[i] - afctee_pos[i,:]
#         d_mag_cub[i] = LA.norm(d[i], axis = 1)
#         d_mag_cub[i] *= d_mag_cub[i]*d_mag_cub[i]
#         #d_mag_cub[i][d_mag_cub == 0] = np.nan
#         F_temp[i] = d[i]* np.reshape(afctor_mass[i], (n_afctor,1)) \
#                     / np.reshape(d_mag_cub[i], (n_afctor,1))
#         F_temp[i][np.isnan(F_temp[i])] = 0
#     
#     F_temp *= cnst.gravitational_constant * afctee_mass
#     F = [np.sum(x, axis=0) for x in F_temp]
#     return F
# =============================================================================


def electrostatics(pos, charge):
    """ electrostatics calculates electrostatic forces between charged
    particles, using F = 1/(4\pi\eps_0)*qQ/r² """
    
    charge = np.array(charge)    
    dist = distances(pos)               # Find distances between objects
    dist_mag = LA.norm(dist, axis = 2)  # And the magnitude of these distances
    dist_mag[dist_mag == 0] = np.nan    # We'll divide soon - 0s not allowed
    dist_cub = dist_mag*dist_mag*dist_mag # r^3
    F_all = 1/(4*np.pi*cnst.epsilon_0) * charge.reshape((1, len(charge), 1)) *\
            charge.reshape((len(charge), 1, 1)) * dist / \
            dist_cub.reshape(np.append(np.shape(dist_mag), 1))
    F_all[np.isnan(F_all)] = 0
    F = np.sum(F_all, axis = 1)
    return F


def lennard_jones_unpacker(affector_pos, affectee_pos, sigma, epsilon):
    orig_shp  = affectee_pos.shape
    
    afctr_pos = affector_pos.flatten()
    afcte_pos = affectee_pos.flatten()
    F = np.empty_like(afctr_pos, object)
    
    for i in range(F.size):
        F[i] = lennard_jones(afctr_pos[i], afcte_pos[i], sigma, epsilon)
        F[i] = np.sum(F[i], axis = 1)
    
    F = F.reshape(orig_shp)
    return F


def lennard_jones(afctr_pos, afcte_pos, sigma, epsilon):
    #afctr_pos = ensemble['affector position']
    #afcte_pos = ensemble['affectee position']
    
    #sigma     = ensemble['sigma']
    sigma_6   = np.power(sigma, 6)
    sigma_12  = np.power(sigma, 12)
    #epsilon   = ensemble['epsilon']
    
    n_afcte   = np.shape(afcte_pos)[0]
    n_afctr   = np.shape(afctr_pos)[0]
    
    
    d           = dist(afcte_pos, afctr_pos)
    d_mag       = LA.norm(d, axis = 2)
    d_pow_8  = np.power(d_mag, 8)
    d_pow_14 = np.power(d_mag, 14)
    F_temp   = 4 * epsilon * d *\
                      (12*sigma_12 / d_pow_14.reshape((n_afcte, n_afctr,1)) -
                       6*sigma_6 / d_pow_8.reshape((n_afcte, n_afctr,1)))
    F_temp[np.isnan(F_temp)] = 0
    
    return F_temp


def lorentz_force(E_fields, B_fields, affectee_charge, affectee_vel):
    orig_shp  = affectee_vel.shape
    
    afcte_vel = affectee_vel.flatten()
    afcte_chg = affectee_charge.flatten()
    E         = E_fields
    B         = B_fields
    F         = np.empty_like(afcte_vel)
    
    for i in range(afcte_vel.size):
        F[i] = afcte_chg[i]*(E + np.cross(afcte_vel[i][0], B))
    
    
    F = F.reshape(orig_shp)    
    return F
    


#### FIELDS
    
def uniform_gravity(afcte_mass, axis_of_acc = 1, g = -10):
    F = np.zeros((afcte_mass.size, 3))
    F[:,axis_of_acc] = g*afcte_mass
    return F


def uniform_E(strength, direction):
    E = np.zeros(3)
    E[direction] = strength
    return E

def uniform_B(strength, direction):
    B = np.zeros(3)
    B[direction] = strength
    return B


def E_from_point(d, d_mag_3, afctr_chg):
    pre = 1/4*np.pi*cnst.epsilon_0
    
    E = pre*d*afctr_chg.reshape(np.append(afctr_chg.shape, 1)) / \
        d_mag_3.reshape(np.append(d_mag_3.shape, 1))
    
    return E

def B_from_particle(d, d_mag_3, afctr_vel, afctr_chg):
    pre = cnst.mu_0/(4*np.pi)
    
    B = pre*afctr_chg*np.cross(afctr_vel, d)/d_mag_3
    return B




# =============================================================================
# for i in range(n_afcte):
#         d[i]        = afctr_pos[i] - afcte_pos[i,:]
#         d_mag       = LA.norm(d[i], axis = 1)
#         d_pow_8[i]  = np.power(d_mag, 8)
#         d_pow_14[i] = np.power(d_mag, 14)
#         F_temp[i]   = 4 * epsilon * d *\
#                       (12*sigma_12/np.reshape(d_pow_14[i], (n_afctr, 1)) -
#                        6*sigma_6/np.reshape(d_pow_8[i], (n_afctr, 1)))
#     
# =============================================================================


# TODO: SIMPLE SURFACE GRAVITY
    
def check_force(force_to_check):
    # TODO: MAKE more GENERAL
    gravity_return = {'keys': ['force gravity', 'args gravity'],
                      'arg_keys': ('affector position', 'affectee position',
                                   'affector mass', 'affectee mass')}
    electrostatics_return = {'keys': ['force electrostatics', 
                                      'args electrostatics'],
                      'arg_keys': ('position', 'charge')}
    lennard_jones_return = {'keys': ['force lennard_jones',
                                     'args lennard_jones'],
                        'arg_keys': ('affector position', 
                                     'affectee position',
                                     'sigma', 'epsilon')}
    
    if force_to_check == gravity:
        return gravity_return
    elif force_to_check == electrostatics:
        return electrostatics_return
    elif force_to_check == lennard_jones:
        return lennard_jones_return
    else:
        return False
    




    
# =============================================================================
#     print(type(mass))
#     
#     dist = distances(pos)               # Find distances between objects
#     dist_mag = LA.norm(dist, axis = 2)  # And the magnitude of these distances
#     dist_mag[dist_mag == 0] = np.nan    # We'll divide soon - 0s not allowed
#     dist_cub = dist_mag*dist_mag*dist_mag # r^3
#     F_all = cnst.gravitational_constant * mass.reshape((1, len(mass), 1)) * \
#             mass.reshape((len(mass), 1, 1)) * dist / \
#             dist_cub.reshape(np.append(np.shape(dist_mag), 1))
#     F_all[np.isnan(F_all)] = 0    
#     F = np.sum(F_all, axis = 1)
# =============================================================================