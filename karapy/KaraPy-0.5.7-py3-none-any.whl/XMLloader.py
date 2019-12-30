import xml.etree.ElementTree as ET 
from KaraPy.KaraWorld import World
from KaraPy.Enums import *

def LoadWorldFile(source, size=0.5):

    data = open(source)
    tree = ET.parse(data)
    root = tree.getroot()

    sizex = int(root.attrib["sizex"]) 
    sizey = int(root.attrib["sizey"]) 

    
    W = World(meshSize=size,size=(sizex,sizey), sp=0.5, _title="XmlLoaded: " + source)
    W.build()
    
    T = root.find("XmlWallPoints")
    for tree in T.findall("XmlPoint"):
        x =  int(tree.attrib["x"])
        y = sizey - int(tree.attrib["y"]) -1
        W.Place(Type.Tree, (x,y))
    L = root.find("XmlPaintedfieldPoints")
    for leaf in L.findall("XmlPoint"):
        x = int(leaf.attrib["x"])
        y = sizey - int(leaf.attrib["y"]) -1
        W.Place(Type.Leaf, (x,y))
    K = root.find("XmlKaraList")
    k = K.find("XmlKara")
    x = int(k.attrib["x"])
    y = sizey - int(k.attrib["y"]) -1
    f = k.attrib["direction"]
    
    W.Place(Type.Kara, (x,y))

    if f == "0":
        W.Move(Move.TurnLeft)
    if f == "1":
        W.Move(Move.TurnLeft)
        W.Move(Move.TurnLeft)
    if f == "2":
        W.Move(Move.TurnRight)
    return W

def SaveWorldFile(World,Source):
    sizex,sizey = World.getSize()



    ka = World.getKara()
    fac = World.getFacing()
    po = World.getKaraPos()

    data = ET.Element("XmlWorld")
    data.set("sizex", str(sizex))
    data.set("sizey", str(sizey))
    data.set("version", "KaraX 1.0 kara")
    t = ET.SubElement(data, "XmlWallPoints")
    p = ET.SubElement(data, "XmlObstaclePoints")
    k = ET.SubElement(data, "XmlPaintedfieldPoints")
    m = ET.SubElement(data, "XmlKaraList")
    s = ET.SubElement(data, "XmlStreetList")
    if ka:
        kara = ET.SubElement(m, "XmlKara")
        kara.set("direction", str(fac.value))
        kara.set("name", "Kara")
        xk, yk = po
        kara.set("x" , str(xk))
        kara.set("y", str(sizey - yk -1))

    array = []
    a = World.getWorldArray()
    
    for xi in range(0, a.__len__()):
        for yi in range(0,a[xi].__len__()):
            if a[xi][yi] == "T":
                f = ET.SubElement(t, "XmlPoint")
                f.set("x", str(xi))
                f.set("y", str(sizey - yi -1))
                array.append(f)
            if a[xi][yi] == "L":
                f = ET.SubElement(k, "XmlPoint")
                f.set("type", "0")
                f.set("x", str(xi))
                f.set("y", str(sizey - yi -1))
                array.append(f)
        
            


    mydata = ET.tostring(data)
    myfile = open(Source, "wb")
    myfile.write(mydata)
    print(mydata.decode())
    myfile.close()