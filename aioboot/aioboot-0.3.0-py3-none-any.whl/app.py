import asyncio
import functools
from typing import Any, Callable, List, Optional, Type, TypeVar, Union

import click
from aiohttp import web
from injector import Binder, Injector, Module as _Module, Scope, ScopeDecorator

from aioboot import ctx
from aioboot.di import RequestScope, SingletonScope, inject
from aioboot.request import Request
from aioboot.response import Response
from aioboot.typedefs import Handler

T = TypeVar("T")
ModuleT = Union[Type["Module"], "Module"]


class Application:
    """
    Creates an application instance.

    **Parameters:**

    * **debug** - Debug exception traceback.
    * **modules** - A list of modules to use when class `Application` is initialized.
    * **auto_bing** - Whether to automatically bind missing types.
    """

    def __init__(
        self,
        debug: bool = False,
        modules: Optional[List[ModuleT]] = None,
        auto_bind: bool = False,
    ):
        self._debug = debug
        self._injector = Injector(auto_bind=auto_bind)
        self._web_app = web.Application(middlewares=[ctx.request_scope_middleware])
        self._cli = click.Group()

        # Add default bindings
        self.bind(Application, to=self, scope=SingletonScope)
        self.bind(Injector, to=self.injector, scope=SingletonScope)
        self.bind(Request, to=ctx.get_current_request, scope=RequestScope)

        # Add default modules
        modules = modules or []
        for module in modules:
            self.add_module(module)

    @property
    def debug(self) -> bool:
        return self._debug

    @property
    def injector(self) -> Injector:
        return self._injector

    @property
    def web_app(self) -> web.Application:
        return self._web_app

    @property
    def cli(self) -> click.Group:
        return self._cli

    def lookup(
        self, interface: Type[T], *, scope: Union[Type[Scope], ScopeDecorator] = None
    ) -> T:
        return self.injector.get(interface, scope=scope)

    def bind(
        self,
        interface: Type[T],
        to: Optional[Any] = None,
        *,
        scope: Union[Type[Scope], ScopeDecorator] = None,
    ) -> None:
        self.injector.binder.bind(interface, to=to, scope=scope)

    def add_module(self, module: Union[Type["Module"], "Module"]) -> None:
        self.injector.binder.install(module)

    def add_startup_event(self, event: Callable) -> None:
        event = self._wrap_event(event)
        self.web_app.on_startup.append(event)

    def add_shutdown_event(self, event: Callable) -> None:
        event = self._wrap_event(event)
        self.web_app.on_shutdown.append(event)

    def add_cleanup_event(self, event: Callable) -> None:
        event = self._wrap_event(event)
        self.web_app.on_cleanup.append(event)

    def add_before_response_event(self, event: Callable) -> None:
        event = self._wrap_before_response_event(event)
        self.web_app.on_response_prepare.append(event)

    def on_startup(self) -> Callable:
        def decorator(event: Callable):
            self.add_startup_event(event)
            return event

        return decorator

    def on_shutdown(self) -> Callable:
        def decorator(event: Callable):
            self.add_shutdown_event(event)
            return event

        return decorator

    def on_cleanup(self) -> Callable:
        def decorator(event: Callable):
            self.add_cleanup_event(event)
            return event

        return decorator

    def on_before_response(self) -> Callable:
        def decorator(event: Callable):
            self.add_before_response_event(event)
            return event

        return decorator

    def freeze(self) -> None:
        self.web_app.freeze()

    async def startup(self) -> None:
        await self.web_app.startup()

    async def shutdown(self) -> None:
        await self.web_app.shutdown()

    async def cleanup(self) -> None:
        await self.web_app.cleanup()

    def add_middleware(
        self, middleware: Callable, *, pos: Optional[int] = None
    ) -> None:
        middleware = self._wrap_middleware(middleware)
        pos = pos or len(self.web_app.middlewares) + 1
        self.web_app.middlewares.insert(pos, middleware)

    def middleware(self, pos: Optional[int] = None) -> Callable:
        def decorator(middleware: Callable) -> Callable:
            self.add_middleware(middleware, pos=pos)
            return middleware

        return decorator

    def add_route(
        self,
        method: str,
        path: str,
        endpoint: Callable,
        *,
        name: Optional[str] = None,
        **kwargs,
    ) -> None:
        endpoint = self._wrap_endpoint(endpoint, **kwargs)
        self.web_app.router.add_route(method, path, handler=endpoint, name=name)

    def route(
        self, method: str, path: str, *, name: Optional[str] = None, **kwargs
    ) -> Callable:
        def decorator(endpoint: Callable) -> Callable:
            self.add_route(method, path, endpoint=endpoint, name=name, **kwargs)
            return endpoint

        return decorator

    def get(self, path: str, *, name: Optional[str] = None, **kwargs) -> Callable:
        return self.route("GET", path, name=name, **kwargs)

    def head(self, path: str, *, name: Optional[str] = None, **kwargs) -> Callable:
        return self.route("HEAD", path, name=name, **kwargs)

    def post(self, path: str, *, name: Optional[str] = None, **kwargs) -> Callable:
        return self.route("POST", path, name=name, **kwargs)

    def put(self, path: str, *, name: Optional[str] = None, **kwargs) -> Callable:
        return self.route("PUT", path, name=name, **kwargs)

    def patch(self, path: str, *, name: Optional[str] = None, **kwargs) -> Callable:
        return self.route("PATCH", path, name=name, **kwargs)

    def delete(self, path: str, *, name: Optional[str] = None, **kwargs) -> Callable:
        return self.route("DELETE", path, name=name, **kwargs)

    def trace(self, path: str, *, name: Optional[str] = None, **kwargs) -> Callable:
        return self.route("TRACE", path, name=name, **kwargs)

    def options(self, path: str, *, name: Optional[str] = None, **kwargs) -> Callable:
        return self.route("OPTIONS", path, name=name, **kwargs)

    def add_command(
        self,
        cmd: Callable,
        *,
        name: Optional[str] = None,
        cli: Optional[click.Group] = None,
        lifespan: bool = True,
    ) -> None:
        make_command = click.command()
        cli = cli or self.cli
        cli.add_command(
            make_command(self._wrap_command(cmd, lifespan=lifespan)), name=name
        )

    def command(self, name: Optional[str] = None, *, lifespan: bool = True) -> Callable:
        def decorator(cmd: Callable) -> Callable:
            self.add_command(cmd, name=name, lifespan=lifespan)
            return cmd

        return decorator

    def main(self) -> None:
        self.cli.main()

    def run(self, host: Optional[str] = None, port: Optional[int] = None) -> None:
        web.run_app(app=self.web_app, host=host, port=port)

    ############################################
    # Private methods
    ############################################

    def _wrap_event(self, event: Callable) -> Callable:
        def wrapper(func):
            assert asyncio.iscoroutinefunction(
                func
            ), "Event function must be a coroutine."

            @functools.wraps(func)
            def wrapped(app: web.Application):  # noqa
                return self.injector.call_with_injection(inject(func))

            return wrapped

        return wrapper(event)

    def _wrap_before_response_event(self, event: Callable) -> Callable:
        def wrapper(func):
            assert asyncio.iscoroutinefunction(
                func
            ), "Before response event function must be a coroutine."

            @functools.wraps(func)
            def wrapped(request: Request, response: Response):  # noqa
                return self.injector.call_with_injection(
                    inject(func), kwargs={"response": response}
                )

            return wrapped

        return wrapper(event)

    def _wrap_middleware(self, middleware: Callable) -> Callable:

        middleware = web.middleware(middleware)

        def wrapper(func):
            assert asyncio.iscoroutinefunction(
                func
            ), "Middleware function must be a coroutine."

            @functools.wraps(func)
            def wrapped(request: Request, handler: Handler):
                return self.injector.call_with_injection(
                    inject(func), kwargs={"request": request, "handler": handler}
                )

            return wrapped

        return wrapper(middleware)

    def _wrap_endpoint(self, endpoint: Callable, **kwargs) -> Callable:
        setattr(endpoint, "__kwargs__", kwargs)

        def wrapper(func):
            assert asyncio.iscoroutinefunction(
                func
            ), "Endpoint function must be a coroutine."

            @functools.wraps(func)
            def wrapped(request: Request):  # noqa
                return self.injector.call_with_injection(inject(func))

            return wrapped

        return wrapper(endpoint)

    def _wrap_command(self, cmd: Callable, lifespan: bool = True) -> Callable:
        def wrapper(func):
            assert asyncio.iscoroutinefunction(
                func
            ), "Command function must be a coroutine."

            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                def call():
                    return self.injector.call_with_injection(
                        inject(func), args=args, kwargs=kwargs
                    )

                async def run():
                    if lifespan:
                        self.web_app.on_startup.freeze()
                        await self.startup()
                        self.freeze()
                        try:
                            await call()
                            await self.shutdown()
                        finally:
                            await self.cleanup()
                    else:
                        await call()

                return asyncio.run(run())

            return wrapped

        return wrapper(cmd)


class Module(_Module):
    def configure(self, binder: Binder) -> None:
        self.register(binder.injector.get(Application))

    def register(self, app: Application) -> None:
        pass
