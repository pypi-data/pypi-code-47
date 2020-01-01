import os
import json
from datetime import date, datetime as dt
import time
from pytrends.request import TrendReq
from pytrends.exceptions import ResponseError
import pandas as pd
import logging

from contendo_utils import *

class GoogleTrendImport:
    @contendo_classfunction_logger
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)

    @contendo_classfunction_logger
    def get_trend_for_list(self, itemList, key, category, categoryName):
        logger.debug('Starting getting trends for ')
        startTime = dt.now()
        filename = 'results/trends/trends_{}_{}_{}.json'.format(categoryName, category, startTime.strftime('%Y%m%dTH%M%S'))
        todayDate = startTime.strftime('%Y-%m-%d')
        outfile = open(filename, 'w')
        # pytrends = TrendReq(hl='en-US', tz=360, proxies=['https://34.203.233.13:80', 'https://35.201.123.31:880'])

        first_ind = True
        itemCount = 0
        for itemDict in itemList:
            item = itemDict[key]
            sleeptime = 1
            itemCount += 1
            logger.debug('%d. Getting item %s, delta=%s', itemCount, item, dt.now() - startTime)
            while True:
                try:
                    time.sleep(sleeptime)
                    self.pytrends.build_payload([item],
                                           cat=category,
                                           timeframe='today 3-m',
                                           geo='US',
                                           gprop='')
                    itemTrend = self.pytrends.interest_over_time()
                    break
                except ResponseError as e:
                    logger.info('Error reading trend {}, sleeptime: {}, delta-time: {}, error: {}'.format(
                        item,
                        sleeptime,
                        dt.now() - startTime,
                        e)
                    )
                    if str(e).find('429') >= 0:
                        sleeptime += 60

                except Exception as e:
                    logger.exception('Exception while reading trend {}, sleeptime: {}, delta-time: {}, error: {}'.format(
                        item,
                        sleeptime,
                        dt.now() - startTime,
                        e)
                    )
                    # make it an empty dataframe and break
                    itemTrend=pd.DataFrame()
                    break

            if itemTrend.shape[0] < 70:
                logger.debug('Not enough trend for item %s, #days: %d', item, itemTrend.shape[0])
                continue

            itemTrend['Date'] = itemTrend.index
            trends = []
            for i, row in itemTrend.iterrows():
                trend = dict()
                trend['Trend'] = row[item]
                trend['Date'] = row['Date'].strftime('%Y-%m-%d')
                trends.append(trend)
            trendsDict = {'ItemTrend': trends, 'CategoryId': category, 'CategoryName': categoryName, 'SampleDate': todayDate}
            trendsDict.update(itemDict)
            trendsDict.pop('count')
            #print(trendsDict)
            outfile.write(json.dumps(trendsDict)+'\n')
            #break
        outfile.close()
        return filename

@contendo_function_logger
def run_trends():
    query = 'SELECT Code, Name, Sector, count(*) count FROM `sportsight-tests.Finance_Data.indices_company_list` left join unnest(Components) group by 1,2,3 having count>0 order by count desc, name'
    bqu = BigqueryUtils()

    gtrend = GoogleTrendImport()
    itemsDict = bqu.execute_query_to_dict(query)
    print('Getting {} items for finance'.format(itemsDict['nRows']))
    trendsDict = {'Finance': 7, 'Financial-Markets': 1163}
    for categoryName, category in trendsDict.items():
        filename = gtrend.get_trend_for_list(itemsDict['Rows'], 'Code', category, categoryName)
        datasetId = 'Trends_Data'
        #bqu.create_dataset(datasetId)
        try:
            bqu.create_table_from_local_file(filename, datasetId, 'daily_trends', writeDisposition='WRITE_APPEND')
        except Exception as e:
            print (e)

@contendo_function_logger
def run_stats():
    # Run the Hypechange metrics calculation
    from contendo_finance_insights import SimpleStatsGenerator
    generator = SimpleStatsGenerator()
    generator.run(configurations=['Finance.EOD'])
    # run the cache
    from dotenv import load_dotenv
    load_dotenv(verbose=True)
    os.system('curl https://api.contendo.ai/finance/v1/get_top_lists/HypeChange?api_key={}'.format(os.environ['CONTENDO_FINANCE_API_KEY']))
    os.system('curl https://api.contendo.ai/finance/v1/get_top_lists/DailyGain?api_key={}'.format(os.environ['CONTENDO_FINANCE_API_KEY']))

    'Done'

if __name__ == '__main__':
    contendo_logging_setup(default_level=logging.DEBUG)
    os.chdir('{}/tmp'.format(os.environ['HOME']))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}/sportsight-tests.json".format(os.environ["HOME"])
    run_trends()
    run_stats()