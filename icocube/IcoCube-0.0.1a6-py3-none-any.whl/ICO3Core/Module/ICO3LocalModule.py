from ICO3Core.Module.ICO3ModulePlugin import ICO3ModulePlugin
from ICO3Plugin.Plugin.ICO3AppParameter import ICO3TaskExtraParameterManager
from ICO3Utilities.Debug.LogDebug import ICO3Log
from ICO3Utilities.Xml.XmlProcess import XmlProcessing


class ICO3LocalModule(ICO3TaskExtraParameterManager):

    theMasterNode = None
    theXmlParameters = None
    thePluginList = None
    theTaskEventList = None
    ModuleName = None
    ModuleID = None
    ModuleMode = None
    theMainFrame = None

    def installModuleParameter(self, prm):
        self.theXmlParameters = prm
        self.ModuleName = XmlProcessing.getAttributeValue(prm, "Name")
        self.ModuleID = XmlProcessing.getAttributeValue(prm, "ModuleID")
        self.ModuleMode = XmlProcessing.getAttributeValue(prm, "ModuleMode")
        ModulePluginPrm = XmlProcessing.getTagElement(self.theXmlParameters, "PluginList")
        self.installPlugin(ModulePluginPrm)
        self.installAllParameters(self.theXmlParameters)

    def installPlugin(self, xmlPluginList):
        PlgList = XmlProcessing.getTagElementList(xmlPluginList, "ICO3PluginApp")
        if self.thePluginList is None:
            self.thePluginList = []
        for PLG in PlgList:
            xPlugin = ICO3ModulePlugin()
            xPlugin.setMainFrame(self.theMainFrame)
            xPlugin.theMasterModule = self
            xPlugin.installAppParameter(PLG)
            xPlugin.InstancePlugin()
          #  xPlugin.theMasterList = self
          #   xPlugin.theMasterManager = self
          #   xPlugin.theModuleMaster = self
            if xPlugin.thePluginInstance is not None:
                self.thePluginList.append(xPlugin)
        return

    def initPluginApp(self):
        if self.thePluginList is None:
            return
        for PLG in self.thePluginList:
            PLG.initPlugin()

    def startPluginApp(self):
        if self.thePluginList is None:
            return
        for PLG in self.thePluginList:
            PLG.startPlugin()

    def RTCLoopPlugin(self, xCount):
        if self.thePluginList is None:
            return
        for PLG in self.thePluginList:
            PLG.RTCLoop(xCount)

    def stopPluginApp(self):
        if self.thePluginList is None:
            return
        for PLG in self.thePluginList:
            PLG.stopPlugin()

    def MainLoopProcess(self):
        if self.thePluginList is None:
            return
        for PLG in self.thePluginList:
            PLG.MainLoopProcess()

    def setMainFrame(self, xMF):
        self.theMainFrame = xMF


    def installTaskEvent(self, xTaskEvent):
        if xTaskEvent is None:
            return
        self.removeTaskEvent(xTaskEvent)
        self.theTaskEventList.append(xTaskEvent)

    def removeTaskEvent(self, xTaskEvent):
        if xTaskEvent is None:
            return
        if self.theTaskEventList is None:
            self.theTaskEventList = []
        xIdx = self.taskEventIndex(xTaskEvent.TasKID)
        if xIdx != -1:
            self.deleteTaskEvent(xIdx)
        pass


    def taskEventIndex(self, xTaskID):
        if self.theTaskEventList is None:
            return -1
        xIdx = 0
        for xTE in self.theTaskEventList:
            if xTE.TasKID == xTaskID:
                return xIdx
            xIdx += 1
        return -1

    def findTaskEvent(self, xTid):
        xIdx = self.taskEventIndex(xTid)
        if xIdx < 0:
            return None
        if xIdx < len(self.theTaskEventList):
            return self.theTaskEventList[xIdx]
        return None

    def deleteTaskEvent(self, xindex):
        if xindex < 0:
            return False
        if xindex < len(self.theTaskEventList):
            del self.theTaskEventList[xindex]
            return True
        return False

    def getModuleID(self):
        if isinstance(self.ModuleID,int):
            return self.ModuleID
        else:
            return int(self.ModuleID)

    def getNode(self):
        return self.theMasterNode

    def sendMessageCheck(self, xMsg):
        xMsg.theMessageHeader.checkMessageHeader(self)
        return self.sendMessage(xMsg)

    def sendMessage(self, xMsg):
        if xMsg.theMessageHeader is None:
            return -1
        if xMsg.theMessageHeader.isModuleOK(self):
            return self.DeliverMessage(xMsg)

        if self.theMasterNode is not None:
            ICO3Log.print("Message","Goto Node to Deliver Message")
            return self.theMasterNode.sendMessage(xMsg)
        ICO3Log.print("Message","No Deliver Message")
        return -1

    def removeThisPlugin(self, xPlugin):
        for PLG in self.thePluginList:
            if PLG.thePluginInstance == xPlugin:
                PLG.thePluginInstance.stopPlugin()
                self.thePluginList.remove(PLG)
                print ("Stop Plugin")
        pass

    def DeliverMessage(self, xMsg):
        ME = self.findTaskEvent(xMsg.theMessageHeader.destinationTaskID)
        if ME is None:
            return -1
        return ME.sendMessage(xMsg)
