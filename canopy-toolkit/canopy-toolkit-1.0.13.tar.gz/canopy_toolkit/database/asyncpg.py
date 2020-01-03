import time
from threading import Timer, Lock
from typing import Optional, Dict, Callable, Coroutine, List

import asyncpg
import async_property
from asyncio_helpers.decorators import coroutine
from asyncpg import Connection
from asyncpg.pool import Pool

from canopy_toolkit.database.abstract import AbstractConnector

buffer_time = 25


class AsyncpgConnector(AbstractConnector):
    """A vault-backed interface to PostgreSQL via asyncpg."""

    _connection: Optional[Connection] = None
    _connection_pool: Optional[Pool] = None

    _max_queries: int
    _max_inactive_connection_lifetime: float

    _init: Optional[Callable] = None
    _setup: Optional[Callable] = None

    lock = Lock()
    timers: List[Timer]

    def __init__(
            self, host: str, database: str, user=None, password=None, port: int = 5432,
            min_connections: int = 1, max_connections: int = 2, max_queries: int = 50000,
            max_inactive_connection_lifetime: float = 300.0, init: Coroutine = None, setup: Coroutine = None,
            role: str = None, vault_config: Dict = None
    ):
        r"""
        Create an instance of the asyncpg database connector.

        :param str host: the database instance hostname to connect to
        :param str database: name of the database to connect to
        :param str user: the username to connect as
        :param str password: the password to authentication
        :param int port: the database port (Default: 5432)
        :param int min_connections: Number of connection the pool will be initialized with (Default: 1)
        :param int max_connections: Max number of connections in the pool (Default: 2)
        :param int max_queries:
            Number of queries after a connection is closed and replaced
            with a new connection.

        :param float max_inactive_connection_lifetime:
            Number of seconds after which inactive connections in the
            pool will be closed.  Pass ``0`` to disable this mechanism.

        :param Coroutine setup:
            A coroutine to prepare a connection right before it is returned
            from :meth:`Pool.acquire() <pool.Pool.acquire>`.  An example use
            case would be to automatically set up notifications listeners for
            all connections of a pool.

        :param Coroutine init:
            A coroutine to initialize a connection when it is created.
            An example use case would be to setup type codecs with
            :meth:`Connection.set_builtin_type_codec() <\
            asyncpg.connection.Connection.set_builtin_type_codec>`
            or :meth:`Connection.set_type_codec() <\
            asyncpg.connection.Connection.set_type_codec>`.
        :param str role: the role to get credentials for from vault
        :param dict vault_config: The vault connect configuration
        """
        AbstractConnector.__init__(
            self, host, database, user, password, port, min_connections, max_connections, role, vault_config
        )
        self._max_queries = max_queries
        self._max_inactive_connection_lifetime = max_inactive_connection_lifetime
        self._init = init
        self._setup = setup
        self.timers = []

    @async_property.async_property
    async def connection(self) -> Connection:
        """
        Get a valid asyncpg connection instance (existing instance is returned if already available).

        :return: An instance of :class:`~asyncpg.connection.Connection`.
        """
        if self._connection and not self._connection.is_closed():
            return self._connection
        self._connection = await self.create_connection()
        return self._connection

    @async_property.async_property
    async def connection_pool(self) -> Pool:
        """
        Get a valid asyncpg connection pool. (existing pool is returned if already available).

        :return: An instance of :class:`~asyncpg.pool.Pool`.
        """
        if self._connection_pool:
            return self._connection_pool
        self._connection_pool = await self.create_connection_pool()
        return self._connection_pool

    async def create_connection(self) -> Connection:
        """
        Create a new asyncpg connection.

        :return: An instance of :class:`~asyncpg.connection.Connection`.
        """
        attributes = self.connection_attributes.copy()
        del attributes['metadata']
        return await asyncpg.connect(**attributes)

    async def create_connection_pool(self) -> Pool:
        """
        Create a new asyncpg connection pool.

        :return: An instance of :class:`~asyncpg.pool.Pool`.
        """
        attributes = self.connection_attributes.copy()
        metadata = attributes['metadata']
        del attributes['metadata']

        expires_at = None

        if metadata['lease_duration'] is not None:
            expires_at = time.time() + metadata['lease_duration']

        pool = await asyncpg.create_pool(
            min_size=self._min_connections,
            max_size=self._max_connections,
            max_queries=self._max_queries,
            max_inactive_connection_lifetime=self._max_inactive_connection_lifetime,
            init=self._init,
            setup=self._setup,
            **attributes
        )

        if expires_at is not None:
            timer = Timer((expires_at - buffer_time) - time.time(), refresh_connection_pool, args=[self, pool])
            self.lock.acquire()
            self.timers.append(timer)
            self.lock.release()
            timer.start()

        return pool

    async def close(self):
        """Close all connections, connection pools and cancel all timers."""
        self.lock.acquire()
        for timer in self.timers:
            timer.cancel()
        self.lock.release()

        if self._connection is not None:
            try:
                await self._connection.close()
            except Exception:
                await self._connection.terminate()

        if self._connection_pool is not None:
            try:
                await self._connection_pool.close()
            except Exception:
                await self._connection_pool.terminate()


@coroutine
async def refresh_connection_pool(connector: AsyncpgConnector, pool: Pool):
    """
    Refresh a connection pool and set a timer for the next recover.

    :param AsyncpgConnector connector: the connector reference
    :param Pool pool: the pool to refresh
    """
    connector.lock.acquire()
    try:
        attributes = connector.connection_attributes.copy()
        if len(connector.timers) > 0:
            connector.timers.pop(0)
    finally:
        connector.lock.release()

    metadata = attributes['metadata']
    del attributes['metadata']

    expires_at = None

    if metadata['lease_duration'] is not None:
        expires_at = time.time() + metadata['lease_duration']

    pool.set_connect_args(**attributes)
    await pool.expire_connections()

    if expires_at is not None:
        timer = Timer((expires_at - buffer_time) - time.time(), refresh_connection_pool, args=[connector, pool])
        connector.lock.acquire()
        connector.timers.append(timer)
        connector.lock.release()
        timer.start()
