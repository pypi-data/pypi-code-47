from datetime import datetime, timedelta
from os import environ
from default_http_client import DefaultHttpClient
import sys
import json


def get_env(var_name, default_value=None):
    return environ.get(var_name) if environ.get(var_name) else default_value


class RotoWireClient():
    def __init__(self, custom_http_client=None):
        self.base_url = get_env('ROTO_WIRE_BASE_URL',
                                'http://api.rotowire.com/')
        self.secret_key = None
        self.auth_header = 'Ocp-Apim-Subscription-Key'
        self.http_client = custom_http_client or DefaultHttpClient()

    # == Instance Methods
    def get_nba_injured_players(self):
        current_secret_key = self.secret_key
        self.secret_key = get_env('ROTO_WIRE_KEY')
        full_url = self.__build_func_url(
            '/Basketball/NBA/Injuries.php?key=%(key)s&format=json',
            key=self.secret_key
        )
        response = self.__do_api_call(full_url)
        self.secret_key = current_secret_key

        return response

    def get_injuries_news_by_date(self, date=None):
        now = date or datetime.now().date()
        current_secret_key = self.secret_key
        self.secret_key = get_env('ROTO_WIRE_KEY')
        full_url = self.__build_func_url(
            '/Basketball/NBA/News.php?key=%(key)s&format=json&date=%(date)s',
            key=self.secret_key, date=now.isoformat()
        )
        response = self.__do_api_call(full_url)
        response = response['Updates']
        output = [x for x in response if (x['Injury']['Type']) or 
                                         ((x['Analysis']).find('available') != -1) or 
                                         ((x['Notes']).find('available') != -1)]
        self.secret_key = current_secret_key

        return output

    def get_injuries_report(self, start_date=None, end_date=None):
        injuries_news = []
        sdate = start_date or datetime.now().date()
        edate = end_date or datetime.now().date()
        for d in self.__date_range(sdate, edate):
            injuries_news += self.get_injuries_news_by_date(d)

        return injuries_news

    # == Private Methods
    def __get_auth_headers(self, headers={}):
        altered_headers = headers.copy()
        altered_headers[self.auth_header] = self.secret_key

        return altered_headers

    def __build_func_url(self, func_url, **place_holders):
        try:
            return self.base_url + func_url % place_holders
        except Exception as e:
            sys.stderr.write(repr(e) + "\n")
            return self.base_url

    def __do_api_call(self, full_url, headers={}):
        auth_headers = self.__get_auth_headers(headers)
        response = self.http_client.get(full_url, auth_headers)

        return json.loads(response) if response else None

    def __date_range(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)+1):
            yield start_date + timedelta(n)
