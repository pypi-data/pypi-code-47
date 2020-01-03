from typing import Dict, Optional

import psycopg2
from psycopg2.extensions import TRANSACTION_STATUS_UNKNOWN
from psycopg2.pool import AbstractConnectionPool

from canopy_toolkit.database.abstract import AbstractConnector


class VaultThreadedConnectionPool(AbstractConnectionPool):
    """A connection pool that works with the threading module."""

    def __init__(self, minconn, maxconn, vault_psycopg, *args, **kwargs):
        """Initialize the threading lock."""
        import threading
        AbstractConnectionPool.__init__(
            self, minconn, maxconn, *args, **kwargs
        )
        self._vault_psycopg = vault_psycopg
        self._lock = threading.Lock()

    def getconn(self, key=None):
        """
        Get a free connection and assign it to 'key' if not None.

        :param str key: the key referencing the connection
        :return: An instance of :class:`~psycopg2.extensions.connection`.
        """
        self._lock.acquire()
        try:
            return self._getconn(key)
        except psycopg2.OperationalError as e:
            err = str(e).lower()
            if 'authentication failed' in err:
                self._kwargs = self._vault_psycopg.connection_attributes
                return self._getconn(key)
            raise e
        finally:
            self._lock.release()

    def putconn(self, conn=None, key=None, close=False):
        """
        Put away an unused connection.

        :param psycopg2.extensions.connection conn: the connection to return
        :param str key: the connection reference key
        :param bool close: should the connection be closed
        """
        self._lock.acquire()
        try:
            self._putconn(conn, key, close)
        finally:
            self._lock.release()

    def closeall(self):
        """Close all connections (even the one currently in use)."""
        self._lock.acquire()
        try:
            self._closeall()
        finally:
            self._lock.release()


class PsycopgConnector(AbstractConnector):
    """A vault-backed interface to PostgreSQL via psycopg2."""

    _connection: Optional[psycopg2.extensions.connection] = None
    _connection_pool: Optional[VaultThreadedConnectionPool] = None

    def __init__(
            self, host: str, database: str, user=None, password=None, port: int = 5432,
            min_connections: int = 1, max_connections: int = 2, role: str = None, vault_config: Dict = None
    ):
        """
        Create an instance of the psycopg2 database connector.

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
        AbstractConnector.__init__(
            self, host, database, user, password, port, min_connections, max_connections, role, vault_config
        )

    @property
    def connection(self):
        """
        Get a valid psycopg2 connection instance.

        :return: An instance of :class:`~psycopg2.extensions.connection`.
        """
        if self._connection and not self._connection.closed:
            try:
                if self._connection.get_transaction_status() != TRANSACTION_STATUS_UNKNOWN:
                    # server connection is not lost
                    return self._connection
            except psycopg2.Error:
                pass
        self._connection = self.create_connection()
        return self._connection

    @property
    def connection_pool(self) -> VaultThreadedConnectionPool:
        """
        Get a valid psycopg2 connection pool.

        :return: An instance of :class:`~canopy_toolkit.database.psycopg2.VaultThreadedConnectionPool`.
        """
        if self._connection_pool:
            return self._connection_pool
        self._connection_pool = self.create_connection_pool()
        return self._connection_pool

    @property
    def _psycopg_connection_attributes(self):
        """
        Psycopg2-specific connection attributes.

        :return: a dictionary with psycopg2 specific connection attributes
        """
        attrs = self.connection_attributes
        return {
            'host': attrs['host'],
            'port': attrs['port'],
            'dbname': attrs['database'],
            'user': attrs['user'],
            'password': attrs['password']
        }

    def create_connection_pool(self) -> VaultThreadedConnectionPool:
        """
        Create a new psycopg2 connection pool.

        :return: An instance of :class:`~canopy_toolkit.database.psycopg2.VaultThreadedConnectionPool`.
        """
        return VaultThreadedConnectionPool(
            minconn=self._min_connections,
            maxconn=self._max_connections,
            vault_psycopg=self,
            **self._psycopg_connection_attributes
        )

    def create_connection(self):
        """
        Create a new psycopg2 connection.

        :return: An instance of :class:`~psycopg2.extensions.connection`.
        """
        return psycopg2.connect(**self._psycopg_connection_attributes)
