import os

from .constants import TelegramMode
from convolut.settings import GLOBAL_PREFIX

LOGGER_TELEGRAM_TOKEN = os.environ.get(f"{GLOBAL_PREFIX}LOGGER_TELEGRAM_TOKEN", None)
LOGGER_TELEGRAM_CHAT_ID = os.environ.get(f"{GLOBAL_PREFIX}LOGGER_TELEGRAM_CHAT_ID", None)
LOGGER_TELEGRAM_MODE = os.environ.get(f"{GLOBAL_PREFIX}LOGGER_TELEGRAM_MODE", TelegramMode.Basic)
LOGGER_TELEGRAM_PROXY = os.environ.get(f"{GLOBAL_PREFIX}LOGGER_TELEGRAM_PROXY", 'https://api.telegram.org')
