from ICO3Plugin.Plugin import ico3plugin
from ICO3Plugin.Plugin.ico3plugincreator import ICO3PluginCreator

from ICO3Utilities.Xml.XmlProcess import XmlProcessing


class ICO3ModulePlugin():

    thePlugInParameters = None
    AppName = None
    Mode = None
    Description = None
    File = None
    Class = None
    Import = None
    XYPosition = None
    Command = None

    thePluginInstance = None
    theMasterModule = None
    theMainFrame = None

    def installAppParameter(self, prm):
        self.thePlugInParameters = prm
        self.AppName = XmlProcessing.getAttributeValue(prm, "Name")
        self.Mode = XmlProcessing.getAttributeValue(prm, "Mode")
        self.Description = XmlProcessing.getAttributeValue(prm, "Description")
        self.File = XmlProcessing.getAttributeValue(prm, "File")
        self.Import = XmlProcessing.getAttributeValue(prm, "Import")
        self.Class = XmlProcessing.getAttributeValue(prm, "Class")
        self.XYPosition = XmlProcessing.getAttributeValue(prm, "XYPosition")
        self.Command = XmlProcessing.getAttributeValue(prm, "Command")
        return

    def InstancePlugin(self):
        self.thePluginInstance = ICO3PluginCreator.instanciatePlugin(self.Import, self.Class, self.theMainFrame, self.XYPosition)
        if  self.thePluginInstance is not None:
            self.thePluginInstance.theModuleMaster = self.theMasterModule
            self.thePluginInstance.theMasterManager = self.theMasterModule
            self.thePluginInstance.installAllParameters(self.thePlugInParameters)
            self.thePluginInstance.setMainFrame(self.theMainFrame)

    def setMainFrame(self, xMF):
        self.theMainFrame = xMF

    def initPlugin(self):
        if self.thePluginInstance is not None:
            self.thePluginInstance.initPlugin(self.Command)

    def startPlugin(self):
        if self.thePluginInstance is not None:
            self.thePluginInstance.startPlugin()

    def stopPlugin(self):
        if self.thePluginInstance is not None:
            self.thePluginInstance.stopPlugin()

    def RTCLoop(self, xCount):
        if self.thePluginInstance is not None:
            self.thePluginInstance.RTCLoop(xCount)

    def MainLoopProcess(self):
        if self.thePluginInstance is not None:
            self.thePluginInstance.MainLoopProcess()
