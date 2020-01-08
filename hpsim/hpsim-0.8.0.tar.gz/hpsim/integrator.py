#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:24:16 2019

@author: hogbobson
"""
import numpy as np
from numpy import linalg as LA


def single_particle(ensemble):
    pass

def n_squared():
    pass


def n_body_nice(ensemble):
    afctor_pos = np.empty_like(ensemble['affectee position'])
    
    temp_pos   = afctor_pos.flatten()
    temp_r     = ensemble['affectee position'].flatten()
    temp_as    = ensemble['affect status'].flatten()
    
    for i in range(temp_pos.size):
        temp_pos[i] = temp_r[i][temp_as[i] <= 0]
    ensemble['affector position'] = np.reshape(temp_pos, afctor_pos.shape)
    
    return ensemble


def update_affector(ensemble):
    afctor_pos = np.empty_like(ensemble['affectee position'])
    
    temp_pos   = afctor_pos.flatten()
    temp_r     = ensemble['affectee position'].flatten()
    temp_as    = ensemble['affect status'].flatten()
    
    for i in range(temp_pos.size):
        af_stat = temp_as[i] <= 0
        temp_pos[i] = temp_r[i][af_stat]
    ensemble['affector position'] = np.reshape(temp_pos, afctor_pos.shape)
    
    return ensemble



# =============================================================================
# def particle_in_cell(ensemble, size_of_cell, max_loc_value):
#     """ 
#     Particle in cell is a function that makes sure the ensemble is
#     organized in the way the force function can use according to the particle-
#     in-cell principle. The inputs are as follows:
#         ensemble:       the ensemble, with plenty of information.
#         size_of_cell:   the cell must have a size, and this is where to define
#                         it.
#         max_loc_value:  PIC has implicit periodic boundary conditions, and 
#                         max_loc_value determines the maximum value a particle's
#                         coordinate can have before it's thrown to the other
#                         end.
#     """
#     num_cell_pr_axis = max_loc_value*2/size_of_cell
# =============================================================================
    

class ParticleInCell:
    def __init__(self, cells, lims):
        if np.inf in lims:
            raise("No infinites in PIC!")
        self.num_cells = cells.size
        
        if type(lims) == type(np.array(1)):
            arena_dims = np.size(lims)//2
            arena_size = np.empty(arena_dims)
            for i in range(arena_dims):
                arena_size[i] = lims[1 + 2*i] - lims[0 + 2*i]
        else:
            arena_size = 2*lims
        self.arena_size = arena_size


def _PIC_quick_append(F, F_temp, ax = 1, neg = 1):
    F_sum = neg*np.sum(F_temp, axis = ax)
    F_shp = np.append(F_sum.shape, 1).astype(int)
    F     = np.append(F, F_sum.reshape(F_shp), axis = 2)
    return F


def PIC_force(ensemble, *forces):
    n_cells    = ensemble['affectee position'].size
    n_pr_dim   = np.power(n_cells, 1/3)
    n          = int(n_pr_dim)
    
    afcte_pos  = ensemble['affectee position'].flatten()
    afctr_pos  = ensemble['affector position'].flatten()
    sigma      = ensemble['sigma']
    epsilon    = ensemble['epsilon']
    
    F_temp     = np.empty(np.append(afcte_pos.shape, 14), object)
    F          = np.empty_like(afcte_pos, object)
    
    for f in forces:
        for i in range(n_cells):
            #print("fcalc cell #" + str(i) + "/" + str(n_cells))
            p = 0 #neighbour counter
            F_temp[i][p] = f(afctr_pos[i], afcte_pos[i], sigma, epsilon)
            F[i] = np.sum(F_temp[i][p], axis = 1)
            fshp = np.append(F[i].shape, 1)
            F[i] = F[i].reshape(fshp)
            
            p += 1
            F_temp[i][p] = f(afctr_pos[(i+1)%n_cells], afcte_pos[i], 
                      sigma, epsilon)
            F[i] = _PIC_quick_append(F[i], F_temp[i][p])
            p += 1
            
            for j in [-1, 0, 1]:
                F_temp[i][p] = f(afctr_pos[(i+n+j)%n_cells], afcte_pos[i],
                          sigma, epsilon)
                F[i] = _PIC_quick_append(F[i], F_temp[i][p])
                p += 1
                
                for k in [-n, 0, n]:
                    F_temp[i][p] = f(afctr_pos[(i+n*n+k+j)%n_cells], 
                              afcte_pos[i], sigma, epsilon)
                    F[i] = _PIC_quick_append(F[i], F_temp[i][p])
                    p += 1
    
    for i in range(n_cells):
        #print("fsum cell #" + str(i) + "/" + str(n_cells))
        p = 1
        F[i] = _PIC_quick_append(F[i], F_temp[(i-1)%n_cells][p], 
                                 ax = 0, neg = -1)
        p += 1
        for j in [1, 0, -1]:
            F[i] = _PIC_quick_append(F[i], F_temp[(i-n+j)%n_cells][p],
                                     ax = 0, neg = -1)
            p += 1
            for k in [n, 0, -n]:
                F[i] = _PIC_quick_append(F[i], F_temp[(i-n*n+k+j)%n_cells][p],
                                         ax = 0, neg = -1)
                p += 1
        F[i] = np.sum(F[i], axis = 2)
    
    F = F.reshape(ensemble['affectee position'].shape)
    return F


def PIC_force_non_periodic(cell_indices, ensemble, *forces):
    n_cells    = ensemble['affectee position'].size
    n          = cell_indices[-1] # # of cells per dimension
    
    afcte_pos  = ensemble['affectee position'].flatten()
    afctr_pos  = ensemble['affector position'].flatten()
    sigma      = ensemble['sigma']
    epsilon    = ensemble['epsilon']
    
    center_indices     = cell_indices[0]
    other_indices      = cell_indices[1]
    neighbours         = cell_indices[2]
    neighbour_counters = cell_indices[3]
    
    F_temp     = np.empty(np.append(afcte_pos.shape, 14), object)
    F          = np.empty_like(afcte_pos, object)
    
    
    
    for f in forces:
        for i in center_indices:
            #print("fcalc cell #" + str(i) + "/" + str(n_cells))
            p = 0 #neighbour counter
            F_temp[i][p] = f(afctr_pos[i], afcte_pos[i], sigma, epsilon)
            F[i] = np.sum(F_temp[i][p], axis = 1)
            fshp = np.append(F[i].shape, 1)
            F[i] = F[i].reshape(fshp)
            
            p += 1
            F_temp[i][p] = f(afctr_pos[i+1], afcte_pos[i], 
                      sigma, epsilon)
            F[i] = _PIC_quick_append(F[i], F_temp[i][p])
            p += 1
            
            for j in [-1, 0, 1]:
                F_temp[i][p] = f(afctr_pos[i+n+j], afcte_pos[i],
                          sigma, epsilon)
                F[i] = _PIC_quick_append(F[i], F_temp[i][p])
                p += 1
                
                for k in [-n, 0, n]:
                    F_temp[i][p] = f(afctr_pos[i+n*n+k+j], 
                              afcte_pos[i], sigma, epsilon)
                    F[i] = _PIC_quick_append(F[i], F_temp[i][p])
                    p += 1
        
        for geo_ind, geo_nei, geo_pcnt in zip(other_indices, neighbours, 
                                  neighbour_counters):
            for ind, nei, pcnt in zip(geo_ind, geo_nei, geo_pcnt):
                for si in ind:
                    p = 0
                    temp = f(afctr_pos[si], afcte_pos[si], sigma, epsilon)
                    F_temp[si][p] = np.zeros_like(temp)
                    p += 1
                    temp = f(afctr_pos[(si+1)%n_cells], afcte_pos[si], 
                                       sigma, epsilon)
                    F_temp[si][p] = np.zeros_like(temp)
                    p += 1
                    for sj in [-1, 0, 1]:
                        temp = f(afctr_pos[(si+n+sj)%n_cells], afcte_pos[si], 
                                 sigma, epsilon)
                        F_temp[si][p] = np.zeros_like(temp)
                        p += 1
                        for sk in [-n, 0, n]:
                            temp = f(afctr_pos[(si+n*n+sk+sj)%n_cells],
                                               afcte_pos[si], 
                                     sigma, epsilon)
                            F_temp[si][p] = np.zeros_like(temp)
                            p += 1
                    
                    #THE FUCKING REST
                    F_temp[si][0] = f(afctr_pos[si], afcte_pos[si],
                                      sigma, epsilon)
                    F[si] = np.sum(F_temp[si][0], axis = 1)
                    fshp = np.append(F[si].shape, 1)
                    F[si] = F[si].reshape(fshp)
                    for ni, p in zip(nei[1:], pcnt[1:]):
                        F_temp[si][p] = f(afctr_pos[si+ni], afcte_pos[si],
                                          sigma, epsilon)
                        F[si] = _PIC_quick_append(F[si], F_temp[si][p])
    
    
    for i in range(n_cells):
        #print("fsum cell #" + str(i) + "/" + str(n_cells))
        p = 1
        F[i] = _PIC_quick_append(F[i], F_temp[(i-1)%n_cells][p], 
                                 ax = 0, neg = -1)
        p += 1
        for j in [1, 0, -1]:
            F[i] = _PIC_quick_append(F[i], F_temp[(i-n+j)%n_cells][p],
                                     ax = 0, neg = -1)
            p += 1
            for k in [n, 0, -n]:
                F[i] = _PIC_quick_append(F[i], F_temp[(i-n*n+k+j)%n_cells][p],
                                         ax = 0, neg = -1)
                p += 1
        F[i] = np.sum(F[i], axis = 2)
    
    F = F.reshape(ensemble['affectee position'].shape)
    return F

            
            
            

def PIC_get_non_periodic_box_indices(arena_out):
    cells         = arena_out[0]
    n_cells       = cells.size
    n_pr_dim      = np.power(n_cells, 1/3)
    n             = int(n_pr_dim)
    
    cell_indices  = np.arange(n_cells)
    cell_ind_shap = cell_indices.reshape(n,n,n)
    
    corner_iter = [0, n-1]
    corner_ind  = np.empty((0, 1))
    for i in corner_iter:
        for j in corner_iter:
            for k in corner_iter:
                corner_ind = np.append(corner_ind, 
                                       cell_ind_shap[i,j,k].reshape(1,1),
                                       axis = 0)
    #corner neighbour, number is indices in a 3x3x3 cube
    cn0  = [0, 1, n, n+1, n*n, n*n + 1, n*n + n, n*n + n + 1]
    cn2  = [0, n-1, n, n*n-1, n*n, n*n+n-1, n*n+n]
    cn6  = [0, 1, n*n-n, n*n-n+1, n*n, n*n+1]
    cn8  = [0, n*n-n-1, n*n-n, n*n-1, n*n]
    cn18 = [0, 1, n, n+1]
    cn20 = [0, n-1, n]
    cn24 = [0, 1]
    cn26 = [0]
    corner_neighbours = [cn0, cn2, cn6, cn8, cn18, cn20, cn24, cn26]
    
    cnp0  = [0,  1,  6, 10,  8, 12,  9, 13]
    cnp2  = [0,  2,  6,  4,  8,  5,  9]
    cnp6  = [0,  1,  7, 11,  8, 12]
    cnp8  = [0,  3,  7,  4,  8]
    cnp18 = [0,  1,  6, 10]
    cnp20 = [0,  2,  6]
    cnp24 = [0,  1]
    cnp26 = [0]
    corner_neighbour_counter = [cnp0, cnp2, cnp6, cnp8,
                                cnp18, cnp20, cnp24, cnp26]
    
    # Corner Givers, number is indices in a 3x3 cube
    cg0  = []
    cg2  = [-1]
    cg6  = [-n, -n+1]
    cg8  = [-1, -n-1, -n]
    cg18 = [-n*n, -n*n+1, -n*n+n, -n*n+n+1]
    cg20 = [-1, -n*n-1, -n*n, -n*n+n-1, -n*n+n]
    cg24 = [-n, -n+1, -n*n-n, -n*n-n+1, -n*n, -n*n+1]
    cg26 = [-1, -n-1, -n, -n*n-n-1, -n*n-n, -n*n-1, -n*n]
    
    cgp0  = []
    cgp2  = [1]
    cgp6  = []
    
    edge_ind = np.empty((0, n-2))
    for i in corner_iter:
        for j in corner_iter:
            edge_ind = np.append(edge_ind, cell_ind_shap[i,j,1:n-1].reshape(
                                                        1, n-2), axis = 0)
            edge_ind = np.append(edge_ind, cell_ind_shap[i,1:n-1,j].reshape(
                                                        1, n-2), axis = 0)
            edge_ind = np.append(edge_ind, cell_ind_shap[1:n-1,i,j].reshape(
                                                        1, n-2), axis = 0)
    #edge neighbour numbers are indices in a 3x3x3 cube
    en1  = [0, 1, n-1, n, n+1, n*n-1, n*n, n*n+1, n*n+n-1, n*n+n, n*n+n+1]
    en3  = [0, 1, n, n+1, n*n-n, n*n-n+1, n*n, n*n+1, n*n+n, n*n+n+1]
    en9  = [0, 1, n, n+1, n*n, n*n+1, n*n+n, n*n+n+1]
    en7  = [0, 1, n*n-n-1, n*n-n, n*n-n+1, n*n-1, n*n, n*n+1]
    en5  = [0, n-1, n, n*n-n-1, n*n-n, n*n-1, n*n, n*n+n-1, n*n+n]
    en11 = [0, n-1, n, n*n-1, n*n, n*n+n-1, n*n+n]
    en19 = [0, 1, n-1, n, n+1]
    en21 = [0, 1, n, n+1]
    en15 = [0, 1, n*n-n, n*n-n+1, n*n, n*n+1]
    en25 = [0, 1]
    en23 = [0, n-1, n]
    en17 = [0, n*n-n-1, n*n-n, n*n-1, n*n]
    edge_neighbours = [en1, en3, en9, en7, en5, en11, en19, en21, en15,
                       en25, en23, en17]
    
    enp1  = [0,  1,  2,  6, 10,  4,  8, 12,  5,  9, 13]
    enp3  = [0,  1,  6, 10,  7, 11,  8, 12,  9, 13]
    enp9  = [0,  1,  6, 10,  8, 12,  9, 13]
    enp7  = [0,  1,  3,  7, 11,  4,  8, 12]
    enp5  = [0,  2,  6,  3,  7,  4,  8,  5,  9]
    enp11 = [0,  2,  6,  4,  8,  5,  9]
    enp19 = [0,  1,  2,  6, 10]
    enp21 = [0,  1,  6, 10]
    enp15 = [0,  1,  7, 11,  8, 12]
    enp25 = [0,  1]
    enp23 = [0,  2,  6]
    enp17 = [0,  3,  7,  4,  8]
    edge_neighbour_counter = [enp1, enp3, enp9, enp7, enp5, enp11,
                              enp19, enp21, enp15, enp25, enp23, enp17]
    
    
    
    side_ind = np.empty((0,n*n-4*n+4))
    for i in corner_iter:
        side_ind = np.append(side_ind, 
                             cell_ind_shap[i,1:n-1,1:n-1].flatten().reshape(
                                         1, n*n - 4*n + 4), axis = 0)
        side_ind = np.append(side_ind,
                             cell_ind_shap[1:n-1,i,1:n-1].flatten().reshape(
                                         1, n*n - 4*n + 4), axis = 0)
        side_ind = np.append(side_ind,
                             cell_ind_shap[1:n-1,1:n-1,i].flatten().reshape(
                                         1, n*n - 4*n + 4), axis = 0)
    # Side neighbours. Numbers are indices in a 3x3x3 cube
    sn4  = [0, 1, n-1, n, n+1, n*n-n-1, n*n-n, n*n-n+1,
           n*n-1, n*n, n*n+1, n*n+n-1, n*n+n, n*n+n+1]
    sn10 = [0, 1, n-1, n, n+1, n*n-1, n*n, n*n+1, n*n+n-1, n*n+n, n*n+n+1]
    sn12 = [0, 1, n, n+1, n*n-n, n*n-n+1, n*n, n*n+1, n*n+n, n*n+n+1]
    sn22 = [0, 1, n-1, n, n+1]
    sn16 = [0, 1, n*n-n-1, n*n-n, n*n-n+1, n*n-1, n*n, n*n+1]
    sn14 = [0, n-1, n, n*n-n-1, n*n-n, n*n-1, n*n, n*n+n-1, n*n+n]
    side_neighbours = [sn4, sn10, sn12, sn22, sn16, sn14]
    
    snp4  = [0,  1,  2,  6, 10,  3,  7, 11,  4,  8, 12,  5,  9, 13]
    snp10 = [0,  1,  2,  6, 10,  4,  8, 12,  5,  9, 13]
    snp12 = [0,  1,  6, 10,  7, 11,  8, 12,  9, 13]
    snp22 = [0,  1,  2,  6, 10]
    snp16 = [0,  1,  3,  7, 11,  4,  8, 12]
    snp14 = [0,  2,  6,  3,  7,  4,  8,  5,  9]
    side_neighbour_counter = [snp4, snp10, snp12, snp22, snp16, snp14]
    
    neighbours = (corner_neighbours, edge_neighbours, side_neighbours)
    neighbour_counters = (corner_neighbour_counter, edge_neighbour_counter,
                          side_neighbour_counter)
    indices = (corner_ind.astype(int),
               edge_ind.astype(int),
               side_ind.astype(int))
    
    center_ind = cell_ind_shap[1:n-1,1:n-1,1:n-1].flatten()
    return (center_ind, indices, neighbours, 
            neighbour_counters, n)


def PIC_make_local_choords_once(arena_out):
    cells = arena_out[0]
    cell_size = arena_out[2]
    limits = arena_out[1]
    n_cells     = cells.size
    n_pr_dim    = np.power(n_cells, 1/3)
    n           = int(round(n_pr_dim))
    loc_choords = np.zeros(np.append(cells.shape, 3), float)
    
    for i in range(n):
        loc_choords[i,:,:,0] = np.arange(-limits, limits, cell_size) \
                                + cell_size/2
        loc_choords[:,i,:,1] = np.arange(limits, -limits, -cell_size) \
                                - cell_size/2
        loc_choords[:,:,i,2] = np.arange(limits, -limits, -cell_size) \
                                - cell_size/2
    return loc_choords.flatten()
    


def PIC_organize(ensemble, arena_out, loc_choords):
    cell_size = arena_out[2]
    
    n_cells    = ensemble['affectee position'].size
    n_pr_dim   = np.power(n_cells, 1/3)
    n          = int(round(n_pr_dim))
    
    
    
    afcte_pos  = ensemble['affectee position'].flatten()
    afctr_pos  = ensemble['affector position'].flatten()
    afcte_mass = ensemble['affectee mass'].flatten()
    afctr_mass = ensemble['affector mass'].flatten()
    afcte_vel  = ensemble['velocity'].flatten()
    afct_stat  = ensemble['affect status'].flatten()
    max_dist = LA.norm(np.ones(3)*cell_size/2)
    for i in range(n_cells):
        pos_loc_choords = afcte_pos[i] - loc_choords[i]
        #num_parts = afcte_pos[i].shape[0]
        outliers = np.where(LA.norm(pos_loc_choords) > max_dist)
        #num_rem_parts = outliers[0].shape[0]
        move_direcs  = np.floor(np.abs(pos_loc_choords[outliers][:])/max_dist)
        move_indices = np.sign(pos_loc_choords[outliers][:]) * move_direcs \
                        * [1, -n, -n*n]
        # TODO: MORE COMMENTS
        # TODO: ANY COMMENTS PLEASE
        move_indices = np.array([np.sum(move_indices)], int)%n_cells
        outlier_ite = np.array([x for x in outliers])
        outlier_ite = outlier_ite.reshape(outlier_ite.shape[::-1])
        for j, k in zip(move_indices, outlier_ite):
            afcte_pos[j]  = np.append(afcte_pos[j], afcte_pos[i][k,:],
                                     axis = 0)
            afctr_pos[j]  = np.append(afctr_pos[j], afctr_pos[i][k,:],
                                     axis = 0)
            afcte_mass[j] = np.append(afcte_mass[j], afcte_mass[i][k],
                                     axis = 0)
            afctr_mass[j] = np.append(afctr_mass[j], afctr_mass[i][k],
                                     axis = 0)
            afcte_vel[j]  = np.append(afcte_vel[j], afcte_vel[i][k,:],
                                     axis = 0)
            afct_stat[j]  = np.append(afct_stat[j], afct_stat[i][k],
                                     axis = 0)
        afcte_pos[i] = np.delete(afcte_pos[i], outliers, axis = 0)
        afctr_pos[i] = np.delete(afctr_pos[i], outliers, axis = 0)
        afcte_mass[i] = np.delete(afcte_mass[i], outliers, axis = 0)
        afctr_mass[i] = np.delete(afctr_mass[i], outliers, axis = 0)
        afcte_vel[i] = np.delete(afcte_vel[i], outliers, axis = 0)
        afct_stat[i] = np.delete(afct_stat[i], outliers, axis = 0)
    
    ensemble['affectee position'] = afcte_pos.reshape(
                                    ensemble['affectee position'].shape)
    ensemble['affector position'] = afctr_pos.reshape(
                                    ensemble['affector position'].shape)
    ensemble['affectee mass'] = afcte_mass.reshape(
                                    ensemble['affectee mass'].shape)
    ensemble['affector mass'] = afctr_mass.reshape(
                                    ensemble['affector mass'].shape)
    ensemble['velocity'] = afcte_vel.reshape(ensemble['velocity'].shape)
    ensemble['affect status'] = afct_stat.reshape(ensemble['affect status'].shape)
    return ensemble
        
    
            
            
    


# =============================================================================
# class ParticleInCell:
#     def __init__(self, size_of_cell, max_loc_value):
#         self.num_cell_pr_axis = max_loc_value*2/size_of_cell
#         self.max = max_loc_value
#         
#         self.n = int(self.num_cell_pr_axis)
#         self.size = size_of_cell
#         
#         self.cells = np.empty((self.n,self.n,self.n), dtype = object)
#         self.thing = [-1, 0, 1]
#         
#     
#     def particle_in_cell(ensemble, self):
#         # BEHOLD THE WORST LOOP OF THE CODE!
#         pos = np.copy(ensemble['affectee position'])
#         movers_minus = pos > self.max
#         movers_plus  = pos < -self.max
#         pos[movers_minus] -= 2*self.max
#         pos[movers_plus]  += 2*self.max
#         ensemble['affectee position'] = pos
#         for i in range(self.n):
#             for j in range(self.n):
#                 for k in range(self.n):
#                     self.cells[i,j,k] = pos[pos[:]//self.size == [i,j,k]]
#         
#         # And then - I was mistaken!
#         for i in range(len(ensemble['affector position'])):
#             box_of_i = ensemble['affectee position'][i]//self.size
#             x = box_of_i[0]
#             y = box_of_i[1]
#             z = box_of_i[2]
#             ensemble['affector position'][i] = np.empty((0,3))
#             for ii in self.thing:
#                 for jj in self.thing:
#                     for kk in self.thing:
#                         ensemble['affector position'][i] = np.append(ensemble[
#                                 'affector position'], self.cells[
#                                         int(x+ii)%self.n,
#                                         int(y+jj)%self.n,
#                                         int(z+kk)%self.n], axis=0)
#         return ensemble
# =============================================================================
