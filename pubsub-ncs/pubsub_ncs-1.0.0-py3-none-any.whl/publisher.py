import json
import socket

from pubsub_ncs.pubsubbase import PubSubBase


class Publisher(PubSubBase):

    def send(self, data):
        if not self.connected:
            self.connection()
        if not data:
            raise None

        if not isinstance(data, (str, bytes, bytearray, memoryview)):
            data = json.dumps(data)

        if isinstance(data, str):
            data = data.encode(self.ENCODING)

        headers = [
            f'Topic: {self.topic}',
            'Role: Pub',
            f'Content-Length: {len(data)}'
        ]
        # header
        self.stream.send(self.DELIMITER.join(headers).encode(self.ENCODING))
        # headerの改行(CRLF)
        self.stream.send(self.DELIMITER.encode(self.ENCODING))
        # CRLF(空行)
        self.stream.send(self.DELIMITER.encode(self.ENCODING))
        # Body
        self.stream.send(data)
