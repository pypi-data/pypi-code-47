class PanelCreationException(Exception):
    """
    PanelCreationException occurs only when the the parameters of Panel class do not fit the requirements.
    """
    def __init__(self, message: str):
        self.args = (message, )


class PermutationsExceededException(Exception):
    """
    PermutationsExceededException occurs only when no place has been found for a given word.
    """
    def __init__(self, message):
        self.args = (message, )
