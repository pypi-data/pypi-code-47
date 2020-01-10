

class LocalTransaction:
    """Maintains messages as a single transaction and provides
    an API to commit.
    """

    def __init__(self, publisher, backend):
        self.publisher = publisher
        self.backend = backend
        self.messages = []

    def issue(self, *args, **kwargs):
        kwargs.setdefault('to_backend', self.to_backend)
        return self.publisher.issue(*args, **kwargs)

    def observe(self, *args, **kwargs):
        kwargs.setdefault('to_backend', self.to_backend)
        return self.publisher.observe(*args, **kwargs)

    def to_backend(self, message, *args, **kwargs):
        """Puts a message on the queue for transmission."""
        self.messages.append(message)

    def commit(self):
        """Transmits the pending messages to the AMQP peer."""
        self.backend.put_many(self.messages)

    def __getattr__(self, attname):
        return getattr(self.publisher, attname)
