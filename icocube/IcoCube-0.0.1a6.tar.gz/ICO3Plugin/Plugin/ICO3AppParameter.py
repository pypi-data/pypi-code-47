from ICO3Plugin.Message.ICO3UUID import ICO3UUID
from ICO3Plugin.Plugin.ICO3NodeWayProcessor import ICO3NodeWayProcessor
from ICO3Utilities.Debug.LogDebug import ICO3Log
from ICO3Utilities.ICO3TokenizerParam import ICO3TokenizerParam
from ICO3Utilities.Xml.XmlProcess import XmlProcessing


class ICO3TaskParameter:
    Name = None
    Mode = None
    Port = None
    Target = None
    Params = None

    def installParameters(self, xPrm):
        self.Name = XmlProcessing.getAttributeValue(xPrm, "Name")
        self.Mode = XmlProcessing.getAttributeValue(xPrm, "Mode")
        self.Port = XmlProcessing.getAttributeValue(xPrm, "Port")
        self.Target = XmlProcessing.getAttributeValue(xPrm, "Target")
        self.Params = XmlProcessing.getAttributeValue(xPrm, "Params")
        return;

class ICO3ExtraParameter:

    Name = None
    Value = None

    def installParameters(self, xPrm):
        self.Name = XmlProcessing.getAttributeValue(xPrm, "Name")
        self.Value = XmlProcessing.getAttributeValue(xPrm, "Value")


class ICO3TaskExtraParameterManager:
    theMasterManager = None

    theInstanceXml = None
    theTaskParametersXml = None
    theExtraParametersXml = None

    theTaskParametersList = None
    theExtraParametersList = None

    def installAllParameters(self, xPrm):
        self.theInstanceXml = xPrm
        self.installTaskParameters(xPrm)
        self.installExtraParameters(xPrm)

    def installTaskParameters(self, xPrm):
        if self.theTaskParametersList is None:
            self.theTaskParametersList = []
        #self.theTaskParametersXml = xPrm

        self.theTaskParametersXml = XmlProcessing.getTagElement(xPrm, "TaskParametersList")
        if(self.theTaskParametersXml == None):
            return;
        XmlList = XmlProcessing.getTagElementList(self.theTaskParametersXml, "ICO3TaskParameter")
        for txParam in XmlList:
            tparam = ICO3TaskParameter()
            tparam.installParameters(txParam)
            self.theTaskParametersList.append(tparam)

    def installExtraParameters(self, xPrm):
        if self.theExtraParametersList is None:
            self.theExtraParametersList = []
        #self.theExtraParametersXml = xPrm

        self.theExtraParametersXml = XmlProcessing.getTagElement(xPrm, "ExtraParametersList")
        if(self.theExtraParametersXml == None):
            return;
        XmlList =  XmlProcessing.getTagElementList(self.theExtraParametersXml, "ICO3ExtraParameter")
        for txParam in XmlList:
            tparam = ICO3ExtraParameter()
            tparam.installParameters(txParam)
            self.theExtraParametersList.append(tparam)

    def getTaskParameterRaw(self, xNM):
        for ITP in self.theTaskParametersList:
            if ITP.Name == xNM:
                return ITP
        if self.theMasterManager is not None:
            return  self.theMasterManager.getTaskParameterRaw(xNM)
        return

    def getExtraParameter(self, xNM):
        for ITP in self.theExtraParametersList:
            if ITP.Name == xNM:
                return ITP
        return None

    def getExtraParameterValue(self, xNM):
        EP = self.getExtraParameter(xNM)
        if EP is None:
            if self.theMasterManager is not None:
                return self.theMasterManager.getExtraParameterValue(xNM)
            return None
        return EP.Value

    def getTaskParameterFlat(self, xNM):
        xTP = self.getTaskParameterRaw(xNM)
        if xTP is None:
            return None
        if xTP.Mode is not None:
            xTP.Mode = self.doTaskParameterItemFlat(xTP.Mode)
        if xTP.Port is not None:
            xTP.Port = self.doTaskParameterItemFlat(xTP.Port)
        if xTP.Target is not None:
            xTP.Target = self.doTaskParameterItemFlat(xTP.Target)
        if xTP.Params is not None:
            xTP.Params = self.doTaskParameterItemFlat(xTP.Params)
        return xTP

    def doTaskParameterItemFlat(self, xTP):
        xTok = ICO3TokenizerParam()
        XR = xTok.processString(xTP, ['@','>',':'])
        for Ti in XR:
            if Ti.TokenType == "STRING":
                try:
                    if Ti.TokenValue[0] == '$':
                        Ti.TokenNew = self.findSubstituteValue(Ti.TokenValue)
                        ICO3Log.print("Plugin",Ti.TokenValue+ "--New-->"+Ti.TokenNew)
                        pass
                except Exception as ex:
                    ICO3Log.print("Plugin","ICO3TaskExtraParameterManager   "+ str(ex))
        RS = xTok.getString(XR)
        return RS

    def findSubstituteValue(self, xTokenValue):
        xVal = xTokenValue.replace("$", "", 1)
        return self.getExtraParameterValue(xVal)
        pass

    def nodeWayProcessing(self, xNwl):
        if xNwl is None:
            return None
        xWL = ICO3NodeWayProcessor.process(xNwl)
        if xWL is not None:
            for xTok in xWL:
                if xTok.TokenType == "STRING":
                    xTok.TokenValue = self.ProcessWayName(xTok.TokenValue)
                    if xTok.TokenValue == None:
                        xTok.TokenValue = ""
            return ICO3TokenizerParam.getString(xWL)
        return xNwl

    def ProcessWayName(self, xNM):
        if xNM is None:
            return xNM
        if len(xNM) < 1:
            return xNM
        if xNM[0] == '>':
            xVL = xNM.replace(">", "", 1)
            return self.getNodeDirWay(xVL)
        else:
            if xNM[0] == '%':
                xVL1 = xNM.replace("%", "", 1)
                return self.getIDNodeDirfrom(xVL1)
            if ICO3UUID.isUUID(xNM):
                return xNM
            if ICO3UUID.isInteger(xNM):
                return xNM

        return self.getSNNodeDirfrom(xNM)

    def getNodeDirWay(self, xNm):
        return self.getWayNodeDirfrom(xNm)

    def getWayNodeDirfrom(self, xNDN):
        if self.theMasterManager is not None:
            return self.theMasterManager.getWayNodeDirfrom(xNDN)
        return None

    def getSNNodeDirfrom(self, xNDN):
        if self.theMasterManager is not None:
            return self.theMasterManager.getSNNodeDirfrom(xNDN)
        return None

    def getIDNodeDirfrom(self, xNDN):
        if self.theMasterManager is not None:
            return self.theMasterManager.getIDNodeDirfrom(xNDN)
        return None