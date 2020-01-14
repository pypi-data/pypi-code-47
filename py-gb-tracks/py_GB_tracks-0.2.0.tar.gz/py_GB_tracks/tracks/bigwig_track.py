from .base_track import BaseTrack


class BigWigTrack(BaseTrack):

    def __init__(self, autoScale=None, maxHeightPixels=None, viewLimits=None, viewLimitsMax=None,
                 alwaysZero=None, graphTypeDefault=None, maxWindowToQuery=None,
                 negateValues=None, smoothingWindow=None, transformFunc=None, windowingFunction=None,
                 yLineMark=None, yLineOnOff=None, gridDefault=None, **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.autoScale = autoScale
        self.maxHeightPixels = maxHeightPixels
        self.viewLimits = viewLimits
        self.viewLimitsMax = viewLimitsMax
        self.alwaysZero = alwaysZero
        self.graphTypeDefault = graphTypeDefault
        self.maxWindowToQuery = maxWindowToQuery
        self.negateValues = negateValues
        self.smoothingWindow = smoothingWindow
        self.transformFunc = transformFunc
        self.windowingFunction = windowingFunction
        self.yLineMark = yLineMark
        self.yLineOnOff = yLineOnOff
        self.gridDefault = gridDefault
