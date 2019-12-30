from ldraw.library.parts.others import Brick2X2
from ldraw.pieces import Group, Piece
from ldraw.figure import Vector
from ldraw.geometry import Identity
from ldraw.library.colours import Dark_Blue
from StarkLego.lego_builders.model.dimensions import StarkDimensions, LdrawDimensions

class StarkBlock():
    def __init__(self, coor_x, coor_y, coor_z, block_instance=None):
        print("block_instance", block_instance)
        self.dimensions = StarkDimensions(block_instance.dimensions.x, block_instance.dimensions.y, block_instance.dimensions.z)
        self.coordinates = StarkDimensions(float(coor_x), float(coor_y),
                                            float(coor_z), flag_convert_from_ldraw=True)
        self.block_instance = block_instance
        
    def __repr__(self):
        return "Dimensions: ({}, {}, {}), Coordinates: ({}, {}, {})".format(
                        self.dimensions.x, self.dimensions.y, self.dimensions.z,
                        self.coordinates.x, self.coordinates.y, self.coordinates.z)

class LdrawBlock():
    def __init__(self, dim_x, dim_y, dim_z, coor_x, coor_y, coor_z):
        self.dimensions = LdrawDimensions(dim_x, dim_y, dim_z)

        self.coordinates = LdrawDimensions(float(coor_x), float(coor_y), 
                                            float(coor_z), flag_convert_from_stark=True)
    def __repr__(self):
        return "Dimensions: ({}, {}, {}), Coordinates: ({}, {}, {})".format(
                        self.dimensions.x, self.dimensions.y, self.dimensions.z,
                        self.coordinates.x, self.coordinates.y, self.coordinates.z)

class TwoXTwoBlock():
    def __init__(self):
        self.dimensions = StarkDimensions(x=2, y=3, z=2)

    def create(self, x, y, z, group=Group()):
        positionDimensions = StarkDimensions(x=x, y=y, z=z)
        convertedX, convertedY, convertedZ = positionDimensions.convertToLdrDimensions(x,y,z)
        return Piece(Dark_Blue, Vector(x=convertedX, y=convertedY, z=convertedZ), Identity(), Brick2X2, group).__repr__()