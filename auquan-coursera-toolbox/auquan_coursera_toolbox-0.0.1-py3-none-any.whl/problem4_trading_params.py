from backtester.trading_system_parameters import TradingSystemParameters
from backtester.features.feature import Feature
from datetime import timedelta
from backtester.dataSource.csv_data_source import CsvDataSource
from backtester.timeRule.custom_time_rule import CustomTimeRule
from backtester.executionSystem.simple_execution_system import SimpleExecutionSystem
from backtester.orderPlacer.backtesting_order_placer import BacktestingOrderPlacer
from backtester.trading_system import TradingSystem
from backtester.version import updateCheck
from backtester.constants import *
from backtester.features.feature import Feature
import pandas as pd
import numpy as np
import os



PAIRIDS = {1 : ['AAPL', 'GOOG'],
           2 : ['ADBE', 'MSFT']}

instrumentIds = ['AAPL', 'ADBE', 'GOOG', 'MSFT']


class MyCustomFeature(Feature):
    ''''
    Custom Feature to implement for instrument. This function would return the value of the feature you want to implement.
    1. create a new class MyCustomFeatureClassName for the feature and implement your logic in the function computeForInstrument() -
    2. modify function getCustomFeatures() to return a dictionary with Id for this class
        (follow formats like {'my_custom_feature_identifier': MyCustomFeatureClassName}.
        Make sure 'my_custom_feature_identifier' doesnt conflict with any of the pre defined feature Ids
        def getCustomFeatures(self):
            return {'my_custom_feature_identifier': MyCustomFeatureClassName}
    3. create a dict for this feature in getInstrumentFeatureConfigDicts() above. Dict format is:
            customFeatureDict = {'featureKey': 'my_custom_feature_key',
                                'featureId': 'my_custom_feature_identifier',
                                'params': {'param1': 'value1'}}
    You can now use this feature by calling it's featureKey, 'my_custom_feature_key' in getPrediction()
    '''
    @classmethod
    def computeForInstrument(cls, updateNum, time, featureParams, featureKey, instrumentManager):
        # Custom parameter which can be used as input to computation of this feature
        param1Value = featureParams['param1']

        # A holder for the all the instrument features
        lookbackInstrumentFeatures = instrumentManager.getLookbackInstrumentFeatures()

        # dataframe for a historical instrument feature (basis in this case). The index is the timestamps
        # atmost upto lookback data points. The columns of this dataframe are the stocks/instrumentIds.
        lookbackInstrumentValue = lookbackInstrumentFeatures.getFeatureDf('stockVWAP')

        # The last row of the previous dataframe gives the last calculated value for that feature (basis in this case)
        # This returns a series with stocks/instrumentIds as the index.
        currentValue = lookbackInstrumentValue.iloc[-1]

        if param1Value == 'value1':
            return currentValue * 0.1
        else:
            return currentValue * 0.5


class MyTradingParams(TradingSystemParameters):
    '''
    initialize class
    place any global variables here
    '''
    def __init__(self, tradingFunctions):
        self.__tradingFunctions = tradingFunctions
        super(MyTradingParams, self).__init__()
        self.__dataSetId = 'trainingW9_trainingData'
        self.__instrumentIds = self.__tradingFunctions.getSymbolsToTrade()
        self.__startDate = '2017/03/31'
        self.__endDate = '2017/07/12'
        self.__capitalMultiplier = 10


    '''
    Returns an instance of class DataParser. Source of data for instruments
    '''

    def getDataParser(self):
        instrumentIds = self.__tradingFunctions.getSymbolsToTrade()
        return CsvDataSource(cachedFolderName='historicalData/',
                             dataSetId=self.__dataSetId,
                             instrumentIds=instrumentIds,
                             downloadUrl = 'https://raw.githubusercontent.com/Auquan/auquan-historical-data/master/qq2Data/',
                             timeKey = '',
                             timeStringFormat = '%Y-%m-%d %H:%M:%S',
                             startDateStr=self.__startDate,
                             endDateStr=self.__endDate,
                             liveUpdates=True,
                             pad=True)

    '''
    Returns an instance of class TimeRule, which describes the times at which
    we should update all the features and try to execute any trades based on
    execution logic.
    For eg, for intra day data, you might have a system, where you get data
    from exchange at a very fast rate (ie multiple times every second). However,
    you might want to run your logic of computing features or running your execution
    system, only at some fixed intervals (like once every 5 seconds). This depends on your
    strategy whether its a high, medium, low frequency trading strategy. Also, performance
    is another concern. if your execution system and features computation are taking
    a lot of time, you realistically wont be able to keep upto pace.
    '''
    def getTimeRuleForUpdates(self):
        return CustomTimeRule(startDate=self.__startDate, endDate=self.__endDate, startTime='9:30', endTime='15:30', frequency='M', sample='30')

    '''
    Returns a timedetla object to indicate frequency of updates to features
    Any updates within this frequncy to instruments do not trigger feature updates.
    Consequently any trading decisions that need to take place happen with the same
    frequency
    '''

    def getFrequencyOfFeatureUpdates(self):
        return timedelta(0, 30)  # minutes, seconds

    def getStartingCapital(self):
        return 2000*self.__capitalMultiplier

    '''
    This is a way to use any custom features you might have made.
    Returns a dictionary where
    key: featureId to access this feature (Make sure this doesnt conflict with any of the pre defined feature Ids)
    value: Your custom Class which computes this feature. The class should be an instance of Feature
    Eg. if your custom class is MyCustomFeature, and you want to access this via featureId='my_custom_feature',
    you will import that class, and return this function as {'my_custom_feature': MyCustomFeature}
    '''

    def getCustomFeatures(self):
        return {'my_custom_feature': MyCustomFeature,
                'prediction': TrainingPredictionFeature,
                'spread': SpreadCalculator,
                'fees_and_spread': FeesCalculator,
                'benchmark_PnL': BuyHoldPnL}


    def getInstrumentFeatureConfigDicts(self):
        # ADD RELEVANT FEATURES HERE

        predictionDict = {'featureKey': 'prediction',
                                'featureId': 'prediction',
                                'params': {'tradingFunctions':self.__tradingFunctions}}
        spreadConfigDict = {'featureKey': 'spread',
                            'featureId': 'spread',
                            'params': {'instrbid': 'Bid Price',
                                       'instrask': 'Ask Price'}}
        feesConfigDict = {'featureKey': 'fees',
                          'featureId': 'fees_and_spread',
                          'params': self.setFees()}
        profitlossConfigDict = {'featureKey': 'pnl',
                                'featureId': 'pnl',
                                'params': {'price': self.getPriceFeatureKey(),
                                           'fees': 'fees'}}
        capitalConfigDict = {'featureKey': 'capital',
                             'featureId': 'capital',
                             'params': {'price': 'stockVWAP',
                                        'fees': 'fees',
                                        'capitalReqPercent': 0.95}}
        benchmarkDict = {'featureKey': 'benchmark',
                     'featureId': 'benchmark_PnL',
                     'params': {'pnlKey': 'pnl'}}

        scoreDict = {'featureKey': 'score',
                     'featureId': 'benchmark_PnL',
                     'params': {'pnlKey': 'pnl'}}

        stockFeatureConfigs = self.__tradingFunctions.getInstrumentFeatureConfigDicts()


        return {INSTRUMENT_TYPE_STOCK: stockFeatureConfigs + [predictionDict,
        spreadConfigDict, feesConfigDict,profitlossConfigDict,capitalConfigDict,benchmarkDict, scoreDict]}

    '''
    Returns an array of market feature config dictionaries
        market feature config Dictionary has the following keys:
        featureId: a string representing the type of feature you want to use
        featureKey: a string representing the key you will use to access the value of this feature.this
        params: A dictionary with which contains other optional params if needed by the feature
    '''

    def getMarketFeatureConfigDicts(self):
    # ADD RELEVANT FEATURES HERE
        scoreDict = {'featureKey': 'score',
                     'featureId': 'score_ll',
                     'params': {'featureName': self.getPriceFeatureKey(),
                                'instrument_score_feature': 'benchmark'}}

        marketFeatureConfigs = self.__tradingFunctions.getMarketFeatureConfigDicts()
        return marketFeatureConfigs + [scoreDict]


    def getPrediction(self, time, updateNum, instrumentManager):

        predictions = pd.Series(index = self.__instrumentIds)

        predictions = self.__tradingFunctions.getPrediction(time, updateNum, instrumentManager, predictions)

        return predictions

    '''
    Returns the type of execution system we want to use. Its an implementation of the class ExecutionSystem
    It converts prediction to intended positions for different instruments.
    '''

    def getExecutionSystem(self):
        return SimpleExecutionSystem(enter_threshold=0.7,
                                    exit_threshold=0.55,
                                    longLimit=10000,
                                    shortLimit=10000,
                                    capitalUsageLimit=0.10 * self.getStartingCapital(),
                                    enterlotSize = 10000, exitlotSize = 10000,
                                    limitType='D', price='stockVWAP')

    '''
    Returns the type of order placer we want to use. its an implementation of the class OrderPlacer.
    It helps place an order, and also read confirmations of orders being placed.
    For Backtesting, you can just use the BacktestingOrderPlacer, which places the order which you want, and automatically confirms it too.
    '''

    def getOrderPlacer(self):
        return BacktestingOrderPlacer()

    '''
    Returns the amount of lookback data you want for your calculations. The historical market features and instrument features are only
    stored upto this amount.
    This number is the number of times we have updated our features.
    '''

    def getLookbackSize(self):
        return 360

    def getPriceFeatureKey(self):
        return 'stockVWAP'

    def getDataSetId(self):
        return self.__dataSetId

    def setDataSetId(self, dataSetId):
        self.__dataSetId = dataSetId

    def getInstrumentsIds(self):
        return self.__instrumentIds

    def setFees(self):
        return {'brokerage': 0.0001,'spread': 'spread'}

    def setCapital(self, capital=5000):
        self.__capitalMultiplier = capital

    def getCapital(self):
        return self.__capitalMultiplier

    def getStartDate(self):
        return self.__startDate

    def getEndDate(self):
        return self.__endDate

    def setStartDate(self, date):
        self.__startDate = date

    def setEndDate(self, date):
        self.__endDate = date

class TrainingPredictionFeature(Feature):

    @classmethod
    def computeForInstrument(cls, updateNum, time, featureParams, featureKey, instrumentManager):

        tf = featureParams['tradingFunctions']
        predictions = tf.getPrediction(time, updateNum, instrumentManager, pd.Series(index = tf.getSymbolsToTrade()))

        return predictions


class SpreadCalculator(Feature):

    @classmethod
    def computeForInstrument(cls, updateNum, time, featureParams, featureKey, instrumentManager):
        instrumentLookbackData = instrumentManager.getLookbackInstrumentFeatures()
        try:
            currentStockBidPrice = instrumentLookbackData.getFeatureDf(featureParams['instrbid']).iloc[-1]
            currentStockAskPrice = instrumentLookbackData.getFeatureDf(featureParams['instrask']).iloc[-1]
        except KeyError:
            logError('Bid and Ask Price Feature Key does not exist')

        currentSpread = currentStockAskPrice - currentStockBidPrice
        return currentSpread / 2.0


class FeesCalculator(Feature):

    @classmethod
    def computeForInstrument(cls, updateNum, time, featureParams, featureKey, instrumentManager):
        instrumentLookbackData = instrumentManager.getLookbackInstrumentFeatures()

        priceData = instrumentLookbackData.getFeatureDf('stockVWAP')
        positionData = instrumentLookbackData.getFeatureDf('position')
        currentPosition = positionData.iloc[-1]
        previousPosition = 0 if updateNum < 2 else positionData.iloc[-2]
        changeInPosition = currentPosition - previousPosition
        fees = pd.Series(np.abs(changeInPosition)*featureParams['brokerage'],index = instrumentManager.getAllInstrumentsByInstrumentId())
        if len(priceData)>1:
            currentPrice = priceData.iloc[-1]
        else:
            currentPrice = 0

        fees = fees*currentPrice + np.abs(changeInPosition)*instrumentLookbackData.getFeatureDf(featureParams['spread']).iloc[-1]
        return fees



class BuyHoldPnL(Feature):
    @classmethod
    def computeForInstrument(cls, updateNum, time, featureParams, featureKey, instrumentManager):
        instrumentLookbackData = instrumentManager.getLookbackInstrumentFeatures()

        priceData = instrumentLookbackData.getFeatureDf('stockVWAP')
        bhpnl = pd.Series(0,index = instrumentManager.getAllInstrumentsByInstrumentId())
        if len(priceData)>1:
            bhpnl += priceData.iloc[-1] - priceData.iloc[-2]

        return bhpnl