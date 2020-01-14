#!/usr/bin/env python3

class OsmObject:
    """ Class to keep track of the ID of subclasses.
    
    Args:
        id(str): Identifies the subclass
        attributes(Dict): Dictionary containing the attributes of the way object

    Attributes:
        id(str): Identifies the subclass
        attributes(Dict): Dictionary containing the attributes of the way object
    """
    def __init__(self,id, attributes):
        if id is None:
            raise TypeError("ID is missing.")
        
        self.id = id
        self.attributes = attributes
