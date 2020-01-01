# coding=utf-8
import uuid
from pod_base import APIException, PodException

from examples.config import *
from sso import PodSSO, SSOException

try:
    device_uid = str(uuid.uuid4())
    sso = PodSSO(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, API_TOKEN, server_type=SERVER_MODE)

    print("Handshake :\n", sso.handshake(device_uid=device_uid))
    # OUTPUT
    # Handshake :
    #  {'algorithm': 'rsa-sha256',
    #       'client': {
    #           'allowedGrantTypes': ['authorization_code', 'refresh_token'],
    #           'allowedRedirectUris': ['http://localhost/test.php'],
    #           'allowedScopes': [
    #               'social_write', 'login', 'profile_write', 'phone', 'social', 'address', 'email', 'profile'
    #           ],
    #           'allowedUserIPs': ['*'],
    #           'captchaEnabled': False,
    #           'client_id': 'CLIENT_ID',
    #           'icon': 'https://core.pod.ir:443/nzh/image/2',
    #           'id': 8292,
    #           'loginUrl': 'https://accounts.pod.land/oauth2/authorize/?client_id=CLIENT_ID&....',
    #           'name': 'شرکت رضا',
    #           'signupEnabled': True,
    #           'url': 'http://localhost/ABCD.php',
    #           'userId': 11963175
    #       },
    #       'device': {
    #           'current': False,
    #           'id': 3066995,
    #           'ip': 'XXX.XXX.XXX.XXX',
    #           'language': 'en',
    #           'lastAccessTime': 1577622730000,
    #           'location': {},
    #           'uid': '57ba0a7c-0000-0000-0000-0000a6033292'
    #       },
    #       'expires_in': 31536000,
    #       'keyFormat': 'pem',
    #       'keyId': '513863377b3c5131577622730',
    #       'publicKey': '-----BEGIN PUBLIC KEY-----\nMIGfMA0G....JnplS735kA2ctQ0UQIDAQAB\n-----END PUBLIC KEY-----'
    #  }

except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except SSOException as e:
    print("SSO Exception\nError {}\nError Description : {}\nStatus Code : {}".format(e.error, e.error_description,
          e.status_code))
except PodException as e:
    print("Pod Exception: ", e.message)
