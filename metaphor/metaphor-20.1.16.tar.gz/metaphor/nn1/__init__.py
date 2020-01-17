"""Package nn1 api
"""
import sys, os
from metaphor.version import __version__

__modulepath__ = ""
def path():
    global __modulepath__
    if not __modulepath__:
        __modulepath__ = __path__[0]
    return __modulepath__

# filelist = []
# for val in sys.path:
#     if val.endswith('metaphor'):
#         for (dirpath, dirnames, filenames) in os.walk(val):
#             filelist.extend([os.path.join(dirpath, val) for val in filenames if val.startswith('services')])
#             break
# servicesList = filelist