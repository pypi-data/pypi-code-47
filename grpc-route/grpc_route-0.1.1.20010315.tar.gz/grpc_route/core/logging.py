# -*- coding: utf-8 -*- 
# @Time     : 2020-01-03 11:54
# @Author   : binger

import sys
import logging
import warnings
from .local import LocalProxy


@LocalProxy
def errors_stream():
    """Find the most appropriate error stream for the application. If a request
    is active, log to ``wsgi.errors``, otherwise use ``sys.stderr``.

    If you configure your own :class:`logging.StreamHandler`, you may want to
    use this for the stream. If you are using file or dict configuration and
    can't import this directly, you can refer to it as
    ``ext://flask.logging.wsgi_errors_stream``.
    """
    return sys.stderr


def has_level_handler(logger):
    """Check if there is a handler in the logging chain that will handle the
    given logger's :meth:`effective level <~logging.Logger.getEffectiveLevel>`.
    """
    level = logger.getEffectiveLevel()
    current = logger

    while current:
        if any(handler.level <= level for handler in current.handlers):
            return True

        if not current.propagate:
            break

        current = current.parent

    return False


#: Log messages to :func:`~flask.logging.wsgi_errors_stream` with the format
#: ``[%(asctime)s] %(levelname)s in %(module)s: %(message)s``.
default_handler = logging.StreamHandler(errors_stream)
default_handler.setFormatter(
    logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
)


def _has_config(logger):
    """Decide if a logger has direct configuration applied by checking
    its properties against the defaults.

    :param logger: The :class:`~logging.Logger` to inspect.
    """
    return (
            logger.level != logging.NOTSET
            or logger.handlers
            or logger.filters
            or not logger.propagate
    )


def create_logger(app):
    logger = logging.getLogger(app.name)

    # 1.1.0 changes name of logger, warn if config is detected for old
    # name and not new name
    for old_name in ("grpc_route.app", "grpc_route"):
        old_logger = logging.getLogger(old_name)

        if _has_config(old_logger) and not _has_config(logger):
            warnings.warn(
                "'app.logger' is named '{name}' for this application,"
                " but configuration was found for '{old_name}', which"
                " no longer has an effect. The logging configuration"
                " should be moved to '{name}'.".format(name=app.name, old_name=old_name)
            )
            break

    if app.debug and not logger.level:
        logger.setLevel(logging.DEBUG)

    if not has_level_handler(logger):
        logger.addHandler(default_handler)

    return logger
