import meager.router
import meager.http
import meager.logger

import base64
import hashlib
import json
import socketserver
import threading

socketserver.TCPServer.allow_reuse_address = True

WS_MAGIC_STRING = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class RequestHandler(socketserver.BaseRequestHandler):
    def ws_decode_frame(self, frame):
        if(not(frame == bytearray(b""))):
            opcode_and_fin = frame[0]
            payload_len = frame[1] - 128
            mask = frame[2:6]
            encrypted_payload = frame[6:6+payload_len]
            payload = bytearray([encrypted_payload[i] ^ mask[i%4] for i in range(payload_len)])
            try:
                return payload.decode("utf-8")
            except(UnicodeDecodeError):
                return "closed"

    def ws_handshake(self, key):
        key = f"{key}{WS_MAGIC_STRING}".encode("utf-8")
        resp_key = base64.standard_b64encode(hashlib.sha1(key).digest()).decode("utf-8")
        ws_response = f"HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: upgrade\r\nSec-WebSocket-Accept: {resp_key}\r\n\r\n".encode("utf-8")
        return ws_response

    def get_incoming_message(self):
        return self.ws_decode_frame(bytearray(self.request.recv(1024)))

    def ws_send_message(self, payload):
        payload = payload.encode("utf-8")
        frame = [129]

        frame += [len(payload)]

        frame_to_send = bytearray(frame) + payload
        self.request.sendall(frame_to_send)


    def handle(self):
        self.raw = self.request.recv(1024).strip()
        self.data = self.raw.decode("utf-8")
        meager.logger.log(__class__, f"Got request from {self.client_address[0]}")
        parsed = meager.http.parse(self.data)
        route_match = self.server._router.match_request(parsed["url"])

        response = {
            "status": "OK 200",
            "http-version": "HTTP/1.1",
            "content-type": "text/html",
            }

        if(route_match):
            kwargs, function, server_options = route_match
            for key, value in server_options.items():
                response[key] = value

            if("Connection" in parsed["headers"]):
                if("Upgrade" in parsed["headers"]["Connection"]): # It is a websocket upgrade
                    if("websocket" in parsed["headers"]["Upgrade"]):
                        key = parsed["headers"]["Sec-WebSocket-Key"]
                        meager.logger.log(__class__, f"Got websocket connection with key: {key}")
                        self.request.sendall(self.ws_handshake(key))
                        function({"ip": self.client_address[0],"request": parsed}, self, **kwargs)
                        return
            response["content"] = function({"ip": self.client_address[0],"request": parsed}, **kwargs)
            self.request.sendall(meager.http.build_response(response).encode("utf-8"))
        else:
            self.request.sendall(b"HTTP/1.1 NOT FOUND 404\r\nContent-Type: text/html\r\n\r\n<h1>404 not found</h1>")

class Server(object):
    def __init__(self, port=2920, host="127.0.0.1"):
        self.port = port
        self.host = host
        self.router = meager.router.Router()

    def serve(self):
        with ThreadedTCPServer((self.host, self.port), RequestHandler) as sockserv:
            sockserv._router = self.router
            sockserv.serve_forever()
