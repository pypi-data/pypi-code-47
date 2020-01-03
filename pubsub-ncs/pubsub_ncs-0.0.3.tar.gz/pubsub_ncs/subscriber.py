import json
import socket

from pubsub_ncs.pubsubbase import PubSubBase


class RecvData:

    def __init__(self, header, body):
        self.header = header
        try:
            self.body = json.loads(body)
        except json.JSONDecodeError:
            self.body = body


class Subscriber(PubSubBase):

    def __init__(self, topic, **kwargs):
        super().__init__(topic, **kwargs)
        self.stream.settimeout(0.1)

    def _recive(self):
        all_data = []
        while True:
            try:
                data = self.stream.recv(1024)
                if data == b'':
                    break
                all_data.append(data)
            except socket.timeout:
                break
            except Exception as e:
                raise e
        all_data = b''.join(all_data)
        return all_data

    def reciver(self, commit_=True) -> 'RecvData':
        while True:
            try:
                body_data = {
                    'commit': commit_
                }
                body_data = json.dumps(body_data)
                data = [
                    f'Topic: {self.topic}',
                    'Role: Sub',
                    f'Content-Length: {len(body_data)}'
                ]
                # header
                self.stream.send(self.DELIMITER.join(
                    data).encode(self.ENCODING))
                # headerの改行
                self.stream.send(self.DELIMITER.encode(self.ENCODING))
                # 空行(CRLF)
                self.stream.send(self.DELIMITER.encode(self.ENCODING))
                # body
                self.stream.send(body_data.encode(self.ENCODING))
                all_data = self._recive()
                if all_data:
                    headers_, body = all_data.split(b'\r\n\r\n', 1)
                    headers = headers_.decode(self.ENCODING)
                    header_data = {}
                    for header in headers.split(self.DELIMITER):
                        parts = header.split(':')
                        if len(parts) == 2:
                            header_data[parts[0].strip()] = parts[1].strip()
                    body_data_: bytes = body[:int(
                        header_data["Content-Length"])]
                    body_data = body_data_.decode(self.ENCODING)
                    yield RecvData(header_data, body_data)
                else:
                    continue
            except Exception as e:
                raise e
