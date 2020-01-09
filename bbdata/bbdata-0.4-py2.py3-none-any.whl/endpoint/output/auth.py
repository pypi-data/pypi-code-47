import json
import requests
from pathlib import Path

from bbdata.config import output_api_url
from bbdata.util import handle_non_ok_status


class Auth:

    credentials = None
    username = None
    password = None
    user_id = None
    secret = None
    headers = None

    def __init__(self):
        home = Path.home()
        credentials = Path(".bbdata/credentials.json")
        credentials_path = home / credentials
        if credentials_path.is_file():
            with open(str(credentials_path)) as json_file:
                data = json.load(json_file)
            self.credentials = data
            self.username = data['username']
            self.password = data['password']
            print("Welcome " + self.username)
        else:
            print("You don't have any credentials file. Create it at ~" + str(credentials))
            print("The content should be :")
            print("""\t{ "username": "<USERNAME>", "password": "<PASSWORD>" }""")

    def login(self):
        url = output_api_url + "/login"
        r = requests.post(url, json=self.credentials)
        if r.status_code == 200:
            self.user_id = r.json()["userId"]
            self.secret = r.json()["secret"]
            self.headers = {
                'bbuser': str(self.user_id),
                'bbtoken': str(self.secret)
            }
            return r.json()
        else:
            handle_non_ok_status(r.status_code)

    def logout(self):
        url = output_api_url + "/logout"
        r = requests.post(url, headers=self.headers)
        if r.status_code == 200:
            self.user_id = None
            self.secret = None
            self.headers = None
            return r.text
        else:
            handle_non_ok_status(r.status_code)

