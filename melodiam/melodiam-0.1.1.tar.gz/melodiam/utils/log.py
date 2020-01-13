import logging
import sys

from ..config import TESTING

LOGGER = logging.getLogger(name="melodiam")
LOGGER.setLevel(logging.DEBUG if TESTING else logging.INFO)

HANDLER = logging.StreamHandler(sys.stdout)
HANDLER.setLevel(logging.DEBUG if TESTING else logging.INFO)
FORMATTER = logging.Formatter("%(asctime)s - %(name)s [%(levelname)s] - %(message)s")
HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(HANDLER)
