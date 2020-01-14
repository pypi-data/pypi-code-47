#!/usr/bin/env python3

from DataStructures.OsmObject import OsmObject
from DataStructures.Node import Node

class Way(OsmObject):
    """ Represents an OSM way node.

    Args:
        id(str): Identifies the way object
        nodes(list<Node>): List of node objects the way is made of
        attributes(Dict): Dictionary containing the attributes of the way object

    Attributes:
        id(str): Identifies the way object
        nodes(list<Node>): List of node objects the way is made of
        attributes(Dict): Dictionary containing the attributes of the way object

    """
    def __init__(self,id, nodes, attributes):
        super().__init__(id, attributes)

        if nodes is None:
            raise TypeError("The nodes property may not be None")
        if not all(isinstance(node, Node) for node in nodes):
            raise TypeError("The nodes property may only contain Node objects")
        if len(nodes) <= 1:
            raise ValueError("A way must have at least 2 Nodes")
        
        self.nodes = nodes
