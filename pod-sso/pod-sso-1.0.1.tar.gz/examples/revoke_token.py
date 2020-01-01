from pod_base import APIException, PodException

from examples.config import *
from sso import PodSSO, SSOException

try:
    TOKEN = "7edf039dae8b45ca99a6defbb38948ae"
    TOKEN_TYPE_HINT = PodSSO.TOKEN_HINT_ACCESS_TOKEN

    sso = PodSSO(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, API_TOKEN, server_type=SERVER_MODE)

    print("Revoke Token:\n", sso.revoke_token(token=TOKEN, token_type_hint=TOKEN_TYPE_HINT))
    # OUTPUT
    # Revoke Token:
    #  True

except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except SSOException as e:
    print("SSO Exception\nError {}\nError Description : {}\nStatus Code : {}".format(e.error, e.error_description,
          e.status_code))
except PodException as e:
    print("Pod Exception: ", e.message)
