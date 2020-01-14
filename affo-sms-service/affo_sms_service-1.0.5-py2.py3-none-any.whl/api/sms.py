import connexion

from affo_sms_service.sms.exception import InvalidPhone
from affo_sms_service.sms.sms_factory import SMSFactory

from . import exception


def create(body: dict) -> tuple:
    factory = SMSFactory()

    try:
        factory.send(from_=body["from"], to=body["phone"], body=body["message"], retry=body.get("retry", False))
    except InvalidPhone as exc:
        raise exception.InvalidPhone(description=str(exc))

    return connexion.NoContent, 201
