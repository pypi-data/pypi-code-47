# -*- coding: utf-8 -*-
#
# Copyright 2017 Ricequant, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#lw李文添加




from rqalpha.interface import AbstractDataSource
from rqalpha.model.instrument import Instrument
# from rqalpha.environment import Environment
import  pandas as pd
import time
import datetime


from gm.api import *


class JuejinDataSource(AbstractDataSource):
    def __init__(self):
        i=1


    def get_all_instruments(self):
        """
        获取所有Instrument。

        :return: list[:class:`~Instrument`]
        """

        symList=['SHFE.RB']
        instmentList=get_instruments(symbols=symList, exchanges=None, sec_types=None, names=None, skip_suspended=True, skip_st=True,
                        fields=None, df=False)



        #给退市日期字段 改个名字，从掘金来的名字 和 rqaplha中的名字不一样。改成rqalpha中的名。
        for aInstu in instmentList:
            aInstu.update(de_listed_date=aInstu.pop("delisted_date"))


        instruments = [Instrument(i) for i in instmentList]
        return instruments
        
    def get_trading_calendar(self,exchange):
        from pandas.tseries.offsets import DateOffset


        currDateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        currDate = currDateTime[0:10]
        nextYearofToday = datetime.datetime.strptime(currDate, '%Y-%m-%d')+ DateOffset(years=1)
        nextYearofTodayStr = nextYearofToday.strftime('%Y-%m-%d')
        aTradingDays = get_trading_dates(exchange=exchange, start_date='2000-01-01', end_date=nextYearofTodayStr)
        dtList=map(pd.to_datetime,aTradingDays)



        return dtList




