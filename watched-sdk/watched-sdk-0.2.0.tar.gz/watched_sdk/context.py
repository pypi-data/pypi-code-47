import requests
from watched_schema import validators
from .common import logger


class Context(object):
    def __init__(self, addon, action):
        if action in addon.addon_actions:
            self.fn = getattr(addon, action)
        else:
            raise ValueError(
                f'Unknown action "{action}" for addon type "{addon.type}"')

        self.action = action
        self.schema = validators['actions'][action]

    def run(self, request):
        request = self.schema['request'](request)
        logger.info("Calling %s: %s", self.action, request)
        response = self.fn(self, **request)
        return self.schema['response'](response)

    def fetch(self, url, method="GET", **kwargs):
        return requests.request(method, url, **kwargs)

    def fetch_remote(self, *args, **kwargs):
        return self.fetch(*args, **kwargs)
