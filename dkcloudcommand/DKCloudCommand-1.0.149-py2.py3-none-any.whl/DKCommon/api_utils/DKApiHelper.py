import json
import pickle
import requests
import six

from .api_utils import validate_and_get_response
from .DKReturnCode import DKReturnCode, SUCCESS, FAIL
from ..DKFileEncode import DKFileEncode
from ..DKPathUtils import (
    normalize_list,
    normalize_recipe_dict,
    UNIX,
    WIN,
)

MESSAGE = 'message'
DESCRIPTION = 'description'
KITCHEN_JSON = 'kitchen.json'


class DKApiHelper(object):

    def __init__(self, url, username=None, password=None, token=None):
        self._url = url
        self._username = username
        self._password = password
        self._jwt = token

        if not self.login_if_invalid_token():
            raise Exception('Failed API login attempt')

    @property
    def url(self):
        return self._url

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def headers(self):
        return {'Authorization': 'Bearer {}'.format(self._jwt)}

    def login_if_invalid_token(self):
        if self._is_token_valid():
            return True
        self._login()
        return self._jwt is not None

    def _login(self):
        url = '%s/v2/login' % (self._url)
        try:
            response = requests.post(
                url, data={
                    'username': self.username,
                    'password': self.password
                }
            )
        except (requests.RequestException, ValueError, TypeError) as c:
            print("login: exception: %s" % str(c))
            return

        try:
            validate_and_get_response(response)
        except Exception as e:
            print("login: exception: %s" % str(e))
            return

        if response is not None:
            if response.text is not None and len(response.text) > 10:
                if response.text[0] == '"':
                    self._jwt = response.text.replace('"', '').strip()
                else:
                    self._jwt = response.text
            else:
                print('Invalid jwt token returned from server')
        else:
            print('login: error logging in')

    def _is_token_valid(self):
        if self._jwt is None:
            return False

        url = '%s/v2/validatetoken' % (self._url)
        try:
            response = requests.get(url, headers=self.headers)
            validate_and_get_response(response)
            return True
        except Exception:
            self._jwt = None
            return False

    def create_order(self, kitchen, recipe_name, variation_name, node_name=None, parameters=None):
        """
        Full graph
        '/v2/order/create/<string:kitchenname>/<string:recipename>/<string:variationname>',
            methods=['PUT']

        Single node
        '/v2/order/create/graph/<string:kitchenname>/<string:recipename>/<string:variationname>',
            methods=['PUT']

        """
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            return DKReturnCode(FAIL, 'issue with kitchen')
        if recipe_name is None or isinstance(recipe_name, six.string_types) is False:
            return DKReturnCode(FAIL, 'issue with recipe_name')
        if variation_name is None or isinstance(variation_name, six.string_types) is False:
            return DKReturnCode(FAIL, 'issue with variation_name')

        payload = {'parameters': parameters or {}}

        if node_name is None:
            url = '%s/v2/order/create/%s/%s/%s' % (self._url, kitchen, recipe_name, variation_name)
        else:
            url = '%s/v2/order/create/graph/%s/%s/%s' % (
                self._url, kitchen, recipe_name, variation_name
            )
            payload['graph-setting'] = [[node_name]]

        data = json.dumps(payload)

        try:
            response = requests.put(url, data=data, headers=self.headers)
        except (requests.RequestException, ValueError) as c:
            return DKReturnCode(FAIL, "create_order: exception: %s" % str(c))
        return DKReturnCode(SUCCESS, None, payload=validate_and_get_response(response))

    def list_kitchen(self):
        url = '%s/v2/kitchen/list' % (self._url)
        try:
            response = requests.get(url, headers=self.headers)
        except (requests.RequestException, ValueError, TypeError) as c:
            return DKReturnCode(FAIL, 'list_kitchen: exception: %s' % str(c))

        rdict = validate_and_get_response(response)
        return DKReturnCode(SUCCESS, None, payload=rdict['kitchens'])

    def get_kitchen_dict(self, kitchen_name):
        rv = self.list_kitchen()

        kitchens = rv.payload if rv.ok() else None

        if kitchens is None:
            return None

        for kitchen in kitchens:
            if isinstance(kitchen,
                          dict) is True and 'name' in kitchen and kitchen_name == kitchen['name']:
                return kitchen
        return None

    def orderrun_detail(self, kitchen, pdict):
        """
        Get the details about a Order-Run (fka Serving)

        :param kitchen: kitchen name
        :param pdict: parameter dictionary
        :return: DKReturnCode
        """
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            return DKReturnCode(FAIL, 'issue with kitchen')

        url = '%s/v2/order/details/%s' % (self._url, kitchen)
        try:
            response = requests.post(url, data=json.dumps(pdict), headers=self.headers)
        except (requests.RequestException, ValueError) as c:
            s = "orderrun_detail: exception: %s" % str(c)
            return DKReturnCode(FAIL, s)

        rdict = validate_and_get_response(response)
        if False:
            pickle.dump(rdict, open("files/orderrun_detail.p", "wb"))

        return DKReturnCode(SUCCESS, None, payload=rdict)

    def create_kitchen(self, existing_kitchen_name, new_kitchen_name, description, message=None):
        if existing_kitchen_name is None or new_kitchen_name is None:
            return DKReturnCode(FAIL, 'Need to supply an existing kitchen name')

        if isinstance(existing_kitchen_name, six.string_types) is False or isinstance(
                new_kitchen_name, six.string_types) is False:
            return DKReturnCode(FAIL, 'Kitchen name needs to be a string')

        if message is None or isinstance(message, six.string_types) is False:
            message = 'update_kitchens'

        data = json.dumps({MESSAGE: message, DESCRIPTION: description})
        url = '%s/v2/kitchen/create/%s/%s' % (self._url, existing_kitchen_name, new_kitchen_name)
        try:
            response = requests.put(url, data=data, headers=self.headers)
        except (requests.RequestException, ValueError, TypeError) as c:
            return DKReturnCode(FAIL, 'create_kitchens: exception: %s' % str(c))

        return DKReturnCode(SUCCESS, None, payload=validate_and_get_response(response))

    def update_kitchen(self, update_kitchen, message):
        if update_kitchen is None:
            return False
        if isinstance(update_kitchen, dict) is False or 'name' not in update_kitchen:
            return False
        if message is None or isinstance(message, six.string_types) is False:
            message = 'update_kitchens'
        data = json.dumps({
            KITCHEN_JSON: update_kitchen,
            MESSAGE: message,
        })
        url = '%s/v2/kitchen/update/%s' % (self._url, update_kitchen['name'])
        try:
            response = requests.post(url, data=data, headers=self.headers)
        except (requests.RequestException, ValueError, TypeError) as c:
            print("update_kitchens: exception: %s" % str(c))
            return None
        validate_and_get_response(response)
        return True

    def order_delete_all(self, kitchen):
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            return DKReturnCode(FAIL, 'issue with kitchen')
        url = '%s/v2/order/deleteall/%s' % (self._url, kitchen)
        try:
            response = requests.delete(url, headers=self.headers)
        except (requests.RequestException, ValueError) as c:
            return DKReturnCode(FAIL, "order_delete_all: exception: %s" % str(c))

        validate_and_get_response(response)
        return DKReturnCode(SUCCESS, None)

    def delete_kitchen(self, existing_kitchen_name, message=None):
        if existing_kitchen_name is None:
            return DKReturnCode(FAIL, 'Need to supply an existing kitchen name')

        if isinstance(existing_kitchen_name, six.string_types) is False:
            return DKReturnCode(FAIL, 'Kitchen name needs to be a string')

        if message is None or isinstance(message, six.string_types) is False:
            message = 'delete_kitchen'

        data = json.dumps({MESSAGE: message})
        url = '%s/v2/kitchen/delete/%s' % (self._url, existing_kitchen_name)
        try:
            response = requests.delete(url, data=data, headers=self.headers)
        except (requests.RequestException, ValueError, TypeError) as c:
            return DKReturnCode(FAIL, 'delete_kitchens: exception: %s' % str(c))

        validate_and_get_response(response)
        return DKReturnCode(SUCCESS, None)

    def get_recipe(self, kitchen, recipe, list_of_files=None):
        if kitchen is None or isinstance(kitchen, six.string_types) is False:
            return DKReturnCode(FAIL, 'issue with kitchen parameter')

        if recipe is None or isinstance(recipe, six.string_types) is False:
            return DKReturnCode(FAIL, 'issue with recipe parameter')

        url = '%s/v2/recipe/get/%s/%s' % (self._url, kitchen, recipe)
        try:
            if list_of_files is not None:
                params = dict()
                params['recipe-files'] = normalize_list(list_of_files, UNIX)
                response = requests.post(url, data=json.dumps(params), headers=self.headers)
            else:
                response = requests.post(url, headers=self.headers)
        except (requests.RequestException, ValueError, TypeError) as c:
            return DKReturnCode(FAIL, "get_recipe: exception: %s" % str(c))

        rdict = validate_and_get_response(response)
        if recipe not in rdict['recipes']:
            message = "Unable to find recipe %s or the stated files within the recipe." % recipe
            return DKReturnCode(FAIL, message)
        else:
            rdict = DKFileEncode.binary_files(DKFileEncode.B64DECODE, rdict)
            return DKReturnCode(SUCCESS, None, payload=normalize_recipe_dict(rdict, WIN))
