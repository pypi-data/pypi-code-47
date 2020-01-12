import atexit
from typing import Optional, Callable, Any
from logging import Logger, getLogger
from time import time

from pika.adapters.blocking_connection import BlockingChannel
from pika.exceptions import ChannelClosedByBroker, ChannelWrongStateError
from pika.frame import Method
from curv_amqp.connection import Connection
from curv_amqp.exceptions import ChannelClosedError, ReconnectingToFastError


class Channel:
    blocking_channel: BlockingChannel

    def __init__(self,
                 connection: Connection,
                 at_exit: Callable[[Connection], Any] = None,
                 logger: Logger = getLogger(__name__),
                 reconnect_time_threshold: float = 1):
        self.reconnect_time_threshold = reconnect_time_threshold
        self.at_exit = at_exit
        self.is_closed = False
        self.logger = logger
        self.connection = connection
        self.blocking_channel = self.connection.channel()
        self.prev_connection_time = time()
        self.reconnect_to_fast_count = 0
        if self.at_exit is None:
            self.at_exit = self.close
        atexit.register(self.at_exit)

    def conditional_reconnect(self):
        if self.is_closed:
            raise ChannelClosedError('Channel is closed!')
        if self.blocking_channel.is_closed:
            time_since_last_connection = time() - self.prev_connection_time
            if time_since_last_connection < self.reconnect_time_threshold:
                self.reconnect_to_fast_count += 1
                if self.reconnect_to_fast_count > 3:
                    raise ReconnectingToFastError('Channel was attempting to reconnect repeatedly too quickly')
            else:
                self.reconnect_to_fast_count = 0
            self.blocking_channel = self.connection.channel()
            self.prev_connection_time = time()

    def close_channel(self):
        if not self.blocking_channel.is_closed:
            try:
                self.blocking_channel.close()
            except ChannelWrongStateError:
                pass

    def close(self):
        self.is_closed = True
        self.close_channel()
        atexit.unregister(self.at_exit)

    def qos(self, prefetch_size: int = 0, prefetch_count: int = 0, global_qos: bool = False):
        """Specify quality of service. This method requests a specific quality
        of service. The QoS can be specified for the current channel or for all
        channels on the connection. The client can request that messages be sent
        in advance so that when the client finishes processing a message, the
        following message is already held locally, rather than needing to be
        sent down the channel. Prefetching gives a performance improvement.

        :param int prefetch_size:  This field specifies the prefetch window
                                   size. The server will send a message in
                                   advance if it is equal to or smaller in size
                                   than the available prefetch size (and also
                                   falls into other prefetch limits). May be set
                                   to zero, meaning "no specific limit",
                                   although other prefetch limits may still
                                   apply. The prefetch-size is ignored if the
                                   no-ack option is set in the consumer.
        :param int prefetch_count: Specifies a prefetch window in terms of whole
                                   messages. This field may be used in
                                   combination with the prefetch-size field; a
                                   message will only be sent in advance if both
                                   prefetch windows (and those at the channel
                                   and connection level) allow it. The
                                   prefetch-count is ignored if the no-ack
                                   option is set in the consumer.
        :param bool global_qos:    Should the QoS apply to all channels on the
                                   connection.

        """
        self.conditional_reconnect()
        self.blocking_channel.basic_qos(prefetch_size=prefetch_size,
                                        prefetch_count=prefetch_count,
                                        global_qos=global_qos)

    def queue_declare(self,
                      queue: str,
                      passive: bool = False,
                      durable: bool = True,
                      exclusive: bool = False,
                      auto_delete: bool = True,
                      arguments: Optional[dict] = None) -> Method:
        """Declare queue, create if needed. This method creates or checks a
        queue. When creating a new queue the client can specify various
        properties that control the durability of the queue and its contents,
        and the level of sharing for the queue.

        Use an empty string as the queue name for the broker to auto-generate
        one. Retrieve this auto-generated queue name from the returned
        `spec.Queue.DeclareOk` method frame.

        :param str queue: The queue name; if empty string, the broker will
            create a unique queue name
        :param bool passive: Only check to see if the queue exists and raise
          `ChannelClosed` if it doesn't
        :param bool durable: Survive reboots of the broker
        :param bool exclusive: Only allow access by the current connection
        :param bool auto_delete: Delete after consumer cancels or disconnects
            # Auto-delete queues you are not using
                Client connections can fail and potentially leave unused resources (queues) behind, which could affect performance. There are three ways to delete a queue automatically.
                Set a TTL policy in the queue; e.g. a TTL policy of 28 days deletes queues that haven't been consumed from for 28 days.
                An auto-delete queue is deleted when its last consumer has canceled or when the channel/connection is closed (or when it has lost the TCP connection with the server).
                An exclusive queue can only be used (consumed from, purged, deleted, etc.) by its declaring connection. Exclusive queues are deleted when their declaring connection is closed or gone (e.g., due to underlying TCP connection loss).
        :param dict arguments: Custom key/value arguments for the queue
        :returns: Method frame from the Queue.Declare-ok response
        :rtype: `pika.frame.Method` having `method` attribute of type
            `spec.Queue.DeclareOk`
        """
        self.conditional_reconnect()
        try:
            return self.blocking_channel.queue_declare(queue=queue,
                                                       durable=durable,
                                                       passive=passive,
                                                       arguments=arguments,
                                                       exclusive=exclusive,
                                                       auto_delete=auto_delete)
        except ChannelClosedByBroker as e:
            if e.reply_code != 406:
                raise e
            return self.blocking_channel.queue_declare(queue=queue,
                                                       durable=not durable,
                                                       passive=passive,
                                                       arguments=arguments,
                                                       exclusive=exclusive,
                                                       auto_delete=auto_delete)
