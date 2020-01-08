"""
Created by adam on 11/4/16
"""
__author__ = 'adam'


def clearplot( plotfunction, *args, **kwargs ):
    """Decorator to clears the matplotlib plot to free system resources before plotting."""
    from matplotlib import pyplot as plt

    def j( *args, **kwargs ):
        try:
            plt.close( plt.gcf() )
        except:
            pass
        try:
            plt.close( 'all' )
        except:
            pass

        plotfunction( *args, **kwargs )

    return j
