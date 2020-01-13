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
import inspect

from functools import wraps
from functools import partial

import ujson

from aiohttp import web
from webargs import aiohttpparser
from webargs import dict2schema

ROUTE_TABLE = []
JSON_RESPONSE = partial(web.json_response, dumps=ujson.dumps)

GET = 1 << 0
POST = 1 << 1


def __to_camel(method_name: str) -> str:
    """
    Function converts to camel
    case specific method name.

    First version of naming:
        <get|set>_your_action -> getYourAction

    Second version of naming:
        _<get|set>            -> get

    :param method_name: As is
    :return: str
    """

    tmp = method_name[:]

    if tmp.startswith('_'):
        tmp = tmp[-(len(tmp) - 1):]

    return "".join(
        w.lower() if i == 0 else w.title() for i, w in enumerate(tmp.split('_'))
    )


def __url_path_format(version_id: str, resource_name: str, method_name: str) -> str:
    """
    Function makes the method path
    using specific format.
    :param version_id: Version of API
    :param method_name: Name of method
    :param resource_name: Name of resource
    :return: str
    """
    return f"/{version_id}/{resource_name}.{method_name}"


def make_route(input_args: dict = None, output_args: dict = None,
               locations: tuple = None, validate: object = None,
               path: str = None, auth_required: callable = None,
               method_types: int = None):
    """
    Functions makes the route for
    wrapped function.
    :param input_args: Map of incoming data scheme
    :param output_args: Map of output scheme
    :param locations: Location of incoming data ('form', 'data', 'json')
    :param validate: Validator of full scheme
    :param path: Stringify path of decorated async function
    :param auth_required: This functions checks credential information inside request headers
    :param method_types: This flags indicates about methods for specific endpoint
    :return: callable
    """
    if not isinstance(method_types, int):
        method_types = GET | POST

    # Prepare dumper for outgoing data
    # if not (isinstance(output_args, dict) or isinstance(output_args, list)):
    #    output_args = {'result': fields.List(fields.Str(), missing=[])}
    if isinstance(output_args, dict):
        schema = dict2schema(output_args)()
    else:
        schema = output_args()

    # Checking locations of data
    # for incoming request
    if not isinstance(locations, tuple):
        locations = ('json', 'querystring')

    def wrapped(fn_: callable):
        # Create the wrapper for original
        # async coroutine function

        @wraps(fn_)
        async def coro_wrapper(request: web.Request):
            # First checking authorization
            auth_data = None
            if inspect.iscoroutinefunction(auth_required):
                auth_data = await auth_required(request)

            # Parsing incoming data using parser and
            # scheme of input arguments
            parsed_data_map = dict()
            if input_args:
                parsed_data_map = await aiohttpparser.parser.parse(
                    input_args, request, locations, validate
                )

            # Injecting data from request's header
            # data
            if auth_data:
                parsed_data_map = {**parsed_data_map, **auth_data}

            # Waiting the result from original function
            # and dumping it
            data = await fn_(**{**parsed_data_map, **{'request': request}})

            if isinstance(data, (web.FileResponse, web.WebSocketResponse, web.Response)):
                return data

            # 1) Validating outgoing data scheme
            # 2) Serialize verified data
            if data is None:
                data = {}
            else:
                if isinstance(output_args, dict):
                    if not isinstance(data, tuple):
                        data = (data,)

                    data = dict(zip(output_args.keys(), data))

            return JSON_RESPONSE(
                schema.dump(data)
            )

        # Last thing is dispatch the route of
        # aiohttp coroutine and it endpoint
        endpoint_path = path
        if not isinstance(endpoint_path, str):
            # First step is extract
            # name of called module
            frm = inspect.stack()[1]
            mod = inspect.getmodule(frm[0])

            # This module name should
            # exclude from global path
            root_file = __name__

            # The full path to wrapped
            # resource endpoint
            resource_path = mod.__name__
            resource_path = resource_path.replace(root_file, '')
            resource_path = resource_path.replace('.', '/')

            # Extract endpoint name
            method_name = __to_camel(fn_.__name__)
            endpoint_path = "/{0}.{1}".format(resource_path, method_name)

        # Add coroutine wrapper inside the webapp
        if (method_types & GET) == GET:
            ROUTE_TABLE.append(
                web.get(endpoint_path, coro_wrapper, allow_head=False)
            )
        if (method_types & POST) == POST:
            ROUTE_TABLE.append(
                web.post(endpoint_path, coro_wrapper)
            )

        return coro_wrapper

    return wrapped
