from urllib.parse import urlencode
import requests

from .base import (
    Users, Locations,
)


class FtAPI:
    BASE_URL = 'https://api.intra.42.fr/v2/'
    MAX_TRY_COUNT = 5

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.try_count = 0
        self.refresh_token()

        self.users = Users(self)
        self.locations = Locations(self)

    def refresh_token(self):
        query = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        url = self._make_url(self.BASE_URL, 'oauth/token', query)
        res = requests.post(url)
        if res.status_code != 200:
            print('Error')
            return
        self.token = res.json().get('access_token')

    def api(self, method, url, **kwargs):
        res = self.resolve_method(method)(url, **kwargs)
        if res.status_code == 401:
            # Not authorized error
            if self.try_count >= self.MAX_TRY_COUNT:
                raise Exception('cant get access_token')
            self.try_count += 1
            self.refresh_token()
            return self.api(method, url, **kwargs)
        self.try_count = 0
        return res

    @staticmethod
    def resolve_method(method: str):
        method = method.upper()
        if method == 'GET':
            return requests.get
        elif method == 'POST':
            return requests.post

    @staticmethod
    def _make_url(base, url='', query=None):
        if query is None:
            query = {}
        return f'{base}{url}?{urlencode(query)}'

    def make_url(self, base, url='', query=None):
        if not query:
            query = {}
        query.update(
            access_token=self.token,
        )
        return self._make_url(base, url, query)
