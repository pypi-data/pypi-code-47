# -*- coding: utf-8 -*-
# Copyright 2019 Ildar.Shirshov <ildar-shirshov@ya.ru>
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
import unicodedata

from functools import partial
from typing import Optional, Union

import asyncio
import ujson

from aiohttp import ClientSession
from aiohttp import hdrs
from aiohttp.web_request import Request
from webargs import aiohttpparser
from webargs import core

JSONCompatible = Union[str, dict, list, set]


async def make_sync_call(fn_: partial) -> object:
    """
    Function makes async call of synchronous
    function.
    :param fn_: partial object
    :return: some data
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, fn_)


async def loads_json(
    req: Request, unicode_normalizing_form: Optional[str] = 'NFKC'
) -> Optional[JSONCompatible]:
    """
    Function loads json data
    from response data (text)
    using ujson module.
    :param req: Incoming request
    :param unicode_normalizing_form: as is
    :return: JSON data structure
    """
    raw_text = await req.text()

    if unicode_normalizing_form:
        raw_text = unicodedata.normalize(unicode_normalizing_form, raw_text)

    return ujson.loads(raw_text) if raw_text else None


async def make_request(
    url: str, params=None, headers=None, method: str = hdrs.METH_GET
) -> Optional[JSONCompatible]:
    """
    Function makes the request
    with specific url and data query.
    :param url: base url
    :param params: parameter for query
    :param headers: as is
    :param method: possible methods POST, GET
    :return: json structure data
    """
    if params is None:
        params = dict()

    if headers is None:
        headers = dict()

    kwargs = {
        hdrs.METH_POST: {'json': params, 'headers': headers},
        hdrs.METH_GET: {'params': params, 'headers': headers},
    }[method]

    async with ClientSession() as session:
        async with session.request(method, url, **kwargs) as resp:
            return await loads_json(resp)


class CachedAIOHttpParser(aiohttpparser.AIOHTTPParser):
    """aiohttp request argument parser."""

    __location_map__ = dict(
        match_info='parse_match_info',
        **core.Parser.__location_map__
    )

    def parse_files(self, req: Request, name: str, field: aiohttpparser.Field) -> None:
        raise NotImplementedError(
            "parse_files is not implemented. You may be able to use parse_form for "
            "parsing upload data."
        )

    async def parse_json(self, req, name, field):
        """Pull a json value from the request."""
        if not self._cache:
            if not (req.can_read_body and aiohttpparser.is_json_request(req)):
                return core.missing

        json_data = self._cache.get('json')
        if json_data is None:
            self._cache["json"] = json_data = await loads_json(req)

        return core.get_value(json_data, name, field, allow_many_nested=True)


aiohttpparser.parser = CachedAIOHttpParser()
aiohttpparser.use_args = aiohttpparser.parser.use_args
aiohttpparser.use_kwargs = aiohttpparser.parser.use_kwargs
