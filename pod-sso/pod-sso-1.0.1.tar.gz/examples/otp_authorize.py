from pod_base import APIException, PodException

from examples.config import *
from sso import PodSSO, SSOException

try:
    sso = PodSSO(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, API_TOKEN, server_type=SERVER_MODE)
    # set private key
    sso.set_private_key(PRIVATE_KEY_PATH)

    by_phone_number = sso.authorize(key_id=KEY_ID, identity=IDENTITY_PHONE)
    print("Authorize (OTP) by Phone Number :\n", by_phone_number)
    # OUTPUT
    # Authorize (OTP) by Phone Number :
    #  {'expires_in': 120, 'identity': '09370000041', 'type': 'PHONE', 'user_id': 11923337}

    by_email = sso.authorize(key_id=KEY_ID, identity="rz.zare@gmail.com", identity_type=PodSSO.IDENTITY_TYPE_EMAIL)
    print("Authorize (OTP) by Email :\n", by_email)
    # OUTPUT
    # Authorize (OTP) by Email :
    #  {'expires_in': 300, 'identity': 'rz***re@gmail.com', 'type': 'EMAIL', 'user_id': 11923337}

except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except SSOException as e:
    print("SSO Exception\nError {}\nError Description : {}\nStatus Code : {}".format(e.error, e.error_description,
          e.status_code))
except PodException as e:
    print("Pod Exception: ", e.message)
