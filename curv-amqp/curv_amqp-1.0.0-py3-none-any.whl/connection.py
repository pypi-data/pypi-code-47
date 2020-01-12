from __future__ import annotations

import atexit
from typing import Callable, Any
from logging import Logger, getLogger
from time import time

from pika.connection import URLParameters, ConnectionParameters, Parameters
from pika.adapters.blocking_connection import BlockingConnection, BlockingChannel
from pika.exceptions import ConnectionWrongStateError

from curv_amqp.exceptions import ConnectionClosedError, ReconnectingToFastError

URLParameters = URLParameters
ConnectionParameters = ConnectionParameters


class Connection:
    blocking_connection: BlockingConnection

    def __init__(self,
                 parameters: Parameters,
                 at_exit: Callable[[Connection], Any] = None,
                 logger: Logger = getLogger(__name__),
                 reconnect_time_threshold: float = 1):
        self.at_exit = at_exit
        self.reconnect_time_threshold = reconnect_time_threshold
        self.is_closed = False
        self.logger = logger
        self.parameters = parameters
        self.blocking_connection = BlockingConnection(self.parameters)
        self.prev_connection_time = time()
        self.reconnect_to_fast_count = 0
        if self.at_exit is None:
            self.at_exit = self.close
        atexit.register(self.at_exit)

    def close_connection(self):
        self.logger.info(f'close_connection called while '
                         f'self.blocking_connection.is_closed="{self.blocking_connection.is_closed}"')
        if not self.blocking_connection.is_closed:
            try:
                self.blocking_connection.close()
            except ConnectionWrongStateError as e:
                self.logger.warning(e)

    def close(self):
        self.is_closed = True
        self.close_connection()
        atexit.unregister(self.at_exit)

    def conditional_reconnect(self):
        if self.is_closed:
            raise ConnectionClosedError('Connection is closed!')
        if self.blocking_connection.is_closed:
            time_since_last_connection = time() - self.prev_connection_time
            if time_since_last_connection < self.reconnect_time_threshold:
                self.reconnect_to_fast_count += 1
                if self.reconnect_to_fast_count > 3:
                    raise ReconnectingToFastError('Connection was attempting to reconnect repeatedly too quickly')
            else:
                self.reconnect_to_fast_count = 0
            self.logger.info(f'conditional_reconnect called while '
                             f'self.blocking_connection.is_closed="{self.blocking_connection.is_closed}"')
            self.blocking_connection = BlockingConnection(self.parameters)
            self.prev_connection_time = time()

    def channel(self, channel_number: int = None) -> BlockingChannel:
        """Create a new channel with the next available channel number or pass
        in a channel number to use. Must be non-zero if you would like to
        specify but it is recommended that you let Pika manage the channel
        numbers.

        :rtype: pika.adapters.blocking_connection.BlockingChannel
        """
        self.conditional_reconnect()
        return self.blocking_connection.channel(channel_number=channel_number)
