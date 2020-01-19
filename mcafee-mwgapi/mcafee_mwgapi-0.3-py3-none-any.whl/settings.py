from webgatewayapi.authenticate import authenticate
from webgatewayapi.parse import parseData


class configuration(object):

    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.validate = authenticate(hostname=self.hostname, port=self.port, https=self.https)

    def retrievsetting(self):
        """
        Retrieve settings from an appliance.
        """
        _url = self.validate.createAppendURL(string="setting")
        _response = self.auth.get(_url)
        return parseData(_response.text)

