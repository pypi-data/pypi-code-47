from typing import Union


class BaseAPI:
    BASE_URL = 'https://api.intra.42.fr/v2/'
    URL = ''

    def __init__(self, ft_api):
        self.base_api = ft_api

    @property
    def token(self):
        return self.base_api.token

    def refresh_token(self):
        self.base_api.refresh_token()

    def __call__(self, method, query=None, **kwargs):
        url = self.base_api.make_url(self.BASE_URL, self.URL, query)
        return self.base_api.api(method, url, **kwargs)


class Users(BaseAPI):
    URL = 'users'

    def __call__(self, query=None, **kwargs):
        return super().__call__('get', query, **kwargs)


class Locations(BaseAPI):
    URL = 'locations'

    def __call__(self, query=None, **kwargs):
        return super().__call__('get', query, **kwargs)
