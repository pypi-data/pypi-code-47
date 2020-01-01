import socket
import ssl
from ipaddress import ip_address, IPv6Address
from typing import Tuple, Union, Optional

from anyio import abc, IPAddressType
from anyio.abc import Socket
from anyio.exceptions import ClosedResourceError


class StreamSocketServer(abc.SocketStreamServer):
    __slots__ = '_socket', '_ssl_context', '_autostart_tls', '_tls_standard_compatible'

    def __init__(self, sock: abc.Socket, ssl_context: Optional[ssl.SSLContext],
                 autostart_tls: bool, tls_standard_compatible: bool) -> None:
        self._socket = sock
        self._ssl_context = ssl_context
        self._autostart_tls = autostart_tls
        self._tls_standard_compatible = tls_standard_compatible

    async def close(self) -> None:
        await self._socket.close()

    @property
    def socket(self) -> Socket:
        return self._socket

    def getsockopt(self, level, optname, *args):
        return self._socket.raw_socket.getsockopt(level, optname, *args)

    def setsockopt(self, level, optname, value, *args) -> None:
        self._socket.setsockopt(level, optname, value, *args)

    @property
    def address(self) -> Union[Tuple[str, int], Tuple[str, int, int, int], str]:
        return self._socket.getsockname()

    @property
    def port(self) -> int:
        address = self._socket.getsockname()
        if isinstance(address, tuple):
            return cast(int, self.address[1])
        else:
            raise ValueError('Not a TCP socket')

    async def accept(self):
        sock, addr = await self._socket.accept()
        try:
            stream = SocketStream(sock, self._ssl_context, None, self._tls_standard_compatible)
            if self._ssl_context and self._autostart_tls:
                await stream.start_tls()

            return stream
        except BaseException:
            await sock.close()
            raise

    async def accept_connections(self):
        while self._socket.fileno() != -1:
            try:
                yield await self.accept()
            except ClosedResourceError:
                break


class UDPSocket(abc.UDPSocket):
    __slots__ = '_raw_socket'

    def __init__(self, sock: socket.SocketType):
        self._raw_socket = sock

    @property
    def raw_socket(self) -> socket.SocketType:
        return self._raw_socket

    async def close(self):
        await self._raw_socket.close()

    @property
    def address(self) -> Union[Tuple[str, int], Tuple[str, int, int, int]]:
        return self._raw_socket.getsockname()

    @property
    def port(self) -> int:
        return self.address[1]

    def getsockopt(self, level, optname, *args):
        return self._raw_socket.getsockopt(level, optname, *args)

    def setsockopt(self, level, optname, value, *args) -> None:
        self._raw_socket.setsockopt(level, optname, value, *args)

    async def receive(self, max_bytes: int) -> Tuple[bytes, Tuple[str, int]]:
        data, addr = await self._raw_socket.recvfrom(max_bytes)
        return data, addr[:2]

    async def receive_packets(self, max_size: int):
        while self._raw_socket.fileno() != -1:
            packet, address = await self.receive(max_size)
            if packet:
                yield packet, address
            else:
                break

    async def send(self, data: bytes, address: Optional[IPAddressType] = None,
                   port: Optional[int] = None) -> None:
        if address is not None and port is not None:
            await self._raw_socket.sendto(data, (str(address), port))
        else:
            await self._raw_socket.send(data)


async def get_bind_address(interface: Optional[IPAddressType]) -> Tuple[str, int, bool]:
    if interface:
        if_addr = ip_address(interface)
        family = socket.AF_INET6 if if_addr.version == 6 else socket.AF_INET
        v6only = interface == '::'
        return str(if_addr), family, v6only
    elif socket.has_ipv6:
        return '::', socket.AF_INET6, False
    else:
        return '0.0.0.0', socket.AF_INET, False
