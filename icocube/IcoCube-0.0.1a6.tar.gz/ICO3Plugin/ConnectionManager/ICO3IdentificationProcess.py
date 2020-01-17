import uuid
from abc import abstractmethod
from enum import Enum

from ICO3Plugin.Message.ICO3UUID import ICO3UUID
from ICO3Utilities.Debug.LogDebug import ICO3Log


class ProcessStateID(Enum):
    RESET = 0
    ACCEPTED = 1
    WAITINITIATORINFO = 2
    WAITSERVERINFO = 3
    WAITACKINFO = 4
    REJECTED = -1
    ERROR = -2




class ICO3IdentificationProcess:
    theLink = None
    isAccepted = False
    processStatus = ProcessStateID.RESET
    localIDMessage = None
    remoteIDMessage = None


    def installLink(self, xLnk):
        if xLnk is None:
            return
        self.theLink = xLnk
        self.createLocalIDMessage()

    @abstractmethod
    def startProcess(self, xLnk):
        pass

    def createLocalIDMessage(self):
        xUUID = ICO3UUID()
        xUUID.shortID = self.theLink.theNode.NodeID
        xUUID.longUUID = self.theLink.theNode.NodeUUID
        self.localIDMessage = IDENTIFICATIONMESSAGE.createFromICO3UUID(xUUID)

    def processIdentificationResult(self):
        if self.theLink is None:
            return
        if self.remoteIDMessage is None:
            return
        self.theLink.targetID = self.remoteIDMessage.theNodeID;
        self.theLink.targetSN = self.remoteIDMessage.theNodeSN;
        self.theLink.identificationProcessCompleted(self.processStatus)
        pass

    @abstractmethod
    def receiveData(self, xData):
        pass

class ICO3InitiatorIdentificationProcess(ICO3IdentificationProcess):
    def startProcess(self, xLnk):
        self.installLink(xLnk)
        ICO3Log.print("Connection","Start Initiator Identification Process>>>>>> " + str(self.localIDMessage))
        xData = self.localIDMessage.getByteArray()
        if self.theLink is not None:
            self.theLink.sendData(xData,0)
            self.processStatus = ProcessStateID.WAITSERVERINFO
            return
        self.processStatus = ProcessStateID.ERROR
        return

    def receiveData(self, xData):
        ICO3Log.print("Connection","Receive ID Data Initiator "+ str(self.processStatus)+"  "+ xData.hex())
        if self.processStatus == ProcessStateID.WAITSERVERINFO:
            self.remoteIDMessage = IDENTIFICATIONMESSAGE.createFromByteArray(xData)
            if self.remoteIDMessage.xCommand == 0:
                xReply = ICO3UUID.get1BytesFromInt(1)               #int(ProcessStateID.ACCEPTED)
                if self.theLink is not None:
                    self.theLink.sendData(xReply,0)
                    self.processStatus = ProcessStateID.ACCEPTED
                    self.processIdentificationResult()
                    return
            xReply = ICO3UUID.get1BytesFromInt(-1)                  #int(ProcessStateID.REJECTED)
            if self.theLink is not None:
                self.theLink.sendData(xReply, 0)
                self.processStatus = ProcessStateID.REJECTED
                self.processIdentificationResult()




class ICO3ListenerIdentificationProcess(ICO3IdentificationProcess):
    def startProcess(self, xLnk):
        self.installLink(xLnk)
        ICO3Log.print("Connection","Start Listener Identification Process>>>>>>>"+ str(self.localIDMessage))
        self.processStatus = ProcessStateID.WAITINITIATORINFO
        return

        xData = self.localIDMessage.getByteArray()
        if self.theLink is not None:
            self.theLink.sendData(xData)
            self.processStatus = ProcessStateID.WAITSERVERINFO
            return
        self.processStatus = ProcessStateID.ERROR
        return

    def receiveData(self, xData):
        print("Receive ID Data Listener "+ str(self.processStatus)+"  "+ xData.hex())
        if self.processStatus == ProcessStateID.WAITINITIATORINFO:
            self.remoteIDMessage = IDENTIFICATIONMESSAGE.createFromByteArray(xData)
            if self.remoteIDMessage.xCommand == 0:
                xReply = self.localIDMessage.getByteArray()
                if self.theLink is not None:
                    self.theLink.sendData(xReply,0)
                    self.processStatus = ProcessStateID.WAITACKINFO
                    return
            self.processStatus = ProcessStateID.ERROR
            return
        if self.processStatus == ProcessStateID.WAITACKINFO:
            xxCmd = int(xData[0])
            if xxCmd < 0:
                self.processStatus = ProcessStateID.REJECTED
                self.processIdentificationResult()
                return
            else:
                self.processStatus = ProcessStateID.ACCEPTED
                self.processIdentificationResult()
                return
        self.processStatus = ProcessStateID.ERROR
        return



class IDENTIFICATIONMESSAGE:
    xCommand = 0
    theNodeID = None
    theNodeSN = None
    theICO3UUID = None

    @staticmethod
    def createFromByteArray(xBA):
        if len(xBA)< 19:
            return None

        XID = ICO3UUID.getICO3UUIDFromIdentificationBytes(xBA)
        IM = IDENTIFICATIONMESSAGE.createFromICO3UUID(XID)
        IM.xCommand = int(xBA[0])
        return IM

    @staticmethod
    def createFromICO3UUID(xUID):
        IM = IDENTIFICATIONMESSAGE()
        IM.theICO3UUID = xUID
        IM.theNodeID = IM.theICO3UUID.shortID
        IM.theNodeSN = IM.theICO3UUID.longUUID
        return IM

    def getByteArray(self):
        return self.theICO3UUID.getIdentificationBytes(self.xCommand)

    def getICO3UUID(self):
        return self.theICO3UUID

    def __str__(self):
        return str(self.theNodeID) +" > "+str(self.theNodeSN)

if __name__ == '__main__':
    XIde = ICO3UUID()
    XIde.shortID = 2754
    XIde.longUUID = uuid.UUID("35a81b1a-c3ac-4ee9-9803-ccf649b31007")
    xIM = IDENTIFICATIONMESSAGE.createFromICO3UUID(XIde)

    xBA = xIM.getByteArray()
    print ("Message : "+ xBA.hex())

    xIM1 = IDENTIFICATIONMESSAGE.createFromByteArray(xBA)
    print(str(xIM1))
    xIM1 = IDENTIFICATIONMESSAGE.createFromByteArray(xBA+xBA)
    print(str(xIM1))



    pass