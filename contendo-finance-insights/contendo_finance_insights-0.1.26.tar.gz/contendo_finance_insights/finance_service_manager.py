import os
import json
from datetime import datetime as dt
import logging

from contendo_utils import *
from contendo_finance_insights import *
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import BadRequest

from pathlib import Path

class FinanceServiceManager():
    #
    # read in the configurations
    @contendo_classfunction_logger
    def __init__(self, project=None):
        self.getstocks = GetStocksData()
        logger.info('Starting get_stock_fundamentals for %s', 'SNP')
        companiesDF = self.getstocks.get_stock_fundamentals(index='SNP')
        symbolList = list(companiesDF['Symbol'])
        logger.info('Starting StockMetricsCalculator for S&P, %s companies', len(symbolList))
        self.smc = StockMetricsCalculator(symbolList, self.getstocks)
        logger.info('Done StockMetricsCalculator')
        self.gsn = GetStockNews()
        self.bqu = BigqueryUtils()

    @contendo_classfunction_logger
    def one_list_generator(self, listName, listConfigDict):
        listConfigFile = 'resource/lists_config.json'
        listsDefDict = ProUtils.get_dict_from_jsonfile(listConfigFile)
        #
        # read the query, configure and run it.
        instructions={}
        if listName in listsDefDict.keys():
            listConfig = listsDefDict[listName]
        else:
            _error = 'List {} does not exist'.format(listName)
            logger.exception(_error)
            raise NotFound(_error)

        instructions['StatName']=listConfig['StatName']
        instructions['RollingDaysCondition'] = 'StatRollingDays="{}"'.format(listConfig['RollingDays'])

        if 'Sector' in listConfigDict:
            instructions['SectorCondition']='Sector="{}"'.format(listConfigDict['Sector'])
        else:
            instructions['SectorCondition']='TRUE'

        if listConfigDict.get('Index', '') in ['DJI', 'SNP']:
            instructions['IndexCondition'] = 'is'+listConfigDict['Index']
        else:
            instructions['IndexCondition'] = 'isSNP'

        minMarketCap = listConfigDict.get('MarketCapMin', 100)
        maxMarketCap = listConfigDict.get('MarketCapMax', 1000000000)
        instructions['MarketCapCondition'] = 'MarketCap BETWEEN {} AND {}'.format(minMarketCap, maxMarketCap)
        instructions['ListSize'] = min(int(listConfigDict.get('ListSize', 5)), 10)

        _listFile = 'cache/{date}-{deploytime}/{listName}-{sector}-{index}-{rollingDays}-{marketCap}-{listSize}.json'.format(
            listName = listName,
            date = dt.now().strftime('%Y-%m-%d'),
            deploytime = os.path.getctime(listConfigFile),
            sector = listConfigDict.get('Sector', 'None'),
            index = instructions['IndexCondition'],
            rollingDays = listConfig['RollingDays'],
            marketCap = '{}to{}M'.format(minMarketCap, maxMarketCap),
            listSize = instructions['ListSize'],
        )
        logger.debug('List cache file=%s', _listFile)
        _ret = self.bqu.read_string_from_gcp(FINANCE_GCP_BUCKET, _listFile)
        if _ret is None:
            finquery = ProUtils.get_string_from_file('{}/queries/top_lists_query.sql'.format(Path(__file__).parent))
            query = ProUtils.format_string(finquery, instructions)
            #
            # Execute the query.
            logger.info('Starting get-top-list for {} query execution.'.format(instructions))
            listDF = self.bqu.execute_query_to_df(query)
            listDict = ProUtils.pandas_df_to_dict(listDF, 'TopRank')
            logger.info('Done get-top-list.')

            #
            # getting additional info
            gsn = GetStockNews()
            for key, stockDict in listDict.items():
                stockDict['InterestingStatements'] = self.get_statements_for_ticker(stockDict['Symbol'])
                stockDict['RelevantNews'] =     gsn.get_stocknews_byticker(stockDict['Symbol'])

            listDict['Description'] = listConfig['QuestionDescription']
            _ret = json.dumps(listDict)
            self.bqu.upload_string_to_gcp(_ret, FINANCE_GCP_BUCKET, _listFile)

        # logger.debug('Return list = %s', listDict )
        return _ret #

    @contendo_classfunction_logger
    def get_statements_for_ticker(self, ticker):
        interestingStatements = dict()
        try:
            interestingStatementsDF = self.smc.get_interesting_statements(ticker)
            count=0
            for i, statement in interestingStatementsDF.iterrows():
                count+=1
                interestingStatements[count] = dict(statement)
        except Exception as e:
            logger.exception("Exception while getting statements for %s", ticker)
            raise e

        return interestingStatements

    @contendo_classfunction_logger
    def ticker_generator(self, ticker):
        #
        # get basic stock data
        companiesDF = self.getstocks.get_stock_fundamentals([ticker])
        if companiesDF.shape[0] == 0:
            raise NotFound('Ticker {} does not exists'.format(ticker))

        stockDict = dict(companiesDF[['Symbol', 'Industry', 'Sector', 'Name', 'Exchange', 'LastClose', 'T52WeekLow', 'T52WeekHigh', 'MarketCapitalizationMln', 'PERatio', 'CompanyLogoURL']].iloc[0])
        logger.info(stockDict)
        #
        # get interestinf statements for the stock.
        companiesDF = self.getstocks.get_stock_fundamentals(index='SNP')
        symbolList = list(companiesDF['Symbol'])
        smc = StockMetricsCalculator(symbolList, self.getstocks)
        stockDict['InterestingStatements'] = self.get_statements_for_ticker(stockDict['Symbol'])
        #
        # get the stock news for the ticker
        gsn = GetStockNews()
        stockDict['RelevantNews'] = gsn.get_stocknews_byticker(stockDict['Symbol'])
        return json.dumps(stockDict)

if __name__ == "__main__":
    contendo_logging_setup(default_level=logging.DEBUG)
    if os.environ.get('CONTENDO_ON_CLOUD', 'no') != 'yes':
        os.chdir('{}/tmp/'.format(os.environ["HOME"]))
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}/sportsight-tests.json".format(os.environ["HOME"])
    os.environ['STOCKNEWS_API_KEY'] = 'oywghpku7talnwtde1k4h5eqonrgze6i1v6fzmcq'

    fsm = FinanceServiceManager()
    # print(dict_to_string(json.loads(fsm.one_list_generator('DollarVolume', {}))))
    print(dict_to_string(json.loads(fsm.ticker_generator('MSFT'))))

