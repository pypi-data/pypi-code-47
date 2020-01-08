import logging
import re
from urllib.parse import urlparse

HTTP_400_RESPONSE = "HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n"


class Message():
    def __init__(self, raw_bytes):
        self.raw = raw_bytes
        self.string = str(self.raw, 'utf8')
        lines = self.string.split("\r\n")
        self.parse_header(lines.pop(0))
        self.parse_fields(lines)
        self.content_length = int(self.fields.get("Content-Length", 0))
        self.content = bytes()

    def parse_fields(self, lines):
        self.fields = {}
        for line in lines:
            for match in re.finditer(r'(?P<key>^.+): (?P<value>.+)$', line):
                self.fields[match.group("key")] = match.group("value")


    def parse_header(self, header):
        if header.startswith("HTTP/"):
            self.type = "response"
            for match in re.finditer(r'^HTTP/\d+\.\d+\s+(?P<status>\d+)\s+(?P<status_text>.*)$', header):
                self.status = int(match.group("status"))
                self.status_text = match.group("status_text")
        else:
            self.type = "unknown"
            for match in re.finditer(r'^(?P<method>\S+)\s+(?P<url>.+)\s+(HTTP/\d+(\.\d+)?)?$', header):
                self.method = match.group("method")
                self.url = match.group("url")
                self.type = "request"
                self.url_path = urlparse(self.url).path

    def finished(self):
        return len(self.content) == self.content_length

    def add_content(self, data):
        self.content += data
        self.raw += data

    def describe(self):
        if self.type in ["request"]:
            return "Request: %s %s" % (self.method, self.url_path)
        elif self.type in ["response"]:
            return "Response: %d %s, %d bytes" % (self.status, self.status_text, self.content_length)
        else:
            return "<unknown message %d bytes, first 50 bytes: %.50s>" % (len(self.raw), repr(str(self.raw, 'utf8')))


class HttpParser():
    DELIMITERS = [
        bytes("\r\n\r\n", 'utf8')
    ]

    class State():
        WAITING_FOR_HTTP = 0
        WAITING_FOR_CONTENT = 1


    def __init__(self):
        self.messages = []
        self.raw_message_header = bytes()
        self.next_message = None
        self.state = HttpParser.State.WAITING_FOR_HTTP


    def feed_http_header_one_byte(self, data):
        assert(isinstance(data, bytes))
        #logging.debug("State: %d" % self.state)
        assert(self.state is HttpParser.State.WAITING_FOR_HTTP)
        assert(self.next_message is None)
        self.raw_message_header += data
        #logging.debug("\n"+repr(str(self.raw_message_header, 'utf8')))
        if any(
            self.raw_message_header.endswith(delimiter) \
                for delimiter in self.DELIMITERS
        ):
            self.next_message = Message(self.raw_message_header)
            self.raw_message_header = bytes()
            if not self.next_message.finished():
                self.state = HttpParser.State.WAITING_FOR_CONTENT
                logging.debug("Waiting for message content (%s)." % (self.next_message.describe(),))
            else:
                self.messages += [self.next_message]
                self.next_message = None
                logging.debug("Completed message with no content.")

    def feed_http_header(self, data):
        for single_byte in data:
            self.feed_http_header_one_byte(bytes([single_byte]))

    def feed_content(self, data):
        assert(self.state is HttpParser.State.WAITING_FOR_CONTENT)
        assert(isinstance(self.next_message, Message))
        self.next_message.add_content(data)
        if self.next_message.finished():
            self.messages += [self.next_message]
            self.next_message = None
            self.state = HttpParser.State.WAITING_FOR_HTTP
            logging.debug("Completed content.")

    def feed(self, data):
        index = 0
        while self.state is HttpParser.State.WAITING_FOR_HTTP \
            and index < len(data):
            single_byte = data[index:index+1]
            self.feed_http_header_one_byte(single_byte)
            index += 1

        if self.state is self.State.WAITING_FOR_CONTENT:
            logging.debug("State: %d, index %d out of %d" % (self.state, index, len(data)))
            self.feed_content(data[index:])

    def has_message(self):
        return len(self.messages) > 0

    def pop_message(self):
        return self.messages.pop(0)

    def peek_message(self):
        return self.messages[0]

    def generate_messages(self, bytes_like):
        for data in bytes_like:
            self.feed(data)
            while self.has_message():
                yield self.pop_message()
