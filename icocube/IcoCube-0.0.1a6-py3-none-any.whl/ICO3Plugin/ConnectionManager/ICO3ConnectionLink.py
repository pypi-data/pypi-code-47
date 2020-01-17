from abc import abstractmethod

from ICO3Plugin.Message.ICO3Message import ICO3Message
from ICO3Plugin.Message.ICO3UUID import ICO3UUID
from ICO3Utilities.Debug.LogDebug import ICO3Log


class ICO3ConnectionLink:
    theConnectionManager = None
    theStatus = None
    theNode = None
    theTarget = None
    #theModule = None
    theIdentificationMode = None
    theIdentificationProcess = None


    theMode = None

    targetID = None
    targetSN = None

    IDUser = 0
    NodeUser = 0x80

    def receiveData2Node(self, xData):
        xMsg = ICO3Message.parseFromByteArray(xData)
        self.theNode.sendMessage(xMsg)


    def setNodeReference(self, xNode):
        self.theMode = "NODE"
        self.theNode = xNode


    def setConnectionManager(self, xConMng):
        self.theConnectionManager = xConMng

    def setStatus(self, xSt):
        self.theStatus = xSt

    def setNode(self, xNd):
        self.theNode = xNd

    def setIdentificationProcess(self, xIdP):
        self.theIdentificationProcess = xIdP

    def isCompatible(self, xID):
        if self.theMode != xID.theMode:
            return False

        if self.theMode == "NODE":
            if self.targetSN == xID.targetSN:
                return True
            if self.targetID == xID.targetID:
                return True
            return False

        if self.theMode == "MODULE":
            if self.targetID == xID.targetID:
                return True
            return False

    @abstractmethod
    def startLinkProcess(self):
        pass

    @abstractmethod
    def stopLinkProcess(self):
        pass

    @abstractmethod
    def sendMessage(self, xMsg):
        pass

    @abstractmethod
    def sendData(self, xData, xUsr):
        pass

    def getMode(self):
        return self.theMode

    def identificationProcessCompleted(self, xStatus):
        ICO3Log.print("Link","Identification Process Completed  " + str(xStatus)+ "  Remote Node :" + str(self.targetID) + " ; "+ str(self.targetSN))
        self.theNode.addLink(self)





