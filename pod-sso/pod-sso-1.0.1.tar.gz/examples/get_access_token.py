from pod_base import APIException, PodException

from examples.config import *
from sso import PodSSO, SSOException

try:
    CODE = "ba0a8cb2b3d3493c8ebfe1616f80d810"

    sso = PodSSO(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, API_TOKEN, server_type=SERVER_MODE)

    print("Access Tokens:\n", sso.get_access_token(code=CODE, redirect_url=REDIRECT_URL))
    # OUTPUT
    # Access Tokens:
    #  {'access_token': '56700418b52840000000000e2ec142c1',
    #  'expires_in': 900,
    #  'id_token': 'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMTky...lIjoi2LHYttinIiwiaWF0IjoxNTc0NzcxODg4LCGENvZGU9Mm',
    #  'refresh_token': '3f1ab8c430900000000000ea8b7e91b6',
    #  'scope': 'phone email profile',
    #  'token_type': 'bearer'
    #  }

except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except SSOException as e:
    print("SSO Exception\nError {}\nError Description : {}\nStatus Code : {}".format(e.error, e.error_description,
          e.status_code))
except PodException as e:
    print("Pod Exception: ", e.message)
