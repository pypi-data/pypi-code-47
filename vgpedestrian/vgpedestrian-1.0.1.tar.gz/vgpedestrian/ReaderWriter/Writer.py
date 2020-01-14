import sys
from xml.dom import minidom
from lxml import etree as ET


class Writer():
    """Writes new osm to the filesystem"""

    def __init__(self, ways):
        self.ways = ways

    def create_single_element(self, way):
        # create element and set attributes
        xml_way = ET.Element('way')
        xml_way.attrib['alg'] = 'vg'  # vg = visbilitygraph
        xml_way.attrib['id'] = way.id


        # create new ref elements for all nodes
        for node in way.nodes:
            new_nd = ET.SubElement(xml_way, 'nd')
            new_nd.attrib['ref'] = node.id

        # Make it navigatable
        pedestrian = ET.SubElement(xml_way, 'tag')
        pedestrian.attrib['k'] = 'highway'
        pedestrian.attrib['v'] = 'pedestrian'

        return xml_way

    def create_elements(self, ways):
        return [self.create_single_element(way) for way in ways]

    def write(self, filepath, new_file):
        """Write the osm / xml file """

        try:
            parser = ET.XMLParser(remove_blank_text=True)
            xml_tree = ET.parse(filepath, parser)
        except FileNotFoundError:
            sys.stderr.write("Filepath for input does not exist\n")
            raise

        way_path = xml_tree.find("way[last()]")
        new_elements = self.create_elements(self.ways)

        try:
            for xml_way in new_elements:
                way_path.addnext(xml_way)
        except AttributeError:
            sys.stderr.write(
                "Appending Element failed, possibly the input file is corrupt\n")
            raise

        try:
            xml_tree.write(new_file, pretty_print=True, encoding="utf-8")
        except Exception as e:
            sys.stderr.write("Writing output file failed\n")
            raise
