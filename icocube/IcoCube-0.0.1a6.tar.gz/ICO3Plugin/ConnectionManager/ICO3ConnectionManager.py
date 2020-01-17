#from ICO3Plugin.ConnectionManager.ICO3IPInitiatorConnection import ICO3IPInitiatorConnection
#from ICO3Plugin.ConnectionManager.ICO3IPListenerConnectionManager import ICO3IPListenerConnectionManager
from ICO3Utilities.Debug.LogDebug import ICO3Log
from ICO3Utilities.Xml.XmlProcess import XmlProcessing


class ICO3ConnectionManager:
    theNodeMaster = None
    theLinklist = None
    Connection = None
    ConnectionMode = None
    XmlParameters = None

    def setNodeMaster(self, xNode):
        self.theNodeMaster = xNode
        theLinklist = []

    def installParameters(self, xPrm):
        self.XmlParameters = xPrm

    def startConnection(self):
        pass

    def stopConnection(self):
        if self.theLinklist is None:
            return
        for XLNK in self.theLinklist:
            XLNK.stopLinkProcess()
        pass


    @staticmethod
    def createConnection( xmlPluginList):
        xTCnx = XmlProcessing.getAllTagElementList(xmlPluginList)
        if xTCnx is None:
            return None
        if len(xTCnx) < 1:
            return None

        xConnection = None
        xTag = xTCnx[0].tag
        if xTag == "NetworkInitiatorConnection":
            ICO3Log.print("Connection","NetworkInitiatorConnection ****************")
            from ICO3Plugin.ConnectionManager.ICO3IPInitiatorConnectionManager import ICO3IPInitiatorConnectionManager
            xConnection = ICO3IPInitiatorConnectionManager()

        if xTag == "NetworkListenerConnection":
            ICO3Log.print("Connection","NetworkInitiatorConnection ****************")
            from ICO3Plugin.ConnectionManager.ICO3IPListenerConnectionManager import ICO3IPListenerConnectionManager
            xConnection = ICO3IPListenerConnectionManager()

        if xTag == "ModuleManagerConnection":
            ICO3Log.print("Connection","ModuleManagerConnection ****************")
        if xConnection is None:
            return None

        xConnection.Connection = XmlProcessing.getAttributeValue(xmlPluginList, "Connection")
        xConnection.ConnectionMode = XmlProcessing.getAttributeValue(xmlPluginList, "ConnectionMode")
        xConnection.installParameters(xTCnx[0])
        return xConnection

    def processLink(self, xLink):
        pass

    def installLink(self, xLink):
        self.addLink(xLink)
        if self.ConnectionMode.upper() == "NODE":
            xLink.setNodeReference(self.theNodeMaster)
        xLink.startLinkProcess()




    def removeLink(self, xLink):
        pass
        # idx = self.findLinkIndex(self, xLink)
        # if idx == -1:
        #     return
        # del self.theLinklist[idx]
        #
        # self.theNodeMaster.deleteLink()
        # return

    def addLink(self, xLink):
        if self.theLinklist is None:
            self.theLinklist = []
        self.theLinklist.append(xLink)
        return


        pass
    def findLinkIndex(self, xLink):
        if self.theLinklist is None:
            return -1;
        idx = 0
        for LNK in self.theLinklist:
            if LNK.isCompatible(xLink):
                return idx
            idx += 1
        return -1


    def updateLink(self, xLink):
        pass
