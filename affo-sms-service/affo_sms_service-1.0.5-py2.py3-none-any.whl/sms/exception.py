__all__ = ["SMSError", "SMSNoSuchGateway", "InvalidPhone"]


class SMSError(Exception):
    pass


class SMSNoSuchGateway(SMSError):
    pass


class InvalidPhone(SMSError):
    pass
