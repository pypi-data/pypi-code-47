from typing import Dict

from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _

from payparts.payparts import PayPartsAPIAdapter
from payparts.consts import DEFAULT_MERCHANT_TYPE, DEFAULT_PARTS_COUNT
from payparts.exceptions import InvalidTokenError
from payparts.forms import PayloadForm, ProductForm
from payparts.models import Log
from payparts.signals import (
    pay_parts_invalid_callback,
    pay_parts_success_callback
)

__all__ = (
    'GetRedirectUrlUseCase',
    'ProcessCallbackUseCase'
)


class GetRedirectUrlUseCase:
    """
    Use case to create payment and build redirect url to perform payment
    """
    @staticmethod
    def raise_errors(form) -> None:
        if not form.is_valid():
            raise ValidationError(form.errors)

    def validate(self, data: Dict) -> None:
        products = data.get('products')
        if not products:
            raise ValidationError(
                _('You must provide products to create payment.'))
        self.raise_errors(PayloadForm(data=data))
        for product in products:
            self.raise_errors(ProductForm(data=product))

    def execute(self, data) -> str:
        data['parts_count'] = (
            data.get('parts_count') or
            DEFAULT_PARTS_COUNT
        )
        data['merchant_type'] = (
            data.get('merchant_type') or
            DEFAULT_MERCHANT_TYPE
        )

        self.validate(data)

        order_data = {
            'order_id': data.pop('order_id'),
            'amount': data.pop('amount'),
            'products': data.pop('products')
        }

        adapter = PayPartsAPIAdapter(**data)
        result = adapter.payment_create(order_data)
        adapter.create_log(result, 'payment_create')

        token = result.get('token')

        if token:
            return adapter.get_redirect_url(token)

        raise InvalidTokenError(
            code='token',
            message=(
                f'Invalid token. '
                f'State: {result.get("state", "")}. '
                f'Error: {result.get("message", "")}'
            )
        )


class ProcessCallbackUseCase:
    """
    Use case to process PayParts callback
    """
    def execute(self, request, data) -> None:
        data['state'] = data.pop('paymentState')

        adapter = PayPartsAPIAdapter()
        log = adapter.create_log(data, 'callback')

        is_valid = adapter.validate_signature(data)

        if is_valid:
            pay_parts_success_callback.send(
                sender=Log,
                log=log,
                request=request
            )
        else:
            pay_parts_invalid_callback.send(
                sender=Log,
                log=log,
                request=request
            )
