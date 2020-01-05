from contextvars import ContextVar
from typing import Any, Dict

from aiohttp import web

from aioboot.request import Request
from aioboot.typedefs import Handler

request_scope_var: ContextVar[Dict[Any, Any]] = ContextVar("request_scope")


def get_current_request() -> Request:
    try:
        request_locals = request_scope_var.get()
        return request_locals["self"]
    except (LookupError, AttributeError):
        raise RuntimeError("Trying to get request out of context.")


@web.middleware
async def request_scope_middleware(request: Request, handler: Handler):
    token = request_scope_var.set({"self": request})
    try:
        return await handler(request)
    finally:
        request_scope_var.reset(token)
