import json
import requests
import base64


class Okta:
    def __init__(self, domain):
        self.domain = domain

    def get_client_credentialflow_token(self, client_id, client_secret, scope='api'):
        url = 'https://' + self.domain + "/oauth2/default/v1/token"
        authStr = client_id + ':' + client_secret
        encodedStr = base64.b64encode(bytes(authStr, "utf-8")).decode()

        payload = {
            'grant_type': 'client_credentials',
            'scope': scope,
        }
        headers = {
            'authorization': 'Basic ' + encodedStr,
        }
        response = requests.post(url, data=payload, headers=headers)
        return json.loads(response.text)
