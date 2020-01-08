import json
from decimal import Decimal


class OriginalJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        else:
            return super(OriginalJsonEncoder, self).default(obj)
