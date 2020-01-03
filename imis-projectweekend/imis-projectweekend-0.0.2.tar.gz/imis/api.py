from dataclasses import dataclass

import requests

import imis.iqa as iqa


class ApiError(Exception):
    pass


class AuthError(ApiError):
    pass


@dataclass
class Auth:

    access_token: str
    token_type: str
    expires_in: int
    user_name: str

    @property
    def authorization_header(self):
        return '{0} {1}'.format(self.token_type, self.access_token)


class Client:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self._auth = self._authenticate()

    def _authenticate(self):
        data = {
            'grant_type': 'password',
            'username': self.username,
            'password': self.password
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = '{0}/token'.format(self.url)
        response = requests.post(url=url, data=data, headers=headers)
        if response.status_code == 400:
            data = response.json()
            raise AuthError(data['error_description'])

        data = response.json()
        return Auth(access_token=data['access_token'],
                    token_type=data['token_type'],
                    expires_in=data['expires_in'],
                    user_name=data['userName'])

    @property
    def auth(self):
        if self._auth is None:
            self._auth = self._authenticate()
        return self._auth

    @auth.setter
    def auth(self, val):
        self._auth = val

    def iqa(self, query_name, *parameters):
        return iqa.iter_items(self, query_name, *parameters)
