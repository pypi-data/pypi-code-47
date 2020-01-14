from .base_track import BaseTrack


class BigInteractTrack(BaseTrack):

    def __init__(self, interactDirectional=None, interactUp=None,
                 interactMultiRegion=None, maxHeightPixels=None, scoreMin=None, spectrum=None, **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.interactDirectional = interactDirectional
        self.interactUp = interactUp
        self.interactMultiRegion = interactMultiRegion
        self.maxHeightPixels = maxHeightPixels
        self.scoreMin = scoreMin
        self.spectrum = spectrum
