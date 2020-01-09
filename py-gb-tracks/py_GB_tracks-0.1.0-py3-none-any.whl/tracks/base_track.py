import logging
from ..meta import FileWriter


class BaseTrack(FileWriter):

    def __init__(self, track, data_type, shortLabel, longLabel, bigDataUrl,
                 html=None, visibility=None, meta=None, color=None,
                 priority=None, altColor=None, boxedCfg=None, chromosomes=None,
                 darkerLabels=None, dataVersion=None, directUrl=None, iframeUrl=None,
                 iframeOptions=None, mouseOverField=None, otherDb=None, pennantIcon=None,
                 tableBrowser=None, url=None, urlLabel=None, urls=None, skipEmptyFields=None,
                 skipFields=None, sepFields=None, parent=None, superTrack=None):
        '''
        '''
        self.track = track
        self.superTrack = superTrack
        self.parent = parent
        self.type = data_type
        self.shortLabel = shortLabel
        self.longLabel = longLabel
        self.bigDataUrl = bigDataUrl
        self.html = html
        self.visibility = visibility
        self.meta = meta
        self.color = color
        self.priority = priority
        self.altColor = altColor
        self.boxedCfg = boxedCfg
        self.chromosomes = chromosomes
        self.darkerLabels = darkerLabels
        self.dataVersion = dataVersion
        self.directUrl = directUrl
        self.iframeUrl = iframeUrl
        self.iframeOptions = iframeOptions
        self.mouseOverField = mouseOverField
        self.otherDb = otherDb
        self.pennantIcon = pennantIcon
        self.tableBrowser = tableBrowser
        self.url = url
        self.urlLabel = urlLabel
        self.urls = urls
        self.skipEmptyFields = skipEmptyFields
        self.skipFields = skipFields
        self.sepFields = sepFields
