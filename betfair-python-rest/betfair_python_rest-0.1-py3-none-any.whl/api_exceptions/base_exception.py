from .exception_enum import APINGExceptionsEnum


class BetFairAPIManagerException(Exception):
    def __init__(self, status):
        description = APINGExceptionsEnum.get_description(status)
        Exception.__init__(self, description)
