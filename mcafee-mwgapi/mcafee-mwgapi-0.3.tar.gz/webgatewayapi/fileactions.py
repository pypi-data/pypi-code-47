from webgatewayapi.authenticate import authenticate


class fileactions(object):
    """
    files class contains following functions calls.

    . Downloading system files
    . Mofifying system files
    . Downloading log file
    . Deleting log file
    . Downloading an uploaded file
    . Adding file to uploaded files
    . Modifying uploaded file
    . Deleting an Uploaded File


    """

    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.validate = authenticate(hostname=self.hostname, port=self.port, https=self.https)


    def systemfilefeed(self, uuid):
        """
        This function requests a system file feed that exist on current appliance.
        This function takes appliance UUID as parameter
        :return: systemfilefeed status
        """
        _url = self.validate.createAppendURL(string='appliances/{}/system'.format(uuid))
        _response = self.auth.get(_url)
        return _response.text


    def downloadsystemfile(self,uuid):
        """
        This function downloads a system file that from current appliance
        :return: downloadsystemfile status
        """

        _url = self.validate.createAppendURL(string='appliances/{}/system/etc/hosts'.format(uuid))
        _response = self.auth.get(_url)
        return _response.text

    def modifysystemfile(self,uuid):
        """
        This function modifies sytem files from current appliance.
        :return: modifysystemfile status
        """

        _url = self.validate.createAppendURL(string='appliances/{}/system/etc/hosts'.format(uuid))
        _response = self.auth.put(_url, headers={'Content-Type': '*/*'})
        return _response.text

    def logfile(self,uuid):
        """
        This function pulls the appliance feed of log files.
        :returns:  logfile status
        """

        _url = self.validate.createAppendURL(string='appliances/{}/log'.format(uuid))
        _response = self.auth.get(_url)
        return _response.text

    def downloadlogfile(self, filename, uuid):
        """
        This function downloads individual log file from the appliance.
        This function takes UUID and log filename as parameter
        :return: download status and file.
        """

        _url = self.validate.createAppendURL(string='appliance/{}/log/debug/{}'.format(uuid, filename))
        _response = self.auth.get(_url, headers={'Accept': 'application/x-download'})
        return _response.text


