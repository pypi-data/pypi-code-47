from socketserver import ThreadingUDPServer, BaseRequestHandler
import logging

import click

logger = logging.getLogger(__name__)


class SimpleUdpHandler(BaseRequestHandler):
    """
    Simple request handler for UDP that will log incoming data.
    """

    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        logger.debug(f"Received UDP Message",
            extra={"data": f"{data!r}", "host": self.client_address[0],
                "port": self.client_address[1], }, )


class EchoUdpHandler(BaseRequestHandler):
    """
    Simple requesthandler that will echo the received data back to the sender.
    """

    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        logger.debug(
            f"Received UDP Message",
            extra={
                "data": f"{data!r}",
                "host": self.client_address[0],
                "port": self.client_address[1],
            },
        )

        socket.sendto(data, self.client_address)


@click.command()
@click.option(
    "--host", "-h", help="Host to bind the server too", default="0.0.0.0", type=str
)
@click.option("--port", "-p", help="Port to bind the server too", type=int)
@click.option(
    "--echo",
    "-e",
    is_flag=True,
    default=False,
    help="If the server should echo the data back to the sender",
)
def udp(host, port, echo):
    """
    Runs a threaded UDP server that logs all datagrams it receives. It can alos act as
    an UDP echo server using the --echo flag

    """
    if echo:
        request_handler = EchoUdpHandler
    else:
        request_handler = SimpleUdpHandler

    with ThreadingUDPServer((host, port), request_handler) as server:
        click.secho(
            f"Staring {server.__class__.__name__} on {host}:{port}",
            fg="bright_yellow",
            blink=True,
        )
        server.serve_forever()
