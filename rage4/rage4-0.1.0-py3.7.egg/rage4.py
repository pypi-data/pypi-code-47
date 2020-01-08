import requests

class Rage4API(object):
    API_ENDPOINT = 'https://rage4.com/rapi/'

    def __init__(self, emailAddress, apiToken):
        self.emailAddress = emailAddress
        self.apiToken = apiToken

    def request(self, endpoint, method='GET', params={}, data={}):
        auth = requests.auth.HTTPBasicAuth(self.emailAddress, self.apiToken)
        return requests.request(method, Rage4API.API_ENDPOINT + endpoint, params=params, data=data, auth=auth).json()

    def getServerInfo(self):
        return self.request('index')

    def getDomains(self):
        return self.request('getdomains')

    def getDomainById(self, id):
        return self.request('getdomain', params={'id': id})

    def getDomainByName(self, name):
        return self.request('getdomainbyname', params={'name': name})

    def createDomain(self, name, email, **kwargs):
        params = {'name': name, 'email': email}
        params.update(kwargs)
        return self.request('createregulardomain', params=params)

    def deleteDomain(self, id):
        return self.request('deletedomain', params={'id': id})
    
    def updateDomain(self, id, email, **kwargs):
        params = {'id': id, 'email': email}
        params.update(kwargs)
        return self.request('updatedomain', params=params)

    def importDomainUsingAxfr(self, name):
        return self.request('importdomain', params={'name': name})

    def importDomainUsingAxfrWithVanityNS(self, name, nsName, nsPrefix):
        return self.request('importdomainext', params={'name': name, 'nsname': nsName, 'nsprefix': nsPrefix})
    
    def syncDomainWithShadowMasterServer(self, name, server, dnssec=False):
        return self.request('syncdomain', params={'name': name, 'server': server, 'dnssec': dnssec})

    def syncSlaveDomainWithShadowMasterServer(self, name, server, dnssec=False):
        return self.request('syncslavedomain', params={'name': name, 'server': server, 'dnssec': dnssec})

    def exportZoneFile(self, id):
        return self.request('exportzonefile', params={'id': id})

    def getDnsSecInfo(self, id):
        return self.request('getdnssecinfo', params={'id': id})
    
    def enableDnsSec(self, id, algorithm):
        return self.request('enablednssec', params={'id': id, 'algorithm': algorithm})

    def disableDnsSec(self, id):
        return self.request('disablednssec', params={'id': id})

    def getTSigKeys(self, id):
        return self.request('gettsiglist', params={'id': id})

    def getNotifyList(self, id):
        return self.request('getnotifylist', params={'id': id})

    def createNotifyListEntry(self, id, ipAddress):
        return self.request('createnotifylist', params={'id': id, 'ipaddress': ipAddress})
    
    def deleteNotifyListEntry(self, id, metaId):
        return self.request('deletenotifylist', params={'id': id, 'metaid': metaId})

    def getAxfrWhiteList(self, id):
        return self.request('getaxfrlist', params={'id': id})

    def createAxfrListEntry(self, id, ipAddress):
        return self.request('createaxfrlist', params={'id': id, 'ipaddress': ipAddress})
    
    def deleteAxfrListEntry(self, id, metaId):
        return self.request('deleteaxfrlist', params={'id': id, 'metaid': metaId})
    
    def listRecords(self, id, name=None):
        return self.request('getrecords', params={'id': id, 'params': params})

    def getRecord(self, id):
        return self.request('getrecord', params={'id': id})

    def createRecord(self, id, name, content, type, priority=1, **kwargs):
        params = {'id': id, 'name': name, 'content': content, 'type': type, 'priority': priority}
        params.update(kwargs)
        return self.request('createrecord', params=params)

    def updateRecord(self, id, name, content, type, priority=1, **kwargs):
        params = {'id': id, 'name': name, 'content': content, 'type': type, 'priority': priority}
        params.update(kwargs)
        return self.request('updaterecord', params=params)

    def deleteRecord(self, id):
        return self.request('deleterecord', params={'id': id})

    def enableRecordFailover(self, id):
        return self.request('recordfailover', params={'id': id, 'active': True})
    
    def disableRecordFailover(self, id):
        return self.request('recordfailover', params={'id': id, 'active': False})

    def enableRecord(self, id):
        return self.request('togglerecord', params={'id': id, 'active': True})
    
    def disableRecord(self, id):
        return self.request('togglerecord', params={'id': id, 'active': False})

    def setRecordState(self, id, **kwargs):
        return self.request('setrecordstate', params={'id': id}, data=kwargs)

    def getWebHooks(self):
        return self.request('getwebhooks')

    def getWebHook(self, id):
        return self.request('getwebhook', params={'id': id})

    def createWebHook(self, name):
        return self.request('createwebhook', params={'name': name})

    def deleteWebHook(self, id):
        return self.request('deletewebhook', params={'id': id})

    def attachWebHook(self, id, webhookId):
        return self.request('attachwebhook', params={'id': id, 'webhook': webhookId})

    def detachWebHook(self, id):
        return self.request('detachwebhook', params={'id': id})

    def getRecordTypes(self):
        return self.request('listrecordtypes')

    def getGeoRegions(self):
        return self.request('listgeoregions')
