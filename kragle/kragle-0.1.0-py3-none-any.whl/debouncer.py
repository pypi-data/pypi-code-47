import asyncio

from typing import Callable, Awaitable


class AsyncTimer:
    def __init__(self, delay: float, callback: Callable[[], Awaitable[None]]):
        self._delay = delay
        self._callback = callback
        self._task = asyncio.create_task(self._job())

    async def _job(self):
        await asyncio.sleep(self._delay)
        await self._callback()

    def cancel(self):
        self._task.cancel()


class Debouncer:
    def __init__(self):
        self.timers = {}

    def debounce(self, delay: float, key: str, fn: Callable[[], Awaitable[None]]) -> None:
        async def call_it():
            self.timers.pop(key, None)
            await fn()

        try:
            self.timers[key].cancel()
        except KeyError:
            pass
        self.timers[key] = AsyncTimer(delay, call_it)
