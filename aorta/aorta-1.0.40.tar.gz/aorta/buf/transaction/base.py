

class BaseTransaction:
    """Base transaction class for transmitting messages."""

    def __init__(self, backend):
        self.backend = backend
        self.messages = messages

    def flush(self):
        """Transmits all messages to the AMQP peer."""
        raise NotImplementedError
