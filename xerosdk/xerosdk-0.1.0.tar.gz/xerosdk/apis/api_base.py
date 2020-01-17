"""
API base class
"""

import json
import requests

from ..exceptions import *


class ApiBase:
    """
    Base class for all API classes
    """

    def __init__(self):
        self.__access_token = None
        self.__tenant_id = None
        self.__server_url = None

    def change_access_token(self, access_token):
        """
        Change old access token with a new one
        Parameters:
            access_token (str): New access token
        """

        self.__access_token = access_token

    def set_server_url(self, server_url):
        """
        Set server URL while creating a connection

        Parameters:
            server_url (str): Server URL for Xero API
        """

        self.__server_url = server_url

    def set_tenant_id(self, tenant_id):
        """
        Set tenant id while creating connection
        Parameters:
            tenant_id (str): Xero tenant ID
        """

        self.__tenant_id = tenant_id

    def _get_request(self, api_url):
        """
        HTTP get request to a given Xero API URL

        Parameters:
            api_url (str): URL of Xero API
        """

        api_headers = {
            'authorization': 'Bearer ' + self.__access_token,
            'xero-tenant-id': self.__tenant_id,
            'accept': 'application/json'
        }

        response = requests.get(
            self.__server_url+api_url,
            headers=api_headers
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result

        if response.status_code == 403:
            raise UnsuccessfulAuthentication(
                'Invalid xero tenant ID or xero-tenant-id header missing'
            )

        if response.status_code == 500:
            raise InternalServerError(
                'Internal server error'
            )

        raise XeroSDKError(
            response.text, response.status_code
        )

    def _post_request(self, data, api_url):
        """
        HTTP post method to send data to Xero API URL

        Parameters:
            data (dict): Data to be sent to Xero API
            api_url (str): URL of Xero API
        """

        api_headers = {
            'Authorization': 'Bearer ' + self.__access_token,
            'xero-tenant-id': self.__tenant_id,
            'accept': 'application/json'
        }

        response = requests.post(
            self.__server_url + api_url,
            headers=api_headers,
            json=data
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result

        if response.status_code == 400:
            error_msg = json.loads(response.text)["Message"]
            raise XeroSDKError(
                error_msg, response.status_code
            )
        if response.status_code == 500:
            raise InternalServerError(
                'Internal server error'
            )

        raise XeroSDKError(
            response.text, response.status_code
        )
