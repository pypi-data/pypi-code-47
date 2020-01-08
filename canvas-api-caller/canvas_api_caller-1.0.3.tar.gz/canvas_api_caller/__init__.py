from builtins import Exception

import requests
import json
import os

from flask import Flask, jsonify, json
from werkzeug.datastructures import MultiDict


def call(access_token, endpoint, params):
    if os.environ.get('CANVAS_BASE_URL') is None:
        return format_json_to_string("CANVAS_BASE_URL not set in environmental variable", 500)

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
            return format_json_to_string("Access Token Not Found", 401)
        elif endpoint is None:
            return format_json_to_string("Canvas Endpoint not specified", 404)
        else:
            return format_json_to_string("Unable to call Canvas API", 500)


def http(request, headers=None):
    if headers is not None:
        if request.method == 'OPTIONS':
            return ('', 204, headers)

    access_token = request.headers.get('X-Canvas-Authorization')
    query_params = request.args
    endpoint = query_params.get('endpoint')
    array_params = MultiDict()

    for k in query_params.keys():
        if k != 'endpoint':
            array_params.add(k, query_params.get(k))

    json_response = call(access_token, endpoint, array_params)
    decoded_response = json.loads(json_response)

    if headers is not None:
        return jsonify({
            "message": decoded_response['message']
        }), decoded_response['code'], headers
    else:
        return jsonify({
            "message": decoded_response['message']
        }), decoded_response['code']


def translate_access_token(access_token):
    prefix = 'Bearer'

    if access_token.startswith(prefix) is False:
        return '%s %s' % (prefix, access_token)
    else:
        return access_token


def format_json_to_string(message, status_code, url=None):
    return json.dumps({
        "code": status_code,
        "url": url,
        "message": message
    })
