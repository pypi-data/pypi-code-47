from asyncio import Future, gather, iscoroutinefunction
from typing import Any, Callable, Set


class Event:
    _callbacks: Set[Callable]

    def __init__(self) -> None:
        self._callbacks = set()

    def __call__(self, **kwargs: Any) -> Future:
        return gather(*[callback(**kwargs) for callback in self._callbacks])

    def register(self, callback: Callable) -> None:
        if not iscoroutinefunction(callback):
            raise AssertionError("Argument callback should be a coroutine function!")

        self._callbacks.add(callback)

    def unregister(self, callback: Callable) -> None:
        self._callbacks.remove(callback)

    def unregister_all(self) -> None:
        self._callbacks.clear()
