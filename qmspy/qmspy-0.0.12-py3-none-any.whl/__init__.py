"""
This is the qmspy module, a python module designed to automate graphing data
collected from a QMS.

Contains the following functions:
                init_data
                add_style
                fit_gaussians
                appearance_energy

Contains the following submodules:
                graph_data


Author: Brian C. Ferrari
"""
from .config            import *

from .add_style         import add_style
from .init_data         import init_data
from .fit_gaussians     import fit_gaussians
from .get_peaks         import get_peaks
from .appearance_energy import appearance_energy

from .graph_data        import *
