#!/usr/bin/env python3

from DataStructures.OsmObject import OsmObject

class Node(OsmObject):
    """ Represents an OSM Node node.

    Args:
        id (str): Identifies the node
        lat (str): Latitudinal information of the node
        lon (str): Longitudinal information of the node
        attributes(dict): Dictionary containing key-value-pairs of attributes of the OpenSpace
    Attributes:
        id (str): Identifies the node
        lat (float): Latitudinal information of the node
        lon (float): Longitudinal information of the node
        attributes(dict): Dictionary containing key-value-pairs of attributes of the OpenSpace
    """
    def __init__(self, id, lat, lon, attributes):
        super().__init__(id, attributes)
        
        self.lat = float(lat)
        self.lon = float(lon)

    def get_coords(self):
        """ Returns a tuple consisting of latitude and longitude.
        Returns:
            Set(float, float): tuple of Latitude and longitude
        """
        return (self.lat, self.lon)
