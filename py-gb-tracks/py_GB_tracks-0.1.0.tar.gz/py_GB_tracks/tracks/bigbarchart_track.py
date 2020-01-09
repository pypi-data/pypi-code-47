from .base_track import BaseTrack


class BigBarChartTrack(BaseTrack):

    def __init__(self, barChartBars=None, barChartColors=None,
                 barChartLabel=None, barChartMaxSize=None, barChartMetric=None,
                 barChartUnit=None, barChartMatrixUrl=None, barChartSampleUrl=None,
                 maxLimit=None, labelFields=None, defaultLabelFields=None, url=None,
                 urlLabel=None, urls=None, **kargs):
        '''
        '''
        super().__init__(**kargs)
        self.barChartBars = barChartBars
        self.barChartColors = barChartColors
        self.barChartLabel = barChartLabel
        self.barChartMaxSize = barChartMaxSize
        self.barChartMetric = barChartMetric
        self.barChartUnit = barChartUnit
        self.barChartMatrixUrl = barChartMatrixUrl
        self.barChartSampleUrl = barChartSampleUrl
        self.maxLimit = maxLimit
        self.labelFields = labelFields
        self.defaultLabelFields = defaultLabelFields
        self.url = url
        self.urlLabel = urlLabel
        self.urls = urls
