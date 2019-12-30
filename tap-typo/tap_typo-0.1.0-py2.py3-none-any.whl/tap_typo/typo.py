# Copyright 2019 Typo
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

import sys
import json  # noqa
import requests

import singer

# Singer Logger
logger = singer.get_logger()


class TypoTap():
    '''
    Typo Module Constructor
    '''

    def __init__(self, api_key, api_secret, cluster_api_endpoint, repository, dataset, audit_id):
        logger.debug('__init__ - self=[%s], api_key=[%s], api_secret=[%s], cluster_api_endpoint=[%s], dataset=[%s], audit_id=[%s]',
                        self, api_key, api_secret, cluster_api_endpoint, dataset, audit_id)
        self.base_url = cluster_api_endpoint
        self.api_key = api_key
        self.api_secret = api_secret
        self.repository = repository
        self.dataset = dataset
        self.audit_id = audit_id

    def post_request(self, url, headers, payload):
        '''
        Generic POST request
        '''

        logger.debug('post_request - self=[%s], url=[%s], headers=[%s], payload=[%s]', self, url, headers, payload)

        try:
            r = requests.post(url, headers=headers, data=json.dumps(payload))
            logger.debug('post_request - r.text=[%s], data=[%s]', r.text, json.dumps(payload))
        except Exception as e:
            logger.error('post_request - Request failed.')
            logger.error(e)
            sys.exit(1)

        logger.debug('post_request - url=[%s], request.status_code=[%s]', url, r.status_code)
        status = r.status_code
        data = r.json()

        if status != 200:
            logger.error('post_request - url=[%s], request.status_code=[%s], response.text=[%s]', url, r.status_code, r.text)
        
        return status, data

    def get_request(self, url, headers, params=None):
        '''
        Generic GET request
        '''

        # Required parameters
        r = requests.get(url, headers=headers, params=params)
        status = r.status_code
        data = r.json()

        logger.debug('get_request - url=[%s], request.status_code=[%s]', url, r.status_code)

        if status != 200:
            logger.error('get_request - url=[%s], request.status_code=[%s], response.text=[%s]', url, r.status_code, r.text)

        return status, data

    def request_token(self):
        '''
        Token Request for other requests
        '''

        logger.debug('request_token - self=[%s]', self)
        # Required parameters
        url = self.base_url.rstrip('/') + '/token'
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "apikey": self.api_key,
            "secret": self.api_secret
        }

        # POST request
        try:
            status, data = self.post_request(url, headers, payload)
        except Exception:
            logger.error('request_token - Please validate your configuration inputs.', exc_info=True)
            sys.exit(1)
            
        # Check Status
        if status != 200:
            logger.error(
                'request_token - Token Request Failed. Please check your credentials. Details: '+
                '{}'.format(data))
            sys.exit(1)

        return data['token']

    def get_dataset(self, dataset):
        '''
        Get Typo dataset
        '''

        # Required parameters
        url = "{0}/repositories/{1}/datasets/{2}/audits/{3}/results".format(
            self.base_url, self.repository, self.dataset, self.audit_id)

        headers = {
            "Content-Type": "application/json", "Authorization": "Bearer {}".format(self.token)
        }

        # Get request
        status, data = self.get_request(url, headers)

        # Check Status
        if status != 200:
            logger.error(data["message"])
            sys.exit(1)

        logger.debug('get_dataset - dataset=[%s], data=[%s]', dataset, data)
        
        output_data = []
        for i in data['data']:
            temp_json = i['data']

            # Inserting output results from Typo
            if i['hasErrors']:
                temp_json['__typo_result'] = 'Error'
            else:
                temp_json['__typo_result'] = 'OK'
                
            output_data.append(i['data'])

        # return data
        return output_data
