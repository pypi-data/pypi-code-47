import abc
from dataclasses import dataclass, field
from typing import Callable, List, Optional


@dataclass
class Route:
    method: str
    path: str
    endpoint: Callable
    name: Optional[str] = None
    params: dict = field(default_factory=dict)


class RouterMixin:
    @abc.abstractmethod
    def add_route(
        self,
        method: str,
        path: str,
        endpoint: Callable,
        *,
        name: Optional[str] = None,
        **params,
    ):
        ...

    def route(
        self, method: str, path: str, *, name: Optional[str] = None, **params
    ) -> Callable:
        def decorator(endpoint: Callable) -> Callable:
            self.add_route(
                method=method, path=path, endpoint=endpoint, name=name, **params
            )
            return endpoint

        return decorator

    def get(self, path: str, *, name: Optional[str] = None, **params) -> Callable:
        return self.route("GET", path, name=name, **params)

    def head(self, path: str, *, name: Optional[str] = None, **params) -> Callable:
        return self.route("HEAD", path, name=name, **params)

    def post(self, path: str, *, name: Optional[str] = None, **params) -> Callable:
        return self.route("POST", path, name=name, **params)

    def put(self, path: str, *, name: Optional[str] = None, **params) -> Callable:
        return self.route("PUT", path, name=name, **params)

    def patch(self, path: str, *, name: Optional[str] = None, **params) -> Callable:
        return self.route("PATCH", path, name=name, **params)

    def delete(self, path: str, *, name: Optional[str] = None, **params) -> Callable:
        return self.route("DELETE", path, name=name, **params)

    def options(self, path: str, *, name: Optional[str] = None, **params) -> Callable:
        return self.route("OPTIONS", path, name=name, **params)

    def trace(self, path: str, *, name: Optional[str] = None, **params) -> Callable:
        return self.route("TRACE", path, name=name, **params)


@dataclass
class Router(RouterMixin):
    prefix: Optional[str] = None
    routes: List[Route] = field(default_factory=list)

    def add_route(
        self,
        method: str,
        path: str,
        endpoint: Callable,
        *,
        name: Optional[str] = None,
        **params,
    ):
        self.routes.append(
            Route(method=method, path=path, endpoint=endpoint, name=name, params=params)
        )
