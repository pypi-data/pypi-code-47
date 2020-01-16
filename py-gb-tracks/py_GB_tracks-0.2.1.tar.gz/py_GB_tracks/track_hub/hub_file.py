from ..meta import FileWriter


class HubFile(FileWriter):

    def __init__(self, hub, shortLabel=None, longLabel=None,
                 genomesFile=None, email=None, descriptionURL=None):
        '''
        '''
        self.hub = hub
        self.shortLabel = shortLabel
        self.longLabel = longLabel
        self.genomesFile = genomesFile
        self.email = email
        self.descriptionURL = descriptionURL
