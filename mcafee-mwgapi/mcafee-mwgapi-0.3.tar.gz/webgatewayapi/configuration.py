from webgatewayapi.authenticate import authenticate
from webgatewayapi.parse import parseData


class configuration(object):

    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.validate = authenticate(hostname=self.hostname, port=self.port, https=self.https)

    def retrieveapplianceconfig(self, uuid):
        _url = self.validate.createAppendURL(string="appliances/{}/configuration".format(uuid))
        _response = self.auth.get(_url)
        return parseData(_response.text)

    def retrieveclusterconfig(self):
        _url = self.validate.createAppendURL(string="cluster/configuration")
        _response = self.auth.get(_url)
        return parseData(_response.text)
