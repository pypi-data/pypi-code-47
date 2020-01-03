from typing import Dict, Optional

from canopy_toolkit.vault.client import Vault


class AbstractConnector:
    """A vault-backed interface to PostgreSQL via different connectors."""

    host: str
    database: str
    user: str
    port: int = 5432

    _min_connections: int = 1
    _max_connections: int = 2

    __password: Optional[str] = None

    __role: Optional[str] = None
    __vault_config: Optional[Dict] = None
    __vault: Optional[Vault] = None

    def __init__(
            self, host: str, database: str, user=None, password=None, port: int = 5432,
            min_connections: int = 1, max_connections: int = 2, role: str = None, vault_config: Dict = None
    ):
        """
        Create an instance of the database connector.

        :param str host: the database instance hostname to connect to
        :param str database: name of the database to connect to
        :param str user: the username to connect as
        :param str password: the password to authentication
        :param int port: the database port (Default: 5432)
        :param int min_connections: Number of connection the pool will be initialized with (Default: 1)
        :param int max_connections: Max number of connections in the pool (Default: 2)
        :param str role: the role to get credentials for from vault
        :param dict vault_config: The vault connect configuration
        """
        if (user is None or password is None) and (vault_config is None or role is None):
            raise ValueError(
                'user + password (or) role+ vault_config is required to authentication with the database'
            )

        if min_connections == 0 and max_connections == 0:
            raise ValueError(
                'min_connections and max_connections cannot be zero'
            )

        if min_connections > max_connections:
            raise ValueError(
                'min_connections cannot be greater than max_connections'
            )

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.__password = password
        self.__role = role
        self.__vault_config = vault_config

        self._min_connections = min_connections
        self._max_connections = max_connections

        if self.__vault_config:
            self.__vault = Vault.instance(**vault_config)

    @property
    def connection_attributes(self) -> Dict:
        """
        Get the connection attributes to create a new connection.

        :return: a dictionary with common connection attributes.
        """
        lease_duration = None
        if self.__vault and self.__role is not None:
            self.user, self.__password, lease_duration = self.__vault.get_database_credentials(self.__role)

        return {
            'host': self.host,
            'port': self.port,
            'database': self.database,
            'user': self.user,
            'password': self.__password,
            'metadata': {
                'lease_duration': lease_duration
            }
        }
