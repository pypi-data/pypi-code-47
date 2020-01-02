import asyncio
import concurrent.futures
from functools import partial
from typing import Any, Callable, Coroutine, List, Optional

from ddtrace import tracer
from ddtrace.context import Context


def current_context() -> Optional[Context]:
    span = tracer.current_span()
    if span:
        return span.context.clone()
    return None


def _warp_trace_context(context: Context, func: Callable, *args) -> Any:
    tracer.context_provider.activate(context)
    return func(*args)


async def run_in_executor(  # pylint: disable=too-many-arguments
    func: Callable,
    *args,
    context: Optional[Context] = None,
    executor: Optional[concurrent.futures.Executor] = None,
    loop: Optional[asyncio.AbstractEventLoop] = None
) -> Coroutine:
    context = context or current_context()
    loop = loop or asyncio.get_event_loop()
    return loop.run_in_executor(executor, _warp_trace_context, context, func, *args)


def gather_in_executor(  # pylint: disable=too-many-arguments
    func: Callable,
    items: List,
    expand: bool = False,
    context: Optional[Context] = None,
    executor: Optional[concurrent.futures.Executor] = None,
    loop: Optional[asyncio.AbstractEventLoop] = None
) -> Coroutine:
    context = context or current_context()
    loop = loop or asyncio.get_event_loop()
    _run_in_executor = partial(run_in_executor, func=func, context=context, executor=executor, loop=loop)
    return asyncio.gather(*[_run_in_executor(*item if expand else item) for item in items])


async def _async_warp_trace_context(context: Context, coroutine: Coroutine, *args) -> Any:
    tracer.context_provider.activate(context)
    return await coroutine(*args)


def gather(coroutine: Coroutine, items: List, expand: bool = False, context: Optional[Context] = None) -> Coroutine:
    context = context or current_context()
    return asyncio.gather(*[_async_warp_trace_context(context, coroutine, *item if expand else item) for item in items])


async def _async_warp_coroutine_trace_context(context: Context, coroutine: Coroutine) -> Any:
    tracer.context_provider.activate(context)
    return await coroutine


def create_task(
    coroutine: Coroutine,
    context: Optional[Context] = None,
    loop: Optional[asyncio.AbstractEventLoop] = None
) -> Coroutine:
    context = context or current_context()
    loop = loop or asyncio.get_event_loop()
    return loop.create_task(_async_warp_coroutine_trace_context(context, coroutine))


async def wait_for(
    coroutine: Coroutine,
    timeout: int,
    context: Optional[Context] = None,
    loop: Optional[asyncio.AbstractEventLoop] = None
) -> Any:
    context = context or current_context()
    loop = loop or asyncio.get_event_loop()
    coroutine = asyncio.wait_for(coroutine, timeout=timeout, loop=loop)
    try:
        return await coroutine
    except asyncio.TimeoutError:
        pass
    return None
