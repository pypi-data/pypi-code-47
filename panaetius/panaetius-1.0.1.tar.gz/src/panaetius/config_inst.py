import os

from panaetius.header import __header__
from panaetius.config import Config


DEFAULT_CONFIG_PATH = f'~/.config/{__header__.lower()}'
CONFIG_PATH = os.environ.get(
    f'{__header__.upper()}_CONFIG_PATH', DEFAULT_CONFIG_PATH
)
CONFIG = Config(CONFIG_PATH)
