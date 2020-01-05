from .client import NotErrorsClient


def capture_message(message):
    NotErrorsClient._global_client.capture_message(message)


def handle_exception():
    NotErrorsClient._global_client.handle_exception()


noterrors_init = NotErrorsClient.init
