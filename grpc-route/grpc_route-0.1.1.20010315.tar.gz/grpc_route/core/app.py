# -*- coding: utf-8 -*- 
# @Time     : 2020-01-01 22:05
# @Author   : binger

import sys
from threading import Lock
from .globals import request
from . import error
from .response import Response
from .common import locked_cached_property
from .logging import create_logger


# 客户端提供注册回调：
#    1. 任何异常的，参数异常和地址
#    2. 连接超时的
#    3. 针对特定服务段的
#    4. 所有请求前后的
#    5. 第一次请求的


# 服务端：
#    1. 第一次请求的，
#    2. 请求前后
#    3. 异常回收的

class RequestEvent(object):
    response_class = Response

    def __init__(self, import_name=None):
        self.import_name = import_name or "__main__"

        self.before_first_request_funcs = []
        self.before_request_funcs = {}
        self.after_request_funcs = {}
        self.error_handler_spec = {}

        self._before_request_lock = Lock()
        self._got_first_request = False

        self.config = {}

    @property
    def debug(self):
        return self.config.get('debug', True)

    @debug.setter
    def debug(self, boolean):
        self.config['debug'] = boolean

    @property
    def name(self):
        return self.import_name

    @locked_cached_property
    def logger(self):
        return create_logger(self)

    def before_request(self, f):
        """
        请求前，注册回调
        注册的回调函数，如果有返回值，回调过程停止，后续栈中还有也不执行
        :param f:
        :return:
        """
        self.before_request_funcs.setdefault(None, []).append(f)

        return f

    def before_first_request(self, f):
        """
        第一次请求前，注册回调
        :param f:
        :return:
        """
        self.before_first_request_funcs.append(f)
        return f

    def after_request(self, f):
        """
        请求后，注册回调
        :param f:
        :return:
        """
        self.after_request_funcs.setdefault(None, []).append(f)
        return f

    def errorhandler(self, code_or_exception):
        """Register a function to handle errors by code or exception class.

        A decorator that is used to register a function given an
        error code.  Example::

            @app.errorhandler(404)
            def page_not_found(error):
                return 'This page does not exist', 404

        You can also register handlers for arbitrary exceptions::

            @app.errorhandler(DatabaseError)
            def special_exception_handler(error):
                return 'Database connection failed', 500

        .. versionadded:: 0.7
            Use :meth:`register_error_handler` instead of modifying
            :attr:`error_handler_spec` directly, for application wide error
            handlers.

        .. versionadded:: 0.7
           One can now additionally also register custom exception types
           that do not necessarily have to be a subclass of the
           :class:`~werkzeug.exceptions.HTTPException` class.

        :param code_or_exception: the code as integer for the handler, or
                                  an arbitrary exception
        """

        def decorator(f):
            self._register_error_handler(None, code_or_exception, f)
            return f

        return decorator

    def register_error_handler(self, code_or_exception, f):
        """
        注册异常回调处理
        :param code_or_exception:
        :param f:
        :return:
        """
        self._register_error_handler(None, code_or_exception, f)

    def _register_error_handler(self, key, code_or_exception, f):
        exc_class, code = code_or_exception, None
        handlers = self.error_handler_spec.setdefault(key, {}).setdefault(code, {})
        handlers[exc_class] = f

    def _find_error_handler(self, e):
        """
        轮训`异常处理`回调
        :param e:
        :return:
        """
        exc_class, code = e, None

        for name, c in (
                (None, code),
        ):
            handler_map = self.error_handler_spec.setdefault(name, {}).get(c)

            if not handler_map:
                continue

            for cls in exc_class.__mro__:
                handler = handler_map.get(cls)

                if handler is not None:
                    return handler

    def make_response(self, rv):
        """
        统一创建返回对象
        包含从返回结果，异常类型2类
        :param rv: 返回结果或者过程的异常
        :return:
        """
        # TODO: 定义一个返回数据的格式

        if not isinstance(rv, self.response_class):
            if isinstance(rv, error.ServerError):
                response = self.response_class(*rv.args)
                response.original_exception = rv
            elif isinstance(rv, Exception):
                response = self.response_class(*error.ServerCode.INTERNAL_ERROR.value)
                response.original_exception = rv
            else:
                response = self.response_class(*error.ServerCode.OK.value, data=rv)
        else:
            response = rv
        return response

    def try_trigger_before_first_request_functions(self):
        """
        轮训第一次使用回调
        :return:
        """
        if self._got_first_request:
            return
        with self._before_request_lock:
            if self._got_first_request:
                return
            for func in self.before_first_request_funcs:
                func()
            self._got_first_request = True

    def handle_user_exception(self, e):
        handler = self._find_error_handler(e)
        if handler:
            return handler(e)
        else:
            raise e

    def handle_exception(self, e):
        """
        处理发生异常
        :param e:
        :return:
        """
        self.log_exception(sys.exc_info())
        server_error = e
        handler = self._find_error_handler(server_error)
        if handler is not None:
            server_error = handler(server_error)

        return self.finalize_request(server_error, from_error_handler=True)

    def log_exception(self, exc_info):
        """Logs an exception.  This is called by :meth:`handle_exception`
        if debugging is disabled and right before the handler is called.
        The default implementation logs the exception as error on the
        :attr:`logger`.

        .. versionadded:: 0.8
        """
        self.logger.error(
            "Exception on %s" % (request.object.handler), exc_info=exc_info
        )

    def full_dispatch_request(self):
        """Dispatches the request and on top of that performs request
        pre and postprocessing as well as HTTP exception catching and
        error handling.

        """
        self.try_trigger_before_first_request_functions()
        try:
            # request_started.send(self)
            rv = self.preprocess_request()
            if rv is None:
                rv = self.dispatch_request()
        except Exception as e:
            rv = self.handle_user_exception(e)
        return self.finalize_request(rv)

    def preprocess_request(self):
        """
        轮训前置回调
        :return:
        """
        funcs = self.before_request_funcs.get(None, ())
        for func in funcs:
            rv = func()
            if rv is not None:
                # 有返回值函数，回调结束
                return rv

    def dispatch_request(self):
        # TODO： 处理请求, 一般具体的处理方法，需要继承
        pass

    def finalize_request(self, rv, from_error_handler=False):
        """
        处理结果的处理过程
        产生返回类型
        :param rv:
        :param from_error_handler:
        :return:
        """
        response = self.make_response(rv)
        try:
            response = self.process_response(response)
            # request_finished.send(self, response=response)
        except Exception:
            if not from_error_handler:
                raise
            self.logger.exception(
                "Request finalizing failed with an error while handling an error"
            )
        return response

    def process_response(self, response):
        """
        轮训后置回调
        :param response: 处理的结果对象
        :return:
        """
        funcs = self.before_request_funcs.get(None, ())
        for handler in funcs:
            response = handler(response)
        return response


if __name__ == "__main__":
    pass
