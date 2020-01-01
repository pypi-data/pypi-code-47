from pod_base import APIException, PodException

from examples.config import *
from sso import PodSSO

try:
    sso = PodSSO(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, API_TOKEN, server_type=SERVER_MODE)

    print("SSO Link(default):", sso.get_login_url())
    # OUTPUT
    # SSO Link(default): https://accounts.pod.ir/oauth2/authorize/?client_id=CLIENT_ID&redirect_uri=http%3A%2F%2Flocalhost&response_type=code

    print("SSO Link with Custom Scope:", sso.get_login_url(scope=["profile", "phone"]))
    # OUTPUT
    # SSO Link with Custom Scope: https://accounts.pod.ir/oauth2/authorize/?client_id=CLIENT_ID&redirect_uri=http%3A%2F%2Flocalhost&response_type=code&scope=profile+phone

    print("SSO Link with state:", sso.get_login_url(state="sses_id=123456"))
    # OUTPUT
    # SSO Link with state: https://accounts.pod.ir/oauth2/authorize/?client_id=CLIENT_ID&redirect_uri=http%3A%2F%2Flocalhost&response_type=code&state=sses_id%3D123456

    print("SSO Link with custom Redirect URL:", sso.get_login_url(redirect_uri="http://google.com"))
    # OUTPUT
    # SSO Link with custom Redirect URL: https://accounts.pod.ir/oauth2/authorize/?client_id=CLIENT_ID&redirect_uri=http%3A%2F%2Fgoogle.com&response_type=code

    print("SSO Link (Signup Page):", sso.get_login_url(prompt="signup"))
    # OUTPUT
    # SSO Link (Signup Page): https://accounts.pod.ir/oauth2/authorize/?client_id=CLIENT_ID&redirect_uri=http%3A%2F%2Flocalhost&response_type=code&prompt=signup

except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
