import requests
import logging
from datetime import timedelta

from prefect.engine.result_handlers import JSONResultHandler
from prefect.utilities.tasks import defaults_from_attrs
from .query import Query
from . import errors


class QueryCA(Query):
    """
    Base Query.
    """
    def __init__(self, url=None, key=None, service=None, max_retries=3, retry_delay=timedelta(minutes=1)):
        super().__init__(url, key, max_retries, retry_delay)
        self.name = "Central Authority Get Company"
        self.log_prefix = self.build_log_prefix()
        self.url = url
        self.key = key
        self.service = service

    def prep(self, url: str, ca_id):
        return "{url}/entity/{ca_id}?includeUnverified=true".format(url=url, ca_id=ca_id)

    def query(self, url):
        if "error" in url:
            return url
        logging.debug("{}: url {}".format(self.log_prefix, url))
        try:
            response = requests.get(
                url=url,
                params={},
                headers={'Authorization': self.key},
            )
            return response
        except:
            return self.error(errors.query_failed(url))

    @defaults_from_attrs('url', 'service')
    def run(self, data, url=None, service=None):
        full_url = self.prep(url, data)
        response = self.query(full_url)
        result = self.process(response)
        return result


class QueryCACompany(QueryCA):
    """
    Query to get datasys or rankings id.
    """
    def __init__(self, url=None, key=None, service=None, max_retries=3, retry_delay=timedelta(minutes=1)):
        super().__init__(url, key, max_retries, retry_delay)
        self.name = "Central Authority Get Company"
        self.log_prefix = self.build_log_prefix()
        self.url = url
        self.key = key
        self.service = service

    def prep(self, url: str, ca_id):
        return "{url}/entity/{ca_id}?includeUnverified=true".format(url=url, ca_id=ca_id)

    def post_process(self, result, service):
        if "error" in result:
            return result
        if "biids" not in result:
            return self.error(errors.field_dne("biids"))
        lst = result["biids"]
        for item in lst:
            if item["service"] == service:
                return item["value"]
        return self.error(errors.service_name_dne(service))

    def query(self, url):
        if "error" in url:
            return url
        logging.debug("{}: url {}".format(self.log_prefix, url))
        try:
            response = requests.get(
                url=url,
                params={},
                headers={'Authorization': self.key},
            )
            if response is not None:
                return response
            return self.error(errors.bad_response)
        except:
            return self.error(errors.query_failed(url))

    @defaults_from_attrs('url', 'service')
    def run(self, data, url=None, service=None):
        full_url = self.prep(url, data)
        response = self.query(full_url)
        result = self.process(response)
        biid = self.post_process(result, service)
        return biid