from .base_track import BaseTrack


class BigGenePredTrack(BaseTrack):

    def __init__(self, labelFields=None, defaultLabelFields=None,
                 labelSeparator=None, **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.labelFields = labelFields
        self.defaultLabelFields = defaultLabelFields
        self.labelSeparator = labelSeparator
