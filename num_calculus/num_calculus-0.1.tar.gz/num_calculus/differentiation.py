""" 
Exercise 5: Calculate the first derivative of a function
"""

import numpy as np


def first_derivative( function, x, dx ):
    # returns the frist derivative of a given function
    
    # function: function of x
    # x       : position to derivate
    # dx      : distance away from x
    
 
    invA = np.matrix([[0.5,-0.5],
                   [1  , 1  ]])
                   
    b = np.matrix([[function(x+dx)-function(x)],
                   [function(x-dx)-function(x)]])
    
    x = invA*b

    # pick the first one for first derivative
    return x.item(1) / dx
