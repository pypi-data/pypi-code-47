from request_limiter.strategy import LimitStrategy


class LimitException(Exception):
    """
    Custom exception raised when the number of request exceeds strategy's limit
    """
    def __init__(self, message, strategy: LimitStrategy):
        super(LimitException, self).__init__(message)
        self.strategy = strategy
