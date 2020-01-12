# MIT License

# Copyright (c) [year] [fullname]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import logging

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
_loggers = set()


def setup_logger(name: str, level: int = logging.DEBUG) -> logging.Logger:
    """Helper function used to configure loggers for the CLI.

    This is preferable to using `logging.dictConfig` or something similar,
    as the log level is not known until command-line arguments can be parsed.
    An event listener can be created to update all loggers with the correct
    CLI preferences once the application logging is initialized.

    This also provides an easy way to configure standard formatting options,
    without forcing too much configuration.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(_setup_handler(level))
    _loggers.add(logger)
    return logger


def _setup_handler(level: int) -> logging.StreamHandler:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    formatter = logging.Formatter(LOG_FORMAT)
    console_handler.setFormatter(formatter)
    return console_handler


def set_log_level(level: int) -> None:
    for logger in _loggers:
        logger.setLevel(level)
