import os
from datetime import datetime as dt
from pathlib import Path
import logging
import pandas as pd

from contendo_utils import *
from contendo_finance_insights import *

class FinanceStatsGenerator(ProducerConsumersEngineMT):
    #
    # read in the configurations
    @contendo_classfunction_logger
    def __init__(self):
        super().__init__(self.queries_generator)
        self.register_handler(self.finance_query_executor)
        self.domain = 'Finance.Stocks'
        self.domainGID = 284194018
        #
        # get the initial configuration

        self.root = str(Path(__file__).parent)
        self.configsheet_url = 'https://docs.google.com/spreadsheets/d/1gwtQlzk0iA4qyLzqaYEk5SggOqNZtJnSSfwnZYDNlAw/export?format=csv&gid={SheetId}&run=1'
        sourceConfigDF = pd.read_csv(self.configsheet_url.format(SheetId='284194018')).fillna('')
        sourceConfigDF['enriched'] = False
        self.sourcesConfigDict = ProUtils.pandas_df_to_dict(sourceConfigDF, 'Configname')
        self.sport_configs = {}
        self.TRUE = True

        self.bqUtils = BigqueryUtils()

    @contendo_classfunction_logger
    def get_source_configuration(self, configName, startTime):
        sourceConfig = self.sourcesConfigDict[configName]
        if sourceConfig['DoIT']!='y' or sourceConfig['enriched']==True:
            return sourceConfig

        sheetId = sourceConfig['SportSheetId']
        #
        # read all relevant metrics
        if sheetId not in self.sport_configs.keys():
            self.sport_configs[sheetId] = pd.read_csv(self.configsheet_url.format(SheetId = str(sourceConfig['SportSheetId']))).fillna('')
            self.sport_configs[sheetId]['SportCode'] = sourceConfig['SportCode']

        sourceConfig['StatsDefDict'] = ProUtils.pandas_df_to_dict(self.sport_configs[sheetId], 'StatName')

        if 'query' not in sourceConfig.keys():
            sourceConfig['query'] = open(self.root + '/queries/' + sourceConfig['QueryFile'], 'r').read().replace('{eod_daily_history_1year}', FINANCE_STOCKS_1YEAR_TABLEID)

        sourceConfig['enriched'] = True
        self.sourcesConfigDict[configName] = sourceConfig
        return sourceConfig

    @contendo_classfunction_logger
    def queries_generator(self, jobQueue, startTime, configurations=None, stats=None, **kwargs):
        startTime = dt.now()
        #
        # Make sure the target dataset exists
        self.bqUtils.create_dataset(FINANCE_DATA_DATASETID)
        #
        # if there are only partial list of configurations
        if not configurations:
            configurations = self.sourcesConfigDict.keys()
        #
        # loop over all configurations and generate
        #print(configurations)
        for sourceConfigName in configurations:
            #
            # get the source configuration
            sourceConfig = self.get_source_configuration(sourceConfigName, startTime)
            #
            # make sure it is required.
            if sourceConfig['DoIT']!='y':
                continue
            #
            # call the relevant generation function.
            print ("running configuration {}".format(sourceConfigName))
            # generatorFunc = eval('self.{}'.format(sourceConfig['generatorFunc']))
            # generatorFunc(jobQueue, sourceConfig, startTime, stats)
            self.financeQueriesGenerator(jobQueue, sourceConfig, startTime, stats)

    @contendo_classfunction_logger
    def financeQueriesGenerator(self, jobQueue, sourceConfig, startTime, stats=None):
        #
        # target table definitions
        financeTableFormat = 'Stat_Finance_{StatSource}_{StatName}_{StatObject}_Rolling_{RollingDays}'
        financeStatsDataset = 'Finance_Stats'
        self.bqUtils.create_dataset(financeStatsDataset)

        #
        # create jobs for all relevant metrics.
        for statDef in sourceConfig['StatsDefDict'].values():

            if statDef['Doit']!='y':
                continue

            #print('Metric: {}, Sport:{}, Delta time: {}'.format(statDef['StatName'], statDef['SportCode'], dt.now() - startTime), flush=True)

            for statObject in statDef['StatObject'].split(',')[:1]:
                for rollingDays in statDef['RollingDaysList'].split(','):
                    _statDef = statDef.copy()
                    _statDef['StatObject'] = statObject
                    rollingDaysInst = {'RollingDays': rollingDays}
                    query = sourceConfig['query']
                    query=ProUtils.format_string(query, _statDef)
                    query=ProUtils.format_string(query, sourceConfig)
                    query=ProUtils.format_string(query, rollingDaysInst)
                    #print (query)
                    #
                    # define the destination table
                    instructions = _statDef
                    instructions['StatTimeframe'] = sourceConfig['StatTimeframe']
                    instructions['StatSource'] = sourceConfig['StatSource']
                    instructions['RollingDays'] = rollingDays
                    targetTable = ProUtils.format_string(financeTableFormat, instructions).replace('.', '_').replace('-', '_')
                    jobDefinition = {
                        'params': {
                            'query': query,
                            'targetDataset': financeStatsDataset,
                            'targetTable': targetTable,
                        },
                        'statName': _statDef['StatName'],
                        'statObject': statObject,
                        'statTimeframe': '{}_Rollingdays'.format(rollingDays)
                    }
                    jobQueue.put(ProducerConsumersEngineMT.PCEngineJobData(self.finance_query_executor, jobDefinition))

    @contendo_classfunction_logger
    def finance_query_executor(self, statName, statObject, statTimeframe, params, startTime, **kwargs):
        #
        # to enforce the schema is correct, we first copy the empty table from the schema template
        # and then append the result to this empty table
        try:
            nRows = self.bqUtils.execute_query_with_schema_and_target(**params)
            print('Returened for Statname: {} ({} rows), StatObject: {}, StatTimeframe: {}, Detlatime: {}'.format(
                statName,
                nRows,
                statObject,
                statTimeframe,
                dt.now() - startTime),
            )
            queryFile = 'results/queries/{}.sql'.format(params['targetTable'])
            f = open(queryFile, 'w')
            f.write(params['query'])
            f.close()
        except Exception as e:
            queryFile = 'errors/{}.sql'.format(params['targetTable'])
            f = open(queryFile, 'w')
            f.write(params['query'])
            f.close()
            # print(queryJob['query'],flush=True)
            print('Error with Statname: {}, StatObject: {}, StatTimeframe: {}'.format(
                statName,
                statObject,
                statTimeframe
            ))


def test():
    startTime=dt.now()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}/sportsight-tests.json".format(os.environ["HOME"])
    os.chdir('{}/tmp/'.format(os.environ["HOME"]))
    fsg = FinanceStatsGenerator()
    fsg.run(configurations=['Finance.EOD'], numExecutors=32, startTime=startTime)

if __name__ == '__main__':
    #print(globals())
    #print(__file__)
    #print(Path(__file__).parent)
    test()
    #print(spread.sheets)
