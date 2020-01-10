import asyncio
from .xbus_pb2 import EnvelopeAck


class EnvelopeReceiver(object):
    def __init__(self, inputname, fragment=None):
        self.inputname = inputname
        self.fragment = fragment
        self.cond = asyncio.Condition()
        self.task = None

    @property
    def reception_status(self):
        return EnvelopeAck.ACCEPTED

    def is_complete(self):
        return True

    async def receive(self, fragment):
        if self.fragment is not None:
            raise RuntimeError(
                "This primitive EnvelopeReceiver cannot handle multiple "
                "fragments")
        await self.cond.acquire()
        try:
            self.fragment = fragment
            self.cond.notify()
        finally:
            self.cond.release()

    async def complete(self, timeout=1):
        if self.task and self.task.done():
            exc = self.task.exception()
            if exc is not None:
                raise exc

        hit_timeout = False

        async def setquit():
            nonlocal hit_timeout
            await asyncio.sleep(timeout)
            await self.cond.acquire()
            try:
                hit_timeout = True
                self.cond.notify()
            finally:
                self.cond.release()

        t = asyncio.ensure_future(setquit())

        await self.cond.acquire()
        try:
            await self.cond.wait_for(
                lambda: hit_timeout or self.fragment is not None)
            if not hit_timeout:
                t.cancel()
            return self.fragment
        finally:
            self.cond.release()
