class AMQPError(Exception):
    pass


class ReconnectingToFastError(AMQPError):
    pass


class ClosedError(AMQPError):
    pass


class ConnectionClosedError(ClosedError):
    pass


class ChannelClosedError(ClosedError):
    pass


class PriorityLevelError(AMQPError):
    pass


class RequeueRetryCountError(AMQPError):
    pass


class MessageAutoAckError(AMQPError):
    pass

