# Standard Library
from functools import reduce # For plotting inequalities

# Third Party
import numpy as np
import sympy as sp
from scipy.stats import norm as normal # For z-table
import matplotlib.pyplot as plt # For plotting inequalities


import matplotlib.ticker as ticker
# Override MultipleLocator to remove tick labels at zero
def tick_values(self, vmin, vmax):
    if vmax < vmin:
        vmin, vmax = vmax, vmin
    step = self._edge.step
    vmin = self._edge.ge(vmin) * step
    n = (vmax - vmin + 0.001 * step) // step
    locs = vmin - step + np.arange(n + 3) * step
    locs = [i for i in locs if i != 0]
    return self.raise_if_exceeds(locs)
ticker.MultipleLocator.tick_values = tick_values

def set_cartesian_plane(axes, xmin=-11.5, xmax=11.5, ymin=-11.5, ymax=11.5, multiples_of=5):
    """Styles a Matplotlib.Axes object to that of a textbook cartesian plane"""

    ax = axes
    # Center the axes on the origin
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    # Set the min/max of the axes
    ax.axis([xmin, xmax, ymin, ymax])
    # Set the tick marks
    ax.minorticks_on()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
    #########################
    # There were multiple issues with matplotlib's gridlines
    # - The x-minor gridlines ignore their z-order and were graphed on top of everything including the text labels
    # - The x-minor gridlines did not appear outside of the vertical range of the plotted lines
    #
    # SOLUTION: Plot gridlines manually
    #########################
    # Set the grid
    minorticks = ax.xaxis.get_minorticklocs()
    for tick in minorticks:
        ax.arrow(xmin, tick,
                 xmax*2, 0,
                 head_width=0.0,
                 head_length=0.0,
                 length_includes_head=False,
                 color=(0.5,0.5,0.5),
                 zorder=1,
                )
    for tick in minorticks:
        ax.arrow(tick, ymin,
                 0, ymax*2,
                 head_width=0.0,
                 head_length=0.0,
                 length_includes_head=False,
                 color=(0.5,0.5,0.5),
                 zorder=1,
                )
    majorticks = ax.xaxis.get_majorticklocs()
    for tick in majorticks:
        ax.arrow(xmin, tick,
                 xmax*2, 0,
                 head_width=0.0,
                 head_length=0.0,
                 length_includes_head=False,
                 color=(0.3,0.3,0.3),
                 zorder=1,
                )
    for tick in majorticks:
        ax.arrow(tick, ymin,
                 0, ymax*2,
                 head_width=0.0,
                 head_length=0.0,
                 length_includes_head=False,
                 color=(0.3,0.3,0.3),
                 zorder=1,
                )
    #########################

    # Draw and label the x- and y-axis with arrowheads
    ax.set_xlabel('$x$', usetex=True, position=(1,0), fontsize='x-large')
    ax.arrow(xmin, 0,
             xmax*2, 0,
             head_width=0.5,
             head_length=0.5,
             length_includes_head=True,
             color='black',
             zorder=5,
            )
    ax.set_ylabel('$y$', usetex=True, position=(0,1), fontsize='x-large')
    ax.arrow(0, ymin,
             0, ymax*2,
             head_width=0.5,
             head_length=0.5,
             length_includes_head=True,
             color='black',
             zorder=5,
            )
    ax.set_aspect('equal')

def plot_inequalities(K, R, B):
    # Construct the inequalities
    ineqs = []
    x, y = sp.symbols('x y')
    X = sp.Matrix([x, y])
    for expr, r, b in zip(K*X, R, B):
        ineqs.append(r(expr, b))
    # Construct the boundary equations for plotting
    boundaries = []
    for expr, b in zip(K*X, B):
        eq = sp.Eq(expr, b)
        solved = sp.solve(eq, y)
        boundaries.append(solved[0])


    ################## Plot ###########
    # Set the axes limits
    xmin = -11.5
    xmax = 11.5
    ymin = -11.5
    ymax = 11.5

    # Plot the solution set
    p = sp.plot_implicit(reduce(sp.And, ineqs), (x, xmin, xmax), (y, ymin, ymax), show=False)
    p[0].line_color = (0.7, 0.7, 0.7)
    # Plot the boundary equations
    for eq in boundaries:
        p_next = sp.plot(eq, (x, xmin, xmax), show=False)
        p_next[0].line_color = 'black'
        p.append(p_next[0])
    plot = p.backend(p)
    plot.process_series()
    fig = plot.fig
    ax = plot.ax[0]
    set_cartesian_plane(ax)

    # Save the plot as a PDF file
    fig.savefig('key_plot.pdf', dpi=80, bbox_inches="tight")

    # Create a blank cartesian plane for the student
    blank_fig, blank_ax = plt.subplots()
    set_cartesian_plane(blank_ax)
    blank_fig.savefig('blank_plot.pdf', dpi=80, bbox_inches="tight")

def partition_set(E, size):
    # Partitions the set E into 'size' non-empty subsets of random length
    if size > len(E):
        raise ValueError('Size cannot be greater than the length of the set.')

    # Randomly select the sizes of the partitions
    cuts = sorted(np.random.choice(range(1,len(E)), size = size - 1, replace = False))
    sizes = [cuts[i] - cuts[i - 1] for i in range(len(cuts))]
    sizes[0] = cuts[0]

    partitions = []
    for size in sizes:
        # Select a random subset from E of length size
        random_subset = set([E.pop() for i in range(size)])
        partitions.append(random_subset)
    partitions.append(E)

    return partitions

def get_set_tex(E):
    elements = ', '.join(map(str, E))
    return r'\{{ {0} \}}'.format(elements)

def rand_nonzero(mag_of_entries: int, size: tuple):
    """Returns a size-tuple with random integer entries where 0 < abs(entries) <= magnitude"""

    coeff = [c for c in range(-mag_of_entries, mag_of_entries+1) if c != 0]
    entries = np.random.choice(coeff, size=size, replace=False)
    return entries

############################### NOT USED YET
class Ztable(object):
    def __init__(self):
        pass

    def get_prob(self, z):
        z = round(z, 2)
        if z > 3.49:
            return 1.0
        elif z < -3.49:
            return 0.0
        else:
            return round(normal.cdf(z, 0, 1), 4)

    def get_zscore(self, p):
        p = round(p, 4)
        return round(normal.ppf(p, 0, 1), 2)

def get_finite_dist(count, precision):
    # Returns a finite probability distribution
    # Returns a finite list, P, of 'count' probabilities rounded to 'precision' decimal places such that sum(P) = 1
    cuts = np.sort(np.random.choice(range(1, 10**precision), size = count - 1, replace = False)/10**precision)
    P = np.zeros(count)
    for i in range(0, count - 1):
        P[i] = cuts[i] - np.sum(P)
    P[-1] = 1 - np.sum(P)
    return P