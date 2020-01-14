from collections import OrderedDict

from affo_sms_service import settings
from affo_sms_service.extensions import db
from affo_sms_service.models.sms_message import SMSMessage

from . import exception
from .utils import Singleton, import_string


class SMSFactory(metaclass=Singleton):
    def __init__(self):
        self.gateways = self._load_gateways()

    @staticmethod
    def _load_gateways():
        gateways = OrderedDict()

        for gateway_path in settings.SMS_GATEWAYS:
            try:
                gateway_class = import_string(gateway_path)
            except (AttributeError, ModuleNotFoundError):
                raise ImportError(f"{gateway_path} is not valid gateway class!")

            gateways.update({gateway_class.name: gateway_class()})

        return gateways

    @staticmethod
    def _get_next_gateway(gateways, current_gateway_name):
        gateway_names = list(gateways.keys())

        if not gateway_names:
            return None

        try:
            current_gateway_name_index = gateway_names.index(current_gateway_name)

            if current_gateway_name_index == len(gateway_names) - 1:
                gateway_name = gateway_names[0]
            else:
                gateway_name = gateway_names[current_gateway_name_index + 1]
        except ValueError:
            return gateway_names[0]

        return gateway_name

    def get(self, name):
        return self.gateways.get(name)

    def get_for_phone(self, phone, retry=False):
        if not self.gateways:
            return None

        last_sms_message = (
            db.session.query(SMSMessage).filter(SMSMessage.to == phone).order_by(SMSMessage.id.desc()).first()
        )

        if last_sms_message:
            gateway_name = last_sms_message.gateway

            if retry:
                gateway_name = self._get_next_gateway(self.gateways, gateway_name)
            gateway = self.gateways[gateway_name]
        else:
            gateway = next(iter(self.gateways.values()))

        return gateway

    def send(self, from_, to, body, retry=False, key=None):
        gateway = self.get_for_phone(phone=to, retry=retry)

        if not gateway:
            raise exception.SMSNoSuchGateway()

        try:
            gateway.send(from_=from_, to=to, body=body)
        finally:
            db.session.add(SMSMessage(from_=from_, to=to, body=body, gateway=gateway.name))
            db.session.commit()
