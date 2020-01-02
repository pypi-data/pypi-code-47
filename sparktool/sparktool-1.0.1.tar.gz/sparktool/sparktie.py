'''
@Date: 2019-11-12 20:51:31
@LastEditors  : ryan.ren
@LastEditTime : 2020-01-02 23:06:36
@Description: spark connection tool
'''
from __future__ import print_function
import re
import prettytable as pt
from pyspark.sql import SparkSession
from pyspark import SparkConf
import sqlparse
import datetime
import os
import json
import sys


class SparkCreator(object):
    def __init__(self, appname=None, ifkudu=True, **param):
        '''
        @description: init
        '''
        ini = os.path.expanduser('~') + '/.sparktool.json'
        with open(ini, 'r') as f:
            cfg = dict(json.load(f))

        self.__tablecovdict = {}
        self.__ifkudu = ifkudu
        self.__database = cfg['kudu']['database']
        self.__kudumaseter = cfg['kudu']['kudumaster']
        self.spark = None
        self.__pyv = sys.version[0]

        if ifkudu and not bool(cfg['kudu']['database'])*bool(cfg['kudu']['kudumaster']):
            raise Exception("Please set database and kudumaster in %s" %ini)

        self.__sparkcreate(appname, param=param)

    def __sparkcreate(self, appname=None, **param):
        '''
        @description: create spsrksession
        @param: ex. {spark.executor.memoryOverhead:'4096'}
        @return: spark
        '''
        if not appname:
            appname = 'sparktool_' + datetime.datetime.strftime(datetime.datetime.now(),'%H%M%S')

        conf = SparkConf()
        conf.setAppName(appname)
        for k, v in param.items():
            if 'spark' in k:
                conf.set(str(k), str(v))
        
        self.spark = SparkSession.builder.config(conf=conf).getOrCreate()

        print('Create SparkSession: {0}'.format(appname))

    def kudu2view(self, tablelist, ifprint=True):
        '''
        @description: kudu table to temporary view
        @param: tablelist, spark
        @return: temporary view
        '''
        if isinstance(tablelist, str):
            tablelist = [tablelist]

        def cov(table):
            view = table.lower().split('.')[0] + "_" + table.lower().split('.')[1]
            self.spark.read \
                      .format('org.apache.kudu.spark.kudu') \
                      .option('kudu.master', self.__kudumaseter) \
                      .option('kudu.table', "impala::"+table) \
                      .load() \
                      .createOrReplaceTempView(view)

            return view
        
        tb = pt.PrettyTable()
        tb.field_names = ["Origin Table", "Temporary View", "If Transform"]

        for x in tablelist:
            if x.upper() in self.__tablecovdict:
                table = x.upper()
                view = self.__tablecovdict[table]
                transform = 'Yes'
                tb.add_row([table, view, transform])

            elif x.lower() in self.__tablecovdict:
                table = x.lower()
                view = self.__tablecovdict[table]
                transform = 'Yes'
                tb.add_row([table, view, transform])

            else:
                try:
                    table = x.upper()
                    view = cov(table)
                    transform = 'New'
                except Exception:
                    try:
                        table = x.lower()
                        view = cov(table)
                        transform = 'New'
                    except Exception:
                        table = x
                        view = ''
                        transform = 'No'
                finally:
                    tb.add_row([table, view, transform])
                    if transform != 'No':
                        self.__tablecovdict[table] = view
        
        if ifprint and tb:
            print(tb)
    
    def sqlcov(self, sql):
        '''
        @description: replace sql
        @param: sql
        @return: spark sql
        '''
        if self.__tablecovdict:
            for k, v in self.__tablecovdict.items():
                if v is not '':
                    sql = re.sub(k, v, sql, flags=re.I)
            return sql
        else:
            return sql

    def print_tablecovdict(self):
        '''
        @description: print tablecovdict
        @return: print
        '''
        tb = pt.PrettyTable()
        tb.field_names = ["Origin Table", "Temporary View", "If Transform"]

        if self.__tablecovdict:
            for k, v in self.__tablecovdict.items():
                if v is not '':
                    transform = 'Yes'
                else:
                    transform = 'No'
                
                tb.add_row([k, v, transform])
            
            print(tb)
        
        else:
            'There is no transformed table'

    def batch_excutesql(self, sqllist, ddkudu_database=None, sqlsel=[]):
        '''
        @description: batch excute
        @return: excutesql
        '''
        if not ddkudu_database:
            if isinstance(ddkudu_database, str):
                ddkudu_database = {ddkudu_database}
                self.__database.update(ddkudu_database)

        if isinstance(sqllist, str):
            sqllist = [sqllist]
        
        def findkudu(sql):
            sql = sql + ' '
            tablelist = set()
            for kuduflag in self.__database:
                compile_temp = re.findall(r'({0}\..+?) '.format(kuduflag), sql, flags=re.I)
                if compile_temp:
                    tablelist.update(set(compile_temp))
           
            return tablelist

        sqlsplit = []
        f = lambda x: x[:-1] if x[-1] == ';' else x
        for sql in sqllist:
            for sqltemp in sqlparse.split(sql):
                if sqltemp.strip() != '':
                    sqlsplit.append(f(sqltemp))
        
        if self.__ifkudu:
            tablelist = set()
            for sql in sqlsplit:
                tablelist.update(findkudu(sql))
            if tablelist:
                print('Tranform Table:')
                self.kudu2view(tablelist, ifprint=True)
                sqlsplit = list(map(self.sqlcov, sqlsplit))
        
        if not sqlsel:
            numsql = len(sqlsplit)
            ranksql = range(numsql)
        else:
            numsql = len(sqlsel)
            ranksql = sqlsel
            
        for i in ranksql:
            print('\rExcute Progress: {0}/{1}'.format(str(i+1), str(numsql)), end='')
            temp = self.spark.sql(sqlsplit[i])
            if i == numsql - 1:
                return temp
