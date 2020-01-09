from .base_track import BaseTrack


class BigChainTrack(BaseTrack):

    def __init__(self, linkDataUrl=None, **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.linkDataUrl = linkDataUrl
