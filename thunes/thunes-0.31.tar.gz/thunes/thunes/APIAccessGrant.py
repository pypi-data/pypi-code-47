import base64
import email
import hashlib
import time

from django.conf import settings
import sys
import os


class APIAccessGrant:

    def __init__(self, urlparm):
        """
        the function for initializing all required params.
        """
        self.apikey = settings.API_KEY
        self.apisecret = settings.API_SECRET
        self.url = settings.API_BASE_URL + urlparm

        self.nonce = int(time.time())
        self.date = email.utils.formatdate(usegmt=True)
        self.nonce_bytes = bytes(str(self.nonce).encode('utf-8'))

    def parmReturn(self):
        """
        the function for calculating all secret information and return a map entity.
        """
        secret = bytes(self.apisecret.encode('utf-8'))
        message = bytes((self.apikey + str(self.nonce) + self.date).encode('utf-8'))
        import hmac
        hmac = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
        resultReturn = {'apikey': self.apikey, 'nonce': self.nonce_bytes,
                        'hmac': hmac, 'date': self.date, 'urlparm': self.url}
        return resultReturn
