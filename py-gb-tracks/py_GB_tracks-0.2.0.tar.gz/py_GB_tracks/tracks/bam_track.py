from .base_track import BaseTrack


class BamTrack(BaseTrack):

    def __init__(self, refUrl=None, bigDataIndex=None,
                 Related=None, bamColorMode=None, bamGrayMode=None, aliQualRange=None,
                 baseQualRange=None, bamColorTag=None, noColorTag=None,
                 bamSkipPrintQualScore=None, indelDoubleInsert=None, indelQueryInsert=None,
                 indelPolyA=None, minAliQual=None, pairEndsByName=None,
                 pairSearchRange=None, showNames=None, doWiggle=None, maxWindowToDraw=None,
                 **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.refUrl = refUrl
        self.bigDataIndex = bigDataIndex
        self.Related = Related
        self.bamColorMode = bamColorMode
        self.bamGrayMode = bamGrayMode
        self.aliQualRange = aliQualRange
        self.baseQualRange = baseQualRange
        self.bamColorTag = bamColorTag
        self.noColorTag = noColorTag
        self.bamSkipPrintQualScore = bamSkipPrintQualScore
        self.indelDoubleInsert = indelDoubleInsert
        self.indelQueryInsert = indelQueryInsert
        self.indelPolyA = indelPolyA
        self.minAliQual = minAliQual
        self.pairEndsByName = pairEndsByName
        self.pairSearchRange = pairSearchRange
        self.showNames = showNames
        self.doWiggle = doWiggle
        self.maxWindowToDraw = maxWindowToDraw

