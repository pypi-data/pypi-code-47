import logging


class Check:
    """
    Takes a list of DataObject and runs the function on the entire list. Returns an error string.
    """
    def __init__(self, name: str, funct) -> None:
        self.name = name
        self.funct = funct

    def run(self, data_lst, metadata=None) -> str:
        logging.debug("running check {}".format(self.name))
        return self.funct(data_lst, metadata)


class CheckEach(Check):
    """
    Takes a list of DataObject and runs the function on each DataObject within the list. Returns an error string.
    """
    def __init__(self, name: str, funct) -> None:
        super().__init__(name, funct)

    def run(self, data_lst, metadata=None) -> str:
        logging.debug("running check all {}".format(self.name))
        for obj in data_lst:
            error = self.funct(obj, metadata)
            if error:
                return error
        return ""
