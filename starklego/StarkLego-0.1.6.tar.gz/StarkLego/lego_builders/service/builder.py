from ldraw.library.parts.others import Brick2X2
from ldraw.pieces import Group, Piece
from ldraw.figure import Vector
from ldraw.geometry import Identity
from ldraw.library.colours import Dark_Blue
import numpy as np
from StarkLego.lego_builders.model.dimensions import StarkDimensions
from StarkLego.lego_builders.model.blocks import TwoXTwoBlock



class LegoWorld():
    def __init__(self, x=4, y=3, z=4):
        self.group = Group()
        self.ldraw_content = ""
        self.world_dimensions= StarkDimensions(x, y, z)
        self.content = np.zeros([x,y,z])
        self.number_of_pieces_placed = 0
        self.y_offset_reference = np.zeros([x,z])
        self.y_global_max = 0
    
    def reset(self):
        self.content = np.zeros([self.world_dimensions.x,self.world_dimensions.y,self.world_dimensions.z])
        self.ldraw_content = ""
        self.number_of_pieces_placed = 0
        self.yMy_offset_referenceap = np.zeros([self.world_dimensions.x, self.world_dimensions.z])
        self.y_global_max = 0
        
    def find_maximum_y_value_in_world(self, part, x, y, z):
        y_global_max = 0
        y_offset = 0
        for i in range(part.dimensions.x):
            for j in range(part.dimensions.z):
                restart = True
                while restart == True:
                    y_offset = int(self.y_offset_reference[x + i,z + j])
                    y_local_max= int(self.y_offset_reference[x + i,z + j])
                    restart = False
                    for k in range(part.dimensions.y+1):
                        if self.content[ x + i, y_offset + k, z + j] == 1:
                            if y_local_max <= y_offset+k:    
                                y_local_max += 1
                                self.y_offset_reference[x + i, z + j] = y_local_max
                                restart = True  
                    if y_local_max > y_global_max:
                        y_global_max = y_local_max
                    if y_global_max > self.y_global_max:
                        self.y_global_max = y_global_max
        return y_global_max         

    def add_part_to_world(self, part, x, z):
        x = int(x)
        z = int(z)
        y = 0
        y = self.find_maximum_y_value_in_world(part, x, y, z)
        for i in range(part.dimensions.x):
            for j in range(part.dimensions.y):
                for k in range(part.dimensions.z):
                    self.content[x+i,y+j,z+k] = 1           
        self.number_of_pieces_placed += 1
        partToAdd = part.create(x, y, z, self.group)
        self.append_to_ldr_file(partToAdd)

    def append_to_ldr_file(self, newLine):
        self.ldraw_content += newLine + "\n"



