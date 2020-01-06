from sys import platform
import logging
import threading
import time
import zmq
import sys
from sys import platform
from ctypes import cdll
import os

class ZinnionAPI(object):
    def __init__(self, token, account, subscription, callback):
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
        logging.info("Python ZTrading    : Starting threads")
        logging.info("Python ZTrading    : Token: %s", token)
        logging.info("Python ZTrading    : Account: %s", account)
        logging.info("Python ZTrading    : Subscription: %s", subscription)

        if platform == "linux" or platform == "linux2":
            # linux
            logging.info("Python ZTrading    : Plataform: Linux")
        elif platform == "darwin":
            # OS X
            logging.info("Python ZTrading    : platform not supported")
            sys.exit()
        elif platform == "win32":
            # Windows...
            logging.info("Python ZTrading    : platform not supported")
            sys.exit()

        if 'ZTRADING_LIB' in os.environ:
            self.ztrading_lib = cdll.LoadLibrary(os.environ['ZTRADING_LIB'])
        else:
            logging.error("Python ZTrading    : Please export ZTRADING_LIB= https://github.com/Zinnion/zpytrading/wiki")
            sys.exit()

        self.token = token
        self.account = account
        self.subscription = subscription

        x = threading.Thread(target=self.stream, args=(callback,))
        y = threading.Thread(target=self.zlib_init, args=())
        x.start()
        y.start()

    def hand_data(self, callback, json):
        callback(json)

    def zlib_init(self):
        logging.info("Python ZTrading    : API startup")
        print(self.ztrading_lib.init(bytes(self.token, 'utf-8'),bytes(self.account, 'utf-8'), bytes(self.subscription, 'utf-8')))

    def stream(self, callback):
        logging.info("Python ZTrading    : Stream startup")
        # Prepare our context and publisher
        context = zmq.Context()
        subscriber = context.socket(zmq.SUB)
        
        if 'ZTRADING_STREAM_ADDR' in os.environ:
            subscriber.connect(os.environ['ZTRADING_STREAM_ADDR'])
        else:
            subscriber.connect("tcp://localhost:5555")
        subscriber.setsockopt(zmq.SUBSCRIBE, b"")

        while True:
            # Read envelope with address
            msg = subscriber.recv_json()
            self.hand_data(callback, msg)

        # We never get here but clean up anyhow
        subscriber.close()
        context.term()
