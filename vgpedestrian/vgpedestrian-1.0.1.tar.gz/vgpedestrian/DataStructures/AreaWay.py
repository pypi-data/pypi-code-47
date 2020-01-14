#!/usr/bin/env python3

from shapely import geometry

from DataStructures.Way import Way
from DataStructures.Node import Node


class AreaWay(Way):
    """ Represents an OSM way whose start and final node are the same.

    Args:
        id(str): Identifies the way object
        nodes(list<Node>): List of node objects the way is made of
        attributes(Dict): Dictionary containing the attributes of the way object

    Attributes:
        id(str): Identifies the way object
        nodes(list<Node>): List of node objects the way is made of
        attributes(Dict): Dictionary containing the attributes of the way object
        polygon(Shapely.geometry.Polygon): Shapely polygon in case the way represents an area, None otherwise.
    """
    def __init__(self,id, nodes, attributes):
        super().__init__(id, nodes, attributes)

        if len(nodes) <= 2:
            raise ValueError("The nodes property must contain at least 3 Node objects.")

        self.polygon = None

    def create_polygon(self):
        self.polygon = geometry.Polygon([node.get_coords() for node in self.nodes])
