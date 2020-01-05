import logging
import threading
import time
import zmq
from ctypes import cdll
ztrading_lib = cdll.LoadLibrary(
    "/home/mauro/zinnion/ztrading/cmake-build-debug/lib/libztrading.so")

class ZinnionAPI(object):
    def __init__(self, token, account, callback):
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
        logging.info("Python ZTrading    : Starting threads")
        logging.info("Python ZTrading    : Token: %s", token)
        logging.info("Python ZTrading    : Account: %s", account)

        self.token = token
        self.account = account
        
        x = threading.Thread(target=self.stream, args=(callback,))
        y = threading.Thread(target=self.zlib_init, args=())
        x.start()
        y.start()

    def hand_data(self, callback, json):
        callback(json)

    def zlib_init(self):
        logging.info("Python ZTrading    : API startup")
        print(ztrading_lib.init(b'Hello World',
                                b'Hello World', b'trade:COINBASEPRO:BTC-USD'))

    def stream(self,callback):
        logging.info("Python ZTrading    : Stream startup")
        # Prepare our context and publisher
        context = zmq.Context()
        subscriber = context.socket(zmq.SUB)
        subscriber.connect("tcp://localhost:5555")
        subscriber.setsockopt(zmq.SUBSCRIBE, b"")
        while True:
            # Read envelope with address
            msg = subscriber.recv_json()
            self.hand_data(callback, msg)

        # We never get here but clean up anyhow
        subscriber.close()
        context.term()
