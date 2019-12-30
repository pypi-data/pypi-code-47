#!/usr/bin/env python3
import json
import requests

AUTH_HEADER = 'auth-token'
BASE_URL = 'https://www.drugshortagescanada.ca/api/v1'
LOGIN_URL = BASE_URL + "/login"
SEARCH_URL = BASE_URL + "/search"
SHORTAGE_URL = BASE_URL + "/shortages"
DISCONTINUATION_URL = BASE_URL + "/discontinuances"

PAGE_LIMIT = 1000   # number of records to request in each page of results. Usually only get 50

class NotLoggedInException(Exception):
    pass

class Session:
    def __init__(self, email, password): 
        self.email = email
        self.password = password
        self.user_data = None
        self.auth_token = None

    def login(self):
        self.response = requests.post(LOGIN_URL, data = {'email': self.email, 'password': self.password})
        self.response.raise_for_status()
        self.user_data = self.response.json()
        self.auth_token = self.response.headers[AUTH_HEADER]

    def _get_request(self, url, params = None):
        """Makes a get request and returns JSON results
           
            Response is stored in self.response

            Raises a NotLoggedInException if .login() has not been called
            Passes on requests exceptions if raised
        """

        if self.auth_token is None: 
            raise NotLoggedInException()

        headers = { AUTH_HEADER : self.auth_token }
        self.response = requests.get(url, headers = headers, params = params)
        self.response.raise_for_status()
        return self.response.json()

    def search(self, **kwargs):
        """
        Parameters:
            orderby = specify the column to sort the results by
                id = report ID
                company_name = the company associated with the report
                brand_name = the drug associated with the report
                status = the current status of the report
                type = the type of report (shortage or discontinuation)
                updated_date = the date of the last change to the report
            order = asc for ascending; desc for descending
            filter_status = only return reports of the given status
            term = main text search value
            din
            report_id

        A list response, like the search query, will return paginated data in the following object:

            total = total objects matched by the request
            limit = the maximum number of objects returned in the single request
            offset = the starting index of the response (defaults to 0)
            page = the current page according to the limit and offset values
            remaining = the number of objects available after the current page (used for infinite list loading)
            data = an array of the requested data
            total_pages = the total number of pages available the request
        """
        return self._get_request(SEARCH_URL, params = kwargs)

    def isearch(self, _filter=None, **kwargs):
        """Stream results as JSON objects

            _filter is a boolean function accepting a JSON object representing a
              row, and if true that row will be yielded.  
            kwargs are passed directly as part of the search request
        """
        kwargs['limit'] = PAGE_LIMIT
        kwargs['offset'] = 0

        results = self.search(**kwargs)
        limit = results['limit']

        for offset in range(limit, results['total']+limit, limit):
            for item in filter(_filter, results['data']):
                yield item
            kwargs['offset'] = offset
            results = self.search(**kwargs)

    def shortage_report(self, report_id): 
        return self._get_request(SHORTAGE_URL + "/" + report_id)

    def discontinuation_report(self, report_id): 
        return self._get_request(DISCONTINUATION_URL + "/" + report_id)


# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4
