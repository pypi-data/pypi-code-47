"""Flespi REST API Class"""
import requests

class FlespiClient:
  """Flespi client"""

  def __init__(self, token='', is_development=False):
    """Constructor"""
    self.is_development = is_development
    self.token = token
    self.url = 'https://flespi.io'
    self.headers = {
      'Accept': 'application/json',
      'Authorization': 'FlespiToken {}'.format(token)
    }

  def get(self, method):
    """GET method"""

    URL = self.url + method
    if self.is_development:
      self.print_request(URL)
    try:
      request = requests.get(URL, headers=self.headers)
      return self.validate_response(request)
    except requests.exceptions.RequestException as err:
      return {
        'error': True,
        'reason': err
      }

  def post(self, method, params):
    """POST method"""
    URL = self.url + method
    if self.is_development:
      self.print_request(URL)
      self.print_parameters(params)
    try:
      request = requests.post(URL, headers=self.headers, json=params)
      return self.validate_response(request)
    except requests.exceptions.RequestException as err:
      return {
        'error': True,
        'reason': err
      }

  def put(self, method, params):
    """PUT method"""

    URL = self.url + method
    if self.is_development:
      self.print_request(URL)
      self.print_parameters(params)
    try:
      request = requests.put(URL, headers=self.headers, json=params)
      return self.validate_response(request)
    except requests.exceptions.RequestException as err:
      return {
        'error': True,
        'reason': err
      }

  def delete(self, method):
    """DELETE method"""

    URL = self.url + method
    if self.is_development:
      self.print_request(URL)
    try:
      request = requests.delete(URL, headers=self.headers)
      return self.validate_response(request)
    except requests.exceptions.RequestException as err:
      return {
        'error': True,
        'reason': err
      }

  def print_request(self, url):
    """Print request method"""

    print("================ FLESPI REQUEST ================")
    print("Request: DELETE {}".format(url))
    print("================================================")

  def print_parameters(self, parameters):
    """Print parameters method"""

    print("================ FLESPI PARAMS ================")
    print("Parameters: {}".format(parameters))
    print("===============================================")

  def validate_response(self, request):
    """Validate response method"""

    return  {
      'error': request.status_code == 200,
      'code': request.status_code,
      'message': request.json()
    }
