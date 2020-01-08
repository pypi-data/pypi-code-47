"""
Contains free-standing global level functions for doing useful stuff
Created by adam on 11/14/16
"""
__author__ = 'adam'

from matplotlib import pylab as plt


def clearplot_function( ):
    """Clears the matplotlib plot to free system resources.
    Call in next cell after plot
    """
    try:
        plt.close( plt.gcf( ) )
        plt.close( 'all' )
    except:
        pass


def rotate_x_labels(axis, degrees=45):
    for tick in axis.get_xticklabels():
        tick.set_rotation(degrees)
