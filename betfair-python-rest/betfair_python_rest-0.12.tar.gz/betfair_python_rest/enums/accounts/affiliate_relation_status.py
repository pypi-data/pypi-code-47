from ..base import BaseEnum


class AffiliateRelationStatus(BaseEnum):
    INVALID_USER = '''Provided vendor client ID is not valid'''
    AFFILIATED = '''Vendor client ID valid and affiliated'''
    NOT_AFFILIATED = '''Vendor client ID valid but not affiliated'''
