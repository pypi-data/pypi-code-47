import json
import stripe

from django.conf import settings

from .models import PaymentIntent, PaymentMethod
from .helpers import attach_payment_method_to_customer
from .exceptions import StripeEventException, StripeWrongEventTypeException

# Configure Stripe API Key
stripe.api_key = getattr(settings, 'STRIPE_API_KEY', None)


def construct_webhook_event(payload, sig_header, endpoint_secret):
    """
    Construct webhook event
    """
    try:

        return stripe.Event.construct_from(
            json.loads(payload),
            sig_header,
            endpoint_secret)
    except ValueError as e:
        raise StripeEventException(e)


def process_payment_intent_succeeded_webhook(payload):
    """
    Process Payment Intent Succeeded Webhook event.

    It will update amount capturable, received, status and attach a Payment Method to a Customer instance if
    it's a new payment method.
    """
    event = construct_webhook_event(payload)

    if event.type != 'payment_intent.succeeded':
        raise StripeWrongEventTypeException('Event is not of type payment_intent.succeeded')

    intent_obj = event.data.object  # contains a stripe.PaymentIntent object
    intent = PaymentIntent.objects.get(stripe_id=intent_obj.id)

    # Get Payment method Stripe ID
    payment_method_stripe_id = intent_obj.payment_method

    # Attach Payment Method to Customer object if it doesn't exist in the system
    if not PaymentMethod.objects.filter(stripe_id=payment_method_stripe_id).exists():
        payment_method = attach_payment_method_to_customer(payment_method_stripe_id, intent.customer)
        intent.payment_method = payment_method

    intent.amount_capturable = intent_obj.amount_capturable
    intent.amount_received = intent_obj.amount_received
    intent.status = intent_obj.status
    intent.save()

    return intent
