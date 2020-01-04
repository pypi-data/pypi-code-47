from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    The abstract base parser for all other parsers to implement.
    """

    @abstractmethod
    def get(self, key):
        raise NotImplementedError

    @abstractmethod
    def set(self, key, value):
        raise NotImplementedError

    @abstractmethod
    def delete(self, key):
        raise NotImplementedError

    @abstractmethod
    def parse(self, file):
        raise NotImplementedError


class ParsingError(Exception):
    """Unable to parse the configuration file"""
