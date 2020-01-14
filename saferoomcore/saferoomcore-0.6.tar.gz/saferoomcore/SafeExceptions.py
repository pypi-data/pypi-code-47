# Class section
class SaferoomException(Exception):

    def __init__(self, message, errors):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # List of custom errors
        self.errors = errors
