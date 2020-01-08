from .._swatches import _swatches
from .._colormaps import _linear3color

def swatches():
    return _swatches(__name__, globals())

swatches.__doc__ = _swatches.__doc__

dcatRodGul = _linear3color("#C86151", "#FFA733", "#FFD81A")
dcatGrønn = _linear3color("#38A161", "#77A186", "#A3AA6F")
dcatBlåFiolet = _linear3color("#3385D1", "#337C9B", "#826BA1")
dcatRodGronn = _linear3color("#C86151", "#38A161", "#A3AA6F")
dcatLysBlaMorkBla = _linear3color("#3385D1", "#66A4DC", "#CCE1F3")






   
