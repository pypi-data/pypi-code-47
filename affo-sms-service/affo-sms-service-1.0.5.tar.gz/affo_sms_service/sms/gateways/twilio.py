from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from affo_sms_service import settings

from .base import BaseSMSGateway
from .. import exception


class TwilioGateway(BaseSMSGateway):
    name = "twilio"

    def __init__(self):
        super().__init__()

        self.client = Client(username=settings.TWILIO_ACCOUNT_SID, password=settings.TWILIO_AUTH_TOKEN)

    def _send(self, to, from_, body):
        return self.client.messages.create(to=to, from_=from_, body=body)

    def send(self, to, from_, body):
        try:
            message = self._send(to, from_, body)
        except TwilioRestException as exc:
            if exc.code == 21211:
                raise exception.InvalidPhone(exc.msg)

            raise exception.SMSError(exc.msg)

        return message
