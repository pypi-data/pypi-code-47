import socket
from threading import Thread

from ICO3Plugin.ConnectionManager.ICO3ConnectionManager import ICO3ConnectionManager
from ICO3Plugin.ConnectionManager.ICO3IPLink import ICO3IPLink
from ICO3Utilities.Debug.LogDebug import ICO3Log
from ICO3Utilities.Xml.XmlProcess import XmlProcessing


class ICO3IPListenerConnectionManager(ICO3ConnectionManager):
    theTargetList = None
    theSocketAddress = None
    theAddressFamily = None
    theListener = None

    def installParameters(self, xPrm):
        super().installParameters(xPrm)
        self.theTargetList = []
        self.theSocketAddress = XmlProcessing.getAttributeValue(xPrm, "ConnectionSocket")
        self.theAddressFamily = XmlProcessing.getAttributeValue(xPrm, "AddressFamily")
        if (self.theAddressFamily is None):
            self.theAddressFamily = "InterNetwork"
        TargetPrm = XmlProcessing.getTagElement(self.XmlParameters, "TargetList")
        if TargetPrm is None:
            return

        xTargetDevicePrmList = XmlProcessing.getAllTagElementList(TargetPrm)
        if xTargetDevicePrmList is None:
            return

        for xTD in xTargetDevicePrmList:
            TGD = ICO3IPTargetID()
            TGD.installParameters(xTD)
            TGD.theConnectionManager = self
            self.theTargetList.append(TGD)
        return

    def startConnection(self):
        self.StarListener()

    def stopConnection(self):
        self.stopListener()
        super().stopConnection()
        pass

    def stopListener(self):
        self.theListener.stopSocketListenning()
        pass

    def StarListener(self):
        xSTh = ICO3IPDeviceListener()
        xSTh.theConnectionManager = self
        xSTh.setBindAddress(ICO3IPTargetID.getIPAddress(self.theSocketAddress))
        xSTh.run()
        self.theListener = xSTh
        return

    def createLink(self, xSocket):
        ICO3Log.print("Connection","Create Link Listener--->" + str(xSocket.getpeername()))
        xLink = ICO3IPLink()
        xLink.theMode = "NODE"
        xLink.theSocket = xSocket
        xLink.theConnectionManager = self
        xLink.theIdentificationMode = "LISTENER"
        self.installLink(xLink)
        pass


class ICO3IPTargetID:
    connectionSocket = None
    typeConnection = None
    nodeConnection = None
    theConnectionManager = None
    theIPSocket = None
    theLinkSocket = None
    SockAddConnect = None


    def installParameters(self, xPrm):
        self.connectionSocket = XmlProcessing.getAttributeValue(xPrm, "ConnectionSocket")
        self.typeConnection = XmlProcessing.getAttributeValue(xPrm, "type")
        self.nodeConnection = XmlProcessing.getAttributeValue(xPrm, "Node")
        pass

    @staticmethod
    def getIPAddress(SAddress):
        if not isinstance(SAddress, str):
            return None
        xSplit = SAddress.split(":")
        return (xSplit[0], int(xSplit[1]))


class ICO3IPDeviceListener():

    BindAddress = None
    theConnectionManager = None
    Running = False
    theIPSocketListener = None


    def setBindAddress(self, xBind):
        self.BindAddress = xBind

    def run(self):
        self.Running = True
        LTread = Thread( target = self.SocketListener)
        LTread.start()

    def stopSocketListenning(self):
        print ("Stop Socket Listener")
        self.Running = False
        if self.theIPSocketListener is not None:
            self.theIPSocketListener.close()

    def SocketListener(self):
        try:
            self.theIPSocketListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.theIPSocketListener.bind(self.BindAddress)
            ICO3Log.print("Connection","Start Listener @ " + str(self.BindAddress))
            self.theIPSocketListener.listen(10)
        except Exception as e:
            ICO3Log.print("Connection","ICO3IPListenerConnectionManager Socket  "+str(e))
            if self.theIPSocketListener is not None:
                self.theIPSocketListener.close()
                self.theIPSocketListener = None
            return
        while self.Running:
            xConn = self.SocketListenerAcceptloop()
            ICO3Log.print("Connection","*************** Accept Loop Listener **********")
            if xConn is not None:
                if self.theConnectionManager is not None:
                    self.theConnectionManager.createLink(xConn)
        ICO3Log.print("Connection","Stop Socket Listener ")
        if self.theIPSocketListener is not None:
            self.theIPSocketListener.close()
            self.theIPSocketListener = None
        pass


    def SocketListenerAcceptloop(self):
        try:
            conn, addr = self.theIPSocketListener.accept()  # Should be ready
            ICO3Log.print("Connection",'New connection from ' + str(addr))
            return conn
        except Exception as e:
            ICO3Log.print("Connection","ICO3IPListenerConnectionManager Accept  "+str(e))
            return None

