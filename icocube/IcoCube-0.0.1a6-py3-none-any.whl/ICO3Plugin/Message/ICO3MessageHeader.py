import uuid

from ICO3Plugin.Message.ICO3UUID import ICO3UUID
from ICO3Utilities.Debug.LogDebug import ICO3Log


class ICO3MessageHeader:
    #    if Raw Message size < 4 don't process it is error.
    #
    #    Data[0] model of the message  0xFF --> Small Message Header,
    #                                   0x00 --> Medium Message Header,
    #                                   Other Large Message Header
    #
    #    -----------Small Message Header ( Data[0] = 0x00 )-------
    #    Is used for task to task message inside the same Module.
    #    Data[1]         Size of the payload message.
    #    Data[2)         Origine Task ID
    #    Data[3]         Destination Task ID
    #    Data[4]...      PayLoad Message
    #    ---------------------------------------------------------
    #
    #    -----------Medium Message Header ( Data[0] = 0xFF )------
    #    Is used for task to task message inside the same Node.
    #    Data[1]         Size of the payload message.
    #    Data[2)         Origine Task ID
    #    Data[3]         Destination Task ID
    #    Data[4]         Origine Module ID
    #    Data[5]         Destination Module ID
    #    Data[6]...      PayLoad Message
    #    ---------------------------------------------------------
    #
    #    -----------Large Message Header-------------------------
    #    Is used for task to task message in any way
    #    Data[0]                 Header Size less 8 bytes
    #    Data[1]                 Size of the payload message. Max 254 bytes dont use 0xFF
    #    Data[2)                 Origine Task ID
    #    Data[3]                 Destination Task ID
    #    Data[4]                 Origine Module ID
    #    Data[5]                 Destination Module ID
    #    Data[6]                 Active Node Pointer in the Way
    #    Data[7]                 Message ID
    #    Data[8]...[(Data[0]+7)] MessageWay
    #    Data[(Data[0]+8)]...    PayLoad Message
    #    ---------------------------------------------------------

    #    -----------Extra Large Message Header--------------------
    #    Is used for task to task message in any way
    #    Data[0]                 Header Size less 8 bytes
    #    Data[1]                 must be 0xFF
    #    Data[2)                 Origine Task ID
    #    Data[3]                 Destination Task ID
    #    Data[4]                 Origine Module ID
    #    Data[5]                 Destination Module ID
    #    Data[6]                 Active Node Pointer in the Way
    #    Data[7]                 Message ID
    #    Data[8]...[(Data[0]+7)] MessageWay
    #    Data[(Data[0]+8)]       PayLoad Message size 4 Bytes (Max 4 GB).
    #    Data[(Data[0]+12)]...   PayLoad Message
    #    ---------------------------------------------------------

    headerMode = "NA"
    headerSize = None
    payLoadSize = None
    origineTaskID = None
    origineModuleID = None
    destinationTaskID = None
    destinationModuleID = None
    activeNodeWayPtr = 0
    messageTag = 0
    nodeWay = None

    def isModuleOK(self, xModule):
        ICO3Log.print("Message","isModuleOK Process")
        if self.headerMode is None:
            self.checkHeaderMode()
        if self.headerMode == "NA":
            self.checkHeaderMode()
        ICO3Log.print("Message"," Header Mode : " + self.headerMode)
        if self.headerMode == "SMALL":
            return True
        xMID = xModule.getModuleID()
        if xMID != self.destinationModuleID:
            return False
        if self.headerMode == "MEDIUM":
            return True
        return self.isNodeOK(xModule.getNode())

    def isLastNode(self):
        if self.activeNodeWayPtr + 1 == len(self.nodeWay):
            return True
        return False

    def isNodeOK(self, xNode):
        if self.headerMode is None:
            self.checkHeaderMode()
        if self.headerMode == "SMALL":
            return True
        if self.headerMode == "MEDIUM":
            return True
        if not self.isLastNode():
            return

        xActNodeRef = self.getActiveNode()

        if xActNodeRef is not None:
            if xActNodeRef.useLong:
                return xActNodeRef.longUUID == xNode.NodeUUID
            else:
                return xActNodeRef.shortID == xNode.NodeID
        return False

    def isLinkOK(self, xLink):
        if self.headerMode is None:
            self.checkHeaderMode()
        if self.headerMode == "SMALL":
            return False
        if self.headerMode == "MEDIUM":
            return False

        xNActNodeRef = self.getNextActiveNode()

        if xNActNodeRef is not None:
            if xNActNodeRef.useLong:
                return xNActNodeRef.longUUID == xLink.targetSN
            else:
                return xNActNodeRef.shortID == xLink.targetID
        return False


    def getActiveNode(self):
        try:
            if self.headerMode == "SMALL":
                return None
            if self.headerMode == "MEDIUM":
                return None
            return self.nodeWay[self.activeNodeWayPtr]
        except:
            return None

    def getNextActiveNode(self):
        try:
            if self.headerMode == "SMALL":
                return None
            if self.headerMode == "MEDIUM":
                return None
            return self.nodeWay[self.activeNodeWayPtr + 1]
        except:
            return None

    def getByteArray(self):
        self.checkHeaderMode()
        if self.headerMode == "SMALL":
            return self.getByteArraySmall()
        if self.headerMode == "MEDIUM":
            return self.getByteArrayMedium()
        if self.headerMode == "LONG":
            return self.getByteArrayLong()
        if self.headerMode == "XLONG":
            return self.getByteArrayXLong()
        return None

    def getByteArraySmall(self):
        xCNT = bytes([0x00])
        if self.payLoadSize > 254:
            return None
        xPLS = ICO3UUID.get1BytesFromInt(self.payLoadSize)
        xOT = ICO3UUID.get1BytesFromInt(self.origineTaskID)
        xDT = ICO3UUID.get1BytesFromInt(self.destinationTaskID)
        return xCNT + xPLS + xOT + xDT

    def getByteArrayMedium(self):
        xCNT = bytes([0xFF])
        if self.payLoadSize > 254:
            return None
        xPLS = ICO3UUID.get1BytesFromInt(self.payLoadSize)
        xOT = ICO3UUID.get1BytesFromInt(self.origineTaskID)
        xDT = ICO3UUID.get1BytesFromInt(self.destinationTaskID)
        xOM = ICO3UUID.get1BytesFromInt(self.origineModuleID)
        xDM = ICO3UUID.get1BytesFromInt(self.destinationModuleID)
        return xCNT + xPLS + xOT + xDT + xOM + xDM

    def getByteArrayLong(self):
        xNWA = self.GetAddrWay2ByteArray()
        xCNT = ICO3UUID.get1BytesFromInt(len(xNWA))
        if self.payLoadSize > 254:
            xPLS = bytes([0xFF])
        else:
            xPLS = ICO3UUID.get1BytesFromInt(self.payLoadSize)
        xOT = ICO3UUID.get1BytesFromInt(self.origineTaskID)
        xDT = ICO3UUID.get1BytesFromInt(self.destinationTaskID)
        xOM = ICO3UUID.get1BytesFromInt(self.origineModuleID)
        xDM = ICO3UUID.get1BytesFromInt(self.destinationModuleID)
        xPTR = ICO3UUID.get1BytesFromInt(self.activeNodeWayPtr)
        xIDX = ICO3UUID.get1BytesFromInt(self.messageTag)

        xMHBA =  xCNT + xPLS + xOT + xDT + xOM + xDM + xPTR + xIDX + xNWA
        if self.payLoadSize > 254:
            return self.getByteArrayXLong(xMHBA)
        return xMHBA

    def getByteArrayXLong(self, xMHBA):
        return xMHBA  + ICO3UUID.get4BytesFromInt(self.payLoadSize)

    @staticmethod
    def parseHeaderFromByteArray(xData):
        xMH = ICO3MessageHeader()
        xMH.installParameterFromByteArray(xData)
        return xMH

    def installParameterFromByteArray(self, xData):
        if xData[0] == 0:
            self.setupSmallHeaderFromByteArray(xData)
            return
        if xData[0] == 0xFF:
            self.setupMediumHeaderFromByteArray(xData)
            return

        self.setupLongHeaderFromByteArray(xData)
        return

    def setupSmallHeaderFromByteArray(self, xData):
        if len(xData) < 4:
            self.headerMode = "NA"
            return
        self.payLoadSize = xData[1]
        self.origineTaskID = xData[2]
        self.destinationTaskID = xData[3]
        self.headerMode = "SMALL"
        self.headerSize = 4
        return

        pass
    def setupMediumHeaderFromByteArray(self, xData):
        self.setupSmallHeaderFromByteArray(xData)
        if len(xData) < 6:
            return

        self.origineModuleID= xData[4]
        self.destinationModuleID= xData[5]
        self.headerMode = "MEDIUM"
        self.headerSize = 6
        pass

    def setupLongHeaderFromByteArray(self, xData):
        self.setupMediumHeaderFromByteArray(xData)
        if len(xData) < 8:
            return
        xNWS = xData[0]
        self.messageTag = xData[7]
        self.activeNodeWayPtr = xData[6]
        (self.nodeWay, xPtr) = ICO3UUID.getNodeWayFromByteArray(xData[8:], xNWS)
        self.headerSize = xPtr + 8
        if self.payLoadSize == 0xFF:
            self.payLoadSize = ICO3UUID.getIntFrom2Bytes(xData[self.headerSize: self.headerSize+4])
            self.headerSize += 4

        return


    def GetAddrWay2ByteArray(self):
        if self.nodeWay == None:
            return None
        if len(self.nodeWay) == 0:
            return None
        ListByte = bytes()
        for  ADR in  self.nodeWay:
            ListByte = ListByte+ ADR.getByteArray()
        return ListByte;

    def cloneHeader(self):
        CHeader = ICO3MessageHeader()
        CHeader.cloneHeaderFrom(self)
        # CHeader.destinationTaskID = self.destinationTaskID
        # CHeader.origineTaskID = self.origineTaskID
        # CHeader.origineModuleID = self.origineModuleID
        # CHeader.destinationModuleID = self.destinationModuleID
        # for xW in self.nodeWay:
        #     CHeader.pushWayItemEnd(xW)
        return CHeader

    def cloneHeaderFrom(self, xHeader):
        self.destinationTaskID = xHeader.destinationTaskID
        self.origineTaskID = xHeader.origineTaskID
        self.origineModuleID = xHeader.origineModuleID
        self.destinationModuleID = xHeader.destinationModuleID
        for xW in xHeader.nodeWay:
            self.pushWayItemEnd(xW)

    def getBackHeader(self):
        CHeader = self.cloneHeader()
        CHeader.doBackHeader()
        return CHeader

    def doBackHeader(self):
        temp = self.origineTaskID
        self.origineTaskID = self.destinationTaskID
        self.destinationTaskID = temp
        temp = self.origineModuleID
        self.origineModuleID = self.destinationModuleID
        self.destinationModuleID = temp
        self.nodeWay.reverse()

    def checkMessageHeader(self, xModule):
        self.checkHeaderMode()
        if self.headerMode == "SMALL":
            return;
        if self.origineModuleID == -1:
            self.origineModuleID = xModule.getModuleID()
        if self.headerMode == "MEDIUM":
            return
        xNodeICO3UUUID = xModule.getNode().getICO3NodeID()
        xFirst = self.nodeWay[0]
        if not xFirst.useLong:
            if xFirst.shortID == xNodeICO3UUUID.shortID:
                return
            xExtra = ICO3UUID.parseUUIDString(str(xNodeICO3UUUID.shortID))
        else:
            if xFirst.longUUID == xNodeICO3UUUID.longUUID:
                return
            xExtra = ICO3UUID.parseUUIDString(str(xNodeICO3UUUID.longUUID))
        if xExtra is not None:
            self.nodeWay.insert(0, xExtra)
        return
        pass

    @staticmethod
    def createHeaderFromString(xString):
        if xString is None:
            return None
        # try:
        xHeader = ICO3MessageHeader()
        XSList = xString.split(">")
        xHeader.setOrigineFromString(XSList[0])
        XSList2 = XSList[1].split(":")
        if len(XSList2) > 1:
            xHeader.setDestinationFromString(XSList2[1])
            xHeader.setWayFromString(XSList2[0])
        else:
            xHeader.setDestinationFromString(XSList2[0])
        return xHeader

        # except Exception as e:
        #     ICO3Log.print("Message",e)
        #     return None
        #
        #
        # return xHeader

    def setDestinationFromString(self, xString):
        XSList = xString.split("@")
        self.destinationTaskID = int(XSList[0])
        if len(XSList) > 1:
            self.destinationModuleID = int(XSList[1])
        return

    def setOrigineFromString(self, xString):
        XSList = xString.split("@")
        self.origineTaskID = int(XSList[0])
        if len(XSList) > 1:
            if XSList[1] == "*":
                self.origineModuleID = -1
            else:
                self.origineModuleID = int(XSList[1])
            return

    def setWayFromString(self, xString):
        self.nodeWay = []
        XSList = xString.split("/")
        for XSL in XSList:
            self.nodeWay.append(ICO3UUID.parseUUIDString(XSL))
        return

    def pushWayItemStart(self, theItem):
        if not isinstance(theItem, ICO3UUID):
            return
        if self.nodeWay == None:
            self.nodeWay = []
        self.nodeWay.index(0, theItem)

    def pushWayItemEnd(self, theItem):
        if not isinstance(theItem, ICO3UUID):
            return
        if self.nodeWay == None:
            self.nodeWay = []
        self.nodeWay.append(theItem)

    def checkHeaderMode(self):
        if self.destinationModuleID == None:
            self.headerMode = "SMALL"
            return
        if self.nodeWay == None:
            self.headerMode = "MEDIUM"
            return
        if len(self.nodeWay) == 0:
            self.headerMode = "MEDIUM"
            return
        self.headerMode = "LONG"

    def nextNodePointer(self):
        if self.headerMode is None:
            self.checkHeaderMode()
        if self.headerMode == "NA":
            self.checkHeaderMode()
        if self.headerMode == "LONG":
            xNS=len(self.nodeWay)
            if xNS > self.activeNodeWayPtr + 1:
                self.activeNodeWayPtr += 1
        return

    def __str__(self):
        self.checkHeaderMode()
        if self.headerMode == "SMALL":
            return self.smallHeaderToString()

        if self.headerMode == "MEDIUM":
            return self.mediumHeaderToString()
        return self.longHeaderToString()

    def __repr__(self):
        str(self)

    def __unicode__(self):
        str(self)

    def smallHeaderToString(self):
        xString = ""
        if self.origineTaskID == None:
            xString += "None>"
        else:
            xString += str(self.origineTaskID) + ">"

        if self.destinationTaskID == None:
            xString += "None"
        else:
            xString += str(self.destinationTaskID)

        return xString

    def mediumHeaderToString(self):
        xString = ""
        if self.origineTaskID == None:
            xString += "None@"
        else:
            xString += str(self.origineTaskID) + "@"

        if self.origineModuleID == None:
            xString += "*>"
        else:
            xString += str(self.origineModuleID) + ">"

        if self.destinationTaskID == None:
            xString += "None@"
        else:
            xString += str(self.destinationTaskID) + "@"

        if self.destinationModuleID == None:
            xString += "####"
        else:
            xString += str(self.destinationModuleID)

        return xString

    def longHeaderToString(self):
        xString = ""
        if self.origineTaskID == None:
            xString += "None@"
        else:
            xString += str(self.origineTaskID) + "@"

        if self.origineModuleID == None:
            xString += "*>"
        else:
            xString += str(self.origineModuleID) + ">"

        xString += self.getWayString() + ":"

        if self.destinationTaskID == None:
            xString += "None@"
        else:
            xString += str(self.destinationTaskID) + "@"

        if self.destinationModuleID == None:
            xString += "####"
        else:
            xString += str(self.destinationModuleID)

        return xString

    def installDestinationString(self, xDest):
        xSplit = xDest.split("@")
        if len(xSplit) < 1:
            return
        try:
            self.destinationTaskID = int(xSplit[0])
        except:
            pass
        if len(xSplit) < 2:
            return
        try:
            self.destinationModuleID = int(xSplit[1])
        except:
            pass
        return

    def installWayString(self, param):
        if param == None:
            return
        xSplit = param.split("/")
        for sW in xSplit:
            xuID = ICO3UUID.parseUUIDString(sW)
            if xuID is not None:
                self.pushWayItemEnd(xuID)

    def installOrigineString(self, xOrg):
        xSplit = xOrg.split("@")
        if len(xSplit) < 1:
            return
        try:
            self.origineTaskID = int(xSplit[0])
        except:
            pass
        if len(xSplit) < 2:
            return
        try:
            self.origineModuleID = int(xSplit[1])
        except:
            pass
        return

    def getWayString(self):
        xString = ""
        xTag = ""
        for xW in self.nodeWay:
            xString += xTag + str(xW)
            xTag = "/"
        return xString

    @staticmethod
    def parseFromString(xString):
        xSplit = xString.split(">")
        if len(xSplit) < 2:
            return
        xHeader = ICO3MessageHeader()
        xHeader.installOrigineString(xSplit[0])
        xxSplit = xSplit[1].split(":")
        if len(xxSplit) < 2:
            xHeader.installDestinationString(xxSplit[0])
            return xHeader
        xHeader.installWayString(xxSplit[0])
        xHeader.installDestinationString(xxSplit[1])
        return xHeader

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

