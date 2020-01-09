import threading

import ioc

from aorta.lib.datastructures import DTO


@ioc.inject('publisher', 'EventPublisher')
@ioc.inject('gateway', 'CommandGateway')
class Context:
    local = threading.local()

    @classmethod
    def fromincoming(cls, incoming):
        return cls(incoming)

    @classmethod
    def current(cls):
        return getattr(cls.local, 'context', None)

    def __init__(self, message):
        self.message = message
        Context.local.context = self

    def handle(self, func, serializer=None):
        """Invokes callable `func` with the message parameters as
        its first positional argument. The message is considered to
        be cleaned and validated at this point, so we may assume
        that the message body is of the appropriate type (e.g. a
        Python dictionary).
        """
        self.params = DTO.fromdict(self.message.body)
        if serializer:
            self.params = serializer.load(self.params)
        return func(self.params)

    def observe(self, *args, **kwargs):
        """Invokes :meth:`~aorta.EventPublisher.observe()`."""
        kwargs.setdefault('correlation_id', self.message.correlation_id)
        kwargs.setdefault('triggered_by', self.message.id)
        return self.publisher.observe(*args, **kwargs)

    def observemany(self, events, **kwargs):
        """Like :meth:`observe()`, but publish all events over a
        single connection. Use for batch operations.
        """
        kwargs.setdefault('correlation_id', self.message.correlation_id)
        kwargs.setdefault('triggered_by', self.message.id)
        return self.publisher.observemany(events, **kwargs)

    def issue(self, *args, **kwargs):
        """Invokes :meth:`~aorta.CommandGateway.issue()`."""
        kwargs.setdefault('correlation_id', self.message.correlation_id)
        kwargs.setdefault('triggered_by', self.message.id)
        return self.gateway.issue(*args, **kwargs)

    def on_rejected(self, handler):
        """Invoked when the handler rejects a message."""
        handler.on_rejected(self.message, self.dto)
