import importlib
import inspect
from abc import abstractmethod

from ICO3Plugin.Message import ICO3Message, ICO3MessageHeader
from ICO3Plugin.Plugin.ICO3AppParameter import ICO3TaskExtraParameterManager
# from ICO3PluginCollection.MessageView.MessageFramePlugin import MessageFramePlugin
from ICO3Utilities.Debug.LogDebug import ICO3Log


class ICO3Plugin(ICO3TaskExtraParameterManager):
    thePlugInParameters = None
    theModuleMaster = None
    theMainFrame = None

    def __init__(self, xMainFrame = None,  XY = None) :
        pass


    # AppName = None
    # Mode = None
    # Description = None
    # File = None
    # Class = None
    # Import = None

    @staticmethod
    def instanciatePlugin(module_name, class_name, xMainFrame, xPosition = None):
        instance = None
        try:
            module = importlib.import_module(module_name)
            xx = inspect.getmembers(module, inspect.isclass)
            class_ = getattr(module, class_name)
            # if issubclass(class_, ICO3FramePlugin) :
            instance = class_(xMainFrame, xPosition)
            # else :
            #     instance = class_()
            return instance
        except Exception as e:
            ICO3Log.print("Plugin","***ERROR****  " +module_name+" "+  class_name + " "+ str(e) )
        return None

    def createMessageHeader(self, xTarget):
        XLP = self.nodeWayProcessing(xTarget)
        return ICO3MessageHeader.ICO3MessageHeader.parseFromString(XLP)

    def sendMessageToTarget(self, xTarget, xMsg):
        xTargetTest = self.getTaskParameterFlat(xTarget)
        if xTargetTest is not None:
            if xTargetTest.Target is not None:
                theSenderHeader = self.createMessageHeader(xTargetTest.Target)
                return self.createSendMessageCheck(theSenderHeader, xMsg)
        return -1

    def sendMessageTo(self, xAddr, xMsg):
        if xAddr is not None:
            theSenderHeader = self.createMessageHeader(xAddr)
            return self.createSendMessageCheck(theSenderHeader, xMsg)
        return -1
        pass

    def sendMessage(self, xMsg):
        return self.theModuleMaster.sendMessage(xMsg)

    def sendMessageCheck(self, xMsg):
        return self.theModuleMaster.sendMessageCheck(xMsg)

    def createSendMessageCheck(self, xHeader,  xMsg):
        xxMsg = ICO3Message.ICO3Message.createMessage(xHeader, xMsg)
        return self.theModuleMaster.sendMessageCheck(xxMsg)

    def installTaskEvent(self, xTaskEvent):
        try:
            if self.theModuleMaster is None:
                return
            self.theModuleMaster.installTaskEvent(xTaskEvent)
            return
        except:
            return

    def getXYExtention(self, XYPos):
        if XYPos is None:
            return "+0+0"
        try:
            xS, yS = XYPos.split(",")
        except:
            return "+0+0"
        xSint = 0
        ySint = 0
        try:
            xSint = int(xS)
        except:
            pass
        try:
            ySint = int(yS)
        except:
            pass
        try:
            return "+"+ str(xSint) +"+"+ str(ySint)
        except Exception as err:
            ICO3Log.print("Plugin",err.with_traceback())
            pass

        return "+0+0"

    def createInstallTaskEventFromTask(self, xTargetName, xCallBack):
        xTargetTest = self.getTaskParameterFlat(xTargetName)
        try:
            if xTargetTest is not None:
                xReceiverPort = xTargetTest.Port
                return self.createInstallTaskEvent(xReceiverPort, xCallBack)
        except:
            pass
        return None

    def createInstallTaskEvent(self, Port, xCallBack):
        try:
            if self.theModuleMaster is None:
                return
            xTaskEvent = ICO3MessageEvent.createEvent(Port, xCallBack)
            self.theModuleMaster.installTaskEvent(xTaskEvent)
            return xTaskEvent
        except:
            return None


    def removeTaskEvent(self, xTaskEvent):
        try:
            if self.theModuleMaster is None:
                return
            self.theModuleMaster.removeTaskEvent(xTaskEvent)
            return
        except:
            return

    def removeMe(self):
        self.theModuleMaster.removeThisPlugin(self)
        pass

    def setMainFrame(self, xMF):
        self.theMainFrame = xMF

    def RTCLoop(self, xCount):
        return

    def MainLoopProcess(self):
        pass

    @abstractmethod
    def initPlugin(self, Argvs):
        pass

    @abstractmethod
    def startPlugin(self):
        pass

    @abstractmethod
    def stopPlugin(self):
        pass


class ICO3MessageEvent:
    TasKID = None
    CallBack = None

    def getTaskID(self):
        return self.TaskID;

    def sendMessage(self, Msg):
        if self.CallBack is not None:
            return self.CallBack(Msg)
        return -1

    @staticmethod
    def createEvent( port, xCallCack):
        try:
            xtheTaskEvent = ICO3MessageEvent()
            xtheTaskEvent.CallBack = xCallCack
            if isinstance(port, int):
                xtheTaskEvent.TasKID = port
            else:
                xtheTaskEvent.TasKID = int(port)
            return xtheTaskEvent
        except:
            return None

class PlugInTest(ICO3Plugin):

    def initPlugin(self, Argvs):
        pass


    def startPlugin(self):
        pass


    def stopPlugin(self):
        pass

    def MainLoopProcess(self):
        pass


if __name__ == '__main__':
    thePLGTest = PlugInTest()
    ICO3Log.print("Plugin","its Done")
