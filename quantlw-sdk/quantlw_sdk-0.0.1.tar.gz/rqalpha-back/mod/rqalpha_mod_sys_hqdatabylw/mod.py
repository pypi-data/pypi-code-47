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


# import sys
# sys.path.append(r'../..')
from rqalpha.interface import AbstractMod
from rqalpha.const import DEFAULT_ACCOUNT_TYPE, MARKET,HQDATATYPE
# from interface import AbstractMod
# from const import DEFAULT_ACCOUNT_TYPE, MARKET,HQDATATYPE

from .data_souce import JuejinDataSource

from .deciders import CNStockTransactionCostDecider, CNFutureTransactionCostDecider, HKStockTransactionCostDecider


class HQDataMod(AbstractMod):
    def start_up(self, env, mod_config):

        if env.config.base.hqDataType == HQDATATYPE.JUEJIN:
            env.set_data_source(JuejinDataSource())
        

    def tear_down(self, code, exception=None):
        pass
