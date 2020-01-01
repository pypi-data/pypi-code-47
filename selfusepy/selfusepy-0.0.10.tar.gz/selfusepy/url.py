#   Copyright 2018-2019 LuomingXu
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  Author : Luoming Xu
#  File Name : url.py
#  Repo: https://github.com/LuomingXu/selfusepy

import json
from urllib.parse import urlencode

import urllib3
from urllib3.response import HTTPResponse


class HttpError(Exception):
  def __init__(self, msg):
    super().__init__(self)
    self.msg = msg

  def __str__(self) -> str:
    return self.msg


class Request(object):
  """
  进一步封装urllib3的接口, 直接提供GET, POST, PUT, DELETE接口, body全部使用json格式
  """

  def __init__(self):
    self.http = urllib3.PoolManager()
    self.UTF8 = 'utf-8'

  def get(self, url: str, head: dict = None, **params: dict) -> HTTPResponse:
    """
    http GET method
    :param head: request header
    :param url: URL
    :param params: http request params. should be class's dict. e.g., url.Request.get('https://example.com', **object.__dict__)
                   if your define a dict variable, you just use it like, url.Request.get('https://example.com', **dict)
    :return:
    """
    if params is not None:
      return self.http.request('GET', url, headers = head,
                               fields = params)
    else:
      return self.http.request('GET', url, headers = head)

  def put(self, url: str, body: object = None, head: dict = None, **params: dict) -> HTTPResponse:
    """
    http PUT method
    :param head: request header
    :param url: URL
    :param body: put body. one object
    :param params: http request params
    :return:
    """
    head['Content-Type'] = 'application/json'
    if params is not None:
      url += '?' + urlencode(params)
    if body is not None:
      return self.http.request('PUT', url, body = json.dumps(body.__dict__),
                               headers = head)
    else:
      return self.http.request('PUT', url, headers = head)

  def post(self, url: str, body: object, head: dict = None, **params: dict) -> HTTPResponse:
    """
    http POST method
    :param head: request header
    :param url: URL
    :param body: post body. one object
    :param params: http request params
    :return:
    """
    head['Content-Type'] = 'application/json'
    if body is None:
      raise HttpError('POST request\'s body can not be None')
    if params is not None:
      url += '?' + urlencode(params)

    return self.http.request('POST', url, body = json.dumps(body.__dict__),
                             headers = head)

  def delete(self, url: str, head: dict, **params: dict) -> HTTPResponse:
    """
    http DELETE method
    :param head: request header
    :param url: URL
    :param params: http request params
    :return:
    """
    if params is not None:
      return self.http.request('DELETE', url, fields = params, headers = head)
    else:
      return self.http.request('DELETE', url, headers = head)
