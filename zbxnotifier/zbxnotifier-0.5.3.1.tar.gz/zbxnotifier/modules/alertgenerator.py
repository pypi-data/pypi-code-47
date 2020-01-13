import sys
from win10toast import ToastNotifier
from threading import Thread
import time
from queue import Queue
import logging
from zbxnotifier.modules.settings import Settings
logger = logging.getLogger('basic')


class Message:
    def __init__(self, title, message):
        self.title = title
        self.message = message


class AlertGenerator:
    notifyier = None
    message_queue = None
    signal_queue = None
    @staticmethod
    def init(signal_queue):
        AlertGenerator.notifyier = ToastNotifier()
        AlertGenerator.message_queue = Queue()
        AlertGenerator.signal_queue = signal_queue

        if sys.platform == 'win32':
            alert_thread = Thread(target=AlertGenerator._alert_worker_windows, args=[])
            alert_thread.start()

    @staticmethod
    def add_alert(message_title, message):
        AlertGenerator.message_queue.put(Message(message_title, message))

    @staticmethod
    def _alert_worker_windows():
        logger.info("Starting windows alert worker")
        while AlertGenerator.signal_queue.empty():
            if not AlertGenerator.message_queue.empty():
                message = AlertGenerator.message_queue.get()
                AlertGenerator.notifyier.show_toast(message.title, message.message, threaded=True, duration=int(Settings.config.get('Application', 'AlertTimeout')))
                while AlertGenerator.notifyier.notification_active():
                    time.sleep(0.1)
                time.sleep(2)
            time.sleep(2)
        logger.info("Stopping windows alert worker")

