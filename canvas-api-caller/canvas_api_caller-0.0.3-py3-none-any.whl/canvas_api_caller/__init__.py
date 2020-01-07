from builtins import Exception

import requests
import json
import os


def call(access_token, endpoint, params):
    if access_token and endpoint is not None:
        try:
            headers = {
                'Authorization': translate_access_token(access_token)
            }

            url = requests.get(
                os.environ.get('CANVAS_BASE_URL') + endpoint,
                params=params,
                headers=headers
            )

            return format_json_to_string(url.json(), url.status_code, url.url)
        except Exception as e:
            return format_json_to_string(e, 500, None)
    else:
        if access_token is None:
            return format_json_to_string("Access Token Not Found", 401, None)
        elif endpoint is None:
            return format_json_to_string("Canvas Endpoint not specified", 404, None)
        else:
            return format_json_to_string("Unable to call Canvas API", 500, None)

def translate_access_token(access_token):
    prefix = 'Bearer'

    if access_token.startswith(prefix) is False:
        return '%s %s'% (prefix, access_token)
    else:
        return access_token

def format_json_to_string(message, status_code, url):
    return json.dumps({
        "code": status_code,
        "url": url,
        "message": message
    })
