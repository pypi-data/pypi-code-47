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

from collections import defaultdict

from rqalpha.interface import AbstractTransactionCostDecider
from rqalpha.environment import Environment
from rqalpha.const import SIDE, HEDGE_TYPE, COMMISSION_TYPE, POSITION_EFFECT


class JuejinDataSource(AbstractTransactionCostDecider):
    def __init__(self, commission_rate, commission_multiplier, min_commission):
        self.commission_rate = commission_rate
        self.commission_multiplier = commission_multiplier
        self.commission_map = defaultdict(lambda: min_commission)
        self.min_commission = min_commission

        self.env = Environment.get_instance()

