from .base_track import BaseTrack


class BigMafTrack(BaseTrack):

    def __init__(self, speciesOrder=None, frames=None, summary=None, **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.speciesOrder = speciesOrder
        self.frames = frames
        self.summary = summary
