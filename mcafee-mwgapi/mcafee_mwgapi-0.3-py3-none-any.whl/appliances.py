
from webgatewayapi.authenticate import authenticate
from webgatewayapi.parse import parseData




class appliances(object):
    """
        appliance class object has default operations an appliance can provide, including "commit". For any appliance
        specific functions this class must be used.

        THIS CLASS CAN BE BROKEN DOWN INTO META CLASS IF NECESSARY
    """

    def __init__(self, auth, hostname, port, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.reference = authenticate(hostname=self.hostname, port=self.port, https=self.https)



    def listAppliances(self, pagesize=10, page=1):
        """
            listAppliances method will generate a full list of appliances available depending on the primary cluster
        logged-in
        :return Full List of Appliances.
        """
        _url = self.reference.createAppendURL(string='appliances')
        _response = self.auth.get(_url, params={'pageSize': pagesize, 'page': page})
        return parseData(_response.text)

    def listAppliancesList(self, name=None, ltype=None):
        """
            listAppliancesList will generate the full list of appliances available in the cluster.
        :param name:
        :param ltype:
        :return: Full list of appliances in the active cluster.
        """
        _url = self.reference.createAppendURL(string='appliances')
        data = {}
        if ltype is not None:
            data['type'] = ltype
        if name is not None:
            data['name'] = name
        _response = self.auth.get(_url, params=data)
        return parseData(_response.text)





















