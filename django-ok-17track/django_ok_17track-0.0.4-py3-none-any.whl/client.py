from typing import NamedTuple, Dict, Union

import requests

from track17.utils import get_api_key

__all__ = (
    'Response',
    'Track17Client'
)

Response = NamedTuple('Response', [
    ('status_code', int),
    ('data', Dict)
])


class Track17Client:
    """
    Client class that implements basic REST methods to make requests to the
    server.
    """
    API_BASE_URL = 'https://api.17track.net/track/'
    API_VERSION = 1

    def __init__(
        self,
        api_base_url: str = None,
        api_version: str = None,
    ):
        """
        Initializes api connector. Received parameters required to
        connect remote server.

        Args:
            api_base_url (str, optional): Base url used to construct url.
            api_version (str, optional): API version to use.
        """
        self.api_base_url = api_base_url or self.API_BASE_URL
        self.api_version = api_version or self.API_VERSION

    def get_base_headers(self) -> Dict:
        return {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
            "Content-Type": "application/json",
        }

    def get_auth_headers(self) -> Dict:
        return {
            "17token": get_api_key()
        }

    def construct_url(self, *args) -> str:
        """
        Returns url with joined args as parts of url.

        Args:
            *args: part of url.

        Returns:
            str: URL
        """
        url = self.api_base_url

        if self.api_version:
            url += f'v{self.api_version}/'

        if not args:
            return url

        joined_args = '/'.join([x.strip('/') for x in args])

        return f'{url}{joined_args}'

    def post(
        self,
        path: str,
        data: Union[Dict, str] = None,
        headers: Dict = None,
    ):
        """
        Method used to send post request to the remote REST API server.

        Args:
            path (str): Corresponding relative path to send request.
            data ([Dict, str], optional): Dictionary, list of tuples, bytes, or file-like object to send.
            headers (Dict, optional): Request headers.

        Returns:
            Response: requests' response instance.

        Raises:
            AttributeError: Unsupported method was used.
        """
        url = self.construct_url(path)

        if headers is None:
            headers = {}

        headers.update(self.get_base_headers())
        headers.update(self.get_auth_headers())

        response = requests.post(url, data, headers=headers)

        return Response(
            status_code=response.status_code,
            data=response.json()
        )
