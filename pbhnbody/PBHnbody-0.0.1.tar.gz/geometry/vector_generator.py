import nbody
import numpy as np
from nbody.geometry.patch import SphericalPatch
from nbody.geometry import sample
from nbody.constants import EARTH_MASS, SECOND, KM, PULSAR_MASS, COMPANION_MASS, BINARY_A, BINARY_E
import PDRandom
import io
import sys

#Outputs the angle between 2 vectors
def anglebt(v1, v2):
    normalize = (np.linalg.norm(v1)*np.linalg.norm(v2))
    if normalize:
        angle = np.arccos(np.dot(v1.T, v2) / normalize)
    else: angle = 0
    return angle

#Defines a transformation matrix that shifts the z axis to the given vector
def ztovec(vector):
    #Shift velocity cone to be centered around the position vector
    z_axis = np.array([0,0,1])
    xy_perp = np.cross(vector, z_axis)
    if not (xy_perp[0] and xy_perp[1]):
        trans_mat = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        return trans_mat
    init_mat = np.asarray([
            z_axis,
            [- vector[0], - vector[1], vector[2]],
            xy_perp
        ]).T

    fin_mat = np.asarray([
            vector,
            z_axis,
            xy_perp
        ]).T
    trans_mat = np.matmul(fin_mat, np.linalg.inv(init_mat))
    return trans_mat
    
#Outputs position and velocity vectors
def vectors(radius = 20, cutoff = 520, maxangle = np.pi/8, pts = 1, flat = False,):
    velocity = []
    
    #Define Maxwell-Boltzmann probability     
    def MB(x):
        a = 110 * np.sqrt(2) * KM / SECOND
        Prob = np.sqrt(2/np.pi) * 1/a**3 * x**2 * np.exp(- x**2 / (2 * a**2))
        return Prob
    
    #disable print output for PDRandom
    class NullWriter(object):
        def write(self, arg):
            pass

    nullwrite = NullWriter()
    oldstdout = sys.stdout
    sys.stdout = nullwrite # disable output

    #establish random Maxwell Botlzmann distribution
    gen = PDRandom.PDRandom(MB, 0 , cutoff * KM / SECOND, 10, dimension=1)
        
    #re-enable outputs
    sys.stdout = oldstdout
    
    #define a sphere of position vectors
    sphere = SphericalPatch(0, np.pi, -np.pi, np.pi)

    #pick one and scale
    position_vector = sample.spherical_sample(sphere, pts)
    position = (radius * position_vector)

    #Defines velocity cone
    velocity_cone = SphericalPatch(0, np.sin(maxangle), -np.pi, np.pi)
    
    z_axis = np.array([0,0,1])
    
    for i in range(pts):
        
        #pick one from the MB distribution or a flat distribution
        if flat == False:
            velocity_scale = gen.Next()
        else: 
            velocity_scale = np.random.random() * cutoff
            
        #Shift velocity cone to be centered around the position vector
        trans_mat = - ztovec(position_vector[i])
        velocity_vector = np.matmul(trans_mat, sample.spherical_sample(velocity_cone, 1).T).T[0]

        #scale
        velocity = velocity_scale * velocity_vector
        #velocity.append(velocity_scale * velocity_vector)
    
    return position, np.stack(velocity)