import requests

from .errors import YuleakAPIError
from .logs import logger


class YuleakClient(object):
    """ Client for Yuleak API.

    Class must be used without instance of it.
    """
    BASE_URL = 'https://api.yuleak.com/'
    APIKEY = 'demo'

    @classmethod
    def set_apikey(cls, apikey):
        """Define the ApiKey to use (by defaut 'demo' is used).

        Args:
            apikey (str): ApiKey to use
        """
        cls.APIKEY = apikey

    @classmethod
    def credits(cls):
        """Get current user remaining credits

        See https://app.yuleak.com/apidoc#get-credits for endpoint details.

        Returns:
            available credits amount
        """
        data = cls.get_request('credits')
        if len(data) == 0:
            return 0
        return data[0].get('credits', 0)

    @classmethod
    def dashboards(cls):
        """Get the current user dashboards list

        See https://app.yuleak.com/apidoc#get-dashboards for endpoint details.

        Returns:
            list of Dashboard items
        """
        from .models.dashboard import Dashboard
        results = []
        for d in cls.get_request('dashboards'):
            results.append(Dashboard(d.get('id'), d.get('name')))
        return results

    @classmethod
    def search(cls, search):
        """Launch a new search (credits will be used). A new dashboard will be created.

        See https://app.yuleak.com/apidoc#post-search for endpoint details.

        Args:
            search (str): Expression to search

        Returns:
            (bool) True if the search has been launched
        """
        return cls.post_request('search', data={'value': search})

    @classmethod
    def get_request(cls, endpoint):
        """Make a GET request to the API.

        Args:
            endpoint (str): Name of the endpoint to query.

        Returns:
            a list of items
        """
        return cls._do_request('GET', endpoint)

    @classmethod
    def post_request(cls, endpoint, data=None):
        """Make a POST request to the API.

        Args:
            endpoint (str): Name of the endpoint to query.
            data (dict): Data to send

        Returns:
            (bool) True if the request performed well
        """
        return cls._do_request('POST', endpoint, data=data)

    @classmethod
    def delete_request(cls, endpoint, params=None):
        """Make a DELETE request to the API.

        Args:
            endpoint (str): Name of the endpoint to query.
            params (dict): GET data to send

        Returns:
            (bool) True if the request performed well
        """
        return cls._do_request('DELETE', endpoint, params=params)

    @classmethod
    def _do_request(cls, method, endpoint, retry=3, params=None, data=None):
        try:
            if params is None:
                params = {}
            if data is None:
                data = {}
            req = requests.request(method,
                                   cls.BASE_URL + endpoint,
                                   headers = {'X-Api-Key': cls.APIKEY},
                                   data = data,
                                   params = params,
                                   timeout=3)
            # Error handling
            if req.status_code not in (200,201):
                raise YuleakAPIError(req.json())
            # Warnings handling
            for warning in req.json().get('warnings', []):
                logger.warning('{0} [{1}]'.format(warning.get('message'), warning.get('code')))
            result = req.json().get('data', [])
            # Pagination
            pagination = req.json().get('pagination')
            if pagination is not None:
                if (pagination.get('total') / pagination.get('max')) > pagination.get('page'):
                    params['page'] = pagination.get('page') + 1
                    result += cls._do_request(method, endpoint, params=params, data=data)
            # Return
            if method == 'GET':
                return result
            else:
                return True
        except YuleakAPIError as e:
            logger.error(e)
            if method == 'GET':
                return []
            else:
                return True
        except requests.exceptions.RequestException as e:
            if retry > 0:
                return cls._do_request(method, endpoint, retry=retry-1, params=params, data=data)
            logger.error(e)
            if method == 'GET':
                return []
            else:
                return True
