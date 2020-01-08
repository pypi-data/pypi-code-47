#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:04:09 2019

@author: hogbobson
"""

import numpy as np
from numpy import random as rng, linalg as LA
from astropy import constants as astcnst
from math import radians as rad
from hpsim import energy
from hpsim.miscfuncs import distances
from hpsim.miscfuncs import legit_body_parametres as lbp
from hpsim.timegen import current_time

class StarSystemGenerator:
    def __init__(self, cells, lims, cell_size):
        self.r      = np.empty((0,3), float)    # Position r
        self.v      = np.empty((0,3), float)    # Velocity v
        self.m      = []                        # Mass m
        self.n      = 0                         # Number of objects
        self.label  = []                        # Label, for ???
        self.affect_status = []
        self.set_time()#td = {'year': 1990, 'month': 4, 'day': 19, 'hour': 0})
        #self.central_star()
        
        # Make cells something I can use
        flatcells_3d = cells.flatten()
        flatcells_1d = cells.flatten()
        for i in range(flatcells_3d.size):
            flatcells_3d[i] = np.empty((0,3), float)
            flatcells_1d[i] = np.array([], float)
        self.cells_3d = np.reshape(flatcells_3d, np.shape(cells))
        self.cells_1d = np.reshape(flatcells_1d, np.shape(cells))
        
        self.r              = np.copy(self.cells_3d)
        self.v              = np.copy(self.cells_3d)
        self.m              = np.copy(self.cells_1d)
        self.label          = np.empty_like(np.copy(self.cells_1d))
        self.affect_status  = np.copy(self.cells_1d)
        
        if np.inf not in lims:
            if np.size(lims) > 1:
                self.offset = np.empty(np.size(lims)//2)
                for i in range(np.size(lims)):
                    self.offset[i] = -lims[0 + 2*i]
            else:
                self.offset = [lims, lims, lims]
        else:
            self.offset = np.zeros((1,3))
        self.c_size = cell_size
        
    
    def _rotation_x(self, phi):
        R = np.zeros((3,3))
        R[0,0] = 1
        R[1,1] = np.cos(phi)
        R[1,2] = -np.sin(phi)
        R[2,1] = np.sin(phi)
        R[2,2] = np.cos(phi)
        return R
    
    
    def _rotation_z(self, phi):
        R = np.zeros((3,3))
        R[0,0] = np.cos(phi)
        R[1,1] = np.cos(phi)
        R[0,1] = -np.sin(phi)
        R[1,0] = np.sin(phi)
        R[2,2] = 1
        return R
        
    
    def _ecc_anomaly(self, E0, e, M):
        E1 = E0 - (E0 - e*np.sin(E0) - M)/(1 - e*np.cos(E0))
        if E1 - E0 > 1e-5:# and E1 < E0:
            return self._ecc_anomaly(E1, e, M)
        elif E1 - E0 < 1e5:# and E1 < E0:
            return E1
        #elif E1 > E0:
        #    raise Exception('orbit is not elliptical')
        
        
    def _orbit_to_cart(self, Omega, i, omega, a, e, M):
        # Get shorter constants        
        G = astcnst.G.value
        M_sun = self.M_sun
        
        # Calculations
        E       = self._ecc_anomaly(M, e, M)
        nu      = 2*np.arctan2(np.sqrt(1+e)*np.sin(E/2), \
                               np.sqrt(1-e)*np.cos(E/2))
        rm      = a * (1 - e*np.cos(E))
        o       = rm * np.array([np.cos(nu), np.sin(nu), 0])
        odot    = np.sqrt(G * M_sun * a) / rm * \
                       np.array([-np.sin(E), np.sqrt(1 - e*e)*np.cos(E), 0])
                       
        # Rotation matrices
        R_z_O   = self._rotation_z(-Omega)
        R_x_i   = self._rotation_x(-i)
        R_z_o   = self._rotation_z(-omega)
        
        # Outputs
        r       = np.dot(R_z_O, np.dot(R_x_i, np.dot(R_z_o, o)))
        v       = np.dot(R_z_O, np.dot(R_x_i, np.dot(R_z_o, odot)))
        #r = o
        #v = odot
        
        # MAYBE MOVE THIS PART OUT EVENTUALLY
        #eps = rad(23.43928)
        #r[1]    = np.cos(eps)*r[1] - np.sin(eps)*r[2]
        #r[2]    = np.sin(eps)*r[1] + np.cos(eps)*r[2]
        #v[1]    = np.cos(eps)*v[1] - np.sin(eps)*v[2]
        #v[2]    = np.sin(eps)*v[1] + np.cos(eps)*v[2]
        
        # Appending
        if not self.r.shape == np.zeros(1).shape:
            cell_indices = np.array((r + self.offset)//self.c_size, int)
        else:
            cell_indices = 0
        
        self.r[cell_indices] = np.append(self.r[cell_indices],
                                          np.array(r).reshape(1,3), axis = 0)
        self.v[cell_indices] = np.append(self.v[cell_indices],
                                          np.array(v).reshape(1,3), axis = 0)
        self.n += 1
        return cell_indices
    
    
    
    def get_ensemble(self):
        afctee_pos  = np.copy(self.cells_3d)
        afctee_vel  = np.copy(self.cells_3d)
        afctee_mass = np.copy(self.cells_1d)
        
        afctor_pos  = np.copy(self.cells_3d)
        afctor_mass = np.copy(self.cells_1d)
        
        temp_pos    = afctee_pos.flatten()
        temp_mass   = afctee_mass.flatten()
        temp_vel    = afctee_vel.flatten()
        
        temp_apos   = afctor_pos.flatten()
        temp_amass  = afctor_mass.flatten()
        
        temp_r      = self.r.flatten()
        temp_v      = self.v.flatten()
        temp_m      = self.m.flatten()
        temp_as     = self.affect_status.flatten()
        
        for i in range(temp_pos.size):
            temp_pos[i]   = temp_r[i][temp_as[i] >= 0]
            temp_vel[i]   = temp_v[i][temp_as[i] >= 0]
            temp_mass[i]  = temp_m[i][temp_as[i] >= 0]
            
            temp_apos[i]  = temp_r[i][temp_as[i] <= 0]
            temp_amass[i] = temp_m[i][temp_as[i] <= 0]
        
        afctee_pos  = np.reshape(temp_pos, afctee_pos.shape)
        afctee_vel  = np.reshape(temp_vel, afctee_vel.shape)
        afctee_mass = np.reshape(temp_mass, afctee_mass.shape)
        
        afctor_pos  = np.reshape(temp_apos, afctor_pos.shape)
        afctor_mass = np.reshape(temp_amass, afctor_mass.shape)
        
        afctee_pos_data = np.empty((0,3), float)
        for i in afctee_pos.flatten():
            afctee_pos_data = np.append(afctee_pos_data, i, axis = 0)
# =============================================================================
#         afctee_pos  = self.r[self.affect_status >= 0]
            
#         afctee_mass = self.m[self.affect_status >= 0]
#         
#         afctor_pos     = np.empty(sum(self.affect_status >= 0), dtype = object)
#         afctor_mass    = np.empty(sum(self.affect_status >= 0), dtype = object)
#         for i in range(sum(self.affect_status >= 0)):
#             afctor_pos[i]  = self.r[self.affect_status <= 0]
#             afctor_mass[i] = self.m[self.affect_status <= 0]
#         
#         afctee_vel  = self.v[self.affect_status >= 0]
# =============================================================================
        
        
        
        ensemble = {'affectee position': afctee_pos,
                    'affectee position data': np.reshape(afctee_pos_data,
                                                         (self.n, 3, 1)),
                    'affector position': afctor_pos,
                    #'distance'      : distances(),
                    'velocity'      : afctee_vel,
                    #'velocity magnitude': LA.norm(afctee_vel, axis = 1),
                    'affectee mass' : afctee_mass,
                    'affector mass' : afctor_mass,
                    'energy'        : None,
                    'energy data'   : None,
                    'number of objects': self.n,
                    'label'         : self.label,
                    'affect status' : self.affect_status,
                    'remaining'     : None
                }
        return ensemble
    
    def set_ensemble(self):
        pass
    
    def set_time(self, td = current_time()):
        """ Function setting the day-number as per section 3 at
            https://stjarnhimlen.se/comp/ppcomp.html """
        y = td['year']
        m = td['month']
        D = td['day']
        UT = td['hour']
        self.day_number = 367*y - 7 * ( y + (m+9)//12 ) // 4 - \
                        3 * ( ( y + (m-9)//7 ) // 100 + 1 ) // 4 + \
                        275*m//9 + D - 730515 + UT/24.0
    
    
    
    def rev(self, angle):
        while angle > np.pi:
            angle -= 2*np.pi
        while angle < -np.pi:
            angle += 2*np.pi
        return angle
    
    
    def mean_anomaly(self, semi_major_axis, M_central = astcnst.M_sun.value):
        pass
        
    
    def central_star(self, mass = astcnst.M_sun.value,
                     is_affected = True, affects = True):
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        zero = np.zeros((1,3))
        if not self.r.shape == np.zeros(1).shape:
            cell_indices = np.array((zero + self.offset)//self.c_size, int)
        else:
            cell_indices = 0
        
        self.M_sun = mass
        self.r[cell_indices] = np.append(self.r[cell_indices], zero, axis = 0)
        self.v[cell_indices] = np.append(self.v[cell_indices], zero, axis = 0)
        self.m[cell_indices] = np.append(self.m[cell_indices], mass)
        self.label[cell_indices] = np.append(self.label[cell_indices], 'Sun')
        self.n += 1
        self.affect_status[cell_indices] = np.append(
                self.affect_status[cell_indices], affect_num)
        
    
    
    # Omega     = Longitude of the Ascending Node (LAN) [rad]
    # i         = Inclination [rad]
    # omega     = Argument of Periapsis [rad]
    # a         = Semi-major-axis [m]
    # e         = Eccentricity [1]
    # M         = Mean anomaly [rad]
    # Thank you to https://stjarnhimlen.se/comp/ppcomp.html
    
    def mercury(self,
                is_affected = True, affects = True):
        # Get shorter constants
        d = self.day_number
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        # Inputs
        Omega   = self.rev(rad(48.3313 + 3.24587E-5 * d))
        i       = self.rev(rad(7.0047 + 5.00E-8 * d))
        omega   = self.rev(rad(29.1241 + 1.01444E-5 * d))
        a       = 0.387098*astcnst.au.value
        e       = 0.205635 + 5.59E-10 * d
        M       = self.rev(rad(168.6562 + 4.0923344368 * d))
        
        cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
        self.label[cell_indices] = np.append(self.label[cell_indices],
                                              'Mercury')
        self.m[cell_indices]  = np.append(self.m[cell_indices],
              astcnst.M_earth.value*0.0553)
        self.affect_status[cell_indices] = np.append(
                self.affect_status[cell_indices], affect_num)
    
    def venus(self,
              is_affected = True, affects = True):
        # Get shorter constants
        d = self.day_number
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        # Inputs
        Omega   = self.rev(rad(76.6799 + 2.46590E-5 * d))
        i       = self.rev(rad(3.3946 + 2.75E-8 * d))
        omega   = self.rev(rad(54.8910 + 1.38374E-5 * d))
        a       = 0.723330*astcnst.au.value
        e       = 0.006773 - 1.302E-9 * d
        M       = self.rev(rad(48.0052 + 1.6021302244 * d))
        
        cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
        self.label[cell_indices] = np.append(self.label[cell_indices], 'Venus')
        self.m[cell_indices]  = np.append(self.m[cell_indices],
              astcnst.M_earth.value*0.815)
        self.affect_status[cell_indices] = np.append(
                self.affect_status[cell_indices], affect_num)
    
    def earth(self,
              is_affected = True, affects = True):
        # Get shorter constants
        d = self.day_number
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        # Inputs
        Omega   = 0.
        i       = 0.
        omega   = self.rev(rad(282.9404 + 4.70935e-5 * d))
        a       = astcnst.au.value
        e       = 0.016709 - 1.151E-9 * d
        M       = self.rev(rad(356.0470 + 0.9856002585 * d))
        
        cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
        self.label[cell_indices] = np.append(self.label[cell_indices], 'Earth')
        self.m[cell_indices]  = np.append(self.m[cell_indices],
              astcnst.M_earth.value)
        self.affect_status[cell_indices] = np.append(
                self.affect_status[cell_indices], affect_num)
        
    
    def mars(self,
             is_affected = True, affects = True):
        # Get shorter constants
        d = self.day_number
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        # Inputs
        Omega   = self.rev(rad(49.5574 + 2.11081E-5 * d))
        i       = self.rev(rad(1.8497 - 1.78E-8 * d))
        omega   = self.rev(rad(286.5016 + 2.92961E-5 * d))
        a       = 1.523688*astcnst.au.value
        e       = 0.093405 + 2.516E-9 * d
        M       = self.rev(rad(18.6021 + 0.5240207766 * d))
        
        cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
        self.label[cell_indices] = np.append(self.label[cell_indices], 'Mars')
        self.m[cell_indices]  = np.append(self.m[cell_indices],
              astcnst.M_earth.value*0.107)
        self.affect_status[cell_indices] = np.append(
                self.affect_status[cell_indices], affect_num)
    
    def jupiter(self,
                is_affected = True, affects = True):
        # Get shorter constants
        d = self.day_number
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        # Inputs
        Omega   = self.rev(rad(100.4542 + 2.76854e-5 * d))
        i       = self.rev(rad(1.3030 - 1.557e-7 * d))
        omega   = self.rev(rad(273.8777 + 1.64505E-5 * d))
        a       = 5.20256*astcnst.au.value
        e       = 0.048498 + 4.469E-9 * d
        M       = self.rev(rad(19.8950 + 0.0830853001 * d))
        
        cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
        self.label[cell_indices] = np.append(self.label[cell_indices],
                  'Jupiter')
        self.m[cell_indices]  = np.append(self.m[cell_indices],
              astcnst.M_jup.value)
        self.affect_status[cell_indices] = np.append(
                self.affect_status[cell_indices], affect_num)
        
        
    def saturn(self,
               is_affected = True, affects = True):
        # Get shorter constants
        d = self.day_number
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        # Inputs
        Omega   = self.rev(rad(113.6634 + 2.38980E-5 * d))
        i       = self.rev(rad(2.4886 - 1.081E-7 * d))
        omega   = self.rev(rad(339.3939 + 2.97661E-5 * d))
        a       = 9.55475*astcnst.au.value
        e       = 0.055546 - 9.499E-9 * d
        M       = self.rev(rad(316.9670 + 0.0334442282 * d))
        
        cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
        self.label[cell_indices] = np.append(self.label[cell_indices],
                  'Saturn')
        self.m[cell_indices]  = np.append(self.m[cell_indices]
              , astcnst.M_earth.value * 95.16)
        self.affect_status[cell_indices] = np.append(
                self.affect_status[cell_indices], affect_num)
    
    def uranus(self,
               is_affected = True, affects = True):
        # Get shorter constants
        d = self.day_number
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        # Inputs
        Omega   = self.rev(rad(74.0005 + 1.3978E-5 * d))
        i       = self.rev(rad(0.7733 + 1.9E-8 * d))
        omega   = self.rev(rad(96.6612 + 3.0565E-5 * d))
        a       = 19.18171 - 1.55E-8 * d * astcnst.au.value
        e       = 0.047318 + 7.45E-9 * d
        M       = self.rev(rad(142.5905 + 0.011725806 * d))
        
        cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
        self.label[cell_indices] = np.append(self.label[cell_indices],
                  'Uranus')
        self.m[cell_indices]  = np.append(self.m[cell_indices],
              astcnst.M_earth.value * 14.54)
        self.affect_status[cell_indices] = np.append(
                self.affect_status[cell_indices], affect_num)
    
    def neptune(self,
                is_affected = True, affects = True):
        # Get shorter constants
        d = self.day_number
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        # Inputs
        Omega   = self.rev(rad(131.7806 + 3.0173E-5 * d))
        i       = self.rev(rad(1.7700 - 2.55E-7 * d))
        omega   = self.rev(rad(272.8461 - 6.027E-6 * d))
        a       = 30.05826 + 3.313E-8 * d * astcnst.au.value
        e       = 0.008606 + 2.15E-9 * d
        M       = self.rev(rad(260.2471 + 0.005995147 * d))
        
        cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
        self.label[cell_indices] = np.append(self.label[cell_indices], 
                  'Neptune')
        self.m[cell_indices]  = np.append(self.m[cell_indices],
              astcnst.M_earth.value * 17.15)
        self.affect_status[cell_indices] = np.append(
                self.affect_status[cell_indices], affect_num)
        
    def all_known_planets(self):
        self.mercury()
        self.venus()
        self.earth()
        self.mars()
        self.jupiter()
        self.saturn()
        #self.uranus()
        #self.neptune()
    
    def random_planets(self, num = 5,
                       is_affected = True, affects = True):
        def log_uniform(low, high, size = 1, base = 10):
            return np.power(base, rng.uniform(low, high, size))
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        for i in range(num):
            Omega = 360*rng.random() - 180
            i     = np.pi/6*rng.randn()
            omega = 360*rng.random() - 180
            a     = log_uniform(-2, 1) * astcnst.au.value
            e     = np.minimum(np.abs(rng.randn()*0.1), 0.95)
            M     = 360*rng.random() - 180
            
            cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
            self.label[cell_indices] = np.append(self.label[cell_indices],
                      ['planet #' + str(i)])
            self.m[cell_indices] = np.append(self.m[cell_indices],
                  log_uniform(22, 28))
            self.affect_status[cell_indices] = np.append(
                    self.affect_status[cell_indices], affect_num)
    
    def random_asteroids(self, num = 500, 
                         is_affected = True, affects = False):
        def log_uniform(low, high, size = 1, base = 10):
            return np.power(base, rng.uniform(low, high, size))
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        for i in range(num):
            Omega = 360*rng.random() - 180
            i     = np.pi/8*rng.randn()
            omega = 360*rng.random() - 180
            a     = abs(rng.randn())*1e7 + astcnst.au.value*5
            e     = np.minimum(np.abs(rng.randn()*0.1), 0.95)
            M     = 360*rng.random() - 180
            
            cell_indices = self._orbit_to_cart(Omega, i, omega, a, e, M)
            #self.label[cell_indices] = np.append(self.label[cell_indices], ['asteroid #' + str(i)])
            self.m[cell_indices] = np.append(self.m[cell_indices],
                  log_uniform(8, 18))
            self.affect_status[cell_indices] = np.append(
                    self.affect_status[cell_indices], affect_num)
    
    
    
    
    

class many_bodies_generator:
    def __init__(self, cells, lims, cell_size, scale = 'molecular',
                 charge_init_and_spread = [None, None],
                 lennard_jones_sig_and_eps = [None, None]):
        
        self.r      = np.empty((0,3), float)    # Position r
        self.v      = np.empty((0,3), float)    # Velocity v
        self.m      = []                        # Mass m
        self.n      = 0                         # Number of objects
        self.label  = []                        # Label, for ???
        self.affect_status = []
        self.parameter_dict = {}
        
        
        flatcells_3d = cells.flatten()
        flatcells_1d = cells.flatten()
        for i in range(flatcells_3d.size):
            flatcells_3d[i] = np.empty((0,3), float)
            flatcells_1d[i] = np.array([], float)
        self.cells_3d = np.array(flatcells_3d.reshape(np.shape(cells)), object)
        self.cells_1d = np.array(flatcells_1d.reshape(np.shape(cells)), object)
        
        self.r              = np.copy(self.cells_3d)
        self.v              = np.copy(self.cells_3d)
        self.m              = np.copy(self.cells_1d)
        self.label          = np.empty_like(np.copy(self.cells_1d), str)
        self.affect_status  = np.copy(self.cells_1d)
        
        if np.size(lims) > 1 and np.inf not in lims:
            self.fromzero = np.empty(np.size(lims)//2)
            self.c_size   = np.empty(np.size(lims)//2)
            for i in range(np.size(lims)):
                self.fromzero[i] = -lims[0 + 2*i]
                self.c_size[i]   = (lims[1 + 2*i] - lims[0 + 2*i])\
                                / np.shape(cells[i])
        elif np.size(lims) == 1 and not lims == np.inf:
            self.fromzero = [lims, lims, lims]
        else:
            self.fromzero = [0, 0, 0]
        self.lims = lims
        self.c_size = cell_size
        
        
        # TODO: MAKE IT AN OPTION TO MAKE YOUR OWN PHYSICAL PARAMETRES,
        # INSTEAD OF JUST CHANING THE VALUES OF THE PARAMETRES I HAVE DEFINED.
        if None not in charge_init_and_spread:
            self.q  = np.copy(self.cells_1d)
            print(cells.shape)
            self.parameter_dict['var charge'] = self.q
            self.parameter_dict['init charge'] = charge_init_and_spread[0]
            self.parameter_dict['spread charge'] = charge_init_and_spread[1]
        else:
            self.q  = None
        
        if None not in lennard_jones_sig_and_eps:
            self.sigma   = lennard_jones_sig_and_eps[0]
            self.epsilon = lennard_jones_sig_and_eps[1]
        else:
            self.sigma   = None
            self.epsilon = None
    
    def make_body_gaussian(self, offset = np.zeros((1,3)), 
                  initial_velocity = np.zeros((1,3)),
                  initial_mass = 1,
                  spread_pos = 0.1,
                  spread_vel = 0,
                  spread_mass = 0,
                  is_affected = True, affects = True):
        """ Makes a body based on input parametres and the parametres
        initialised in the instance of many_bodies_generator. """
        def log_uniform(low, high, size = 1, base = 10):
            return np.power(base, rng.uniform(low, high, size))
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        if not self.lims == np.inf:
            limmax = np.array([self.lims, self.lims, self.lims])
        else:
            limmax = np.array([spread_pos, spread_pos, spread_pos])
        limmin = -limmax
        
        pos = np.minimum(np.maximum(spread_pos * rng.randn(3) + offset,
                                    limmin + self.c_size),
                         limmax - self.c_size)
        vel = spread_vel * rng.randn(3) + initial_velocity
        mass = np.abs(spread_mass * rng.randn(1)) + initial_mass
        
        cell_indices = (pos + self.fromzero)//self.c_size
        cell_indices = [int(x) for x in cell_indices[0]]
        c = cell_indices
        
        # Setting up setting up the secial parametres
        par_keys = list(self.parameter_dict.keys())
        for i in np.arange(0, len(par_keys), 3):
            self.parameter_dict[par_keys[i]][cell_indices][:] = \
                np.append(self.parameter_dict[par_keys[i]][cell_indices][:],
                          self.parameter_dict[par_keys[i+2]] * rng.randn(1) +
                          self.parameter_dict[par_keys[i+1]])
        self.r[c[0], c[1], c[2]] = np.append(
                self.r[c[0], c[1], c[2]], pos.reshape((1,3)), axis = 0)
        self.v[c[0], c[1], c[2]] = np.append(
                self.v[c[0], c[1], c[2]], vel.reshape((1,3)), axis = 0)
        self.m[c[0], c[1], c[2]] = np.append(self.m[c[0], c[1], c[2]], mass)
        self.affect_status[c[0], c[1], c[2]] = np.append(
                self.affect_status[c[0], c[1], c[2]], affect_num)
        self.n += 1
    
    
    def make_body_uniform(self, offset = np.zeros((1,3)),
                          initial_velocity = np.zeros((1,3)),
                          initial_mass = 1,
                          lim_pos = 0,
                          lim_vel = 0,
                          spread_mass = 0,
                          is_affected = True, affects = True):
        def log_uniform(low, high, size = 1, base = 10):
            return np.power(base, rng.uniform(low, high, size))
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        if not np.any(self.lims == np.inf):
            limmax = np.array([self.lims, self.lims, self.lims])
        else:
            limmax = np.array([lim_pos, lim_pos, lim_pos])
        
        pos = (2*rng.rand(3)-1)*limmax + offset
        vel = (2*rng.rand(3)-1)*lim_vel + initial_velocity
        mass = np.abs(spread_mass * rng.randn(1)) + initial_mass
        
        if len(self.cells_1d.shape) > 1:
            cell_indices = np.array((pos + self.fromzero)//self.c_size)
            cell_indices = [int(x) for x in cell_indices[0]]
            c = cell_indices
            
            # Setting up setting up the secial parametres
            par_keys = list(self.parameter_dict.keys())
            for i in np.arange(0, len(par_keys), 3):
                print(cell_indices)
                self.parameter_dict[par_keys[i]][cell_indices][:] = \
                    np.append(self.parameter_dict[par_keys[i]][cell_indices][:],
                              self.parameter_dict[par_keys[i+2]] * rng.randn(1) +
                              self.parameter_dict[par_keys[i+1]])
            self.r[c[0], c[1], c[2]] = np.append(
                    self.r[c[0], c[1], c[2]], pos.reshape((1,3)), axis = 0)
            self.v[c[0], c[1], c[2]] = np.append(
                    self.v[c[0], c[1], c[2]], vel.reshape((1,3)), axis = 0)
            self.m[c[0], c[1], c[2]] = np.append(self.m[c[0], c[1], c[2]], mass)
            self.affect_status[c[0], c[1], c[2]] = np.append(
                    self.affect_status[c[0], c[1], c[2]], affect_num)
            self.n += 1
        else:
            par_keys = list(self.parameter_dict.keys())
            for i in np.arange(0, len(par_keys), 3):
                self.parameter_dict[par_keys[i]][0] = \
                    np.append(self.parameter_dict[par_keys[i]][0],
                              self.parameter_dict[par_keys[i+2]] * rng.randn(1) +
                              self.parameter_dict[par_keys[i+1]])
            self.r[0] = np.append(self.r[0], pos.reshape((1,3)), axis = 0)
            self.v[0] = np.append(self.v[0], vel.reshape((1,3)), axis = 0)
            self.m[0] = np.append(self.m[0], mass)
            self.affect_status[0] = np.append(self.affect_status[0], affect_num)
            self.n += 1
            
    
    
    def make_many_bodies(self, num_bods, offset = 0, 
                  initial_velocity = 0,
                  initial_mass = 1e60,
                  spread_pos = 10,
                  spread_vel = 0,
                  spread_mass = 0,
                  is_affected = True, affects = True):
        """ Makes a body based on input parametres and the parametres
        initialised in the instance of many_bodies_generator. """
        def log_uniform(low, high, size = 1, base = 10):
            return np.power(base, rng.uniform(low, high, size))
        
        affect_num = is_affected - affects
        # -1 = affects only, 1 = is affected only, 0 = both
        
        pos = spread_pos * rng.randn((num_bods, 3)) + offset
        vel = spread_vel * rng.randn((num_bods, 3)) + initial_velocity
        mass = np.abs(spread_mass * rng.randn(num_bods)) + initial_mass
        
        cell_indices = (pos + self.fromzero)//self.c_size
        
        # Setting up setting up the secial parametres
        par_keys = list(self.parameter_dict.keys())
        for i in np.arange(0, len(par_keys), 3):
            self.parameter_dict[par_keys[i]][cell_indices][:] = \
                np.append(self.parameter_dict[par_keys[i]][cell_indices][:],
                          self.parameter_dict[par_keys[i+2]] * \
                          rng.randn(num_bods) +
                          self.parameter_dict[par_keys[i+1]])
        self.r[cell_indices] = np.append(self.r[cell_indices], pos, axis = 0)
        self.v[cell_indices] = np.append(self.v[cell_indices], vel, axis = 0)
        self.m[cell_indices] = np.append(self.m[cell_indices], mass)
        self.n += num_bods
        for i in range(num_bods):
            self.affect_status[cell_indices] = np.append(
                    self.affect_status[cell_indices], affect_num)
        
    
    
    def get_ensemble(self):
        
        afctee_pos  = np.copy(self.cells_3d)
        afctee_vel  = np.copy(self.cells_3d)
        afctee_mass = np.copy(self.cells_1d)
        
        afctor_pos  = np.copy(self.cells_3d)
        afctor_mass = np.copy(self.cells_1d)
        
        temp_pos    = afctee_pos.flatten()
        temp_mass   = afctee_mass.flatten()
        temp_vel    = afctee_vel.flatten()
        
        temp_apos   = afctor_pos.flatten()
        temp_amass  = afctor_mass.flatten()
        
        temp_r      = self.r.flatten()
        temp_v      = self.v.flatten()
        temp_m      = self.m.flatten()
        temp_as     = self.affect_status.flatten()
        
        for i in range(temp_pos.size):
            temp_pos[i]   = temp_r[i][temp_as[i] >= 0]
            temp_vel[i]   = temp_v[i][temp_as[i] >= 0]
            temp_mass[i]  = temp_m[i][temp_as[i] >= 0]
            
            temp_apos[i]  = temp_r[i][temp_as[i] <= 0]
            temp_amass[i] = temp_m[i][temp_as[i] <= 0]
        
        afctee_pos  = np.reshape(temp_pos, afctee_pos.shape)
        afctee_vel  = np.reshape(temp_vel, afctee_vel.shape)
        afctee_mass = np.reshape(temp_mass, afctee_mass.shape)
        
        afctor_pos  = np.reshape(temp_apos, afctor_pos.shape)
        afctor_mass = np.reshape(temp_amass, afctor_mass.shape)
        
        afctee_pos_data = np.empty((0,3), float)
        for i in afctee_pos.flatten():
            afctee_pos_data = np.append(afctee_pos_data, i, axis = 0)
        
        ensemble = {'affectee position': afctee_pos,
                    'affectee position data': np.reshape(afctee_pos_data,
                                                         (self.n, 3, 1)),
                    'affector position': afctor_pos,
                    #'distance'      : distances(self.r, self.r),
                    'velocity'      : self.v,
                    #'velocity magnitude': LA.norm(self.v, axis = 1),
                    'affectee mass' : afctee_mass,
                    'affector mass' : afctor_mass,
                    'energy'        : None,
                    'energy data'   : None,
                    'number of objects': self.n,
                    'label'         : self.label,
                    'affect status' : self.affect_status,
                    'remaining'     : None,
                    'charge'        : self.q,
                    'sigma'         : self.sigma,
                    'epsilon'       : self.epsilon
                }
        return ensemble
        
        
    
    
def solar_system(cells_lims):
    cells, lims, cell_size = cells_lims
    SSG = StarSystemGenerator(cells, lims, cell_size)
    SSG.central_star()
    SSG.all_known_planets()
    
    ensemble = SSG.get_ensemble()
    #ensemble = energy.brute_kinetic_energy(ensemble)
    return ensemble
    
def random_solar_system():
    SSG = StarSystemGenerator()
    SSG.central_star()
    SSG.random_planets(10)
    #SSG.velocities_with_central_star()
    
    ensemble = SSG.get_ensemble()
    #ensemble = energy.brute_kinetic_energy(ensemble)
    return ensemble
        
def n_body_nice(cells_lims, num_planets = 10, num_asts = 200):
    cells, lims, cell_size = cells_lims
    SSG = StarSystemGenerator(cells, lims, cell_size)
    SSG.central_star()
    SSG.all_known_planets()
    SSG.random_asteroids(num = num_asts)
    
    ensemble = SSG.get_ensemble()
    return ensemble

def no_central_object(num_bodies = 10):
    MBG = many_bodies_generator(charge_init_and_spread = [1, 0])
    for i in range(num_bodies):
        MBG.make_body()
    return MBG.get_ensemble()


def lennard_jones_example(cells_lims, num_bodies = 10,
                          sig = 2e-2, eps = -4000):
    #rng.seed(1)
    cells, lims, cell_size = cells_lims
    MBG = many_bodies_generator(cells, lims, cell_size,
                                lennard_jones_sig_and_eps=[sig,eps])
    for i in range(num_bodies):
        MBG.make_body_uniform()
    return MBG.get_ensemble()

def particle_in_B(cells_lims):
    MBG = many_bodies_generator(*cells_lims, charge_init_and_spread=[-1,0])
    MBG.make_body_uniform(offset = [1,0,0], initial_velocity = [0,1,0],
                          initial_mass = 1)
    return MBG.get_ensemble()
    

def two_body_problem(cells_lims):
    MBG = many_bodies_generator(*cells_lims)
    MBG.make_body_uniform(offset = [1,0,0], initial_velocity = [0,1,0],
                          initial_mass = astcnst.G.value) 
    MBG.make_body_uniform(offset = [-1,0,0], initial_velocity = [0,-1,0],
                          initial_mass = astcnst.G.value)
    return MBG.get_ennsemble()

