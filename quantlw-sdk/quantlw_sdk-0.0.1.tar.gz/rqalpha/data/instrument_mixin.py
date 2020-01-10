# -*- coding: utf-8 -*-
#
# Copyright 2019 Ricequant, Inc
#
# * Commercial Usage: please contact public@ricequant.com
# * Non-Commercial Usage:
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
import six

# #lw 李文修改 本py文件


class InstrumentMixin(object):
    def __init__(self, instruments):


        #lw 李文修改。原始代码注释。
        # self._instruments = {i.order_book_id: i for i in instruments}
        # self._sym_id_map = {i.symbol: k for k, i in six.iteritems(self._instruments)
        #                     # 过滤掉 CSI300, SSE50, CSI500, SSE180
        #                     if not i.order_book_id.endswith('INDX')}

        self._instruments = {i.symbol: i for i in instruments}





    def sector(self, code):
        return [v.order_book_id for v in self._instruments.values()
                if v.type == 'CS' and v.sector_code == code]

    def industry(self, code):
        return [v.order_book_id for v in self._instruments.values()
                if v.type == 'CS' and v.industry_code == code]

    def all_instruments(self, types, dt=None):
        return [i for i in self._instruments.values()
                if ((dt is None or i.listed_date.date() <= dt.date() <= i.de_listed_date.date()) and
                    (types is None or i.type in types))]

    def _instrument(self, sym_or_id):
        try:
            return self._instruments[sym_or_id]
        except KeyError:
            pass

    def instruments(self, sym_or_ids):
        if isinstance(sym_or_ids, six.string_types):
            return self._instrument(sym_or_ids)

        return [i for i in [self._instrument(sid) for sid in sym_or_ids] if i is not None]

    def get_future_contracts(self, underlying, date):
        date = date.replace(hour=0, minute=0, second=0)
        futures = [v for o, v in six.iteritems(self._instruments)
                   if v.type == 'Future' and v.underlying_symbol == underlying and
                   not o.endswith('88') and not o.endswith('99')]
        if not futures:
            return []

        return sorted(i.order_book_id for i in futures if i.listed_date <= date <= i.de_listed_date)
