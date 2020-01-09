#  Copyright (c) 2019 Samsung, Inc. and its affiliates.
#
#  This source code is licensed under the RESTRICTED license found in the
#  LICENSE file in the root directory of this source tree.

import io
import os
import pathlib
import uuid

import mock
import pytest

import disco
from .base_test import BaseTest
from disco import Asset
from contextlib import contextmanager

test_file_dir = os.path.dirname(os.path.realpath(__file__))
txt_file = os.path.join(test_file_dir, 'test_files', 'text_file.txt')
img_file = os.path.join(test_file_dir, 'test_files', 'disco-logo.png')

file_content = {}


class FTypes(object):
    text = 'Text'
    image = 'Image'


def setup_module():
    global file_content
    with io.FileIO(txt_file) as txt_f:
        file_content[FTypes.text] = txt_f.read()

    with io.FileIO(img_file) as img_f:
        file_content[FTypes.image] = img_f.read()


class TestAsset(BaseTest):

    def test__request_url_for_upload_with_cluster(self):
        asset = Asset()
        fname = self.random_str('filename')
        cluster = self.random_str('cluster')
        excpected = {
            'key': fname,
            'clusterId': cluster
        }
        _rest = mock.MagicMock('Asset.rest')

        asset.rest = _rest
        asset._request_url_for_upload(fname, cluster)
        _rest.assert_called_once_with(url='/files/uploadparams',
                                      data=excpected,
                                      method='post')

    def test__request_url_for_upload_without_cluster(self):
        asset = Asset()
        _rest = mock.MagicMock('Asset.rest')
        asset.rest = _rest

        fname = self.random_str('filename')
        excpected = {
            'key': fname,
        }
        asset._request_url_for_upload(fname, None)
        _rest.assert_called_once_with(url='/files/uploadparams',
                                      data=excpected,
                                      method='post')

    def test__register_file(self):
        asset = Asset()
        _rest = mock.MagicMock('Asset.rest')
        asset.rest = _rest

        token = self.random_str('token')
        send_result = self.random_str('id')
        _rest.return_value = {'id': send_result}
        result = asset._register(token)
        _rest.assert_called_once_with(url='/files',
                                      data={'token': token},
                                      method='post')

        assert result == send_result

    file_argument_parameters = [
        (b'Lol I have text \n and newlines here.', FTypes.text),
        ('Lol I have text \n and newlines here.', FTypes.text),
        (io.StringIO('Lol I have text \n and newlines here.'), FTypes.text),
        (io.BytesIO(b'Lol I have text \n and newlines here.'), FTypes.text),
        (open(os.path.abspath(txt_file), 'r'), FTypes.text),
        (open(os.path.abspath(txt_file), 'rb'), FTypes.text),
        (pathlib.Path(txt_file), FTypes.text),
        (pathlib.Path(img_file), FTypes.image),
        (open(os.path.abspath(img_file), 'rb'), FTypes.image)
    ]
    @pytest.mark.parametrize('file_argument', file_argument_parameters)
    def test_upload_file_mocked(self, file_argument):
        generated_id = str(uuid.uuid4())
        generated_url = '/some-storage/%s' % generated_id
        generated_name = 'file_%s.bin' % generated_id
        generated_token = 'token>%s' % generated_id
        generated_fields = {'x': generated_id, 'y': generated_name}

        with mock.patch('disco.asset.Asset._request_url_for_upload') \
                as request_url_mock, \
                mock.patch('disco.asset.Asset._upload_with_callback') as _upload_with_callback, \
                mock.patch('disco.asset.Asset._register') as register_file_mock:

            request_url_mock.return_value = {
                'url': generated_url,
                'fields': generated_fields,
                'token': generated_token
            }

            register_file_mock.return_value = generated_id

            file_id = disco.asset.upload_file(generated_name, file_argument[0], show_progress_bar=False)

            request_url_mock.assert_called_once_with(generated_name, None)
            expected_body = file_content[file_argument[1]]

            _upload_with_callback.assert_called_once_with(
                generated_url, generated_name, form_fields=generated_fields,
                file_content_bytes=expected_body, callback=self.is_function())
            register_file_mock.assert_called_once_with(generated_token)

            assert file_id == generated_id
