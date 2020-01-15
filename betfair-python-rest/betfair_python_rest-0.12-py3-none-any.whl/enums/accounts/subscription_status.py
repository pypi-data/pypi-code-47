from ..base import BaseEnum


class SubscriptionStatus(BaseEnum):
    ALL = '''Any subscription status'''
    ACTIVATED = '''Only activated subscriptions'''
    UNACTIVATED = '''Only unactivated subscriptions'''
    CANCELLED = '''Only cancelled subscriptions'''
    EXPIRED = '''Only expired subscriptions'''

