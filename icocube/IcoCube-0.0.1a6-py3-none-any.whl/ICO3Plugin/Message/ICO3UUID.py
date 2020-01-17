import uuid
from typing import Type

from ICO3Utilities.Debug.LogDebug import ICO3Log


class ICO3UUID:
    longUUID = None
    shortID = None
    useLong = True


    def setID(self, xID):

        xSC = xID.__class__.__name__
#        xSC1 = type(xID).__name__
#        if isinstance(xID, type(uuid)):
        if(xSC == "UUID"):
            self.longUUID = xID
            self.useLong = True
            return
        if(xSC == "uuid"):
            self.longUUID = xID
            self.useLong = True
            return
        if isinstance(xID, int):
            self.shortID = xID
            self.useLong = False
        return

    @staticmethod
    def parseUUIDString(xString):
        xUID = ICO3UUID()
        try:
            xInt = int(xString)
            if xInt > -1 or xInt < (256*256):
                xUID.setID(xInt)
                return xUID
        except:
            pass

        try:
            xud = uuid.UUID(xString)
            if not xud == None:
                xUID.setID(xud)
                return xUID
        except:
            return

    @staticmethod
    def isUUID( xString):
        try:
            xud = uuid.UUID(xString)
            return True
        except:
            return False

    def getIdentificationBytes(self, xCMD):
        BID = ICO3UUID.get2BytesFromInt(self.shortID)
        BUUID = ICO3UUID.get16BytesFromUUID(self.longUUID)
        BCMD = ICO3UUID.get1BytesFromInt(xCMD)
        return BCMD+BID+BUUID

    def getByteArray(self):
        if not self.useLong:
            if self.shortID is None:
                return bytes()
            return ICO3UUID.get2BytesFromInt(self.shortID)
        xBA = bytes([0xFF]) + bytes([0xFF]) +ICO3UUID.get16BytesFromUUID(self.longUUID)
        return xBA

    @staticmethod
    def getNodeWayFromByteArray(xData, xSize):
        listWay = []
        ICO3Log.print("Message","ParseNodeWay "+ str(xSize) + "   "+xData.hex())
        xPtr = 0
        while xPtr < xSize:
            xTag = ICO3UUID.getIntFrom2Bytes(xData[xPtr: xPtr +2])
            xPtr += 2
            if xTag == 0xFFFF:
                xW = ICO3UUID.createICO3UUIDFrom16Bytes(xData[xPtr: xPtr+16])
                xPtr += 16
                listWay.append(xW)
            else:
                xW = ICO3UUID.createICO3UUIDFromInt(xTag)
                listWay.append(xW)

        return (listWay, xPtr)

    @staticmethod
    def getICO3UUIDFromIdentificationBytes(xData):
        ICO3Log.print("Message","-->"+ xData.hex())
        if len(xData) < 19:
            return None
        CMD = xData[0]
        XID = xData[1:3]
        XUUID = xData[3:]
        if len(XUUID) > 16:
            XUUID = XUUID[0:16]
        xICO3UUID = ICO3UUID()
        xICO3UUID.shortID = ICO3UUID.getIntFrom2Bytes(XID)
        xICO3UUID.longUUID = ICO3UUID.getUUIDFrom16Bytes(XUUID)
        return xICO3UUID




    @staticmethod
    def isInteger(xInt):
        try:
            xI = int(xInt)
            return True
        except:
            return False



    @staticmethod
    def get1BytesFromInt(xInt):
        return xInt.to_bytes(1, byteorder='little')

    @staticmethod
    def get2BytesFromInt(xInt):
        return xInt.to_bytes(2, byteorder='little')

    @staticmethod
    def get4BytesFromInt(xInt):
        return xInt.to_bytes(4, byteorder='little')

    @staticmethod
    def get16BytesFromUUID(xUUID):
        return xUUID.bytes

    @staticmethod
    def getUUIDFrom16Bytes(xData):
        return uuid.UUID(bytes=xData)

    @staticmethod
    def createICO3UUIDFrom16Bytes(xData):
        xU = ICO3UUID()
        xU.useLong = True
        xU.longUUID = ICO3UUID.getUUIDFrom16Bytes(xData)
        return xU

    @staticmethod
    def createICO3UUIDFromInt(xData):
        xU = ICO3UUID()
        xU.useLong = False
        xU.shortID = xData
        return xU

    @staticmethod
    def getIntFrom2Bytes(xData):
        return int.from_bytes(xData, byteorder='little')

    def toString(self):
        return str(self.shortID) + "<>" + str(self.longUUID)

    def __str__(self):
        if not self.useLong:
            return str(self.shortID)
        else:
            return str(self.longUUID)


    def __repr__(self):
        str(self)

    def __unicode__(self):
        str(self)
if __name__ == '__main__':
    TestUUID = uuid.UUID("35a81b1a-c3ac-4ee9-9803-ccf649b31007")
    xID = 2754
    xBytesINT = xID.to_bytes(2, byteorder='little')
    xByteUUID = TestUUID.bytes
    xTestUUID = uuid.UUID(bytes=xByteUUID)
    if TestUUID == xTestUUID:
        ICO3Log.print("Message","Hourra !!!!!")
    xTID = int.from_bytes(xBytesINT, byteorder='little')
    if xID == xTID:
        ICO3Log.print("Message","Hourra Hourra ....")
    BID = ICO3UUID.get2BytesFromInt(xID)
    BUUID = ICO3UUID.get16BytesFromUUID(TestUUID)
    BCMD = ICO3UUID.get1BytesFromInt(0)
    ICO3Log.print("Message","0-->" + BCMD.hex())
    BFull = BCMD+BID
    ICO3Log.print("Message","1-->" + BFull.hex())
    BFINAL = BFull+BUUID
    ICO3Log.print("Message","x-->"+ BFINAL.hex())
    BX = BCMD+BID+BUUID
    ICO3Log.print("Message","bx-->"+ BX.hex())
    XIde = ICO3UUID()
    XIde.shortID = 2754
    XIde.longUUID = uuid.UUID("35a81b1a-c3ac-4ee9-9803-ccf649b31007")
    BBX = XIde.getIdentificationBytes()
    ICO3Log.print("Message","bbx-->" + BBX.hex())

    xx3UUID = ICO3UUID.getICO3UUIDFromIdentificationBytes(BBX)

    ICO3Log.print("Message","xx-->" + xx3UUID.toString())

