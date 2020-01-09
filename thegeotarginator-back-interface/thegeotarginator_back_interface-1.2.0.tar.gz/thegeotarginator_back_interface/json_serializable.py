from abc import ABC, abstractmethod


class DictSerializable(ABC):
    @staticmethod
    @abstractmethod
    def from_dict(data: dict):
        pass
