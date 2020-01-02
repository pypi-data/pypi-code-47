from proton.utils import BlockingConnection

from .base import BaseBuffer


class BlockingBuffer(BaseBuffer):
    """A 'buffer' implementation that immediately transmits the
    message to the AMQP peer and raises an exception on failure.
    Use in applications where the caller needs immediate feedback
    on the success of a message delivery.

    Note that delayed (not-before) transmissions are not supported
    by this buffer implementation.
    """

    @property
    def connection(self):
        if self._connection is None:
            self._connection = BlockingConnection(self.url)
        return self._connection

    @property
    def sender(self):
        if self._sender is None:
            self._sender = self.connection.create_sender(self.channel)
        return self._sender

    def __init__(self, url, channel=None):
        self.url = url
        self.channel = channel
        self._connection = None
        self._sender = None

    def enqueue(self, message, *args, **kwargs):
        """Queue a new message for transmission. Since this buffer
        implementation immediately sends the message to the AMQP
        peer, :meth:`enqueue` blocks until succesful delivery or
        exception.

        Args:
            message (proton.Message): the message to enqueue.

        Returns:
            None
        """
        if message.address is None:
            raise ValueError("Message.address must not be `None`.")
        self.sender.send(message)
