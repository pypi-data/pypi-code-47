#!/usr/bin/env python3

from shapely import geometry

from DataStructures.Way import Way
from DataStructures.Node import Node


class LineWay(Way):
    """ Represents an OSM way with different start and final nodes.

    Args:
        id(str): Identifies the way object
        nodes(list<Node>): List of node objects the way is made of
        attributes(Dict): Dictionary containing the attributes of the way object

    Attributes:
        id(str): Identifies the way object
        nodes(list<Node>): List of node objects the way is made of
        attributes(Dict): Dictionary containing the attributes of the way object
        line(Shapely.geometry.LineString): A line representation of the way object
    """

    def __init__(self, id, nodes, attributes):
        super().__init__(id, nodes, attributes)
        self.line = None

    def create_line(self):
        self.line = geometry.LineString([node.get_coords() for node in self.nodes])
