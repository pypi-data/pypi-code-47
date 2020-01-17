from metaphor.version_nntoolbox import __version__
import os

def version(): return __version__


__modulepath__ = ""
def path():
    global __modulepath__
    if not __modulepath__:
        __modulepath__ = __path__[0]
    return __modulepath__
parentdir = os.path.dirname(path())
