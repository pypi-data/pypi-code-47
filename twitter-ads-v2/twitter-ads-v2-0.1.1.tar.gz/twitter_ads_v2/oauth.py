import string
import random
import time

import oauthlib.oauth1.rfc5849.signature as oauth1
from oauthlib.oauth1.rfc5849.utils import escape
from urllib.parse import urlencode


class OAuth1(object):

    @classmethod
    def get_auth_header(self, client, method, base_uri, params, body=[]):
        uri_query = self._dict_to_string(params)
        headers = self._get_base_headers(client)
        c_params = self._collect_parameters(uri_query, body, headers)
        n_params = oauth1.normalize_parameters(c_params)
        base_string = oauth1.signature_base_string(
            method,
            base_uri,
            n_params
        )
        signature = oauth1.sign_hmac_sha1(
            base_string,
            client.consumer_secret,
            client.access_token_secret
        )
        headers['Authorization'] = (
            headers['Authorization'] + ', oauth_signature="' + escape(signature) + '"'
        )
        return headers['Authorization']

    def _collect_parameters(uri_query, body=[], headers=None):
        return oauth1.collect_parameters(
            uri_query=uri_query,
            body=body,
            headers=headers,
            exclude_oauth_signature=True,
            with_realm=False
        )

    def _dict_to_string(params):
        return urlencode(params)

    def _get_base_headers(client):
        nonce = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        timestamp = int(time.time())
        headers = {
            "Authorization": (
                'OAuth '
                'oauth_nonce="' + nonce + '", '
                'oauth_timestamp=' + str(timestamp) + ', '
                'oauth_token="' + client.access_token + '", '
                'oauth_consumer_key="' + client.consumer_key + '", '
                'oauth_signature_method="HMAC-SHA1", '
                'oauth_version="1.0"'
            )
        }
        return headers
