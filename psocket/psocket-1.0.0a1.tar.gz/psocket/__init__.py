import logging
import socket


class SocketClient:
    """
    Create socket and establish connect to service using tuple host+port
    """

    def __init__(self, host, port, logger_enabled: bool = True):
        self.host = host
        self.port = port
        self.logger_enabled = logger_enabled

        # Initialize logger
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.disabled = not self.logger_enabled

        self.logger.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter(fmt='%(asctime)-15s [%(name)s] [LINE:%(lineno)d] [%(levelname)s] %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def __str__(self):
        return str(self.socket_response())

    @property
    def client(self):
        """Create socket connection within 7 sec timeout"""

        try:
            return socket.create_connection((self.host, self.port), timeout=7)
        except ConnectionRefusedError as err:
            self.logger.error(f'Cannot establish socket connection to {self.host}:{self.port}')
            raise err

    def is_host_available(self, port: int = 0, timeout: int = 5) -> bool:
        """Check remote host is available using specified port.

        Port 0 used by default. Used port from construct is not specified.
        """

        port_ = port if port else self.port

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            response = sock.connect_ex((self.host, port_))
            result = False if response else True
            self.logger.info(f'{self.host}:{self.port} is available: {result}')
            return result

    def greeting(self):
        return self.client.recv(65536).decode().strip()

    def send_command(self, cmd=''):
        command = self._encode_command(cmd)

        self.logger.debug('COMMAND: ' + cmd)

        try:
            self.client.send(command)
            response = self.socket_response()
            self.logger.debug(response)

            return response
        except AttributeError as err:
            self.logger.error(err)
            # raise

    def socket_response(self):
        data = self.client.recv(65536).decode()
        response = data.strip().split('\n')
        self.logger.debug('[RESPONSE]: ' + str(response))
        return response

    def close_connection(self):
        self.client.close()

    @staticmethod
    def _encode_command(cmd):
        return (cmd + '\n').encode()

    def get_sock_name(self) -> tuple:
        """Get local IP and port"""
        return self.client.getsockname()

    def get_peer_name(self) -> tuple:
        """Get remote IP and port"""
        return self.client.getpeername()
