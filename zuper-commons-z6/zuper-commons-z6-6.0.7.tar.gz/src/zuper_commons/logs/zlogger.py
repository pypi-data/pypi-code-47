import inspect
import logging
from logging import Logger
from typing import Dict, Union

import termcolor

__all__ = ["ZLogger"]


class ZLogger:
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARN = logging.WARN
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    logger: Logger

    def __init__(self, logger: Union[Logger, str], child: str = None):
        if isinstance(logger, str):
            logger = logging.getLogger(logger)
            logger.setLevel(logging.DEBUG)
        if child is not None:
            orig_name = logger.name
            logger = logger.getChild(child)
            if orig_name in child:
                logger.name = child

        self.logger = logger

        try:
            # noinspection PyUnresolvedReferences
            from zuper_typing import debug_print

            self.debug_print = debug_print
        except ImportError:
            self.debug_print = str

        from zuper_commons.text import pretty_dict

        self.pretty_dict = pretty_dict
        # monkeypatch_findCaller()

    def info(
        self, msg: str = None, *args, stacklevel: int = 0, **kwargs: object
    ) -> None:
        level = logging.INFO
        self._log(level=level, msg=msg, args=args, stacklevel=stacklevel, kwargs=kwargs)

    def debug(
        self, msg: str = None, *args, stacklevel: int = 0, **kwargs: object
    ) -> None:
        level = logging.DEBUG
        self._log(level=level, msg=msg, args=args, stacklevel=stacklevel, kwargs=kwargs)

    def warn(self, msg: str = None, *args, stacklevel: int = 0, **kwargs) -> None:
        level = logging.WARN
        self._log(level=level, msg=msg, args=args, stacklevel=stacklevel, kwargs=kwargs)

    def warning(self, msg: str = None, *args, stacklevel: int = 0, **kwargs) -> None:
        level = logging.WARN
        self._log(level=level, msg=msg, args=args, stacklevel=stacklevel, kwargs=kwargs)

    def error(
        self, msg: str = None, *args, stacklevel: int = 0, **kwargs: object
    ) -> None:
        level = logging.ERROR
        self._log(level=level, msg=msg, args=args, stacklevel=stacklevel, kwargs=kwargs)

    def _log(
        self, level: int, msg: str, args, stacklevel: int, kwargs: Dict[str, object]
    ) -> None:
        if not self.logger.isEnabledFor(level):
            return
        res = {}

        def lab(x):
            return termcolor.colored(x, attrs=["dark"])

        for i, a in enumerate(args):
            res[lab(str(i))] = self.debug_print(a)

        for k, v in kwargs.items():
            res[lab(k)] = self.debug_print(v)

        if res:

            s = self.pretty_dict(msg, res, leftmargin=" ")
            if not msg:
                s = "\n" + s
            # if msg:
            #     s = msg + '\n' + indent(rest, ' ')
            # else:
            #     s = rest
        else:
            s = msg

        stack = inspect.stack()
        # 0 is us
        # 1 is one of our methods
        stacklevel += 2
        # for i, frame_i in enumerate(stack[:5]):
        #     x = '***' if i == stacklevel else '   '
        #     print(i, x, frame_i.filename, frame_i.function)
        frame = stack[stacklevel]
        pathname = frame.filename
        lineno = frame.lineno
        funcname = str(frame.function)
        locals = frame[0].f_locals
        # print(list(locals))
        if "self" in locals:
            # print(locals['self'])
            typename = locals["self"].__class__.__name__
            funcname = typename + ":" + funcname
        funcname = termcolor.colored(funcname, "red")
        record = self.logger.makeRecord(
            self.logger.name,
            level,
            pathname,
            lineno,
            s,
            (),
            exc_info=None,
            func=funcname,
            extra=None,
            sinfo=None,
        )
        self.logger.handle(record)
        # self.logger.log(level, s)

    def getChild(self, child_name) -> "ZLogger":
        return ZLogger(self.logger, child_name)

    def setLevel(self, level: int) -> None:
        self.logger.setLevel(level)
