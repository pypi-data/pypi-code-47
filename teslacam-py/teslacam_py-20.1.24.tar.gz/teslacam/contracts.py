from abc import ABC, abstractmethod

from teslacam.config import Configuration
from teslacam.models import Clip

class Notifier(ABC):
    def __init__(self, cfg: Configuration):
        self.__cfg = cfg

    @property
    def config(self) -> Configuration:
        return self.__cfg

    @abstractmethod
    def notify(self, message: str):
        pass

class Uploader(ABC):
    def __init__(self, cfg: Configuration):
        self.__cfg = cfg

    @property
    def config(self) -> Configuration:
        return self.__cfg

    @abstractmethod
    def can_upload(self) -> bool:
        pass

    @abstractmethod
    def upload(self, clip: Clip):
        """
        Uploads the clip.
        """
        pass