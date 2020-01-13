import requests

from .error import OctopyException


def get(url, params=None, headers=None):
    response = requests.get(url, params=params or {}, headers=headers or {})
    if not response.status_code in range(requests.codes.ok, 205):
        raise OctopyException(
            f"\n\t\t\tMessage: {response.json()['message']}\n\t\t\tCode: {response.status_code}\n"
        )

    status_code = response.status_code
    try:
        response = response.json()
        if type(response) == list:
            if len(response) and type(response[0]) == dict:
                for item in response:
                    item.update({"status_code": status_code})
            else:
                return response
        else:
            response.update({"status_code": status_code})
    except:
        response = {"status_code": status_code}

    return response


def post(url, params=None, headers=None):
    response = requests.post(url, json=params or {}, headers=headers or {})
    if not response.status_code in range(requests.codes.ok, 205):
        raise OctopyException(
            f"\n\t\t\tMessage: {response.json()['message']}\n\t\t\tCode: {response.status_code}\n"
        )

    status_code = response.status_code
    try:
        response = response.json()
        if type(response) == dict:
            response.update({"status_code": status_code})
    except:
        response = {"status_code": status_code}

    return response


def put(url, params=None, headers=None):
    response = requests.put(url, json=params or {}, headers=headers or {})
    if not response.status_code in range(requests.codes.ok, 205):
        raise OctopyException(
            f"\n\t\t\tMessage: {response.json()['message']}\n\t\t\tCode: {response.status_code}\n"
        )

    status_code = response.status_code
    try:
        response = response.json()
        if type(response) == dict:
            response.update({"status_code": status_code})
    except:
        response = {"status_code": status_code}

    return response


def patch(url, params=None, headers=None):
    response = requests.patch(url, json=params or {}, headers=headers or {})
    if not response.status_code in range(requests.codes.ok, 205):
        raise OctopyException(
            f"\n\t\t\tMessage: {response.json()['message']}\n\t\t\tCode: {response.status_code}\n"
        )

    status_code = response.status_code
    try:
        response = response.json()
        if type(response) == dict:
            response.update({"status_code": status_code})
    except:
        response = {"status_code": status_code}

    return response


def delete(url, params=None, headers=None):
    response = requests.delete(url, json=params or {}, headers=headers or {})
    if not response.status_code in range(requests.codes.ok, 205):
        raise OctopyException(
            f"\n\t\t\tMessage: {response.json()['message']}\n\t\t\tCode: {response.status_code}\n"
        )

    status_code = response.status_code
    try:
        response = response.json()
        if type(response) == dict:
            response.update({"status_code": status_code})
    except:
        response = {"status_code": status_code}

    return response
