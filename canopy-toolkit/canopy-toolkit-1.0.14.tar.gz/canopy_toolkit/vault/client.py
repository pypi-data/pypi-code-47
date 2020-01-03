import os
import sys
import urllib.request
import threading
from typing import Optional, Dict, Tuple
from urllib.parse import urlparse, ParseResult

import botocore.session
import hvac
from hvac import Client
from hvac.api.auth_methods import Aws

default_vault_address = os.getenv('VAULT_ADDR', 'http://127.0.0.1:8200')


class Vault:
    """The Canopy Vault client."""

    vault_server: str = default_vault_address
    authentication_mode: str = 'token'

    _client: Optional[Client] = None
    _instance: Optional = None
    _lock = threading.Lock()

    parameters: Dict = {}

    @classmethod
    def instance(cls, server=default_vault_address, authentication_mode='token', client=None, **kwargs):
        """
        Get an instance of vault.

        :param str server: the url of the vault server
        :param str authentication_mode: Mode of authentication (token/iam/ec2)
        :param hvac.v1.Client client: the hvac client to use if required
        :param dict kwargs: any additional parameters
        :return: A vault client instance
        """
        with Vault._lock:
            if Vault._instance is None or 'pytest' in sys.modules:
                Vault._instance = Vault(server, authentication_mode, client, **kwargs)
        return Vault._instance

    def __init__(self, server=default_vault_address, authentication_mode='token', client=None, **kwargs):
        """
        Create an instance of vault.

        :param str server: the url of the vault server
        :param str authentication_mode: Mode of authentication (token/iam/ec2)
        :param hvac.v1.Client client: the hvac client to use if required
        :param kwargs: any additional parameters
        """
        self.authentication_mode = authentication_mode
        self.vault_server = server
        self.parameters = kwargs
        self._client = client

    @property
    def client(self) -> Client:
        """
        Get an authenticated HVAC Vault client.

        :return: An authenticated instance of :class:`~hvac.v1.Client`.
        """
        if self._client is not None:
            # if client is already authenticated use that directly instead of creating a new one.
            if self._client.is_authenticated():
                return self._client
            else:
                # noinspection PyBroadException
                try:
                    self._client.close()
                except Exception:
                    pass

        client = hvac.Client(url=self.vault_server)
        if self.authentication_mode == 'token':
            client.token = self.parameters['token']
        elif self.authentication_mode == 'iam':
            session = botocore.session.get_session()
            credentials = session.get_credentials()
            aws = Aws(client.adapter)
            vault_server_url: ParseResult = urlparse(self.vault_server)
            region = self.parameters.get('region')
            aws.iam_login(
                access_key=credentials.access_key,
                secret_key=credentials.secret_key,
                session_token=credentials.token,
                role=self.parameters['role'],
                header_value=self.parameters.get('iam_header', vault_server_url.netloc.partition(':')[0]),
                region='us-east-1' if region is None else region
            )
        elif self.authentication_mode == 'ec2':
            metadata_service = self.parameters.get('metadata_service', 'http://169.254.169.254')
            contents = urllib.request.urlopen(f'{metadata_service}/latest/dynamic/instance-identity/pkcs7')\
                .read() \
                .decode('utf-8') \
                .replace('\n', '')
            aws = Aws(client.adapter)
            aws.ec2_login(contents, nonce=self.parameters['nonce'], role=self.parameters['role'], mount_point='aws')
        else:
            getattr(client, 'auth_' + self.authentication_mode)(**self.parameters)

        self._client = client
        return self._client

    def logout(self, revoke_token=True):
        """
        Logout and reset the vault client.

        :param bool revoke_token: should the token be revoked (Defaults to True)
        """
        self._client.logout(revoke_token=revoke_token)
        self._client = None

    def get_database_credentials(self, role: str) -> Tuple[str, str, int]:
        """
        Get the database credentials.

        :param str role: the role to get credentials for
        :return: a tuple containing (username, password, lease_duration)
        """
        credentials = self.client.read(f'database/creds/{role}')
        return credentials['data']['username'], credentials['data']['password'], credentials['lease_duration']

    def get_system_credentials(self, role: str):
        """
        Get system user credentials.

        :param str role: the role to get credentials for
        :return: a tuple containing (username, token, lease_duration)
        """
        credentials = self.client.read(f'system-user/tokens/{role}')
        return credentials['data']['username'], credentials['data']['token'], credentials['data']['token_ttl']
