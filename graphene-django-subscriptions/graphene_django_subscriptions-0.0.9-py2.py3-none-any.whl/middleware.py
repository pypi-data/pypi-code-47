# -*- coding: utf-8 -*-
from promise import is_thenable


class SubscriptionMiddleware:
    def resolve(self, next, root, info, **kwargs):
        result = next(root, info, **kwargs)
        if info.operation.operation == "subscription" and is_thenable(result):
            return result.get()
        return result
