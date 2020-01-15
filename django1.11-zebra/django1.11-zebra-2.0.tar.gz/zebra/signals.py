"""
Provides the following signals:

V1

- zebra_webhook_recurring_payment_failed
- zebra_webhook_invoice_ready
- zebra_webhook_recurring_payment_succeeded
- zebra_webhook_subscription_trial_ending
- zebra_webhook_subscription_final_payment_attempt_failed
- zebra_webhook_subscription_ping_sent

v2

- zebra_webhook_charge_succeeded
- zebra_webhook_charge_failed
- zebra_webhook_charge_refunded
- zebra_webhook_charge_disputed
- zebra_webhook_customer_created
- zebra_webhook_customer_updated
- zebra_webhook_customer_deleted
- zebra_webhook_customer_card_updated
- zebra_webhook_customer_subscription_created
- zebra_webhook_customer_subscription_updated
- zebra_webhook_customer_subscription_deleted
- zebra_webhook_customer_subscription_trial_will_end
- zebra_webhook_customer_discount_created
- zebra_webhook_customer_discount_updated
- zebra_webhook_customer_discount_deleted
- zebra_webhook_invoice_created
- zebra_webhook_invoice_updated
- zebra_webhook_invoice_payment_succeeded
- zebra_webhook_invoice_payment_failed
- zebra_webhook_invoiceitem_created
- zebra_webhook_invoiceitem_updated
- zebra_webhook_invoiceitem_deleted
- zebra_webhook_plan_created
- zebra_webhook_plan_updated
- zebra_webhook_plan_deleted
- zebra_webhook_coupon_created
- zebra_webhook_coupon_updated
- zebra_webhook_coupon_deleted
- zebra_webhook_transfer_created
- zebra_webhook_transfer_failed
- zebra_webhook_ping

"""
import sys

import django.dispatch


# v1 API webhooks
WEBHOOK_ARGS = ["customer", "full_json"]

zebra_webhook_recurring_payment_failed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_invoice_ready = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_recurring_payment_succeeded = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_subscription_trial_ending = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_subscription_final_payment_attempt_failed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_subscription_ping_sent = django.dispatch.Signal(providing_args=[])

# v2 API webhooks
WEBHOOK2_ARGS = ["full_json"]
ZEBRA_WEBHOOK_SIGNAL_PREFIX = 'zebra_webhook_'
ZEBRA_VERIFIED_WEBHOOK_SIGNAL_SUFFIX = '_verified'
#
# To add a new webhook, simply add its name to the following list.
#
WEBHOOK_NAMES = ['charge_succeeded', 'charge_failed', 'charge_refunded',
                 'charge_disputed', 'customer_created', 'customer_updated',
                 'customer_deleted', 'customer_subscription_created',
                 'customer_subscription_updated',
                 'customer_subscription_deleted',
                 'customer_subscription_trial_will_end',
                 'customer_discount_created', 'customer_discount_updated',
                 'customer_discount_deleted',
                 'customer_card_created',
                 'customer_card_updated',
                 'customer_card_deleted',
                 'invoice_created', 'invoice_updated',
                 'invoice_payment_succeeded', 'invoice_payment_failed',
                 'invoiceitem_created', 'invoiceitem_updated',
                 'invoiceitem_deleted', 'plan_created',
                 'plan_updated', 'plan_deleted', 'coupon_created',
                 'coupon_updated', 'coupon_deleted', 'transfer_created',
                 'transfer_failed', 'ping', ]
WEBHOOK_MAP = {}
module = sys.modules[__name__]
for name in WEBHOOK_NAMES:
    signal_name = ZEBRA_WEBHOOK_SIGNAL_PREFIX + name
    signal = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
    setattr(module, signal_name, signal)
    WEBHOOK_MAP[name] = signal

    verified_signal_name = signal_name + ZEBRA_VERIFIED_WEBHOOK_SIGNAL_SUFFIX
    verified_signal = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
    setattr(module, verified_signal_name, verified_signal)
    WEBHOOK_MAP[name + ZEBRA_VERIFIED_WEBHOOK_SIGNAL_SUFFIX] = verified_signal
