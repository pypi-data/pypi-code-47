import time
from typing import Dict, Union, List, Any, Optional, Tuple

import pyotp
from requests.adapters import HTTPAdapter
from requests.auth import AuthBase
from requests_toolbelt.sessions import BaseUrlSession
from urllib3 import Retry

from canopy_toolkit.api.exceptions import CanopyAPIException, CanopyClientException, \
    MultiFactorAuthenticationRequired, MultiFactorActivationRequired
from canopy_toolkit.vault.client import Vault

CanopyResponseDataTypes = Union[Any, Dict]
CanopyResponse = Union[List[CanopyResponseDataTypes], CanopyResponseDataTypes]


class RequestsAuthenticator(AuthBase):
    """Authenticator for requests session to handle token refreshing."""

    def __init__(self, base_client):
        """
        Initialize the authenticator.

        :param base_client: the base canopy client
        """
        self.base_client = base_client

    def __call__(self, r):
        """
        Refresh the token.

        :param r: the request to mutate with new token
        :return: the modified request
        """
        self.base_client.ensure_session()
        if self.base_client.token is not None:
            r.headers['Authorization'] = self.base_client.token
        return r


class BaseCanopyClient:
    """The Basic Canopy API Client."""

    token: Optional[str] = None
    username: Optional[str] = None

    session: BaseUrlSession
    engine_session: BaseUrlSession
    ephemeral_session: BaseUrlSession
    current_user_id: Optional[int] = None

    _token_valid_until: Optional[int] = None

    __password: Optional[str] = None
    __mfa_secret_key: Optional[str] = None
    __mfa_code: Optional[str] = None

    __role: Optional[str] = None
    __vault_config: Optional[Dict] = None
    __vault: Optional[Vault] = None

    def __init__(
            self,
            api_server: str,
            username: str = None,
            password: str = None,
            mfa_secret_key: str = None,
            mfa_code: str = None,
            role: str = None,
            vault_config=None,
            app_id: str = 'canopy_python_sdk',
            engine_server: Optional[str] = None,
            ephemeral_file_server: str = 'https://ephemeral.canopy.cloud',
            websocket_server: str = None,
            retries: int = 3,
            retry_backoff_factor: float = 0.3
    ):
        """
        Create a new instance of the Basic Canopy Python client.

        :param str api_server: The API server to connect to.
        :param str username: The username to login with.
        :param str password: The password to login with.
        :param str mfa_secret_key: The MFA secret to generate the TOTP pin code. (Ignored if mfa_code is provided)
        :param str mfa_code: The TOTP pin code to use.
        :param str role: the role to get credentials for from vault
        :param dict vault_config: The vault connect configuration
        :param str app_id: The App ID
        :param str engine_server: The engine server to connect to.
        :param str ephemeral_file_server: The server of the ephemeral file service
        :param str websocket_server: websocket endpoint hostname
        :param int retries: number of times to retry failed requests
        :param float retry_backoff_factor: a backoff factor to apply between attempts after the second try
        """
        if (username is None or password is None) and (role is None or vault_config is None):
            raise CanopyClientException(
                'Username + password (or) role + vault_config is required to authentication with canopy API'
            )

        self.api_server = api_server
        self.websocket_server = websocket_server
        self.username = username

        self.__password = password
        self.__mfa_secret_key = mfa_secret_key
        self.__mfa_code = mfa_code

        self.__role = role
        self.__vault_config = vault_config
        if vault_config is not None:
            self.__vault = Vault.instance(**vault_config)

        if engine_server is None:
            engine_server = api_server.replace('api', 'engine', 1)

        self.session = BaseUrlSession(base_url=f'{api_server}/api/v1/')
        self.engine_session = BaseUrlSession(base_url=engine_server)
        self.ephemeral_session = BaseUrlSession(base_url=f'{ephemeral_file_server}/api/v1/')

        self.session.auth = RequestsAuthenticator(self)
        self.engine_session.auth = RequestsAuthenticator(self)

        for s in self._sessions:
            # Configure request retries if required
            if retries > 0:
                adapter = HTTPAdapter(
                    max_retries=Retry(
                        total=retries,
                        read=retries,
                        connect=retries,
                        backoff_factor=retry_backoff_factor,
                        status_forcelist=(500, 502, 503, 504),
                        method_whitelist=None
                    )
                )
                s.mount('http://', adapter)
                s.mount('https://', adapter)
            s.headers.update({
                'x-auth-username': username,
                'x-app-id': app_id,
                'user-agent': 'CanopyPythonSDK/1.0'
            })

    def set_token(self, token: str):
        """
        Set the authorization token for the client.

        :param str token: the authorization token to set
        """
        self.token = token
        for c in self._sessions:
            c.headers.update({
                'authorization': token
            })

    def websocket(self):
        """Get an instance of a websocket client."""
        from canopy_toolkit.api.websocket import CanopyWebsocketClient
        return CanopyWebsocketClient(self)

    def login(self):
        """Log the user in and store the token for future user."""
        if self._uses_vault:
            self._login_via_vault()
        else:
            self._login_via_userpass()
        return self

    def _login_via_vault(self):
        """Perform the login operation via Vault system user."""
        self.username, self.token, lease_duration = self.__vault.get_system_credentials(self.__role)
        self._token_valid_until = time.time() + lease_duration
        self.set_token(self.token)

    def _login_via_userpass(self):
        """Perform the login operation via username-password-mfa."""
        res = self.session.post('sessions', json={
            'user': {
                'username': self.username,
                'password': self.__password,
            }
        })
        if res.ok:
            body = res.json()

            self.current_user_id = body['id']
            token = body['token']
            login_flow = body['login_flow']

            if login_flow == 'logged_in':
                return self.set_token(token)

            if login_flow == '2fa_verification':
                mfa_code = self.__mfa_code
                if mfa_code is None:
                    if self.__mfa_secret_key is None:
                        raise MultiFactorAuthenticationRequired('MFA secret key or OTP is required.')
                    mfa_code = pyotp.TOTP(self.__mfa_secret_key).now()

                res = self.session.post(
                    'sessions/otp/validate',
                    params={'otp_code': mfa_code},
                    headers={'authorization': token}
                )
                if res.ok:
                    return self.set_token(res.json()['token'])
                else:
                    raise CanopyAPIException('OTP Validation Failed', res)

            if login_flow == '2fa_activation':
                raise MultiFactorActivationRequired('This account requires 2FA Activation before use.')
            else:
                raise CanopyClientException(f'Unhandled login flow {login_flow}.')
        else:
            raise CanopyAPIException('User login failed', res)

    def lookup_self(self) -> Dict:
        """
        Get details of the current logged in user.

        :return: the user details as a dictionary
        """
        self_user = self.get('user_details')
        self.current_user_id = self_user['id']
        return self_user

    def get(
            self,
            path: str,
            params: Dict = None,
            headers: Dict = None,
            connection_id: str = None,
            engine: bool = False
    ) -> CanopyResponse:
        """
        Make a GET Request to Canopy API.

        :param str connection_id: Connection ID if needs to be requested via websocket
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :param bool engine: Make the request to engine server
        :return: json response as a dictionary
        """
        return self._do_request('GET', path, params, headers, None, connection_id, engine)

    def post(
            self,
            path: str,
            params: Dict = None,
            data: Dict = None,
            headers: Dict = None,
            connection_id: str = None,
            engine: bool = False
    ) -> CanopyResponse:
        """
        Make a POST Request to Canopy API.

        :param str connection_id: Connection ID if needs to be requested via websocket
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :param dict data: The json data (as a dictionary) to send in body
        :param bool engine: Make the request to engine server
        :return: json response as a dictionary
        """
        return self._do_request('POST', path, params, headers, data, connection_id, engine)

    def put(
            self,
            path: str,
            params: Dict = None,
            data: Dict = None,
            headers: Dict = None,
            connection_id: str = None,
            engine: bool = False
    ) -> CanopyResponse:
        """
        Make a PUT request to Canopy API.

        :param str connection_id: Connection ID if needs to be requested via websocket
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :param dict data: The json data (as a dictionary) to send in body
        :param bool engine: Make the request to engine server
        :return: json response as a dictionary
        """
        return self._do_request('PUT', path, params, headers, data, connection_id, engine)

    def patch(
            self,
            path: str,
            params: Dict = None,
            data: Dict = None,
            headers: Dict = None,
            connection_id: str = None,
            engine: bool = False
    ) -> CanopyResponse:
        """
        Make a PATCH request to Canopy API.

        :param str connection_id: Connection ID if needs to be requested via websocket
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :param dict data: The json data (as a dictionary) to send in body
        :param bool engine: Make the request to engine server
        :return: json response as a dictionary
        """
        return self._do_request('PATCH', path, params, headers, data, connection_id, engine)

    def delete(
            self,
            path: str,
            params: Dict = None,
            data: Dict = None,
            headers: Dict = None,
            connection_id: str = None,
            engine: bool = False
    ) -> CanopyResponse:
        """
        Make a DELETE request to Canopy API.

        :param str connection_id: Connection ID if needs to be requested via websocket
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :param dict data: The json data (as a dictionary) to send in body
        :param bool engine: Make the request to engine server
        :return: json response as a dictionary
        """
        return self._do_request('DELETE', path, params, headers, data, connection_id, engine)

    def _do_request(
            self,
            method: str,
            path: str,
            params: Dict = None,
            headers: Dict = None,
            data: Dict = None,
            connection_id: str = None,
            engine: bool = False
    ) -> CanopyResponse:
        """
        Perform a HTTP request to the API server.

        :param str method: the HTTP method to call (GET/POST/PATCH/PUT/DELETE)
        :param str connection_id: Connection ID if needs to be requested via websocket
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :param dict data: The json data (as a dictionary) to send in body
        :param bool engine: Make the request to engine server
        :return: json response as a dictionary
        """
        if connection_id is not None:
            return self._do_websocket_request(connection_id, method=method, path=path, params=params, headers=headers)

        request_session = self.session if not engine else self.engine_session
        self.ensure_session()

        res = getattr(request_session, method.lower())(path, params=params, json=data, headers=headers)
        if not res.ok:
            raise CanopyAPIException(f'Failed to {method.upper()} {path}', res)
        return res.json()

    def _do_websocket_request(
            self,
            connection_id: str,
            method: str,
            path: str,
            params: Dict = None,
            headers: Dict = None
    ):
        """
        Perform a request to the websocket proxy. Response will be received via websocket connection.

        :param str method: the HTTP method to call (GET/POST/PATCH/PUT/DELETE)
        :param str connection_id: Connection ID to match response with request
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :return: json response as a dictionary
        """
        if params is None:
            params = {}
        if headers is None:
            headers = {}

        headers.update({
            'x-auth-username': self.session.headers.get('x-auth-username'),
            'x-app-id': self.session.headers.get('x-app-id'),
            'user-agent': self.session.headers.get('user-agent'),
        })

        self.ensure_session()

        res = self.session.post('/api/ws', json={
            'connectionId': connection_id,
            'request': {
                'method': method,
                'path': path,
                'queryParams': params,
                'headers': headers,
            }
        })
        if not res.ok:
            raise CanopyAPIException('Failed to make a ws request. ', res)
        return res.json()

    def ensure_session(self):
        """Refresh the session if token has expired."""
        if self._uses_vault and (time.time() + 120) > self._token_valid_until:
            self._login_via_vault()

    @property
    def _sessions(self) -> Tuple[BaseUrlSession, ...]:
        """List of sessions to authenticate."""
        return self.session, self.ephemeral_session, self.engine_session

    @property
    def _uses_vault(self) -> bool:
        """If vault should be used for the connection."""
        return self.__vault is not None and self.__role is not None
