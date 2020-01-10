import requests

import imis.iqa as iqa


class ApiError(Exception):
    pass


class AuthError(ApiError):
    pass


class Auth:

    def __init__(self, access_token, token_type, expires_in, user_name):
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.user_name = user_name

    @property
    def authorization_header(self):
        return '{0} {1}'.format(self.token_type, self.access_token)

    @classmethod
    def authenticate(cls, url, username, password):
        data = {
            'grant_type': 'password',
            'username': username,
            'password': password
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url=url, data=data, headers=headers)
        if response.status_code == 400:
            data = response.json()
            raise AuthError(data['error_description'])

        data = response.json()
        return cls(access_token=data['access_token'],
                    token_type=data['token_type'],
                    expires_in=data['expires_in'],
                    user_name=data['userName'])


class Client:

    _authenticator = Auth

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self._auth = Client._authenticator.authenticate(f'{url}/token', username, password)

    @property
    def auth(self):
        if self._auth is None:
            self._auth = Client._authenticator.authenticate(f'{self.url}/token', self.username, self.password)
        return self._auth

    @auth.setter
    def auth(self, val):
        self._auth = val

    def iqa(self, query_name, *parameters):
        return iqa.iter_items(self, query_name, *parameters)
