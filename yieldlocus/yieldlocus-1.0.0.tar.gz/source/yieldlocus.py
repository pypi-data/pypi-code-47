# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:14:53 2020

@author: Omkar
"""

import numpy as np
import matplotlib.pyplot

#x = np.linspace(-2,2,11)
#y = np.linspace(-2,2,11)
#(X,Y) = np.meshgrid(x,y)
#
#r0=1;
#r90=1;
#sig_yield=0.01;
#
#A = X**2 + (Y**2)*((r0*(1+r90))/((r0*(1+r90)))) - ((2*r0)/(1+r0))*X*Y - sig_yield
#
#matplotlib.pyplot.contour(X,Y,A,[1])
#matplotlib.pyplot.show()

def hill48(r0,r90,sig_yield):
    x = np.linspace(-2,2,11)
    y = np.linspace(-2,2,11)
    (X,Y) = np.meshgrid(x,y)
#    r0=1;
#    r90=1;
#    sig_yield=0.01;
    A = X**2 + (Y**2)*((r0*(1+r90))/((r0*(1+r90)))) - ((2*r0)/(1+r0))*X*Y - sig_yield
    matplotlib.pyplot.contour(X,Y,A,[1])
    matplotlib.pyplot.show()
    return;
    
    
    
    
    