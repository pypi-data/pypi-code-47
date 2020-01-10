
class BIO465:
    """
    BIO 465 is a container object that gets content associated with
    the BIO465 course at Brigham Young University
    """
    def __init__(self):
        self.dataframes = []
        self.homeworks = []
        self.labs = []

    """ retrieves a list of lab objects from the instantiated class """
    def get_labs(self) -> list:
        return self.labs

    """ retrieves a list of homework objects from the instantiated class """
    def get_homeworks(self) -> list:
        return self.homeworks

    """ retrieves a list of pandas data frame objects from the instantiated class """
    def get_dataframes(self) -> list:
        return self.dataframes
