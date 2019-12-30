from KaraPy.KaraWorld import World
from KaraPy.Enums import Move, Sensor, Type 
from KaraPy.XMLloader import *
# Kara = World(5)
# Kara.build()
# Kara.Place(Type.Kara, (0, 0))
# Kara.Place(Type.Tree, (4, 0))

# def Walk():
#     if not Kara.getSensor(Sensor.TF):
#         Kara.Move(Move.Go)
#         Walk()
#     else:
#         Kara.Move(Move.TurnLeft)
#         Kara.Move(Move.Down)

# Walk()

W = LoadWorldFile("test.world", 3)
W.setSpeed(1)
def carry1():
    if not W.getSensor(Sensor.TF) and not W.getSensor(Sensor.L):
        W.Move(Move.TurnRight)
        W.Move(Move.Go)
        W.Move(Move.Down)
        W.Move(Move.TurnLeft)
        W.Move(Move.Go)
        W.Move(Move.TurnLeft)
        W.Move(Move.Go)
        W.Move(Move.TurnRight)
        carry1()
    if not W.getSensor(Sensor.TF) and W.getSensor(Sensor.L):
        W.Move(Move.Go)
        carry0()
    if W.getSensor(Sensor.TF) and not W.getSensor(Sensor.L):
         W.Move(Move.TurnRight)
         W.Move(Move.Go)
         W.Move(Move.Down)
         W.Move(Move.TurnRight)
         nextrow()
    if W.getSensor(Sensor.TF) and W.getSensor(Sensor.L):
         W.Move(Move.TurnRight)
         W.Move(Move.Go)
         W.Move(Move.TurnRight)
         nextrow()

def carry0():
    if not W.getSensor(Sensor.TF) and not W.getSensor(Sensor.L):
        W.Move(Move.Go)
        carry0()
    if not W.getSensor(Sensor.TF) and W.getSensor(Sensor.L):
        W.Move(Move.TurnRight)
        W.Move(Move.Go)
        W.Move(Move.Down)
        W.Move(Move.TurnLeft)
        W.Move(Move.Go)
        W.Move(Move.TurnLeft)
        W.Move(Move.Go)
        W.Move(Move.TurnRight)
        carry1()
    if W.getSensor(Sensor.TF) and not W.getSensor(Sensor.L):
         W.Move(Move.TurnRight)
         W.Move(Move.Go)
         W.Move(Move.TurnRight)
         nextrow()
    if W.getSensor(Sensor.TF) and W.getSensor(Sensor.L):
         W.Move(Move.TurnRight)
         W.Move(Move.Go)
         W.Move(Move.Down)
         W.Move(Move.TurnRight)
         nextrow()

def nextrow():
    if not W.getSensor(Sensor.TF) and  not W.getSensor(Sensor.TL):
        W.Move(Move.Go)
        nextrow()
    if W.getSensor(Sensor.TF) and  not W.getSensor(Sensor.TL):
        W.Move(Move.TurnRight)
        W.Move(Move.TurnRight)
        W.Move(Move.Go)
        carry1()
    if W.getSensor(Sensor.TL):
        return

carry1()
s = input()