import requests
from bbdata.config import output_api_url
from bbdata.util import handle_response, handle_non_ok_status


class Me:

    base_path = "/me"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self):
        """
        Get my profile.

        GET /me
        https://bbdata.daplab.ch/api/#me_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def get_groups(self, admin=False):
        """
        Get the list of groups I am part of.

        GET /me/groups
        https://bbdata.daplab.ch/api/#me_groups_get
        """
        params = {
            "admin": admin
        }
        url = output_api_url + self.base_path + "/groups"
        r = requests.get(url, params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def get_apikeys(self):
        """
        Get the list of apikeys. Apikeys are used to access this api
        (see the bbtoken used in the security schemes). Apikeys can be
        read-only or read/write and can have an expiration date. Use
        read-only apikeys for applications using the api.

        GET /me/apikeys
        https://bbdata.daplab.ch/api/#me_apikeys_get
        """
        url = output_api_url + self.base_path + "/apikeys"
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def put_apikeys(self, writable, expire, description=None):
        """
        Generate a new apikey. An optional description can be specified
        in the body.

        PUT /me/apikeys
        https://bbdata.daplab.ch/api/#me_apikeys_put
        """
        params = {
            "writable": writable,
            "expire": expire
        }
        data = {
            "description": description
        }

        if len(description) <= 65:
            raise ValueError("The description is too big")

        durations = expire.split("-")
        for duration in durations:
            d = duration[:-1]
            u = duration[-1]

            if d < 0:
                raise ValueError(d + " duration is lower than 0")

            if u not in ["d", "h", "m", "s"]:
                raise ValueError(u + " is not a duration unit")

        url = output_api_url + self.base_path + "/apikeys"
        r = requests.put(url, data, params=params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def post_apikeys(self, api_key_id, read_only, secret, user_id):
        """
        Edit an apikey. All properties except the secret will be overriden.
        Use it with parcimony and beware of the expiration date (in UTC).

        POST /me/apikeys
        https://bbdata.daplab.ch/api/#me_apikeys_post
        """
        json = {
            "id": api_key_id,
            "readOnly": read_only,
            "secret": secret,
            "userId": user_id
        }
        url = output_api_url + self.base_path + "/apikeys"
        r = requests.post(url, json, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def delete_apikeys(self, api_key_id):
        """
        Revoke an apikey.

        DELETE /me/apikeys
        https://bbdata.daplab.ch/api/#me_apikeys_delete
        """
        params = {
            "apikeyId": api_key_id
        }
        url = output_api_url + self.base_path + "/apikeys"
        r = requests.delete(url, params, headers=self.auth.headers)
        return handle_non_ok_status(r.status_code)
