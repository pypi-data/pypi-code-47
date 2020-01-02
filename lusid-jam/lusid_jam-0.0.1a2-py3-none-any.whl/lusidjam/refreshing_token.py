from collections import UserString
from datetime import datetime, timedelta
import os


class RefreshingToken(UserString):
    def __init__(self, access_token_location=os.getenv("FBN_ACCESS_TOKEN_FILE", None)):

        token_data = {"expires": datetime.now(), "current_access_token": ""}

        current_access_token = ""

        def get_token():

            # Check if the env variable exists in the os
            # Check if the environmental variable exists, but the file is not on the os

            if access_token_location == None or not(os.path.exists(access_token_location)):

                token_data["current_access_token"] = None

            elif token_data["expires"] <= datetime.now():
                with open(access_token_location, "r") as access_token_file:
                    token_data["current_access_token"] = access_token_file.read()

                token_data["expires"] = datetime.now() + timedelta(seconds=120)

            return token_data["current_access_token"]

        self.access_token = get_token

    def __getattribute__(self, name):
        token = object.__getattribute__(self, "access_token")()
        if name == "data":
            return token
        return token.__getattribute__(name)
