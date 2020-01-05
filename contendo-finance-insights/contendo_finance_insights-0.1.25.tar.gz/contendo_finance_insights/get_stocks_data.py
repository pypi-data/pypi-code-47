import pandas as pd
import os
import datetime
from datetime import datetime as dt, timedelta, date
import logging

from contendo_utils import *
from contendo_finance_insights import *

# get list of stock action from date to date

class GetStocksData:
    @contendo_classfunction_logger
    def __init__(self):
        self.bqu = BigqueryUtils()
        self.companiesDF = None
        self.stocksDF = None
        self.resourceDir = 'resource'
        self.companiesDataFileName = '{}/companies.csv'.format(self.resourceDir, date.today())
        self.stocksDataFileName = '{}/stocks.csv'.format(self.resourceDir, date.today())
        self.companiesURL = 'Finance/companies.csv'
        self.stocksURL = 'Finance/stocks.csv'

    @contendo_classfunction_logger
    def update_stock_data(self):
        _yearAgo = (date.today()-timedelta(days=380)).strftime('%Y%m%d')
        _stocksQuery = """SELECT * FROM `Finance_Data.{eod_daily_history_1year}` where date > parse_date('%Y%m%d','{fromDate}') order by Symbol, Date""".format(
            fromDate=_yearAgo,
            eod_daily_history_1year=FINANCE_STOCKS_1YEAR_TABLEID,
        )
        logger.debug('updating with this query: %s', _stocksQuery)
        _targetDataset = 'temp'
        _targetTable = 'fin_stocks_data'
        logger.debug('Creating temp stocks data table %s.%s.', _targetDataset, _targetTable)
        _nRows = self.bqu.execute_query_with_schema_and_target(
            query=_stocksQuery,
            targetDataset=_targetDataset,
            targetTable=_targetTable,
        )
        logger.debug('Temp stocks table created, nrows=%d. uploading to GCS...', _nRows)
        result = self.bqu.save_table_to_gcs(_targetDataset, _targetTable, FINANCE_GCP_BUCKET, self.stocksDataFileName)
        logger.debug('Downloading from GCS to %s...', self.stocksDataFileName)
        self.bqu.download_from_gcp(FINANCE_GCP_BUCKET, self.stocksDataFileName, self.stocksDataFileName)
        self.stocksDF = pd.read_csv(self.stocksDataFileName)

    @contendo_classfunction_logger
    def update_companies_data(self):
        _companiesQuery = """SELECT * FROM `sportsight-tests.Finance_Data.all_company_data` WHERE MarketCapitalizationMln > 100"""
        _targetDataset = 'temp'
        _targetTable = 'fin_companies_data'
        logger.debug('Creating temp companies data table %s.%s.', _targetDataset, _targetTable)
        _nRows = self.bqu.execute_query_with_schema_and_target(
            query=_companiesQuery,
            targetDataset=_targetDataset,
            targetTable=_targetTable,
        )
        logger.debug('Temp companies table created, nrows=%d. uploading to GCS...', _nRows)
        result = self.bqu.save_table_to_gcs(_targetDataset, _targetTable, FINANCE_GCP_BUCKET, self.companiesDataFileName)
        logger.debug('Downloading from GCS to %s...', self.companiesDataFileName)
        self.bqu.download_from_gcp(FINANCE_GCP_BUCKET, self.companiesDataFileName, self.companiesDataFileName)
        self.companiesDF = pd.read_csv(self.companiesDataFileName)

    @contendo_classfunction_logger
    def get_stockdata_by_dates(self, stocklist, from_date, to_date):
        #
        # Read the stock data from file.
        if self.stocksDF is None:

            # TODO: @Yahali - check if need to add check for update required.

            self.stocksDF = pd.read_csv(self.stocksDataFileName)
            self.stocksDF['Date1'] = self.stocksDF['Date'].astype(str)

        if len(stocklist)>0:
            symbol_condition = 'Symbol in {tickersString} and '.format(tickersString=str(stocklist))
        else:
            symbol_condition = ''

        stocksQuery = '{symbol_condition} Date1 >= "{from_date}" and Date1 <= "{to_date}"'.format(symbol_condition=symbol_condition, from_date=from_date, to_date=to_date)
        stockDataDF = self.stocksDF.query(stocksQuery)
        stockDataDF.index = pd.to_datetime(stockDataDF['Date'])
        stockDataDF.rename_axis("date", axis='index', inplace=True)
        return stockDataDF

    # get list of stock action x days to date
    @contendo_classfunction_logger
    def get_stockdata_by_cal_days(self, stocklist, numdays, to_date):
        from_date = to_date - datetime.timedelta(days=numdays-1)
        return self.get_stockdata_by_dates(stocklist, from_date, to_date)

    @contendo_classfunction_logger
    def get_stock_fundamentals(self, stocklist=None, index=None, exchange=None):
        #
        # get updated company data
        if self.companiesDF is None:
            self.companiesDF = pd.read_csv(self.companiesDataFileName)

        if stocklist is not None:
            where_condition = 'Symbol in {tickersString}'.format(tickersString=str(stocklist))
        elif index in ['DJI', 'SNP']:
            where_condition = 'is{index}'.format(index=index)
        elif exchange in ['NASDAQ', 'NYSE']:
            where_condition = 'Exchange=="{exchange}"'.format(exchange=exchange)
        else:
            return self.companiesDF

        return self.companiesDF.query(where_condition)

def test():
    startTime = dt.now()
    getstocks = GetStocksData()
    # getstocks.update_companies_data()
    getstocks.update_stock_data()
    return
    companiesDF = getstocks.get_stock_fundamentals(exchange='NYSE')
    #companiesDF = getstocks.get_stock_fundamentals(['MSFT', 'AAPL'])
    symbolList = list(companiesDF['Symbol'])
    print(symbolList, len(symbolList))
    print(dt.now()- startTime)
    #a = get_stockdata_by_cal_days(["AAPL","IBM"],90,datetime.date.today())
    a = getstocks.get_stockdata_by_cal_days([], 365, datetime.date.today())
    print(dt.now()- startTime)
    print(a.shape)

if __name__ == '__main__':
    contendo_logging_setup(default_level=logging.DEBUG)
    os.chdir('{}/tmp'.format(os.environ['HOME']))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}/sportsight-tests.json".format(os.environ["HOME"])
    test()
