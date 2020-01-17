import selectors
# from threading import Thread
import time
from threading import Thread

from ICO3Plugin.ConnectionManager.ICO3ConnectionManager import ICO3ConnectionManager
from ICO3Plugin.ConnectionManager.ICO3IPLink import ICO3IPLink
from ICO3Utilities.Debug.LogDebug import ICO3Log
from ICO3Utilities.Xml.XmlProcess import XmlProcessing
import socket


class ICO3IPInitiatorConnectionManager(ICO3ConnectionManager):

    theTargetList = None
    theSocketAddress = None


    def installParameters(self, xPrm):
        super().installParameters(xPrm)
        self.theTargetList = []
        self.theSocketAddress = XmlProcessing.getAttributeValue(xPrm, "SocketAddress")
        TargetPrm = XmlProcessing.getTagElement(self.XmlParameters, "TargetList")
        if TargetPrm is None:
            return

        xTargetDevicePrmList = XmlProcessing.getAllTagElementList(TargetPrm)
        if xTargetDevicePrmList is None:
            return



        for xTD in xTargetDevicePrmList:
            TGD = ICO3IPTargetDevice()
            TGD.installParameters(xTD)
            TGD.theConnectionManager = self
            self.theTargetList.append(TGD)
        return

    def startConnection(self):
        print ("I start a connection !!!!!!!!!!! IPInitiator")
        for xTRG in self.theTargetList:
            self.StartConnectionFromTarget(xTRG)

            # xConn = xTRG.startConnection()
            # if xConn is not None:
            #     self.createLink(xConn, xTRG)

    def StartConnectionFromTarget(self, xTarget):
        xConThread = LinkConnectionCreator(self, xTarget)
        xConThread.run()

        # xConn = xTarget.startConnection()
        # if xConn is not None:
        #     self.createLink(xConn, xTarget)
        # else:
        #     ICO3Log.print("Connection","Connection Failed")

    def stopConnection(self):
        super().stopConnection()
        pass

    def getIPSocketAddress(self):
        return self.theSocketAddress

    def createLink(self, xSocket, xTarget):
        ICO3Log.print("Connection","Create Link Initiator --->"  + str(xSocket.getpeername()))
        xLink = ICO3IPLink()
        xLink.theMode = "NODE"
        xLink.theSocket = xSocket
        xLink.theTarget = xTarget
        xLink.theConnectionManager = self
        xLink.theIdentificationMode = "INITIATOR"
        self.installLink(xLink)
        pass

class LinkConnectionCreator():
    theConnectionManager = None
    theTarget = None
    theLoop = False

    def __init__(self, xConManager = None, xTrg = None):
        self.theConnectionManager = xConManager
        self.theTarget = xTrg

    def run(self):
        if self.theConnectionManager is None:
            return
        if self.theTarget is None:
            return
        self.theLoop = True
        LTread = Thread( target = self.SocketConnection)
        LTread.start()
        pass

    def SocketConnection(self):
        while self.theLoop:
            xConn = self.theTarget.startConnection()
            if xConn is not None:
                ICO3Log.print("Connection","Connection Ok Create Link")
                self.theConnectionManager.createLink(xConn, self.theTarget)
                return

            ICO3Log.print("Connection","Connection Failed try again")
            time.sleep(1)

        ICO3Log.print("Connection","End of Loop Connection")



class ICO3IPTargetDevice:
    connectionSocket = None
    theAddressFamily = None;
    typeConnection = None
    nodeConnection = None
    theConnectionManager = None
    theIPSocket = None
    theLinkSocket = None
    SockAddConnect = None
    sel = selectors.DefaultSelector()

    def installParameters(self, xPrm):
        self.connectionSocket = XmlProcessing.getAttributeValue(xPrm, "ConnectionSocket")
        self.theAddressFamily = XmlProcessing.getAttributeValue(xPrm, "AddressFamily")
        if (self.theAddressFamily is None):
            self.theAddressFamily = "InterNetwork"
        self.typeConnection = XmlProcessing.getAttributeValue(xPrm, "type")
        self.nodeConnection = XmlProcessing.getAttributeValue(xPrm, "Node")
        pass

    def startConnection(self):
        try:
            self.theIPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #self.getIPAddress(self.theConnectionManager.getIPSocketAddress())
            self.SockAddBind = self.getIPAddress(self.theConnectionManager.getIPSocketAddress())
            self.theIPSocket.bind(self.SockAddBind)
            self.SockAddConnect = self.getIPAddress(self.connectionSocket)
            self.theIPSocket.connect(self.SockAddConnect)
            ICO3Log.print("Connection","Connection IP OK")
            return self.theIPSocket
        except Exception as e:
            ICO3Log.print("Connection","ICO3IPInitiatorConnectionManager   " + str(e))
            return None

    def getIPAddress(self, SAddress):
        if not isinstance(SAddress, str):
            return None
        xSplit = SAddress.split(":")
        return (xSplit[0], int(xSplit[1]))


