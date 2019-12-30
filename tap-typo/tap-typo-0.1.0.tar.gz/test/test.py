# Copyright 2019 Typo. All Rights Reserved.
#
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
#
# you may not use this file except in compliance with the
#
# License.
#
#
#
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing, software
#
# distributed under the License is distributed on an "AS IS" BASIS,
#
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#
# implied. See the License for the specific language governing
#
# permissions and limitations under the License.
#
#
#
# This product includes software developed at
#
# or by Typo (https://www.typo.ai/).
# !/usr/bin/env python3
# 11, 20, 29

import json
import unittest
from unittest.mock import patch
import tap_typo.__init__ as init
from tap_typo.typo import TypoTap


class TestTypo(unittest.TestCase):

    @patch('tap_typo.typo.requests.post')
    def test_request_token(self, mock_post):
        print("Test: When API key and API secret are provided, a token",
              "property should be returned in the API return.")

        # Mock returns
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"token": "test"}

        # Mock parameters
        typo_1 = TypoTap(
            cluster_api_endpoint='https://www.mock.com',
            api_key='typo_key',
            api_secret='typo_secret',
            repository='mock',
            dataset='mock',
            audit_id='123'
        )

        expected_headers = {
            "Content-Type": "application/json"
        }
        expected_payload = {
            "apikey": "typo_key",
            "secret": "typo_secret"
        }

        token = typo_1.request_token()
        mock_post.assert_called_with(
            'https://www.mock.com/token', data=json.dumps(expected_payload), headers=expected_headers)
        self.assertEqual(token, 'test')

    @patch('tap_typo.typo.requests.get')
    def test_valid_get_dataset_without_errors(self, mock_get):
        print('Test: When dataset is provided with an audit id, API should return a "data" property ',
              'with the processed datasets from Typo. Audit results (OK) will be inserted into the dataset ',
              'if no errors are found.')

        # Mock returns
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'code': 'GET_AUDIT_RESULTS_SUCCESS',
            'message': 'Get audit results success',
            'data': [
                {
                    'tag': '',
                    'qualityLabel': 'Not Set',
                    'qualityFeedback': '',
                    'data': {
                        'date': 'today',
                        'typo': 'tap'
                    },
                    'hasErrors': 0
                }
            ]
        }

        # Mock Parameters
        typo_2 = TypoTap(
            cluster_api_endpoint='https://www.mock.com',
            api_key='typo_key',
            api_secret='typo_secret',
            repository='mock_repo',
            dataset='mock_dataset',
            audit_id='123'
        )
        typo_2.token = '123'

        expected_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 123"
        }

        # Expected function return
        expected_return = [
            {
                'date': 'today',
                'typo': 'tap',
                '__typo_result': 'OK'
            }
        ]


        data_out = typo_2.get_dataset("mock_dataset")
        mock_get.assert_called_with(
            'https://www.mock.com/repositories/mock_repo/datasets/mock_dataset/audits/123/results', headers=expected_headers, params=None)
        self.assertEqual(data_out, expected_return)
    
    @patch('tap_typo.typo.requests.get')
    def test_valid_get_dataset_with_errors(self, mock_get):
        print('Test: When dataset is provided with an audit id, API should return a "data" property ',
              'with the processed datasets from Typo. Audit results (Error) will be inserted into the dataset ',
              'if errors are found.')

        # Mock returns
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'code': 'GET_AUDIT_RESULTS_SUCCESS',
            'message': 'Get audit results success',
            'data': [
                {
                    'tag': '',
                    'qualityLabel': 'Not Set',
                    'qualityFeedback': '',
                    'data': {
                        'date': 'today',
                        'typo': 'tap'
                    },
                    'hasErrors': 1
                }
            ]
        }

        # Mock Parameters
        typo_2 = TypoTap(
            cluster_api_endpoint='https://www.mock.com',
            api_key='typo_key',
            api_secret='typo_secret',
            repository='mock_repo',
            dataset='mock_dataset',
            audit_id='123'
        )
        typo_2.token = '123'

        expected_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 123"
        }

        # Expected function return
        expected_return = [
            {
                'date': 'today',
                'typo': 'tap',
                '__typo_result': 'Error'
            }
        ]


        data_out = typo_2.get_dataset("mock_dataset")
        mock_get.assert_called_with(
            'https://www.mock.com/repositories/mock_repo/datasets/mock_dataset/audits/123/results', headers=expected_headers, params=None)
        self.assertEqual(data_out, expected_return)

    @patch('tap_typo.typo.requests.get')
    def test_invalid_get_dataset(self, mock_get):
        print('Test: When a request is not valid, tap-typo should exit with guidance on what went',
              'wrong with the request.')

        # Mock returns
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {
            "message": "GET request failed."}
        
        # Mock Parameters
        typo_3 = TypoTap(
            cluster_api_endpoint='https://www.mock.com',
            api_key='typo_key',
            api_secret='typo_secret',
            repository='mock',
            dataset='mock',
            audit_id='123'
        )
        typo_3.token = '123'

        with self.assertRaises(SystemExit) as cm:
            typo_3.get_dataset("mock")
        self.assertEqual(cm.exception.code, 1)

    def test_discover_mode(self):
        print('Test: In discover mode, a "generic" schema will be provided.')

        # Expected function return
        expected_return = {
            'streams': [
                {
                    'stream': 'channel', 
                    'tap_stream_id': 'channel', 
                    'schema': {
                        'type': [
                            'null', 
                            'object'
                        ],
                        'additionalProperties': True, 
                        'properties': {}
                    }, 
                    'metadata': [], 
                    'key_properties': []
                    }
                ]
        }

        input_config = {
            'dataset': 'channel'
        }

        schema_return = init.discover(input_config['dataset'])
        self.assertEqual(schema_return, expected_return)


if __name__ == '__main__':
    unittest.main()
