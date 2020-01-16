from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from django_magnificent_messages import MessageBackend


class MessageMiddleware(MiddlewareMixin):
    """
    Middleware that handles temporary messages.
    """

    def process_request(self, request):
        request.dmm_backend = MessageBackend(request)

    def process_response(self, request, response):
        """
        Update the notification_storage backend (i.e., save the messages).

        Raise ValueError if not all messages could be stored and DEBUG is True.
        """
        # A higher middleware layer may return a request which does not contain
        # messages notification_storage, so make no assumption that it will be there.
        if hasattr(request, 'dmm_backend'):
            unstored_messages = request.dmm_backend.update(response)
            if unstored_messages and settings.DEBUG:
                raise ValueError('Not all temporary messages could be stored.')
        return response
