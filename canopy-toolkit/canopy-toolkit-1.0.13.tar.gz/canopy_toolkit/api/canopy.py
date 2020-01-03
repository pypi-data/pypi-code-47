import posixpath
import tempfile
from typing import List, Dict, Optional, IO

from requests import HTTPError

from canopy_toolkit.api.base import BaseCanopyClient
from canopy_toolkit.api.exceptions import CanopyAPIException


class CanopyClient(BaseCanopyClient):
    """The Canopy API Client."""

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
        Create a new instance of the Canopy Python client with utility methods for common endpoints.

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
        BaseCanopyClient.__init__(
            self, api_server, username, password, mfa_secret_key,
            mfa_code, role, vault_config, app_id, engine_server, ephemeral_file_server, websocket_server,
            retries, retry_backoff_factor
        )

    def lookup_user(self, username: str) -> Optional[Dict]:
        """
        Lookup a user by username from the backend.

        :param username: the username to search
        :return: the user details as dictionary if found else None
        """
        res = self.get('admin/users', params={'keyword': username, 'page': '1', 'per_page': '30'})
        for user in res['users']:
            if user['username'] == username:
                return user
        return None

    def get_reports_templates(self, language: str = 'en') -> List[Dict]:
        """
        List all reports template.

        :param language: the language to search (default: en)
        :return: a list of template information
        """
        return self.get('reports/templates', params={'language': language})

    def get_tableau_details(self, device: str = 'desktop') -> List[str]:
        """
        Get the tableau details for a user.

        :param device: the device to look for (default: desktop)
        :return: a list of tableau tokens
        """
        return self.get('tableau_details', params={'device': device})

    def validate_filename(self, filename: str) -> Optional[Dict]:
        """
        Validate the given filename.

        :param filename: the file name to validate
        :return: None if file name valid else the error response as dictionary
        """
        res = self.ephemeral_session.post('upload/validate_filename', json={'filename': filename})
        if res.status_code >= 500:
            raise CanopyAPIException('Failed to validate filename', res)
        try:
            res.raise_for_status()
            return None
        except HTTPError:
            return res.json()

    def list_assets(self, sub_path: str, partner: str) -> List[Dict]:
        """
        List assets for a partner.

        :param sub_path: the sub path to look for
        :param partner: the partner whose assets to load
        :return: list of assets
        """
        res = self.ephemeral_session.get(posixpath.join('assets', sub_path.replace('/', ''), partner.replace('/', '')))
        if not res.ok:
            raise CanopyAPIException('Failed to list assets', res)
        return res.json()

    def upload_file_to_ephemeral(self, file_handle: IO) -> Dict:
        """
        Upload a given file handle to ephemeral s3 bucket.

        :param file_handle: the file handle of the opened file to upload
        :return: the response as dictionary
        """
        res = self.ephemeral_session.post('upload', files={'file': file_handle})
        if not res.ok:
            raise CanopyAPIException('Failed to upload file', res)
        return res.json()

    def download_file_by_key(self, key: str) -> str:
        """
        Download a file by key and store it to a temp file.

        :param key: the file reference key
        :return: the path to the downloaded file
        """
        res = self.ephemeral_session.get('get_file', params={'download': 'true', 'key': key})
        if not res.ok:
            raise CanopyAPIException('Failed to download file', res)
        temp_file = tempfile.mktemp()
        with open(temp_file, 'wb') as fd:
            for chunk in res.iter_content(chunk_size=128):
                fd.write(chunk)
        return temp_file


cached_clients = {}


def get_canopy_client(*args, **kwargs) -> CanopyClient:
    """
    Get a new logged in canopy client. Return from cache if already used. Else create new.

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
    :return: an authenticated Canopy API client instance
    """  # noqa: to not throw an error for the above args documentation
    kwargs = {
        k: kwargs[k] for k in kwargs
        if k in list(CanopyClient.__init__.__code__.co_varnames)
    }

    api_server = kwargs.get('api_server')
    username = kwargs.get('username')

    if len(args) > 2:
        username = args[1]
        api_server = args[0]

    cache_key = f'{api_server}:{username}'

    if cache_key in cached_clients:
        return cached_clients[cache_key]

    client = CanopyClient(*args, **kwargs)
    client.login()
    cached_clients[cache_key] = client
    return client
