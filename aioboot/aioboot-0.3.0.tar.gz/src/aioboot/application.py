import asyncio
import functools
import inspect
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union, cast

import click
from injector import Binder, Module as _Module
from starlette.exceptions import ExceptionMiddleware
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.errors import ServerErrorMiddleware
from starlette.routing import Router as StarletteRouter
from starlette.types import Receive, Scope as ASGIScope, Send

from aioboot import context
from aioboot.cli import CommandGroup
from aioboot.dependency import Injector, Scope, ScopeDecorator, SingletonScope, inject
from aioboot.request import Request
from aioboot.routing import Router, RouterMixin

T = TypeVar("T")
ModuleT = Union[Type["Module"], "Module"]


class Application(RouterMixin):
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
        middleware: Optional[List[Middleware]] = None,
        modules: Optional[List[ModuleT]] = None,
        auto_bind: bool = False,
    ):

        self._debug = debug
        self._injector = Injector(auto_bind=auto_bind)
        self._cli = click.Group()
        self._router = StarletteRouter()
        self._exception_handlers: Dict[Union[int, Type[Exception]], Callable] = {}
        self._middleware: List[Middleware] = middleware or []
        self._middleware_stack = self._build_middleware_stack()

        # Add default bindings
        self.bind(Application, to=self, scope=SingletonScope)
        self.bind(Injector, to=self.injector, scope=SingletonScope)
        self.bind(Request, to=context.get_current_request, scope=SingletonScope)

        # Add default middleware
        self.add_middleware(context.request_scope_middleware)

        # Add default modules
        modules = modules or []
        for module in modules:
            self.add_module(module)

    async def __call__(self, scope: ASGIScope, receive: Receive, send: Send) -> None:
        scope["app"] = self
        await self._middleware_stack(scope, receive, send)

    @property
    def debug(self) -> bool:
        return self._debug

    @property
    def injector(self) -> Injector:
        return self._injector

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
        event = self._inject_event(event)
        self._router.on_startup.append(event)

    def add_shutdown_event(self, event: Callable) -> None:
        event = self._inject_event(event)
        self._router.on_shutdown.append(event)

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

    async def startup(self) -> None:
        await self._router.startup()

    async def shutdown(self) -> None:
        await self._router.shutdown()

    def add_middleware(self, middleware: Union[Middleware, Callable]) -> None:
        if inspect.isfunction(middleware):
            middleware = Middleware(
                BaseHTTPMiddleware,
                dispatch=self._inject_middleware(cast(Callable, middleware)),
            )
        self._middleware.insert(0, cast(Middleware, middleware))
        self._middleware_stack = self._build_middleware_stack()

    def middleware(self) -> Callable:
        def decorator(middleware: Callable) -> Callable:
            self.add_middleware(middleware)
            return middleware

        return decorator

    def add_exception_handler(
        self, status_or_exc: Union[int, Type[Exception]], *, handler: Callable
    ) -> None:
        self._exception_handlers[status_or_exc] = self._inject_exception_handler(
            handler=handler
        )
        self._middleware_stack = self._build_middleware_stack()

    def exception_handler(self, status_or_exc: Union[int, Type[Exception]]) -> Callable:
        def decorator(handler: Callable) -> Callable:
            self.add_exception_handler(status_or_exc, handler=handler)
            return handler

        return decorator

    def add_route(
        self,
        method: str,
        path: str,
        endpoint: Callable,
        *,
        name: Optional[str] = None,
        **params,
    ) -> None:
        endpoint = self._inject_endpoint(endpoint, **params)
        self._router.add_route(path, endpoint=endpoint, methods=[method], name=name)

    def add_router(self, router: Router, *, prefix: Optional[str] = None) -> None:
        prefix = prefix or router.prefix or ""
        if prefix and (not prefix.startswith("/") or prefix.endswith("/")):
            raise ValueError(
                "A path prefix must start with '/' and must not end with '/', "
                "as the routes will start with '/'."
            )
        for route in router.routes:
            self.add_route(
                method=route.method,
                path=f"{prefix}{route.path}",
                endpoint=route.endpoint,
                name=route.name,
                **route.params,
            )

    def add_command(
        self,
        cmd: Callable,
        *,
        name: Optional[str] = None,
        cli: Optional[click.Group] = None,
        lifespan: bool = True,
    ) -> None:
        make_command = click.command()
        cli = cli or self._cli
        cli.add_command(
            make_command(self._inject_command(cmd, lifespan=lifespan)), name=name
        )

    def add_command_group(self, group: CommandGroup) -> None:
        cli = click.Group(name=group.name)
        for command in group.commands:
            self.add_command(
                command.cmd, name=command.name, lifespan=command.lifespan, cli=cli
            )
        self._cli.add_command(cli)

    def command(self, name: Optional[str] = None, *, lifespan: bool = True) -> Callable:
        def decorator(cmd: Callable) -> Callable:
            self.add_command(cmd, name=name, lifespan=lifespan)
            return cmd

        return decorator

    def main(self) -> None:
        self._cli.main()

    def run(self, host: str = "localhost", port: int = 8000) -> None:
        try:
            import uvicorn
        except ImportError:
            raise ImportError("Install `uvicorn` to use run method.")

        uvicorn.run(app=self, host=host, port=port)

    ############################################
    # Private methods
    ############################################

    def _build_middleware_stack(self):

        debug = self.debug
        error_handler = None
        exception_handlers = {}

        for key, value in self._exception_handlers.items():
            if key in (500, Exception):
                error_handler = value
            else:
                exception_handlers[key] = value

        middleware = (
            [Middleware(ServerErrorMiddleware, handler=error_handler, debug=debug)]
            + self._middleware
            + [
                Middleware(
                    ExceptionMiddleware, handlers=exception_handlers, debug=debug
                )
            ]
        )

        app = self._router
        for cls, options in reversed(middleware):
            app = cls(app=app, **options)

        return app

    ############################################
    # Dependency injection methods
    ############################################

    def _inject_event(self, event: Callable) -> Callable:
        def wrapper(func):
            assert asyncio.iscoroutinefunction(
                func
            ), "Event function must be a coroutine."

            @functools.wraps(func)
            async def wrapped():
                return await self.injector.call_with_injection(inject(func))

            return wrapped

        return wrapper(event)

    def _inject_middleware(self, middleware: Callable) -> Callable:
        def wrapper(func):
            assert asyncio.iscoroutinefunction(
                func
            ), "Middleware dispatch function must be a coroutine."

            @functools.wraps(func)
            async def wrapped(request: Request, call_next: Callable):
                return await self.injector.call_with_injection(
                    inject(func), args=(request, call_next)
                )

            return wrapped

        return wrapper(middleware)

    def _inject_exception_handler(self, handler: Callable) -> Callable:
        def wrapper(func):
            assert asyncio.iscoroutinefunction(
                func
            ), "Exception handler function must be a coroutine."

            @functools.wraps(func)
            async def wrapped(request: Request, exc: Exception):
                return await self.injector.call_with_injection(
                    inject(func), args=(request, exc)
                )

            return wrapped

        return wrapper(handler)

    def _inject_endpoint(self, endpoint: Callable, **params) -> Callable:
        setattr(endpoint, "__params__", params)

        def wrapper(func):
            assert asyncio.iscoroutinefunction(
                func
            ), "Endpoint function must be a coroutine."

            @functools.wraps(func)
            async def wrapped(request: Request):  # noqa
                return await self.injector.call_with_injection(inject(func))

            return wrapped

        return wrapper(endpoint)

    def _inject_command(self, cmd: Callable, lifespan: bool = True) -> Callable:
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
                        await self.startup()
                        try:
                            await call()
                        finally:
                            await self.shutdown()
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
