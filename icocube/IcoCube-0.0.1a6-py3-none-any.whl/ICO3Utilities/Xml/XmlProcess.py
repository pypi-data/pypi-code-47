import uuid
from xml.etree import ElementTree

from lxml import etree
import os

from ICO3Utilities.Debug.LogDebug import ICO3Log


class XmlProcessing:

    @staticmethod
    def process(file, rootTag):
        if (os.path.isabs(file)):
            filePath = file
        else:
            filePath = OptPathFile + file
        if (os.path.isfile(filePath)):
            tree = etree.parse(filePath)
            if (tree != None):
                root = tree.getroot()
                ICO3Log.print("Root",root)
                if (root.tag == rootTag):  # element = XmlProcessing.tree.Element()
                    return root
                return

        ICO3Log.print("Plugin","Error wrong File ->" + filePath)
        return

    @staticmethod
    def checkTag(root, rootTag):
        return (root.tag == rootTag)

    @staticmethod
    def getTagElement(Element, xTagName):
        children = Element.getchildren()
        for child in children:
            if (child.tag == xTagName):
                return child
        return

    @staticmethod
    def getTagElementList(Element, xTagName):
        xList = []
        # xml_str = ElementTree.tostring(Element).decode()
        # ICO3Log.print("Plugin",str(xml_str))
        # children = None
        try:
            children = Element.getchildren()
            for child in children:
                if (child.tag == xTagName):
                    xList.append(child)
        finally:
            return xList

    @staticmethod
    def getAllTagElementList(Element):
        xList = []
        # xml_str = ElementTree.tostring(Element).decode()
        # ICO3Log.print("Plugin",str(xml_str))
        # children = None
        try:
            children = Element.getchildren()
            for child in children:
                xList.append(child)
        finally:
            return xList

    @staticmethod
    def getTagElementListinGroup(Element, xTagName):
        xList = []
        # xml_str = ElementTree.tostring(Element).decode()
        # ICO3Log.print("Plugin",str(xml_str))
        # children = None
        try:
            children = Element.getchildren()
            for child in children:
                if (XmlProcessing.isTagInsideGroup(child.tag, xTagName)):
                    xList.append(child)
        finally:
            return xList

    @staticmethod
    def isTagInsideGroup(xTag, xTagGroup):
        for xRtag in xTagGroup:
            if (xTag == xRtag):
                return True
        return False

    @staticmethod
    def getAttributeValue(Element, AttValue):
        try:
            return Element.attrib[AttValue]
        except:
            return None

    @staticmethod
    def getIntegerAttribute(Element, AttValue):
        try:
            xVL =  Element.attrib[AttValue]
            return int(xVL)
        except:
            return None


    @staticmethod
    def getFloatAttribute(Element, AttValue):
        try:
            xVL =  Element.attrib[AttValue]
            return float(xVL)
        except:
            return None

    @staticmethod
    def getUUIDAttribute(Element, AttValue):
        try:
            xVL =  Element.attrib[AttValue]
            return uuid.UUID(xVL)
        except:
            return None



OptPathFile = "C:/Users/Gilles/Documents/Icocube/"
