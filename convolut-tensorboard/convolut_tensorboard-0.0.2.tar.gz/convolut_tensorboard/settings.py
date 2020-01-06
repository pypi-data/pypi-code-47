import os

from .constants import TensorboardMode
from convolut.settings import GLOBAL_PREFIX

LOGGER_TENSORBOARD_MODE = os.environ.get(f"{GLOBAL_PREFIX}LOGGER_TENSORBOARD_MODE", TensorboardMode.Basic)
LOGGER_TENSORBOARD_FOLDER = os.environ.get(f"{GLOBAL_PREFIX}LOGGER_TENSORBOARD_FOLDER", "logs/tensorboard")
