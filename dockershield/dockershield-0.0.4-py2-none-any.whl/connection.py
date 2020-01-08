import threading
import select
import logging
import time

from .parser import HttpParser, Message, HTTP_400_RESPONSE

class Connection(threading.Thread):
    """
        Class to represent a two-way connection
        This acts as a Man-In-The-Middle between docker and docker clients
        Each connection runs in its own thread.
    """

    DENIED_RESPONSE = bytes(HTTP_400_RESPONSE,"utf8")
    CHUNK_SIZE=1024

    def __init__(self, client_socket, upstream_socket, parent, filters):
        """
        Constructor Method
            Inputs:
                client_socket: Socket connected to the docker client.
                upstream_socket: Socket connected to the docker server
                parent: A DockerShield instance which this connection is a part of
                filters: List of filtering rules
        """
        self.filtered = client_socket
        self.upstream = upstream_socket
        self.socket_map = {
            self.filtered: self.upstream,
            self.upstream: self.filtered
        }
        self.running = False
        self.lock = threading.RLock()
        self.parent = parent
        self.filters = filters
        self.parser_map = {
            self.filtered: HttpParser(),
            self.upstream: HttpParser()
        }
        self.last_messages = {
            self.filtered: [],
            self.upstream: []
        }
        self.closed_map = {}
        self.upgraded = False
        self.strikes = 0
        super(Connection, self).__init__(daemon=True)

    def close(self):
        """
        Close both ends of the connection
        Also sets flag so that the thread will stop.
        """
        with self.lock:
            self.running = False
            if self.filtered is not None:
                self.filtered.close()
                self.filtered = None
            if self.upstream is not None:
                self.upstream.close()
                self.upstream = None
            if self in self.parent.connections:
                self.parent.connections.remove(self)

    def handle_closed(self, closed_socket):
        """
        Handle a socket closed event
            Inputs:
                closed_socket: The socket that was just closed.
                Must be one of [self.upstream, self.filtered]
        """

        # Check if the socket was already closed before
        if not self.closed_map.get(closed_socket, False):
            # Print information only if the socket wasn't already closed before
            logging.info("Connection closed on %s end" % self.describe_socket(closed_socket))
            self.closed_map[closed_socket] = True

        # We only stop running if:
        #   1. The client disconnects during a regular HTTP connection
        #   2. The server disconnects at any point
        # We don't stop running if:
        #   1. The client disconnects, but connection is upgraded and server is still connected
        if (closed_socket is self.filtered and not self.upgraded) \
            or closed_socket is self.upstream:
            with self.lock:
                self.running = False

    def read_socket_data(self, timeout=30.0):
        """
        Reads data from both ends of the connection,
        applies filtering rules, and if allowed, passes it to the other end of the connection.
        This also detects if either end of the connection is closed.
        """

        start_time = time.time()
        # We know that poll is more scalable than select, but select is easier (plus we only have 2 sockets, right?)
        readable, _, _ = select.select([self.filtered, self.upstream], [self.filtered, self.upstream], [], timeout)

        # When there is no data, print a warning every 10 seconds
        if len(readable) == 0 and (time.time() - start_time) >= 10.0:
            logging.warn("No data on either end.")

        for input_socket in readable:
            data = input_socket.recv(self.CHUNK_SIZE)
            if len(data) == 0:
                self.handle_closed(input_socket)
                continue

            logging.debug("Read %d bytes from %s" % (len(data), self.describe_socket(input_socket)))
            if not self.upgraded:
                self.parser_map[input_socket].feed(data)
            else:
                self.socket_map[input_socket].sendall(data)

    def describe_socket(self, socket_instance):
        """
        Print a string that describes a socket
            Inputs:
                socket_instance: The socket. Must be one of [self.filtered, self.upstream]
        """
        if socket_instance is self.filtered:
            return "<client>"
        elif socket_instance is self.upstream:
            return "<docker>"
        else:
            assert(socket_instance in [self.filtered, self.upstream])
            return "<unknown>"


    def handle_http_messages(self):
        """
        Handle a completed HTTP message (either a request or response)
        """
        for input_socket, parser in self.parser_map.items():
            if not parser.has_message():
                continue
            output_socket = self.socket_map[input_socket]
            message = parser.pop_message()
            if not self.filters.is_message_allowed(message):
                logging.info("Filtered out a message: %s from %s" % (message.describe(), self.describe_socket(input_socket)))
                if input_socket is self.filtered:
                    input_socket.sendall(self.DENIED_RESPONSE)
                    input_socket.close()
                    with self.lock:
                        self.running = False
                continue

            logging.debug("Allowed a message: %s from %s" % (message.describe(), self.describe_socket(input_socket)))

            if message.type in ["response"]:
                assert(input_socket is self.upstream)
                if message.status in [101] and message.status_text in ["UPGRADED"]:
                    logging.warn("The connection was upgraded; no more filtering will be applied!")
                    self.upgraded = True
            output_socket.sendall(message.raw)

    def inner_loop(self,timeout=120.0):
        """
        The inner loop for the thread
        """
        self.read_socket_data(timeout)
        if not self.upgraded:
            self.handle_http_messages()

    def run(self):
        """
        Thread task.
        Loops until self.running is False
        """
        logging.debug("Started")
        with self.lock:
            self.running = True

        running = True
        while running:
            try:
                self.inner_loop()
            except OSError as e:
                logging.warn("Connection broken: %s" % repr(e))
                running = False

            with self.lock:
                running = running and self.running
        self.close()
