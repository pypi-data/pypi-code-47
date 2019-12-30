from decimal import Decimal

import stripe

from django.conf import settings

from .models import PaymentIntent, Customer, PaymentMethod

# Configure Stripe API Key
stripe.api_key = getattr(settings, 'STRIPE_API_KEY', None)


def generate_new_payment_intent(amount,
                                customer=None,
                                payment_method=None,
                                statement_descriptor_suffix=None,
                                setup_future_usage=None,
                                capture_method=PaymentIntent.CAPTURE_AUTOMATIC,
                                currency='eur'):
    """
    Create new Payment Intent based on parameters provided.

    Returns: PaymentIntent from database with populated fields.
    """
    intent_obj = stripe.PaymentIntent.create(
        amount=convert_to_stripe_amount(amount),
        currency=currency,
        customer=customer,
        payment_method=payment_method,
        setup_future_usage=setup_future_usage,
        capture_method=capture_method,
        statement_descriptor_suffix=statement_descriptor_suffix
    )

    # Store in database PaymentIntent
    intent = PaymentIntent.objects.create(stripe_id=intent_obj.id,
                                          amount=intent_obj.amount,
                                          amount_capturable=intent_obj.amount_capturable,
                                          amount_received=intent_obj.amount_received,
                                          currency=intent_obj.currency,
                                          customer=customer,
                                          payment_method=payment_method,
                                          description=intent_obj.description,
                                          capture_method=intent_obj.capture_method,
                                          client_secret=intent_obj.client_secret,
                                          setup_future_usage=intent_obj.setup_future_usage,
                                          statement_descriptor=intent_obj.statement_descriptor,
                                          statement_descriptor_suffix=intent_obj.statement_descriptor_suffix,
                                          status=intent_obj.status
                                          )

    # return Database Object back
    return intent


def create_stripe_customer(user):
    """
    Create Customer object on Stripe API from Django User object.
    """
    customer_obj = stripe.Customer.create(
        email=user.email,
        name=f"{user.first_name} {user.last_name}"
    )

    customer = Customer.objects.create(stripe_id=customer_obj.id,
                                       user=user,
                                       name=customer_obj.name,
                                       address=customer_obj.address,
                                       email=customer_obj.email)

    return customer


def attach_payment_method_to_customer(payment_method_stripe_id, customer):
    pm_object = stripe.PaymentMethod.attach(payment_method_stripe_id, customer=customer.stripe_id)

    payment_method = PaymentMethod.objects.create(stripe_id=pm_object.id,
                                                  customer=customer,
                                                  user=customer.user,
                                                  brand=pm_object.card.brand,
                                                  country=pm_object.card.country,
                                                  funding=pm_object.card.funding,
                                                  exp_month=pm_object.card.exp_month,
                                                  exp_year=pm_object.card.exp_year,
                                                  last4=pm_object.card.last4,
                                                  fingerprint=pm_object.card.fingerprint,
                                                  supports_3d_secure=pm_object.card.three_d_secure_usage.supported)

    return payment_method


def convert_to_stripe_amount(amount):
    # Convert 1.00€ to 100 for different types
    if type(amount) == Decimal:
        return int(f"{amount * Decimal(100):.0f}")
    else:
        return int(f"{Decimal(amount) * Decimal(100):.0f}")
