import sys
from .spect import Spect


class SpectCaller(sys.modules[__name__].__class__):
    """Wrapper to make the module itself callable.

    See:
        - https://stackoverflow.com/questions/1060796/callable-modules
    """

    def __call__(self, obj):  # module callable
        return Spect(obj)


sys.modules[__name__].__class__ = SpectCaller
