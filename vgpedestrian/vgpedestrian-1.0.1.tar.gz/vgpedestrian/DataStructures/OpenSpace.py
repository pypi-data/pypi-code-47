#!/usr/bin/env python3
from shapely import geometry

from DataStructures.Relation import Relation

class OpenSpace(Relation):
    """ This class represents an area navigatable by pedestrians

    Args:
        id(str): Identifies the OpenSpace
        outer_ways(list<Way>): List containing outer members of the OpenSpace, e.g. Ways
        inner_ways(list<Way>): List containing inner members of the OpenSpace, e.g. Ways
        attributes(dict): Dictionary containing key-value-pairs of attributes of the OpenSpace
    Attributes:
        id(str): Identifies the OpenSpace
        outer_ways(list<Way>): List containing outer members of the OpenSpace, e.g. Ways
        inner_ways(list<Way>): List containing inner members of the OpenSpace, e.g. Ways
        attributes(dict): Dictionary containing key-value-pairs of attributes of the OpenSpace
        polygon_with_holes(Shapely.geometry.Polygon): Shapely polygon representing the OpenSpace
    """

    def __init__(self, id, outer_ways, inner_ways, attributes):
        super().__init__(id, outer_ways, inner_ways, attributes)
        self.polygon_with_holes = None

    def create_polygon_with_holes(self):
        """Creates a Shapely.geometry.Polygon object by generating an outer border using outer_ways
        and inner holes by iterating over inner_ways.

        Sets polygon_with_holes to the created Shapely.geometry.Polygon.
        """
        shell = self.concatenate_outer_ways()

        holes = []
        for way in self.inner_ways:
            holes.append([node.get_coords() for node in way.nodes])

        self.polygon_with_holes = geometry.Polygon(shell, holes)
        
    def concatenate_outer_ways(self):
        """Takes all elements of the attribute outer_ways and concatenates them to create one list
           of coordinates.

        Return one list of coordinates based on all outer_ways.
        """
        all_outer_nodes = []
        for area in self.outer_ways:
            all_outer_nodes.extend(area.nodes) 
        return [node.get_coords() for node in all_outer_nodes]
    
