from abc import abstractmethod


class BaseForm:

    @abstractmethod
    def data(self):
        raise AttributeError('the data attribute is required')
