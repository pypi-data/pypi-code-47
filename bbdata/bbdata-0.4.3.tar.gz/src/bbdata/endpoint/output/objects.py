import requests
from bbdata.config import output_api_url
from bbdata.util import handle_response


class Objects:

    base_path = "/objects"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get_all(self, tags=None, search=None, page=None, per_page=None,
                writable=False):
        """
        Get the list of accessible objects.

        GET /objects
        https://bbdata.daplab.ch/api/#objects_get
        """
        params = {
            "tags": tags,
            "search": search,
            "page": page,
            "perPage": per_page,
            "writable": writable,
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def put(self, name, unit_symbol, owner, description=None):
        """
        Create a new object.

        PUT /objects
        https://bbdata.daplab.ch/api/#objects_put
        """
        json = {
            "name": name,
            "description": description,
            "unitSymbol": unit_symbol,
            'owner': owner
        }
        url = output_api_url + self.base_path
        r = requests.put(url, json=json, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def get(self, object_id):
        """
        Get an object.

        GET /objects/{objectIs}
        https://bbdata.daplab.ch/api/#objects__objectid__get
        """
        url = output_api_url + self.base_path + "/" + str(object_id)
        r = requests.get(url, headers=self.auth.headers)
        # return ObjectResponse(r.json())
        return handle_response(r.status_code, r.json())

    def post(self, object_id, data):
        """
        Edit the name and/or the description of the object.
        Only the properties appearing in the body will be modified.

        POST /objects/{objectId}
        https://bbdata.daplab.ch/api/#objects__objectid__post
        """
        # TODO The data to send isn't define in the API Docs
        url = output_api_url + self.base_path + "/" + str(object_id)
        r = requests.post(url, data, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def delete(self, object_id):
        """
        Delete the object with the given id

        POST /objects/{objectId}
        https://bbdata.daplab.ch/api/#objects__objectid__delete
        """
        # TODO This method is in the Postman profile but isn't in the docs
        url = output_api_url + self.base_path + "/" + str(object_id)
        r = requests.delete(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def post_disable(self, object_id):
        """
        Disable this object. All associated tokens will be removed.

        POST /objects/{objectId}/disable
        https://bbdata.daplab.ch/api/#objects__objectid__disable_post
        """
        url = output_api_url + self.base_path + "/" + str(object_id) \
            + "/disable"
        r = requests.post(url, headers=self.auth.headers)
        return handle_response(r.status_code, True)

    def post_enable(self, object_id):
        """
        Enable this object.

        POST /objects/{objectId}/enable
        https://bbdata.daplab.ch/api/#objects__objectid__enable_post
        """
        url = output_api_url + self.base_path + "/" + str(object_id) \
            + "/enable"
        r = requests.post(url, headers=self.auth.headers)
        return handle_response(r.status_code, True)

    def get_tokens(self, object_id, description=None):
        """
        Get the list of tokens for the object. A token is used to submit new
        measures (see input-api).

        An optional description can be passed in the
        body (max 65 characters).

        GET /objects/{objectId}/tokens
        https://bbdata.daplab.ch/api/#objects__objectid__tokens_get
        """
        # TODO The API docs says it's possible to pass an optional description
        #   but it looks like it's a mistake for a GET request...
        url = output_api_url + self.base_path + "/" + str(object_id) \
            + "/tokens"
        json = {
            "description": description
        }
        r = requests.get(url, json, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def put_tokens(self, object_id):
        """
        Generate a new secured token.

        PUT /objects/{objectId}/tokens
        https://bbdata.daplab.ch/api/#objects__objectid__tokens_put
        """
        # TODO The optional description should probably be added in this
        #  method
        url = output_api_url + self.base_path + "/" + str(object_id) \
            + "/tokens"
        r = requests.put(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def post_tokens(self, object_id, description):
        """
        Edit the token's description.

        POST /objects/{objectId}/tokens
        https://bbdata.daplab.ch/api/#objects__objectid__tokens_post
        """
        url = output_api_url + self.base_path + "/" + str(object_id) \
            + "/tokens"
        json = {
            "description": description
        }
        r = requests.post(url, json=json, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def delete_tokens(self, object_id, token_id):
        """
        Revoke a token.

        DELETE /objects/{objectId}/tokens
        https://bbdata.daplab.ch/api/#objects__objectid__tokens_delete
        """
        url = output_api_url + self.base_path + "/" + str(object_id) \
            + "/tokens"
        params = {
            "tokenId": token_id
        }
        r = requests.delete(url, params=params, headers=self.auth.headers)
        return handle_response(r.status_code, True)

    def put_tags(self, object_id, tags):
        """
        Add tags to the object.

        PUT /objects/{objectId}/tags
        https://bbdata.daplab.ch/api/#objects__objectid__tags_put
        """
        url = output_api_url + self.base_path + "/" + str(object_id) \
            + "/tags"
        params = {
            "tags": tags
        }
        r = requests.put(url, params=params, headers=self.auth.headers)
        return handle_response(r.status_code, True)

    def delete_tags(self, object_id, tags):
        """
        Remove tags.

        DELETE /objects/{objectId}/tags
        https://bbdata.daplab.ch/api/#objects__objectid__tags_delete
        """
        url = output_api_url + self.base_path + "/" + str(object_id) \
            + "/tags"
        params = {
            "tags": tags
        }
        r = requests.put(url, params=params, headers=self.auth.headers)
        return handle_response(r.status_code, True)

    def get_comments(self, object_id):
        """
        Get all comments attached to this object. Use the /comments endpoint
        for more actions.

        GET /objects/{objectId}/comments
        https://bbdata.daplab.ch/api/#objects__objectid__comments_get
        """
        url = output_api_url + self.base_path + "/" + str(object_id) \
            + "/comments"
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())
