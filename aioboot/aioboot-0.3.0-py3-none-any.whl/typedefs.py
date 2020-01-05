from typing import Awaitable, Callable

from aioboot.request import Request
from aioboot.response import Response

Handler = Callable[[Request], Awaitable[Response]]
