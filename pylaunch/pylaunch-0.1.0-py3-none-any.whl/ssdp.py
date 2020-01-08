import socket
import struct
import json

ST_ROKU = 'roku:ecp'
ST_DIAL = 'urn:dial-multiscreen-org:service:dial:1'
__DEFAULT_TIMEOUT__ = 1

class SimpleServiceDiscoveryProtocol:
    
    TIMEOUT = __DEFAULT_TIMEOUT__
    
    def __init__(self, st):
        self.st = st
        self.timeout = SimpleServiceDiscoveryProtocol.TIMEOUT
        self.message = DiscoveryMessage(self.st)

    def broadcast(self) -> list:
        ttl = struct.pack('b', 1)
        results = []

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
            s.settimeout(self.timeout)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
            s.sendto(self.message.encode('utf8'), self.message.DISCOVER_GROUP)

            while True:
                try:
                    data, _ = s.recvfrom(4096)
                    response = HTTPResponse(data)
                    results.append(response)
                except socket.timeout:
                    break
        return results

    @classmethod
    def settimeout(cls, timeout):
        if not isinstance(timeout, (int, float)):
            raise ValueError(f'timeout must be of type int or float and not {type(timeout)}.')
        cls.TIMEOUT = timeout

class DiscoveryMessage(str):

    DISCOVER_GROUP = ('239.255.255.250', 1900)
    
    def __new__(cls, st):
        MESSAGE_CONFIG = {
            'HOST': '%s:%s' % cls.DISCOVER_GROUP,
            'ST': st,
            'MX': SimpleServiceDiscoveryProtocol.TIMEOUT,
            'MAN': 'ssdp:discover'
        }

        DISCOVER_MESSAGE = 'M-SEARCH * HTTP/1.1\r\n' + '\r\n'.join(
            ['%s:%s' % (key, value) for (key, value) in MESSAGE_CONFIG.items() if value]
        ) + '\r\n'

        return str.__new__(cls, DISCOVER_MESSAGE)

class HTTPResponse(dict):
    def __init__(self, response_text):
        
        response = response_text.decode('utf-8').split('\r\n')
        status_line = response[0]

        self.http_version, self.status_code, self.status = status_line.split()
        self.headers = {}

        for line in response[1:]:
            line = line.split()
            if len(line) == 2:
                header_name = line[0][:-1]
                header_value = line[1]
                self.headers[header_name.lower()] = header_value.lower()

    @property
    def json(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.json
