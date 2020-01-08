import re
import logging
from .parser import Message

class Filters():

    class Exception(Exception):
        pass

    def __init__(self, d):
        self.blacklisted_methods = d.get("method", {}).get("blacklist", []) or []
        self.whitelisted_methods = d.get("method", {}).get("whitelist", []) or []

        blacklist_url_strings = d.get("url", {}).get("blacklist", []) or []
        whitelist_url_strings = d.get("url", {}).get("whitelist", []) or []

        self.blacklist_regex = [re.compile('^'+s+'$') for s in blacklist_url_strings]
        self.whitelist_regex = [re.compile('^'+s+'$') for s in whitelist_url_strings]

        self.include_version = d.get("url", {}).get("include_version", False)
        self.strict_blacklist = d.get("url", {}).get("strict_blacklist", False)

        self.version_regex = re.compile(r'^v\d+\.\d+$')
        self.has_any_blacklist = any((
            self.blacklisted_methods,
            self.blacklist_regex
        ))

    def is_listed(self, comparison_string, regex_list, logging_label):
        for regex in regex_list:
            logging.debug("%s: Check %s vs %s" % (logging_label, comparison_string, regex))
            if regex.search(comparison_string):
                return True
        return False

    def whitelisted(self, comparison_string):
        return self.is_listed(comparison_string, self.whitelist_regex, "Whitelist")

    def blacklisted(self, comparison_string):
        return self.is_listed(comparison_string, self.blacklist_regex, "Blacklist")

    def is_request_allowed(self, message):
        assert(message.type in ["request"])
        endpoint_list = message.url_path.split("/")
        if endpoint_list.pop(0) != "":
            logging.debug("Block URL that doesn't start with /")
            return False

        # Filter method
        if message.method in self.blacklisted_methods \
            and message.method not in self.whitelisted_methods:
            return False

        version_string = endpoint_list[0]
        if not self.version_regex.search(version_string):
            logging.warn("No version string.")
        elif not self.include_version:
            endpoint_list.pop(0)

        comparison_string = "/".join(endpoint_list)
        logging.debug("Check %s" % comparison_string)

        if self.strict_blacklist:
            return not self.blacklisted(comparison_string)
        else:
            return self.whitelisted(comparison_string) or not self.blacklisted(comparison_string)

    def is_response_allowed(self, message):
        assert(message.type in ["response"])
        return True

    def is_message_allowed(self, message):
        assert(isinstance(message, Message))
        if not self.has_any_blacklist:
            logging.warn("No blacklisting enabled; all messages allowed!")
        if message.type in ["request"]:
            return self.is_request_allowed(message)
        elif message.type in ["response"]:
            return self.is_response_allowed(message)
        else:
            logging.warn("Allowing unknown message %s" % message.describe())
        return True
