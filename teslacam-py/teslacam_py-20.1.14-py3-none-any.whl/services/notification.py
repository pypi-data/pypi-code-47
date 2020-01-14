from typing import Optional

from teslacam.config import Configuration
from teslacam.consts import NOTIFIERS
from teslacam.contracts import Notifier

class NotificationService:
    def __init__(self, cfg: Configuration):
        self.__notifier = NotificationService.__get_notifier(cfg)

    def notify(self, msg: str):
        if not self.__notifier:
            return

        self.__notifier.notify(msg)

    @staticmethod
    def __get_notifier(cfg: Configuration) -> Optional[Notifier]:
        if not cfg.notifier:
            return None

        return NOTIFIERS[cfg.notifier](cfg)