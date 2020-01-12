import asyncio
import pathlib
import ssl
import websockets

port = 25842

async def hello(websocket, path):
    print("client asdas")
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

class Server(object):
    @staticmethod
    def start():
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        localhost_pem = pathlib.Path(__file__).with_name("file.pem")
        ssl_context.load_cert_chain(localhost_pem)

        start_server = websockets.serve(
            hello, "localhost", port, ssl=ssl_context
        )

        asyncio.get_event_loop().run_until_complete(start_server)

        print(F"WSS started and using port: {port}")

        asyncio.get_event_loop().run_forever()

def main():
    Server.start()

if __name__ == "__main__":
    main()
