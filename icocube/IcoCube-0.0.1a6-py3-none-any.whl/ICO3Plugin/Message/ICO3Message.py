import uuid

from ICO3Plugin.Message.ICO3MessageHeader import ICO3MessageHeader
from ICO3Plugin.Message.ICO3UUID import ICO3UUID
from ICO3Utilities.Debug.LogDebug import ICO3Log


class ICO3Message:

    theMessageHeader = None

    thePayload = None

    def toByteArray(self):
        if self.thePayload is None:
            return  None
        if self.theMessageHeader is None:
            return None
        try:
            self.theMessageHeader.payLoadSize = len(self.thePayload)
            xDTMH = self.theMessageHeader.getByteArray()
            return xDTMH + self.thePayload
        except Exception as e:
            ICO3Log.print("Message",e)
            return None


        pass

    @staticmethod
    def parseFromByteArray(xData):
        xMsg = ICO3Message()
        xMsg.theMessageHeader = ICO3MessageHeader.parseHeaderFromByteArray(xData)
        xHS = xMsg.theMessageHeader.headerSize
        xPLS = xMsg.theMessageHeader.payLoadSize
        xPLD = xData[xHS:]
        if len(xPLD) != xPLS:
            return xMsg
        xMsg.thePayload = xPLD
        return xMsg

    def getPayloadString(self):
        return str(self.thePayload, encoding = 'utf-8')


    def setPayloadString(self, xString):
        self.thePayload = bytes(xString, 'utf-8')
        pass

    @staticmethod
    def createMessage(xHM, xPL):
        xMsg = ICO3Message()
        xMsg.theMessageHeader = None
        if isinstance(xHM, str):
            xMsg.theMessageHeader = ICO3MessageHeader.createHeaderFromString(xHM)
        else:
            xMsg.theMessageHeader = ICO3MessageHeader.createHeaderFromString(str(xHM))

        if isinstance(xPL, str):
            xMsg.setPayloadString(xPL)
        else:
            xMsg.thePayload = xPL
        return xMsg

if __name__ == '__main__':
    TestHeader = ICO3MessageHeader()
    TestHeader.origineTaskID = 129
    TestHeader.destinationTaskID = 210
    xxx = str(TestHeader)
    ICO3Log.print("Message",str(TestHeader))
    xTestHeader = ICO3MessageHeader.parseFromString(xxx)
    ICO3Log.print("Message",str(xTestHeader))
    TestHeader.destinationModuleID = 12
    ICO3Log.print("Message",str(TestHeader))
    xxTestHeader = ICO3MessageHeader.parseFromString(xxx)
    ICO3Log.print("Message",str(xxTestHeader))

    TestHeader.origineModuleID = 8
    xxxx = str(TestHeader)
    ICO3Log.print("Message",xxxx)
    xxxTestHeader = ICO3MessageHeader.parseFromString(xxxx)
    ICO3Log.print("Message",str(xxxTestHeader))
    Dint = ICO3UUID()
    Dint.setID(5)
    TestHeader.pushWayItemEnd(Dint)

    Duuid = ICO3UUID()
    Duuid.setID(uuid.uuid4())
    TestHeader.pushWayItemEnd(Duuid)

    ICO3Log.print("Message",str(TestHeader))

    xDuuid = ICO3UUID()
    xDuuid.setID(uuid.uuid4())
    TestHeader.pushWayItemEnd(xDuuid)
    ICO3Log.print("Message",str(TestHeader))
    ICO3Log.print("Message","BackHeader")
    BackHeader = TestHeader.getBackHeader()
    ICO3Log.print("Message","Back -->>" + str(BackHeader))

    ICO3Log.print("Message",str(TestHeader))
    AXX = str(TestHeader)
    ICO3Log.print("Message",AXX)
    xxxTestHeader = ICO3MessageHeader.parseFromString(AXX)
    ICO3Log.print("Message","Parsed  -->>" + str(xxxTestHeader))
    xxxTestHeader.payLoadSize = 55
    xBA = xxxTestHeader.getByteArray()

    xMessage = ICO3Message()
    xMessage.theMessageHeader = xxxTestHeader
    xMessage.setPayloadString("Ici est la c'est beau !!!!!!!!!!!!!!")
    xMD = xMessage.toByteArray()
    ICO3Log.print("Message","Message "+ xMD.hex())
    xMsgBk = ICO3Message.parseFromByteArray(xMD)

    ICO3Log.print("Message","Back Message "+ xMsgBk.theMessageHeader.getByteArray().hex()+"   "+ xMsgBk.getPayloadString())


    ICO3Log.print("Message",xBA.hex())
    PT = ICO3MessageHeader.parseHeaderFromByteArray(xBA)
    ICO3Log.print("Message",str(PT))
    xxxTestHeader.payLoadSize = 1200
    xBA = xxxTestHeader.getByteArray()
    ICO3Log.print("Message",xBA.hex())
    PT = ICO3MessageHeader.parseHeaderFromByteArray(xBA)
    ICO3Log.print("Message",str(PT))
    TestHeader = ICO3MessageHeader()
    TestHeader.origineTaskID = 129
    TestHeader.destinationTaskID = 210
    TestHeader.payLoadSize = 55
    xBA = TestHeader.getByteArray()
    ICO3Log.print("Message",xBA.hex())
    PT = ICO3MessageHeader.parseHeaderFromByteArray(xBA)
    ICO3Log.print("Message",str(PT))
    TestHeader.destinationModuleID = 12
    TestHeader.origineModuleID = 8
    xBA = TestHeader.getByteArray()
    PT = ICO3MessageHeader.parseHeaderFromByteArray(xBA)
    ICO3Log.print("Message",xBA.hex())
    ICO3Log.print("Message",str(PT))





