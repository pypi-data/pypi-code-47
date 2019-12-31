import http.client
import socket
import json
import os
import sys

if sys.version_info[0] == 2:
    from urlparse import urlparse
elif sys.version_info[0] == 3:
    from urllib.parse import urlparse

from .errors import *


class BuddyNSAPI:
    def __init__(self, key, endpoint='https://www.buddyns.com/api/v2/', validate_auth=True, timeout=4):
        """Construct a client to the BuddyNS API.
        
        @param key          authentication token
        @param endpoint     optional custom API base URL"""
        # permit overriding default API base with environment variable
        if 'BUDDYNS_API_DESTINATION' in os.environ:
            endpoint = os.environ['BUDDYNS_API_DESTINATION']
        self.endpoint = self.parse_base(endpoint)
        self.apikey = key
        self.base_path = self.endpoint[3].rstrip('/') + '/'
        self.timeout = timeout
        self.conn = None
        if validate_auth:
            # issue one request to validate authentication
            try:
                self.list_domains()
            except BuddyNSAPIError:
                raise AuthenticationFailed("Provided API key '%s' fails to authenticate." % self.apikey)
            except socket.timeout as e:
                raise
            except:
                raise

    def __del__(self):
        self.close()

    def parse_base(self, base):
        up = urlparse(base)
        return (up.scheme, up.hostname, up.port or (443 if up.scheme == 'https' else 80), up.path)

    def reconn(fun):
        def _conrun(self, *args, **kwargs):
            if not self.conn:
                self.conn = self.connect()
            try:
                return fun(self, *args, **kwargs)
            except http.client.ImproperConnectionState:
                # reconnect and try again, once
                self.conn = self.connect()
                return fun(self, *args, **kwargs)
        return _conrun

    def connect(self):
        """Return a connection obj to the API host."""
        if self.endpoint[0] == 'https':
            return http.client.HTTPSConnection(host=self.endpoint[1], port=self.endpoint[2], timeout=self.timeout)
        return http.client.HTTPConnection(host=self.endpoint[1], port=self.endpoint[2], timeout=self.timeout)

    def close(self):
        self.conn.close()

    def get_headers(self, add_custom_headers={}):
        """Return the required headers to query API."""
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "Authorization": "Token %s" % self.apikey,
            }
        headers.update(add_custom_headers)
        return headers

    def validate_status(self, response, wanted_status, errtype=BuddyNSAPIError, custom_msg=None):
        """Verify that a response has the wanted_status code or raise an exception with a given message."""
        if response.status != wanted_status:
            raise errtype(custom_msg or ('API call failed: code %d, msg "%s".' % (response.status, response.read())))

    def element_path(self, *args):
        """Compose the path for an element (ends without /)."""
        return self.base_path + '/'.join(args)

    def resource_path(self, *args):
        """Compose the path for a resource (ends in /)."""
        return self.base_path + '/'.join(args) + '/'

    @reconn
    def add_domain(self, domain, master):
        """Issue API call to add one domain.
        
        @param domain       (string) domain to add
        @param master       (string) IPv4 or IPv6 address of DNS master
        
        @return     (dictionary) outcome from server"""
        postbody = 'master=%s&name=%s' % (master, domain)
        self.conn.request('POST', self.resource_path('zone'), body=postbody, headers=self.get_headers())
        resp = self.conn.getresponse()
        self.validate_status(resp, 201, errtype=PermissionDenied)
        return json.loads(resp.read())

    @reconn
    def remove_domain(self, domain):
        """Issue API call to remove a domain.
        
        @param domain   (string) name of domain to remove"""
        self.conn.request('DELETE', self.element_path('zone', domain), headers=self.get_headers())
        self.validate_status(self.conn.getresponse(), 204, errtype=DoesNotExist)
    
    @reconn
    def list_domains(self):
        """Return the list of domains currently registered.
        
        @return     (list of dictionaries) domain entries registered"""
        self.conn.request('GET', self.resource_path('zone'), headers=self.get_headers())
        resp = self.conn.getresponse()
        self.validate_status(resp, 200)
        return json.loads(resp.read())

    @reconn
    def get_domain(self, domain):
        """Return the properties of a currently registered domain.

        @param domain   (string) name of domain
        
        @return     (dictionary) properties of domain."""
        self.conn.request('GET', self.element_path('zone', domain), headers=self.get_headers())
        resp = self.conn.getresponse()
        self.validate_status(resp, 200, errtype=DoesNotExist)
        return json.loads(resp.read())

    @reconn
    def get_domain_status(self, domain):
        """Return the status properties of a currently registered domain.

        @param domain   (string) name of domain

        @return     (dictionary) status properties of domain."""
        self.conn.request('GET', self.resource_path('zone', domain, 'status'), headers=self.get_headers())
        resp = self.conn.getresponse()
        self.validate_status(resp, 200, errtype=DoesNotExist)
        return json.loads(resp.read())

    @reconn
    def get_domain_delegation(self, domain):
        """Return the delegation properties of a currently registered domain.

        @param domain   (string) name of domain

        @return     (dictionary) delegation properties of domain."""
        self.conn.request('GET', self.resource_path('zone', domain, 'delegation'), headers=self.get_headers())
        resp = self.conn.getresponse()
        self.validate_status(resp, 200, errtype=DoesNotExist)
        return json.loads(resp.read())

    @reconn
    def sync_domain(self, domain):
        """Request immediate synchronization for a domain.

        @param domain   (string) name of domain
        """
        self.conn.request('GET', self.element_path('sync', domain), headers=self.get_headers())
        resp = self.conn.getresponse()
        self.validate_status(resp, 204, errtype=DoesNotExist)
        return {}
