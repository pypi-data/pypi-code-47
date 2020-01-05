import requests
import os
import json

class NoticeSlackLine():
    default_api_url = {
        "slack": "https://hooks.slack.com/services/",
        "line": 'https://notify-api.line.me/api/notify'
    }
    
    def __init__(self, app="slack", token=None):
        """
        Notice to Slack or LINE.

        Parameters:
            app : string (Default:"slack")
                "line" or "slack"
            token : string (Default:None)
                String of API Token 
                or
                The path where the token is located.

        Returns:
            None 
        """
        self.app = app
        
        if token is None:
            raise ValueError("token is not passed as an argument")
        elif os.path.isfile(token): # tokenがファイル形式のとき
            with open(token) as token_file: # JSON形式だと対応していないかも
                self.token = token_file.read()
        else:
            self.token = token
        
    def _send_line(self, message):
        """ 
        Notice to LINE.

        Parameters:
            message : string
                Notice message.

        Returns:
            None
        """
        payload = {"message": message}
        headers = {"Authorization": 'Bearer ' + self.token}
        requests.post(self.default_api_url["line"], data=payload, headers=headers)
        
    def _send_slack(self, message):
        """ 
        Notice to Slack.

        Parameters:
            message : string
                Notice message.

        Returns:
            None
        """
        if self.token.startswith(self.default_api_url["slack"]):
            URL = self.token
        else:
            URL = self.default_api_url["slack"] + self.token
        print(URL)
        payload = {
            "text": message,
#             "icon_emoji": ":heart" # アイコンを変更したいときに設定
        }
        
        data = json.dumps(payload)
        requests.post(URL, data)
    
    def notice(self, message="Processes completed."):
        """
        Notice to Slack or LINE.

        Parameters:
            message : string
                Notice message
        Returns:
            None
        """
        if self.app == "slack":
            self._send_slack(message)
        elif self.app == "line":
            self._send_line(message)