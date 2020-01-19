from webgatewayapi.authenticate import authenticate



class actions(object):
    """
    actions class contains following functions calls.

    • restart — Restart an appliance
    • shutdown — Shut down an appliance
    • flushcache — Flush the cache
    • rotateLogs — Rotate log files
    • rotateAndPushLogs — Rotate and push log files
    • license — Import a license

    """

    def __init__(self, auth, hostname, port, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.validate = authenticate(hostname=self.hostname, port=self.port, https=self.https)

    def restart(self, uuid=None):
        """
        restart an appliance, restart parameter is used as the action name.
        restart function takes appliance UUID as parameter.
        :return: restart status
        """
        _url = self.validate.createAppendURL(string='appliances/{}/action/restart'.format(uuid))
        _response = self.auth.get(_url)
        return _response.text

    def shutdown(self, uuid=None):
        """
        shutdown an appliance, shutdown parameter is used as the action name.
        shutdown function takes appliance UUID as parameter.
        :return: restart status
        """
        _url = self.validate.createAppendURL(string='appliances/{}/action/shutdown'.format(uuid))
        _response = self.auth.get(_url)
        return _response.text

    def flushcache(self, uuid=None):
        """
        flushcache an appliance, flushcache parameter is used as the action name.
        flushcache function takes appliance UUID as parameter.
        :return: restart status
        """
        _url = self.validate.createAppendURL(string='appliances/{}/action/flushcache'.format(uuid))
        _response = self.auth.get(_url)
        return _response.text

    def rotatelogs(self, uuid=None):
        """
        rotatelogs an appliance, rotatelogs parameter is used as the action name.
        rotatelogs function takes appliance UUID as parameter.
        :return: restart status
        """
        _url = self.validate.createAppendURL(string='appliances/{}/action/rotatelogs'.format(uuid))
        _response = self.auth.get(_url)
        return _response.text

    def rotateflushlogs(self, uuid=None):
        """
        rotateflushlogs an appliance, rotateflushlogs parameter is used as the action name.
        rotateflushlogs function takes appliance UUID as parameter.
        :return: restart status
        """
        _url = self.validate.createAppendURL(string='appliances/{}/action/rotateAndPushLogs'.format(uuid))
        _response = self.auth.get(_url)
        return _response.text

    def license(self, uuid=None):
        """
        license an appliance, license parameter is used as the action name.
        license function takes appliance UUID as parameter.
        :return: restart status
        """
        _url = self.validate.createAppendURL(string='appliances/{}/action/license'.format(uuid))
        _response = self.auth.get(_url)
        return _response.text



