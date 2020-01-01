from pod_base import APIException, PodException

from examples.config import *
from sso import PodSSO, SSOException

try:
    REFRESH_TOKEN = "3f1ab8c430900000000000ea8b7e91b6"

    sso = PodSSO(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, API_TOKEN, server_type=SERVER_MODE)

    print("Refresh Access Tokens:\n", sso.refresh_access_token(refresh_token=REFRESH_TOKEN))
    # OUTPUT
    # Refresh Access Tokens:
    #  {'access_token': '8503901217da40000000000565c90e3e',
    #  'expires_in': 900,
    #  'id_token': 'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMTkyMzMzNyIsImlzc........NvcmUucG9TsJ1E3ZHV_q-4',
    #  'refresh_token': '3f1ab8c430900000000000ea8b7e91b6',
    #  'scope': 'phone email profile',
    #  'token_type': 'bearer'
    #  }

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except SSOException as e:
    print("SSO Exception\nError {}\nError Description : {}\nStatus Code : {}".format(e.error, e.error_description,
          e.status_code))
except PodException as e:
    print("Pod Exception: ", e.message)
