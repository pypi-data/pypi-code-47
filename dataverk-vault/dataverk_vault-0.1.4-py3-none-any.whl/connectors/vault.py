import requests


class VaultConnector:

    def __init__(self, settings):
        self._settings = settings

    @property
    def secrets(self):
        return self._read_secrets()

    def db_credentials(self, vault_path):
        return self._read_db_credentials(vault_path)

    def __enter__(self):
        self._client_token = self._authenticate()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _read_secrets(self):
        """ Fetch secrets from vault and return dict

        :return: dict: secrets
        """
        res = requests.get(self._settings["secrets_url"],
                           headers={"X-Vault-Token": self._client_token})
        res.raise_for_status()
        return res.json()["data"]

    def _read_db_credentials(self, vault_path):
        """ Get new database credentials

        :param vault_path: str
        :return: string with username and password
        """
        res = requests.get(f"{self._settings['vault_address']}/v1/{vault_path}",
                           headers={"X-Vault-Token": self._client_token})

        res.raise_for_status()
        credentials = res.json()["data"]
        return f"{credentials['username']}:{credentials['password']}"

    def _authenticate(self):
        res = requests.post(self._settings["auth_url"],
                            json={"jwt": self._settings["token"], "role": self._settings["app_name"]})
        res.raise_for_status()
        return res.json()["auth"]["client_token"]
