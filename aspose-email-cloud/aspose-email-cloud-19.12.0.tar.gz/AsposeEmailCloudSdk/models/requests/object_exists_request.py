#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="object_exists_request.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
#  </copyright>
#  <summary>
#    Permission is hereby granted, free of charge, to any person obtaining a
#   copy  of this software and associated documentation files (the "Software"),
#   to deal  in the Software without restriction, including without limitation
#   the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell  copies of the Software, and to permit persons to whom the
#   Software is  furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all  copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#  </summary>
#  ----------------------------------------------------------------------------
##for __init__.py:from AsposeEmailCloudSdk.models.requests.object_exists_request import ObjectExistsRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class ObjectExistsRequest(BaseRequest):
    """
    Request model for object_exists operation.
    Initializes a new instance.

    :param path (str) File or folder path e.g. '/file.ext' or '/folder'
    :param storage_name (str) Storage name
    :param version_id (str) File version ID
    """

    def __init__(self, path: str, storage_name: str = None, version_id: str = None):
        BaseRequest.__init__(self)
        self.path = path
        self.storage_name = storage_name
        self.version_id = version_id

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `object_exists`")

        collection_formats = {}
        path = '/email/storage/exist/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('storageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))
        path_parameter = '{' + self._lowercase_first_letter('versionId') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.version_id if self.version_id is not None else '')
        else:
            if self.version_id is not None:
                query_params.append((self._lowercase_first_letter('versionId'), self.version_id))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
