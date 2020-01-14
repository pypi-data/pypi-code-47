#!/usr/bin/env python3
from DataStructures.Way import Way
from DataStructures.OsmObject import OsmObject

class Relation(OsmObject):
    """ This class represents a complex OSM Relation node that is an area and navigatable by pedestrians.

    Args:
        id(str): Identifies the Relation
        outer_ways(list<Way>): List containing outer members of the Relation, e.g. Ways
        inner_ways(list<Way>): List containing inner members of the Relation, e.g. Ways
        attributes(dict): Dictionary containing key-value-pairs of attributes of the Relation

    Attributes:
        id(str): Identifies the Relation
        outer_ways(list<Way>): List containing outer members of the Relation, e.g. Ways
        inner_ways(list<Way>): List containing inner members of the Relation, e.g. Ways
        attributes(dict): Dictionary containing key-value-pairs of attributes of the Relation
    """
    def __init__(self, id, outer_ways, inner_ways, attributes):
        super().__init__(id, attributes)

        if outer_ways is None or inner_ways is None:
            raise TypeError("May not be None")
        if not all(isinstance(way, Way) for way in outer_ways):
            raise TypeError("The outer_ways property may only contain Way objects and not be empty")
        if not all(isinstance(way, Way) for way in inner_ways):
            raise TypeError("The inner_ways property may only contain Way objects and not be empty")
        if len(outer_ways) < 1:
            raise ValueError("Must contain at least 1 Way object")
        self.outer_ways = outer_ways
        self.inner_ways = inner_ways
