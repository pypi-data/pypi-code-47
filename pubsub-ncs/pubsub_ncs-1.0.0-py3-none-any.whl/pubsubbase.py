import socket
from concurrent.futures import Future
import os


class PubSubBase:
    ENCODING = 'utf-8'
    DELIMITER = '\r\n'

    def __init__(self, topic, **kwargs):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.stream = s
        self.topic = topic
        self.host = self.port = None
        if 'host' in kwargs:
            self.host = kwargs['host']
        else:
            self.host = str(os.getenv('pubsub_host', None))
        if 'port' in kwargs:
            self.port = kwargs['port']
        else:
            self.port = os.getenv('pubsub_port', None)
        if not self.port is None:
            self.port = int(self.port)
        self._connected = False
        self.connection()

    def _get_connected(self) -> bool:
        return self._connected

    connected = property(fget=_get_connected)

    def connection(self, _host=None, _port=None):
        try:
            host = _host or self.host or 'localhost'
            port = _port or self.port or 49152
            if not self._connected:
                self.stream.connect((host, port))
                self._connected = True
        except ConnectionRefusedError:
            raise ConnectionRefusedError('接続出来ません %(host)s:%(port)s' % {
                                         'host': host, 'port': str(port)})

    def close(self):
        self.stream.close()
        self._connected = False
