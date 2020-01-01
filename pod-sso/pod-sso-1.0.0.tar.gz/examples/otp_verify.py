from pod_base import APIException, PodException

from examples.config import *
from sso import PodSSO, SSOException

try:
    sso = PodSSO(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, API_TOKEN, server_type=SERVER_MODE)
    # set private key
    sso.set_private_key(PRIVATE_KEY_PATH)

    verify_otp = sso.verify_otp(key_id=KEY_ID, otp=OTP_CODE, identity=IDENTITY_PHONE)

    print("Verify OTP :\n", verify_otp)
    # OUTPUT
    # Verify OTP  :
    #  {'code': 'ba0a8cb2b3d3493c8ebfe1616f80d810'}

    print(sso.get_access_token(verify_otp["code"], redirect_url=None))
    # OUTPUT
    # {
    #   'access_token': 'a05bffd7084c4e2897400822927ffcbd',
    #   'expires_in': 900,
    #   'id_token': 'eyJhbGciOiJSUzI1NiJ9.eyJzdW....0S_nQPc2-e1upTnYafbpT6u6rLL6GlBy',
    #   'refresh_token': '431c6f0f4a624440b68425c10aca0bff',
    #   'scope': 'profile',
    #   'token_type': 'bearer'
    # }
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except SSOException as e:
    print("SSO Exception\nError {}\nError Description : {}\nStatus Code : {}".format(e.error, e.error_description,
          e.status_code))
except PodException as e:
    print("Pod Exception: ", e.message)
