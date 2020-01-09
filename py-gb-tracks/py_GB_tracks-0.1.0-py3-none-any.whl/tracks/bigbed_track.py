from .base_track import BaseTrack


class BigBedTrack(BaseTrack):

    def __init__(self, itemRgb=None, colorByStrand=None, denseCoverage=None,
                 labelOnFeature=None, exonArrows=None, exonNumbers=None, scoreFilter=None,
                 scoreFilterLimits=None, maxItems=None, maxWindowToDraw=None, minGrayLevel=None,
                 noScoreFilter=None, spectrum=None, scoreMax=None, scoreMin=None,
                 thickDrawItem=None, searchIndex=None, searchTrix=None, labelFields=None,
                 defaultLabelFields=None, labelSeparator=None, bedNameLabel=None,
                 exonArrowsDense=None, itemImagePath=None, itemBigImagePath=None,
                 linkIdInName=None, nextExonText=None, prevExonText=None, scoreLabel=None,
                 showTopScorers=None, **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.itemRgb = itemRgb
        self.colorByStrand = colorByStrand
        self.denseCoverage = denseCoverage
        self.labelOnFeature = labelOnFeature
        self.exonArrows = exonArrows
        self.exonNumbers = exonNumbers
        self.scoreFilter = scoreFilter
        self.scoreFilterLimits = scoreFilterLimits
        self.maxItems = maxItems
        self.maxWindowToDraw = maxWindowToDraw
        self.minGrayLevel = minGrayLevel
        self.noScoreFilter = noScoreFilter
        self.spectrum = spectrum
        self.scoreMax = scoreMax
        self.scoreMin = scoreMin
        self.thickDrawItem = thickDrawItem
        self.searchIndex = searchIndex
        self.searchTrix = searchTrix
        self.labelFields = labelFields
        self.defaultLabelFields = defaultLabelFields
        self.labelSeparator = labelSeparator
        self.bedNameLabel = bedNameLabel
        self.exonArrowsDense = exonArrowsDense
        self.itemImagePath = itemImagePath
        self.itemBigImagePath = itemBigImagePath
        self.linkIdInName = linkIdInName
        self.nextExonText = nextExonText
        self.prevExonText = prevExonText
        self.scoreLabel = scoreLabel
        self.showTopScorers = showTopScorers
