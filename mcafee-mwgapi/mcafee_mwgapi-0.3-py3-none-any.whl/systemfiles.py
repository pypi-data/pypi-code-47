from webgatewayapi.authenticate import authenticate
from webgatewayapi.parse import parseData


class configuration(object):

    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.validate = authenticate(hostname=self.hostname, port=self.port, https=self.https)

    def retrievsystemfile(self, uuid):
        """
        method will get the system file from a specific appliance as needed.
        :return status of operation
        """
        _url = self.validate.createAppendURL(string="appliances/{}/system".format(uuid))
        _response = self.auth.get(_url)
        return parseData(_response.text)

    def downloadsystemfile(self, uuid, name):
        """
            Download system file will get the data of the file.
            :return status of operation.
        """
        _url = self.validate.createAppendURL(string="appliances/{}/system/{}".format(uuid, name))
        _response = self.auth.get(_url)
        return parseData(_response.text)


    def modifysystemfile(self, uuid, name, data):
        """
        Modify system file will push an api with the modified system file.
        :return status of operation.
        """
        _url = self.validate.createAppendURL(string="appliances/{}/system/{}".format(uuid, name))
        _response = self.auth.put(_url, params=data)
        return parseData(_response.text)


    def fileDelete(self, filename, uuid):
        """
            fileDelete will delete specific file from the appliance, if it exists.
        :param filename: Name of existing file to delete.
        :return: status of operation.
        """
        _url = self.validate.createAppendURL(string='appliances/{}/files/{}'.format(uuid, filename))
        _response = self.auth.delete(_url)
        return parseData(_response.text)


    def fileUpload(self, name, filedata,uuid ):
        """
            fileUpload will upload all a file with filename and filedata provided.
        :param filename: name of the file.
        :param filedata: new file data
        :return: status of the operation
        """
        _url = self.validate.createAppendURL(string='appliances/{}/files/{}'.format(uuid, name))
        _response = self.auth.put(_url, data=filedata.read(), headers={'Content-Type': 'application/xml'})
        return parseData(_response.text)
