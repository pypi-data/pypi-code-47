from builtins import Exception

import requests
import json
import os


def call(access_token, endpoint, params):
    if access_token and endpoint is not None:
        try:
            headers = {
                'Authorization': access_token
            }

            url = requests.get(
                os.environ.get('CANVAS_BASE_URL') + endpoint,
                params=params,
                headers=headers
            )

            return json.dumps({
                "code": url.status_code,
                "url": url.url,
                "message": url.json()
            })
        except Exception as e:
            return json.dumps({
                "code": 500,
                "message": e,
                "url": None
            })
    else:
        if access_token is None:
            return json.dumps({
                "message": "Access Token not found",
                "code": 401,
                "url": None
            })
        elif endpoint is None:
            return json.dumps({
                "message": "Canvas Endpoint not specified",
                "code": 404,
                "url": None
            })
        else:
            return json.dumps({
                "message": "Unable to call Canvas API",
                "code": 500,
                "url": None
            })
