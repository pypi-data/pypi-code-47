import time
import uuid
from threading import Lock, Thread
from typing import Type

import lxml
from lxml import etree
from lxml.etree import Element

from ICO3Core.Module.ICO3LocalModule import ICO3LocalModule
from ICO3Plugin.ConnectionManager.ICO3ConnectionManager import ICO3ConnectionManager
from ICO3Plugin.Message.ICO3UUID import ICO3UUID
from ICO3Plugin.Plugin.ICO3AppParameter import ICO3TaskExtraParameterManager
from ICO3Utilities.Debug.LogDebug import ICO3Log
from ICO3Utilities.Xml.XmlProcess import XmlProcessing


class ICO3LocalNode(ICO3TaskExtraParameterManager):

    theXmlParan = None
    theModuleList = None
    theConnectionList = None
    theNodeLinkList = None
    theModuleLinkList = None
    theNodeDirectory = None
    theMainFrame = None
    NodeName = None
    NodeID = None
    NodeMode = None
    NodeUUID = None
    mutexNodeLink = None
    RTCPeriod = 0

    connectionModel = ["NetworkListenerConnection",
                       "ModuleListenerConnection",
                       "ModuleManagerConnection",
                       "NetworkInitiatorConnection"]

    @staticmethod
    def create(root):
        ICO3Log.print("Root",str(type(root)));
        try:
            if not (XmlProcessing.checkTag(root, "ICO3Node")):
                return
        except:
            return;
        # if not (isinstance(root, lxml.etree.Element )):
        #     return
        ILN = ICO3LocalNode()
        ILN.theXmlParan = root
        return ILN

    def checkNode(self):
        try:
            if self.NodeID is None:
                return False
            if not isinstance(self.NodeID, int):
                self.NodeID = int(self.NodeID)
            if self.NodeUUID is None:
                return False
            if not isinstance(self.NodeUUID, uuid.UUID):
                self.NodeUUID = uuid.UUID(self.NodeUUID)
            return True
        except:
            return False

    def setupDebug(self):
        DebugPrm = XmlProcessing.getTagElement(self.theXmlParan, "Debug")
        if DebugPrm is None:
            ICO3Log.clearParams()
        else:
            AttDebugPrint = XmlProcessing.getAttributeValue(DebugPrm, "Print")
            ICO3Log.setupParams(AttDebugPrint)

        pass

    def installParameters(self):
        ICO3Log.print("Roots",str(self.theXmlParan))
        NodePrm = XmlProcessing.getTagElement(self.theXmlParan, "ICO3NodeParameters")
        self.installNodeParameter(NodePrm)
        ModulePrm = XmlProcessing.getTagElement(self.theXmlParan, "ModulesList")
        self.installModuleList(ModulePrm)
        ConnectionPrm = XmlProcessing.getTagElement(self.theXmlParan, "ConnectionList")
        self.installConnectionList(ConnectionPrm)
        NodeDirPrm = XmlProcessing.getTagElement(self.theXmlParan, "NodeDirectory")
        self.installNodeDirectory(NodeDirPrm)
        self.installAllParameters(self.theXmlParan)

    def installNodeParameter(self, prm):
        self.NodeName = XmlProcessing.getAttributeValue(prm, "Name")
        self.NodeID = XmlProcessing.getAttributeValue(prm, "NodeID")
        self.NodeMode = XmlProcessing.getAttributeValue(prm, "NodeMode")
        NPNodeSN = XmlProcessing.getAttributeValue(prm, "NodeSN")
        self.NodeUUID = None
        if (NPNodeSN != None):
            self.NodeUUID = uuid.UUID(NPNodeSN)
        xxRTCP = XmlProcessing.getIntegerAttribute(prm, "RTCPeriod")
        if(xxRTCP != None):
            self.RTCPeriod = xxRTCP

    def installModuleList(self, xmlPrm):
        ModulePrm = XmlProcessing.getTagElementList(xmlPrm, "ICO3ModuleParameters")
        for xModuleParam in ModulePrm:
            LM = ICO3LocalModule()
            LM.setMainFrame(self.theMainFrame)
            LM.installModuleParameter(xModuleParam)
            LM.theMasterNode = self
            LM.theMasterManager = self
            self.addModule2List(LM)
        return

    def setMainFrame(self, xMF):
        self.theMainFrame = xMF

    def initNodeSystem(self):
        if self.theModuleList is None:
            return
        for module in self.theModuleList:
            module.initPluginApp()
        return

    def startAllNodePluginApp(self):
        self.mutexNodeLink = Lock()
        if self.theModuleList is not None:
            for module in self.theModuleList:
                module.startPluginApp()
        return

    def RTCLoopPlugin(self, xCount):
        if self.theModuleList is not None:
            for module in self.theModuleList:
                module.RTCLoopPlugin(xCount)
        return

    def startRTCLoopProcess(self):
        if self.RTCPeriod == None:
            return
        if self.RTCPeriod == 0:
            return
        LTread = Thread( target = self.RTCLoopProcess)
        LTread.start()
        pass

    def RTCLoopProcess(self):
        xCount = 0
        if self.RTCPeriod != None:
            while(self.RTCPeriod != 0) :
                time.sleep(self.RTCPeriod/1000)
                self.RTCLoopPlugin(xCount)
                xCount = xCount +1
            pass



    def startAllNodeConnection(self):

        if self.theConnectionList is not None:
            for connect in self.theConnectionList:
                connect.startConnection()
        return


    def stopNodeSystem(self):
        for xModule in self.theModuleList:
            xModule.stopPluginApp()
        for xConMng in self.theConnectionList:
            xConMng.stopConnection()

        self.theModuleList = None
        self.theConnectionList = None
        self.theNodeLinkList = None
        self.theModuleLinkList = None
        pass


    def MainLoopProcess(self):
        if self.theModuleList is None:
            return
        for module in self.theModuleList:
            module.MainLoopProcess()
        return



    def addModule2List(self, xModule):
        if self.theModuleList is None:
            self.theModuleList = []
        for xMdl in self.theModuleList:
            if xMdl.ModuleID  == xModule.ModuleID:
                return -1
        self.theModuleList.append(xModule)
        return 1

    def getModule(self, xMid):
        if self.theModuleList is None:
            self.theModuleList = []
        for xMdl in self.theModuleList:
            if xMdl.ModuleID == str(xMid):
                return xMdl
        return None

    def installConnectionList(self, xmlPrm):
        if self.theConnectionList is None:
            self.theConnectionList = []
        ConnectionPrm = XmlProcessing.getTagElementList(xmlPrm, "ICO3ConnectionParameters")
        if ConnectionPrm is None:
            return
        for xPrm in ConnectionPrm:
            xCM = ICO3ConnectionManager.createConnection(xPrm)
            if xCM is not None:
                xCM.setNodeMaster(self)
                self.theConnectionList.append(xCM)

        return

    def findLink(self, xList, xLink):

        ICO3Log.print("Link","Find Link " + str(len(xList)))
        idx = 0
        for LNK in xList:
            ICO3Log.print("Link","Loop Link ")
            if LNK.isCompatible(xLink):
                return idx
            idx += 1
        return -1

    def addLink(self, xLink):
        self.mutexNodeLink.acquire()
        xRSLT = -1
        if xLink.theMode == "NODE":
            if self.theNodeLinkList is None:
                self.theNodeLinkList = []
            idx = self.findLink(self.theNodeLinkList, xLink)
            if idx == -1:
                ICO3Log.print("Link","Install Node Link ")
                xRSLT = self.theNodeLinkList.append(xLink)

        if xLink.theMode == "MODULE":
            if self.theModuleLinkList is None:
                self.theModuleLinkList = []
            idx = self.findLink(self.theModuleLinkList, xLink)
            if idx == -1:
                xRSLT = self.theModuleLinkList.append(xLink)
        self.mutexNodeLink.release()
        return xRSLT

    def deleteLink(self, xLink):
        xRet = -1
        if xLink.theMode == "NODE":
            if self.theNodeLinkList is None:
                return -1
            self.mutexNodeLink.acquire()
            idx = self.findLink(self.theNodeLinkList, xLink)
            if idx != -1:
                del self.theNodeLinkList[idx]
                xRet = 1
            self.mutexNodeLink.release()

        if xLink.theMode == "MODULE":
            if self.theModuleLinkList is None:
                return -1
            self.mutexNodeLink.acquire()
            idx = self.findLink(self.theModuleLinkList, xLink)
            if idx != -1:
                del self.theModuleLinkList[idx]
                xRet = 1
            self.mutexNodeLink.release()

        return xRet

    def restartTarget(self, xTrg):
        if xTrg is not None:
            if xTrg.theConnectionManager is not None:
                xTrg.theConnectionManager.StartConnectionFromTarget(xTrg)
        pass


    def installNodeDirectory(self, xmlPrm):
        NDirList = XmlProcessing.getTagElementList(xmlPrm, "ICO3NodeDirectoryItem")
        for xND in NDirList:
            theNDir = ICO3NodeDirectoryItem()
            theNDir.installNodeDirectoryParameter(xND)
            self.addNodeDirectory2List(theNDir)
        return

    def addNodeDirectory2List(self, xNode):
        if self.theNodeDirectory is None:
            self.theNodeDirectory = []
        for xMdl in self.theNodeDirectory:
            if xMdl.Name  == xNode.Name:
                return -1
        self.theNodeDirectory.append(xNode)
        return 1

    def getNodeDirectory(self, xNDN):
        try:
            for xND in self.theNodeDirectory:
                if xND.Name == xNDN:
                    return xND
            return None
        except:
            return None

    def CallBack_updateConnection(self, xConnectionLink, xMode):
        pass

    def getWayNodeDirfrom(self, xNDN):
        xND = self.getNodeDirectory(xNDN)
        if xND is None:
            return None
        return xND.getWay()

    def getSNNodeDirfrom(self, xNDN):
        xND = self.getNodeDirectory(xNDN)
        if xND is None:
            return None
        return xND.getNodeSN()


    def getIDNodeDirfrom(self, xNDN):
        xND = self.getNodeDirectory(xNDN)
        if xND is None:
            return None
        return xND.getNodeID()

    def sendMessage(self, xMsg):
        if xMsg is not None:
            if xMsg.theMessageHeader.isNodeOK(self):
                xMID = xMsg.theMessageHeader.destinationModuleID
                xModule = self.getModule(xMID)
                if xModule is not None:
                    return xModule.sendMessage(xMsg)
                return -1
            else:
                if self.theNodeLinkList is not None:
                    for xLink in self.theNodeLinkList:
                        if xMsg.theMessageHeader.isLinkOK(xLink):
                            return xLink.sendMessage(xMsg)

        return -1

    def getICO3NodeID(self):
        xNID = ICO3UUID()
        xNID.longUUID = self.NodeUUID
        xNID.shortID = self.NodeID
        xNID.useLong = None
        return xNID


class ICO3NodeDirectoryItem:
    Name = None
    NodeId = None
    NodeSN = None
    Way = None

    def installNodeDirectoryParameter(self, prm):
        self.theXmlParameters = prm
        self.Name = XmlProcessing.getAttributeValue(prm, "Name")
        self.NodeId = XmlProcessing.getAttributeValue(prm, "NodeID")
        self.NodeSN = XmlProcessing.getAttributeValue(prm, "NodeSN")
        self.Way = XmlProcessing.getAttributeValue(prm, "Way")

    def getWay(self):
        return self.Way.replace("*", str(self.NodeSN))

    def getNodeID(self):
        return str(self.NodeId)

    def getNodeSN(self):
        return str(self.NodeSN)