#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:46:43 2019

@author: hogbobson
"""

import numpy as np
import h5py
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import pyplot as plt
from matplotlib import animation


def save_to_hdf5(data, name, groups, group_rows):
    fname = name + '.hdf5'
    with h5py.File(fname, 'w') as f:
        for gname, grows in zip(groups, group_rows):
            f.create_dataset(gname, data = data[grows,:,:])
    


def no_plot(a, b):
    return None


def standard_plot(everything):
    ensemble = everything['ensemble']
    n = ensemble['number of objects']
    plt.figure(num = 0, figsize = (8,8))
    for i in range(n):
        plt.plot(ensemble['affectee position data'][i,0,:], 
                 ensemble['affectee position data'][i,1,:], '-',
                 label = ensemble['label'][i],
                 color = (abs(np.sin(i)), 0 + i/n, 1-i/n))
    plt.xlabel('x')
    plt.ylabel('y')
    xlim = np.max(ensemble['affectee position data'])*1.1
    #xlim = 5*1e11
    plt.axis((-xlim, xlim, -xlim, xlim))
    plt.legend()
    plt.show()
    return None


def mkfile(data, name):
    fname = name + '.hdf5'
    f = h5py.File(fname, 'w')
    f.create_dataset(name, data = data)
    f.close()
    

def simple_2d_anim(ensemble, stps):
    data = ensemble['affectee position data']
    nobjs = ensemble['number of objects']
    nsteps = int(stps/20)
    labels = ensemble['label']
    
    fig, ax = plt.subplots(figsize = (8,8))
    lim = np.max(abs(data))*1.2
    if lim > 1e13:
        lim = 2e12
    
    x = data[:,0,:]
    y = data[:,1,:]
    
    x_start = data[:,0,0]
    y_start = data[:,1,0]
    
    
    
    #s = np.empty(nobjs)
    #s[0] = 10
    #s[1:7] = 2
    #s[8:] = 0.5
    s = np.ones(nobjs)*3
    
    if np.size(labels) == nobjs:
        lines = [ax.plot(x_start[j], y_start[j], 'o', ms = s[j] )[0] \
             for j in range(int(nobjs))]
    else:
        lines = [ax.plot(x_start[j], y_start[j], 'o', ms = s[j])[0] \
             for j in range(int(nobjs))]
    
# =============================================================================
#         lines = []
#         lines.append(ax.plot(x_start[0], y_start[0], 'o', c='y', ms=8))
#         for i in np.arange(1,5):
#             lines.append(ax.plot(x_start[i], y_start[i], 'o', c='g', ms=3))
#         for j in np.arange(5,nobjs):
#             lines.append(ax.plot(x_start[j], y_start[j], '.', c='b', ms=1))
# =============================================================================
    
    ax.set_xlim([-lim, lim])
    ax.set_xlabel('x [m]')
    ax.set_ylim([-lim, lim])
    ax.set_ylabel('y [m]')
    ax.legend()
    
    
    def animate(i, x, y, lines):
        for line, p in zip(lines, range(int(nobjs))):
            line.set_xdata(x[p,i])
            line.set_ydata(y[p,i])
        return lines
    
    
    
    ani = animation.FuncAnimation(fig, animate, np.arange(0,nsteps-1), \
                                  fargs = (x, y, lines), \
                                  interval = 4)
    
    plt.draw()
    
    #ani.save('yolo.MPEG', writer = 'ffmpeg')
    return ani
    
def simple_3d_anim(ensemble, stps):
    def update_points(num, dataLines, sub):
        sub.clear()
        sub.scatter(
                np.array(dataLines[0])[0,num],
                np.array(dataLines[0])[1,num],
                np.array(dataLines[0])[2,num],
                s=100,
                marker='o',
                c='yellow'
                )
        
        sub.scatter(
                np.array(dataLines[1:4])[:,0,num],
                np.array(dataLines[1:4])[:,1,num],
                np.array(dataLines[1:4])[:,2,num],
                s=5,
                marker='o',
                c='blue'
                )
        
        sub.scatter(
                np.array(dataLines[5:])[:,0,num],
                np.array(dataLines[5:])[:,1,num],
                np.array(dataLines[5:])[:,2,num],
                s=.1,
                marker='.',
                c='green'
                )
        
        sub.set_xbound(-sub.xm, sub.xm)
        sub.set_ybound(-sub.ym, sub.ym)
        sub.set_zbound(-sub.zm, sub.zm)
    
        
        
        
        

    # Attaching 3D axis to the figure
    fig = plt.figure()
    sub = fig.add_subplot(111, projection = '3d')
    
    
    data = ensemble['affectee position data']
    numobjs = ensemble['number of objects']
    numstps = stps
    
    datalines = [data[i] for i in range(int(numobjs))]
    print(np.shape(datalines))
    
    
    
    lim = np.max(data)
    if lim > 1e13:
        lim = 2e13
    if lim == np.inf or lim == np.nan:
        lim = 2e13
    
    sub.xm = lim
    sub.ym = lim
    sub.zm = lim
# =============================================================================
#     # Setting the axes properties
#     ax.set_xlim3d([-lim, lim])
#     ax.set_xlabel('X')
#     
#     ax.set_ylim3d([-lim, lim])
#     ax.set_ylabel('Y')
#     
#     ax.set_zlim3d([-lim, lim])
#     ax.set_zlabel('Z')
# =============================================================================
    
    #ax.set_title('3D Test')
    
    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update_points, numstps, \
                                       fargs=(datalines, sub), \
                                       interval=34)
    line_ani.save('yolo.gif', writer='imagemagick', fps=30)
    
    print('hello')
    
    
    return None