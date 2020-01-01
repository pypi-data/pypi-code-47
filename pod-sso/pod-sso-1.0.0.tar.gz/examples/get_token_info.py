from pod_base import APIException, PodException

from examples.config import *
from sso import PodSSO, SSOException

try:
    TOKEN = "de57fd694600000000000588940ab958"
    TOKEN_TYPE_HINT = PodSSO.TOKEN_HINT_ACCESS_TOKEN

    sso = PodSSO(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, API_TOKEN, server_type=SERVER_MODE)

    print("Token Info:\n", sso.get_token_info(token=TOKEN, token_type_hint=TOKEN_TYPE_HINT))
    # OUTPUT
    # Token Info:
    #  {'active': True,
    #  'client_id': '11963175zc96000000b3b6af506fa358f',
    #  'device_uid': '68ca9029b6602000000d244d82a5c121',
    #  'exp': 1577619274,
    #  'scope': 'phone email profile',
    #  'sub': '11923337'
    #  }

    print("Invalid Token Info or Expired Token:\n", sso.get_token_info(token="546564654654",
                                                                       token_type_hint=TOKEN_TYPE_HINT))
    # OUTPUT
    # Invalid Token Info or Expired Token:
    #  {'active': False}
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except SSOException as e:
    print("SSO Exception\nError {}\nError Description : {}\nStatus Code : {}".format(e.error, e.error_description,
          e.status_code))
except PodException as e:
    print("Pod Exception: ", e.message)
