import sys
import uuid

from ICO3Core.Node import ICO3LocalNode
from ICO3Utilities.Xml.XmlProcess import XmlProcessing

Argv = sys.argv
if (len(Argv) > 2):
    print(str(Argv))
else:
    exit()

XmlRoot = XmlProcessing.process(Argv[2],"ICO3Node" )
if (XmlRoot == None):
    print("XML ERROR --> Exit()")
    exit()

theNode = ICO3LocalNode.ICO3LocalNode.create(XmlRoot)
if(theNode == None):
    print( "Cannot Create Main Node")
    exit()
theNode.installParameters()
print( "Node Installed")

theNode.start()

XmlRoot1 = XmlProcessing.process("MongoDBClient.xml","ICO3Node" )
theNode1 = ICO3LocalNode.ICO3LocalNode.create(XmlRoot1)

NPElement = XmlProcessing.getTagElement(XmlRoot, "ICO3NodeParameters")
NPName = XmlProcessing.getAttributeValue(NPElement, "Name")
NPNodeID = XmlProcessing.getAttributeValue(NPElement, "NodeID")
NPNodeMode = XmlProcessing.getAttributeValue(NPElement, "NodeMode")
NPNodeSN = XmlProcessing.getAttributeValue(NPElement, "NodeSN")
NodeUUID = None
if(NPNodeSN != None):
    NodeUUID = uuid.UUID(NPNodeSN)
print( "Create Node Name="+str(NPName)+"  ID="+str(NPNodeID+"  Mode="+str(NPNodeMode+"  SN="+str(NodeUUID))))
TestUUID = uuid.UUID("35a81b1a-c3ac-4ee9-9803-ccf649b31007")
if(NodeUUID == TestUUID):
    print("Hourra ->"+ str(TestUUID))