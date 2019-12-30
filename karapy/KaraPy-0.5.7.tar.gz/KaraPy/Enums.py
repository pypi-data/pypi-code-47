from enum import  Enum

class Type(Enum):
    Leaf = 0
    Tree = 1
    Kara = 2
    
class Move(Enum):
    Go = 0
    TurnRight = 1
    TurnLeft = 2
    Up = 3
    Down = 4

class Facing(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3

class Sensor(Enum):
    TF = 0
    TR = 1
    TL = 2
    L  = 3
