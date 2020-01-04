class Error(Exception):
    """ Base exception class """
    pass


class UserNotFound(Error):
    """ Raised when requested user does not exist """
    pass
