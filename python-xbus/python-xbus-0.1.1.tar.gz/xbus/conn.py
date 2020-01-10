import asyncio
from nats.aio.utils import hex_rand, INBOX_PREFIX
from nats.aio.errors import ErrTimeout


def ClientConn(nc, accountID):
    return CustomInboxPrefixConn(nc, INBOX_PREFIX + str(accountID) + '.in.')


class CustomInboxPrefixConn:
    "Wraps a nats.Client with custom inbox prefix request functions"

    def __init__(self, nc, prefix):
        self.nc = nc
        self.inbox_prefix = prefix

    def __getattr__(self, attr):
        return getattr(self.nc, attr)

    def next_inbox(self):
        return ''.join([
            self.inbox_prefix,
            hex_rand(0x10),
            hex_rand(0x10),
            hex_rand(0x10),
            hex_rand(0x10),
            hex_rand(0x24),
        ])

    async def timed_request(self, subject, payload, timeout=0.5):
        inbox = self.next_inbox()
        future = asyncio.Future(loop=self._loop)
        sid = await self.subscribe(inbox, future=future, max_msgs=1)
        await self.auto_unsubscribe(sid, 1)
        await self.publish_request(subject, inbox, payload)

        try:
            msg = await asyncio.wait_for(future, timeout, loop=self._loop)
            return msg
        except asyncio.TimeoutError:
            future.cancel()
            raise ErrTimeout


class FixedInboxConn:
    def __init__(self, nc, inbox):
        self.nc = nc
        self.inbox = inbox

    def __getattr__(self, attr):
        return getattr(self.nc, attr)

    async def timed_request(self, subject, payload, timeout=0.5):
        inbox = self.inbox
        future = asyncio.Future(loop=self._loop)
        sid = await self.subscribe(inbox, future=future, max_msgs=1)
        await self.auto_unsubscribe(sid, 1)
        await self.publish_request(subject, inbox, payload)

        try:
            msg = await asyncio.wait_for(future, timeout, loop=self._loop)
            return msg
        except asyncio.TimeoutError:
            future.cancel()
            raise ErrTimeout
