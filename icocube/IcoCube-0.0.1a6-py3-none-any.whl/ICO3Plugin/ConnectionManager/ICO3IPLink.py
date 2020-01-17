import traceback
from threading import Thread

from ICO3Plugin.ConnectionManager.ICO3ConnectionLink import ICO3ConnectionLink
from ICO3Plugin.ConnectionManager.ICO3IdentificationProcess import ICO3ListenerIdentificationProcess, \
    ICO3InitiatorIdentificationProcess
from ICO3Plugin.ConnectionManager.ICO3PhyDataBuffer import ICO3PhyDataBuffer
from ICO3Plugin.Message.ICO3Message import ICO3Message
from ICO3Plugin.Message.ICO3UUID import ICO3UUID
from ICO3Utilities.Debug.LogDebug import ICO3Log


class ICO3IPLink(ICO3ConnectionLink):

    theSocket = None
    theLoopReading = False
    theReadBuffer = None

    def sendMessage(self, xMsg):
        xMsg.theMessageHeader.nextNodePointer()
        xData = xMsg.toByteArray()
        xSTR = xData.hex()
        self.sendData(xData, self.NodeUser)
        return 1

    def startLinkProcess(self):
        ICO3Log.print("Connection","Start Link Process : " + self.theMode + "  "+ str(self.theNode.NodeUUID) + "  "+ self.theIdentificationMode)
        if self.theSocket is None:
            ICO3Log.print("Connection","No Socket Available")
            return
        self.startReadProcess()
        if self.theIdentificationMode == "INITIATOR":
            self.theIdentificationProcess = ICO3InitiatorIdentificationProcess()
        if self.theIdentificationMode == "LISTENER":
            self.theIdentificationProcess = ICO3ListenerIdentificationProcess()
        if self.theIdentificationProcess is not None:
            self.theIdentificationProcess.startProcess(self)

    def startReadProcess(self):
        if self.theSocket is None:
            return
        self.theLoopReading = True
        LTread = Thread( target = self.readLoopProcess)
        LTread.start()
        pass

    def stopLinkProcess(self):
        self.killComSocket()

    def readLoopProcess(self):
        while self.theLoopReading:
            try:
                xData = self.theSocket.recv(1024)
                if xData is not None:
                    xSize = len(xData)
                    if xSize != 0 :
                        self.processPhyDataReceived(xData)
            except Exception as e:
                ICO3Log.print("Connection","ICO3IPLink   " + str(e))
                self.killComSocket()
                self.restartLink()
                return e
        self.killComSocket()

        return
    def killComSocket(self):
        ICO3Log.print("Connection","Kill Com Socket ")
        self.theLoopReading = False
        self.theSocket.close()
        self.theNode.deleteLink(self)

    def restartLink(self):
        if self.theIdentificationMode != "LISTENER":
            self.theNode.restartTarget(self.theTarget)
            ICO3Log.print("Connection","***** Try to Restart Link (Need to write function) *******")
        else :
            ICO3Log.print("Connection","***** Wait reconnection by Initiator *********")
        pass


    def processPhyDataReceived(self, xData):
        ICO3Log.print("Connection","Data Received  " + xData.hex())
        if self.theReadBuffer is None:
            self.theReadBuffer = ICO3PhyDataBuffer()
        self.theReadBuffer.pushData(xData)

        while self.theReadBuffer.isComplete() > 0:
            RDBuffer = self.theReadBuffer.getPayload()
            RDUser = self.theReadBuffer.getUserID()
            self.theReadBuffer = self.theReadBuffer.getNextPhyBuffer()
            self.processInputBufferData(RDBuffer, RDUser)

        return

    def processInputBufferData(self, xData, xUser):
        if xUser == self.IDUser:
            if self.theIdentificationProcess is not None:
                self.theIdentificationProcess.receiveData(xData)
                return
            return
        if xUser == self.NodeUser:
            self.receiveData2Node(xData)
            return
        return

    def sendData(self,xData,xUsr):
        try:
            xSize = ICO3UUID.get2BytesFromInt( len(xData))
            xUser = ICO3UUID.get2BytesFromInt(xUsr)
            xPr = xUser+xSize
            xPData = xPr + xData
            self.sendPhyData(xPData)

        except Exception as e:
            ICO3Log.print("Connection","sendData "+ str(e))
            return


    def sendPhyData(self,xData):
        if self.theSocket is not None:
            try:
                ICO3Log.print("Connection","Send  Data " + xData.hex())
                self.theSocket.send(xData)
                return True
            except Exception as e:
                return False



