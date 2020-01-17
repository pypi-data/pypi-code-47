import uuid

from ICO3Plugin.Message.ICO3UUID import ICO3UUID
from ICO3Utilities.Debug.LogDebug import ICO3Log


class ICO3PhyDataBuffer:

    theBuffer = None
    theUserID = None
    theSize = None
    rawBuffer = None
    theNextPhyBuffer =  None

    def setPayLoad(self, xPayLoad):
        if xPayLoad is not None:
            self.theBuffer = xPayLoad
            self.theSize = len(self.theBuffer)

    def setUser(self, xUser):
        self.theUserID = xUser

    def isComplete(self):
        if self.rawBuffer is None:
            return -1
        if len(self.rawBuffer) < 4:
            return -1
        self.theUserID = ICO3UUID.getIntFrom2Bytes(self.rawBuffer[0:2])
        self.theSize = ICO3UUID.getIntFrom2Bytes(self.rawBuffer[2:4])

        if len(self.rawBuffer) < (self.theSize + 4):
            return -1
        return 1

    def pushData(self, xData):
        ICO3Log.print("Connection","Push Data : "+ xData.hex())
        ICO3Log.print("Connection","Push Data User : " + xData[0:2].hex())
        ICO3Log.print("Connection","Push Data Size : " + xData[2:4].hex())
        if self.rawBuffer is None:
            self.rawBuffer = xData
        else:
            self.rawBuffer = self.rawBuffer +xData

        if len(self.rawBuffer) < 4:
            return -1
        self.theUserID = ICO3UUID.getIntFrom2Bytes(xData[0:2])
        self.theSize = ICO3UUID.getIntFrom2Bytes(xData[2:4])

        if len(self.rawBuffer) < (self.theSize+4):
            return -1

        self.theBuffer = self.rawBuffer[4:(4+ self.theSize)]
        xremainBuffer = self.rawBuffer[(4+ self.theSize):]
        self.theNextPhyBuffer = ICO3PhyDataBuffer()
        if xremainBuffer is not None:
            if len(xremainBuffer) > 0:
                self.theNextPhyBuffer.pushData(xremainBuffer)
        return 1



    def getNextPhyBuffer(self):
        return self.theNextPhyBuffer

    def getPayload(self):
        return self.theBuffer

    def getUserID(self):
        return self.theUserID

    def getPhyMessage(self):
        try:
            if self.theBuffer is None:
                return None
            if self.theUserID is None:
                return  None
            self.theSize = len(self.theBuffer)
            xBU = ICO3UUID.get2BytesFromInt(self.theUserID)
            xBS = ICO3UUID.get2BytesFromInt(self.theSize)
            return xBU+xBS+self.theBuffer
        except:
            pass
        return None


if __name__ == '__main__':
    XIde = ICO3UUID()
    XIde.shortID = 2754
    XIde.longUUID = uuid.UUID("35a81b1a-c3ac-4ee9-9803-ccf649b31007")
    BBX = XIde.getIdentificationBytes(0)

    x2BBX = BBX + BBX
    PDB = ICO3PhyDataBuffer()
    PDB.setUser(1)
    PDB.setPayLoad(BBX)
    xPhyMess = PDB.getPhyMessage()

    RPDB = ICO3PhyDataBuffer()
    if RPDB.pushData(xPhyMess) > 0:
        if(RPDB.isComplete() > 0):
            ICO3Log.print("Connection","PhyDataBuffer Complete")
        ICO3Log.print("Connection","Message RCEV:"+ str(RPDB.getUserID())+"  Size : "+ str(RPDB.theSize)+ "Msg : " + str(RPDB.getPayload().hex()))
        RPDB = RPDB.getNextPhyBuffer()
    xPhyMess1 = xPhyMess + xPhyMess
    if RPDB.pushData(xPhyMess1) > 0:
        ICO3Log.print("Connection","Message RCEV:"+ str(RPDB.getUserID())+"  Size : "+ str(RPDB.theSize)+ "Msg : " + str(RPDB.getPayload().hex()))
        RPDB = RPDB.getNextPhyBuffer()
        if (RPDB.isComplete() > 0):
            ICO3Log.print("Connection","PhyDataBuffer Complete")
            ICO3Log.print("Connection","Message RCEV:" + str(RPDB.getUserID()) + "  Size : " + str(RPDB.theSize) + "Msg : " + str(RPDB.getPayload().hex()))
            RPDB = RPDB.getNextPhyBuffer()
            ICO3Log.print("Connection","Buffer is Complete : "+str(RPDB.isComplete()))













