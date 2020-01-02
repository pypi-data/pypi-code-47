from abc import ABC, abstractmethod


class DataBroker(ABC):
    """Abstract class for storing data."""

    def __init__(self):
        super(DataBroker, self).__init__()

    @abstractmethod
    def load(self, *args, **kwargs):
        """
        Load the saved data.
        """
        pass

    @abstractmethod
    def save(self, *args, **kwargs):
        """
        Save the data to
        given format by the
        chosen DataBroker.
        """
        pass
