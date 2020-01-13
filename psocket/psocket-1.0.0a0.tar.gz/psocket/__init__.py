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

        try:
            self.sock = socket.create_connection((self.host, self.port))
        except ConnectionRefusedError as err:
            self.logger.error(f'Cannot establish socket connection to {self.host}:{self.port}')
            raise err

    def __str__(self):
        return str(self.socket_response())

    def greeting(self):
        return self.sock.recv(65536).decode().strip()

    def send_command(self, cmd=''):
        command = self._encode_command(cmd)

        self.logger.debug('CONTROL: ' + cmd)

        try:
            self.sock.send(command)
            response = self.socket_response()
            self.logger.debug(response)

            return response
        except AttributeError as err:
            self.logger.error(err)
            # raise

    def socket_response(self):
        data = self.sock.recv(65536).decode()
        response = data.strip().split('\n')
        self.logger.debug('[RESPONSE]: ' + str(response))
        return response

    def close_connection(self):
        self.sock.close()

    @staticmethod
    def _encode_command(cmd):
        return (cmd + '\n').encode()
