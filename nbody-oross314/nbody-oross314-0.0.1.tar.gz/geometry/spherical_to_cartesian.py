import numpy as np
from nbody.geometry.vector_generator import vectors, anglebt, ztovec

#Outputs cartesian coordinates based on a set of standard spherical coordinates, r, theta, phi
def ptocartesian(r, theta, phi):
    bh_x = r * np.sin(theta) * np.cos(phi)
    bh_y = r * np.sin(theta) * np.sin(phi)
    bh_z = r * np.cos(theta)
    return bh_x, bh_y, bh_z

#Outputs cartesian coordiantes based on a radius, alpha and beta values and designed specifically for the velocity vector
def vtocartesian(bh_v, alpha, beta, position):       
    v_pre = bh_v * np.array([np.cos(beta), np.sin(beta), np.cos(alpha)])
    bh_vx, bh_vy, bh_vz = np.matmul(ztovec(position[0]), v_pre)
    return bh_vx, bh_vy, bh_vz