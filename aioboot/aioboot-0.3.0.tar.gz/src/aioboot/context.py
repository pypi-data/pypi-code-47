from contextvars import ContextVar
from typing import Any, Callable, Dict

from aioboot.request import Request

request_scope_var: ContextVar[Dict[Any, Any]] = ContextVar("request_scope")


def get_current_request() -> Request:
    try:
        request_locals = request_scope_var.get()
        return request_locals["self"]
    except (LookupError, AttributeError):
        raise RuntimeError("Trying to get request out of context.")


async def request_scope_middleware(request: Request, call_next: Callable):
    token = request_scope_var.set({"self": request})
    try:
        return await call_next(request)
    finally:
        request_scope_var.reset(token)
