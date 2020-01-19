
from webgatewayapi.authenticate import authenticate



class activities(object):
    """
    activities class contains following function calls.

    • versions - check version of MWG-REST/MWG-OS/MWG-UI
    • back-up - perform backup
    • commit - commit Changes
    • hearbeat - keep a session alive
    • discard - discard changes
    • restore - restore configuration

    """
    def __init__(self, auth, hostname, port, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.validate = authenticate(hostname=self.hostname, port=self.port, https=self.https)

    def backup(self):
        """
        generates configuration backup for the appliance your are currently working on,
        the backup parameter from the McAfee documentation is used in this function.
        :return: backup data/status.
        """
        _response = self.auth.get(self.validate.createAppendURL(string='backup'))
        return _response.text


    def commit(self):
        """
        commit is used to "Save Changes" or "Commit" to the appliances which can save changes that is
        modified or created.
        :return: commit status
        """
        _url = self.validate.createAppendURL(string='commit')
        _response = self.auth.post(_url)
        return _response

    def heartbeat(self):
        """
        heartbeat parameter keeps the session alive that you are currently working in
        :return: heartbeat status
        """
        _url = self.validate.createAppendURL(string='heartbeat')
        _response = self.auth.post(_url, verify=False)
        return _response.text

    def discard(self):
        """
        to discard changed that have been made to the item such as system files, log files, lists and other on
        current appliance, the discard parameter is used.
        :return: discard status
        """
        _url = self.validate.createAppendURL(string='discard')
        _response = self.auth.post(_url, verify=False)
        return _response.text

    def version(self, mwgrest=None, mwgui=None):
        """
        Request information on the version of the REST interface or standard user interface of the appliance you are
        currently working on, version parameter can be used.
        :return: version status
        """
        string = 'version'
        if mwgrest is not None:
            string = '{}/{}'.format(string, mwgrest)
        if mwgui is not None:
            string = '{}/{}'.format(string, mwgui)

        _url = self.validate.createAppendURL(string=string)
        _response = self.auth.get(_url)
        return _response.text

    def restore(self):
        """
        To restore configuration of the appliance you are currently working on, the restore parameter is used.
        :return: restore status
        """
        _url = self.validate.createAppendURL(string='restore')
        _response = self.auth.post(_url, verify=False, headers={'Content-Type': 'application/xml'})
        return _response.text





