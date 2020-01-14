from .base_track import BaseTrack


class BigNarrowPeakTrack(BaseTrack):

    def __init__(self, pValueFilter=None, qValueFilter=None, signalFilter=None, **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.pValueFilter = pValueFilter
        self.qValueFilter = qValueFilter
        self.signalFilter = signalFilter
