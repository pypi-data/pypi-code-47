import logging

from code_instrumentation import add_logging_level
logging.getLogger(__name__).addHandler(logging.NullHandler())
__all__ = ['Timer']