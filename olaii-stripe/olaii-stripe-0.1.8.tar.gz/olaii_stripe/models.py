from django.db import models
from django.conf import settings


class Customer(models.Model):
    stripe_id = models.CharField(max_length=255)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='stripe_customer')

    name = models.CharField(max_length=255, null=True, blank=True)

    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.stripe_id}] {self.email}"


class PaymentMethod(models.Model):
    FUNDING_CREDIT = 'credit'
    FUNDING_DEBIT = 'debit'
    FUNDING_PREPAID = 'prepaid'
    FUNDING_UNKNOWN = 'unknown'

    FUNDING_OPTIONS = [
        (FUNDING_CREDIT, 'Credit'),
        (FUNDING_DEBIT, 'Debit'),
        (FUNDING_PREPAID, 'Prepaid'),
        (FUNDING_UNKNOWN, 'Unknown'),
    ]

    stripe_id = models.CharField(max_length=255)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='stripe_cards')
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)

    # Card Details
    brand = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
    funding = models.CharField(max_length=255, choices=FUNDING_OPTIONS, default=FUNDING_UNKNOWN)

    exp_month = models.PositiveIntegerField(default=0)
    exp_year = models.PositiveIntegerField(default=0)
    last4 = models.CharField(max_length=255)

    fingerprint = models.CharField(max_length=255)
    supports_3d_secure = models.BooleanField()

    deleted = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.stripe_id}] {self.last4}"


class PaymentIntent(models.Model):
    CAPTURE_AUTOMATIC = 'automatic'
    CAPTURE_MANUAL = 'manual'

    CAPTURE_OPTIONS = [
        (CAPTURE_AUTOMATIC, 'Automatic'),
        (CAPTURE_MANUAL, 'Manual'),
    ]

    FUTURE_ON_SESSION = 'on_session'
    FUTURE_OFF_SESSION = 'off_session'

    FUTURE_USAGE_OPTIONS = [
        (FUTURE_ON_SESSION, 'On Session'),
        (FUTURE_OFF_SESSION, 'Off Session'),
    ]

    STATUS_REQUIRES_PAYMENT_METHOD = 'requires_payment_method'
    STATUS_REQUIRES_CONFIRMATION = 'requires_confirmation'
    STATUS_REQUIRES_ACTION = 'requires_action'
    STATUS_PROCESSING = 'processing'
    STATUS_REQUIRES_CAPTURE = 'requires_capture'
    STATUS_CANCELED = 'canceled'
    STATUS_SUCCEEDED = 'succeeded'

    STATUS_OPTIONS = [
        (STATUS_REQUIRES_PAYMENT_METHOD, 'Requires Payment Method'),
        (STATUS_REQUIRES_CONFIRMATION, 'Requires Confirmation'),
        (STATUS_REQUIRES_ACTION, 'Requires Action'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_REQUIRES_CAPTURE, 'Requires Capture'),
        (STATUS_CANCELED, 'Canceled'),
        (STATUS_SUCCEEDED, 'Succeeded')
    ]

    stripe_id = models.CharField(max_length=255)

    amount = models.PositiveIntegerField(default=0)
    amount_capturable = models.PositiveIntegerField(default=0)
    amount_received = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=3, default='eur')

    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='payment_intents')
    payment_method = models.ForeignKey(PaymentMethod, null=True, blank=True, on_delete=models.SET_NULL)

    description = models.TextField(blank=True, null=True)

    canceled_at = models.DateTimeField(null=True, blank=True)
    cancellation_reason = models.CharField(max_length=255, null=True, blank=True)

    capture_method = models.CharField(max_length=255, choices=CAPTURE_OPTIONS, default=CAPTURE_AUTOMATIC)

    client_secret = models.CharField(max_length=255)

    setup_future_usage = models.CharField(max_length=255, null=True, blank=True, choices=FUTURE_USAGE_OPTIONS, default=None)

    # Only for non-card payments
    statement_descriptor = models.CharField(max_length=22, null=True, blank=True)
    # For Card payments
    statement_descriptor_suffix = models.CharField(max_length=22, null=True, blank=True)

    status = models.CharField(max_length=255, choices=STATUS_OPTIONS, default=STATUS_REQUIRES_PAYMENT_METHOD)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.stripe_id}] {self.amount} {self.currency}"
