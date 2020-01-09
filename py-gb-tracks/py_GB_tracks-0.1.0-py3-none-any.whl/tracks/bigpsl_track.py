from .base_track import BaseTrack


class BigPslTrack(BaseTrack):

    def __init__(self, baseColorUseCds=None, baseColorUseSequence=None,
                 baseColorDefault=None, showDiffBasesAllScales=None, labelFields=None,
                 defaultLabelFields=None, labelSeparator=None, **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.baseColorUseCds = baseColorUseCds
        self.baseColorUseSequence = baseColorUseSequence
        self.baseColorDefault = baseColorDefault
        self.showDiffBasesAllScales = showDiffBasesAllScales
        self.labelFields = labelFields
        self.defaultLabelFields = defaultLabelFields
        self.labelSeparator = labelSeparator
