import turtle, time
from KaraPy.Enums import *
from KaraPy.KaraBrain import State, Transition

class World:
    
    def getKara(self):
        return self.Kara
    
    def getFacing(self):
        return self.facing
    
    def getKaraPos(self):
        return self.KaraPos
    
    def getSize(self):
        return (int(self.width/self.mesh), int(self.height/self.mesh))

    def __init__(self,  meshSize, size, sp = 0.5, _title=""):
        self.width, self.height = size
        self.height = self.height * 50 * meshSize
        self.width = self.width * 50 * meshSize
        self.mesh =  1 * 50 * meshSize 
        self.world = []
        self.worldType = []
        self.availableT = []
        self.title = _title
        self.States = []
        self.Kara = False
        self.KaraPos = (0,0)
        if sp >= 0 and sp <= 1:
            self.speed = 1.1 - sp 
        else:
            print("<KaraPy>Speed value must be between 0 and 1! \nDefaulted it to 0.5")
            self.speed = 0.5

    def build(self):
        self.canvas = turtle.Screen()
        #canvas.bgpic("logo.gif")
        self.canvas.setup(width=self.width + 100, height=self.height + 100)
        self.canvas.screensize(self.width , self.height)
        self.canvas.bgcolor("lightgreen")
        self.canvas.title("Kara Python version 0.2 " + self.title )
        t = turtle.Turtle()
        t.speed(10)
        t.hideturtle()
        t.penup()
        t.goto( self.width/2 * -1, self.height/2 * -1 )
        t.pendown()
        t.goto(self.width/2, self.height/2 * -1)
        t.goto(self.width/2, self.height/2)
        t.goto(self.width/2 * -1, self.height/2)
        t.goto(self.width/2 * -1, self.height/2 * -1)
        self.drawMesh(t)
        for w in range(int(self.width/self.mesh)):
            self.world.insert(w, [])
            self.worldType.insert(w, [])
            for h in range(int(self.height/self.mesh)):
                self.world[w].insert(h,None)  
                self.worldType[w].insert(h, "N")
        time.sleep(self.speed)
                
    def drawMesh(self , t):
        t.speed(1000)
        w = 0
        while w < self.width/2:
            t.setx(t.position()[0] + self.mesh)
            t.sety(t.position()[1] * -1)
            w = w + self.mesh/2
        t.penup()
        t.goto(self.width/2 * -1, self.height/2 * -1)
        t.pendown()

        h = 0
        while h < self.height/2:
            t.sety(t.position()[1] + self.mesh)
            t.setx(t.position()[0] * -1)
            h = h + self.mesh/2 

    def Place(self, tile, pos):
        x,y = pos
        if x < self.width/self.mesh and y < self.height/self.mesh and x >= 0 and y >= 0 :  
            if self.world[x][y] == None:
                xa = x * self.mesh - self.width/2  + self.mesh/2
                ya = y * self.mesh - self.height/2 + self.mesh/2
        
                if tile == Type.Tree:
                    t = turtle.Turtle()
                    t.shape("square")
                    t.shapesize((self.mesh - 10) /25)
                    t.color("brown")
                    t.penup()
                    t.speed(100)
                    t.goto(xa, ya)
                    self.world[x][y] = t
                    self.worldType[x][y] = "T"
                if tile == Type.Leaf:
                    t = turtle.Turtle()
                    t.shape("circle")
                    t.shapesize((self.mesh - 10) /25)
                    t.color("darkgreen")
                    t.penup()
                    t.speed(100)
                    t.goto(xa, ya)
                    self.world[x][y] = t
                    self.worldType[x][y] = "L"
                if tile == Type.Kara:
                    if not self.Kara:
                        t = turtle.Turtle()
                        t.shape("turtle")
                        t.shapesize((self.mesh - 10) /30)
                        t.color("#750000")
                        t.penup()
                        t.hideturtle()
                        t.goto(xa, ya)
                        t.showturtle()
                        self.facing = Facing.Right
                        self.KaraPos = (x,y)
                        self.Kara = True
                        self.KaraObj = t
                        
                    else:
                        print("<KaraPy>There is already one Kara in the world")
            elif self.worldType[x][y] == "L" and tile == Type.Kara:
                xa = x * self.mesh - self.width/2  + self.mesh/2
                ya = y * self.mesh - self.height/2 + self.mesh/2
                if not self.Kara:
                    t = turtle.Turtle()
                    t.shape("turtle")
                    t.shapesize((self.mesh - 10) /30)
                    t.color("red")
                    t.penup()
                    t.hideturtle()
                    t.goto(xa, ya)
                    t.showturtle()
                    self.facing = Facing.Right
                    self.KaraPos = (x,y)
                    self.Kara = True
                    self.KaraObj = t
                else:
                    print("<KaraPy>There is already one Kara in the world")
            else:
                print("<KaraPy>There is already an Object")
        else:
            print("<KaraPy>Position out of Grid")

    def getWorldArray(self):
        return self.worldType

    def Move(self, move):
        global Kara, facing, world, KaraPos , speed, width, height, mesh, worldType, KaraObj, availableT
        x,y = self.KaraPos
        if self.Kara:
            if move == Move.Go:
                if self.facing == Facing.Right:
                    if not (x == self.width/self.mesh -1):
                        o = self.worldType[x + 1][y]
                        if o == "T":
                            print("<KaraPy>Kara can not walk there is a tree in front of her.")
                        else:
                            xa = (x +1) * self.mesh - self.width/2  + self.mesh/2
                            ya = y * self.mesh - self.height/2 + self.mesh/2
                            self.KaraPos = (x+1 , y)
                            self.KaraObj.goto(xa, ya)
                    else:
                        o = self.worldType[0][y]
                        if o == "T":
                            print("<KaraPy>Kara can not walk there is a tree in front of her.")
                        else:
                            xa = 0 * self.mesh - self.width/2  + self.mesh/2
                            ya = y * self.mesh - self.height/2 + self.mesh/2
                            self.KaraPos = (0 , y)
                            self.KaraObj.goto(self.width/2 , ya)
                            self.KaraObj.hideturtle()
                            self.KaraObj.goto(self.width/2 * -1, ya)
                            self.KaraObj.showturtle()
                            self.KaraObj.goto(xa, ya)

                if self.facing == Facing.Left:
                    if not (x == 0):
                        o = self.worldType[x - 1][y]
                        if o == "T":
                            print("<KaraPy>Kara can not walk there is a tree in front of her.")
                        else:
                            xa = (x - 1) * self.mesh - self.width/2  + self.mesh/2
                            ya = y * self.mesh - self.height/2 + self.mesh/2
                            self.KaraPos = (x - 1 , y)
                            self.KaraObj.goto(xa, ya)
                    else:
                        o = self.worldType[int(self.width/self.mesh - 1)][y]
                        if o == "T":
                            print("<KaraPy>Kara can not walk there is a tree in front of her.")
                        else:
                            xa = int(self.width/self.mesh - 1) * self.mesh - self.width/2  + self.mesh/2
                            ya = y * self.mesh - self.height/2 + self.mesh/2
                            KaraPos = (int(self.width/self.mesh - 1) , y)
                            self.KaraObj.goto(self.width/2 * -1, ya)
                            self.KaraObj.hideturtle()
                            self.KaraObj.goto(self.width/2, ya)
                            self.KaraObj.showturtle()
                            self.KaraObj.goto(xa, ya)

                if self.facing == Facing.Up:
                    if not (y == self.height/self.mesh -1):
                        o = self.worldType[x][y + 1]
                        if o == "T":
                            print("<KaraPy>Kara can not walk there is a tree in front of her.")
                        else:
                            xa = x * self.mesh - self.width/2  + self.mesh/2
                            ya = (y + 1) * self.mesh - self.height/2 + self.mesh/2
                            self.KaraPos = (x , y + 1)
                            self.KaraObj.goto(xa, ya)
                    else:
                        o = self.worldType[x][0]
                        if o == "T":
                            print("<KaraPy>Kara can not walk there is a tree in front of her.")
                        else:
                            xa = x * self.mesh - self.width/2  + self.mesh/2
                            ya = 0 * self.mesh - self.height/2 + self.mesh/2
                            self.KaraPos = (x , 0)
                            self.KaraObj.goto(xa, self.height/2)
                            self.KaraObj.hideturtle()
                            self.KaraObj.goto(xa, self.height/2 * -1)
                            self.KaraObj.showturtle()
                            self.KaraObj.goto(xa, ya)

                if self.facing == Facing.Down:
                    if not (y == 0):
                        o = self.worldType[x][y - 1]
                        if o == "T":
                            print("<KaraPy>Kara can not walk there is a tree in front of her.")
                        else:
                            xa = x * self.mesh - self.width/2  + self.mesh/2
                            ya = (y - 1) * self.mesh - self.height/2 + self.mesh/2
                            self.KaraPos = (x , y - 1)
                            self.KaraObj.goto(xa, ya)
                    else:
                        o = self.worldType[x][int(self.height/self.mesh -1)]
                        if o == "T":
                            print("<KaraPy>Kara can not walk there is a tree in front of her.")
                        else:
                            xa = x * self.mesh - self.width/2  + self.mesh/2
                            ya = int(self.height/self.mesh - 1) * self.mesh - self.height/2 + self.mesh/2
                            self.KaraPos = (x , int(self.height/self.mesh - 1))
                            self.KaraObj.goto(xa, self.height/2 * -1)
                            self.KaraObj.hideturtle()
                            self.KaraObj.goto(xa, self.height/2)
                            self.KaraObj.showturtle()
                            self.KaraObj.goto(xa, ya)

            if move == Move.TurnLeft:
                if self.facing == Facing.Right:
                    self.facing = Facing.Up
                    t = KaraObj
                    t.left(90)
                elif self.facing == Facing.Left:
                    self.facing = Facing.Down
                    t = KaraObj 
                    t.left(90)
                elif self.facing == Facing.Up:
                    self.facing = Facing.Left
                    t = KaraObj
                    t.left(90)
                elif self.facing == Facing.Down:
                    self.facing = Facing.Right
                    t = KaraObj
                    t.left(90)

            if move == Move.TurnRight:
                if self.facing == Facing.Right:
                    self.facing = Facing.Down
                    t = self.KaraObj
                    t.right(90)
                elif self.facing == Facing.Left:
                    self.facing = Facing.Up
                    t = self.KaraObj 
                    t.right(90)
                elif self.facing == Facing.Up:
                    self.facing = Facing.Right
                    t = self.KaraObj
                    t.right(90)
                elif self.facing == Facing.Down:
                    self.facing = Facing.Left
                    t = self.KaraObj
                    t.right(90)
        
            if move == Move.Up:
                o = self.worldType[x][y]
                if o == "L":
                    t = self.world[x][y]
                    t.hideturtle()
                    self.availableT.append(t)
                    self.world[x][y] = None
                    self.worldType[x][y] = "N"
                else:
                    print("<KaraPy>Kara kann kein Kleeblat aufheben wo keins Liegt.")
        
            if move == Move.Down:
                o = self.worldType[x][y]
                if not o == "L":
                    xa = x * self.mesh - self.width/2  + self.mesh/2
                    ya = y * self.mesh - self.height/2 + self.mesh/2
                    if self.availableT.__len__() > 0:
                        t = self.availableT[0]
                        self.availableT.remove(t)
                        t.goto(xa, ya)
                        t.showturtle()
                        self.world[x][y] = t
                        self.worldType[x][y] = "L"
                    else:
                        t = turtle.Turtle()
                        t.hideturtle()
                        t.shape("circle")
                        t.shapesize((mesh - 10) /25)
                        t.color("darkgreen")
                        t.penup()
                        t.goto(xa, ya)
                        t.showturtle()
                        self.world[x][y] = t
                        self.worldType[x][y] = "L"
                    self.KaraObj.goto(xa,ya)
                else:
                    print("<KaraPy>Kara kann kein Kleeblatt hinlegen wo bereits eins liegt.")
        else:
            print("<KaraPy>There is no Kara in the Wolrd")
        time.sleep(self.speed)

    def setSpeed(self, sp):
        if sp >= 0 and sp <= 1:
            	self.speed = 1.1 - sp
        else:
            print("<KaraPy>Speed value must be between 0 and 1! \nDefaulted it to 0.5")
            speed = 0.5
        
    def getSensor(self, sensor):
        x,y = self.KaraPos
        if sensor == Sensor.L:
            o = self.worldType[x][y]
            return o == "L"
        if sensor == Sensor.TF:
            if self.facing == Facing.Right:
                o = self.worldType[x +1][y]
                return o == "T"
            if self.facing == Facing.Left:
                o = self.worldType[x -1][y]
                return o == "T"
            if self.facing == Facing.Up:
                o = self.worldType[x][y + 1]
                return o == "T"
            if self.facing == Facing.Down:
                o = self.worldType[x][y -1]
                return o == "T"
        if sensor == Sensor.TL:
            if self.facing == Facing.Right:
                o = self.worldType[x][y + 1]
                return o == "T"
            if self.facing == Facing.Left:
                o = self.worldType[x][y -1]
                return o == "T"
            if self.facing == Facing.Up:
                o = self.worldType[x + 1][y]
                return o == "T"
            if self.facing == Facing.Down:
                o = self.worldType[x -1][y]
                return o == "T" 
        if sensor == Sensor.TR:
            if self.facing == Facing.Right:
                o = self.worldType[x -1][y]
                return o == "T"
            if self.facing == Facing.Left:
                o = self.worldType[x +1][y]
                return o == "T"
            if self.facing == Facing.Up:
                o = self.worldType[x][y - 1]
                return o == "T"
            if self.facing == Facing.Down:
                o = self.worldType[x][y +1]
                return o == "T"

    def setBrain(self, _States):
        self.States = _States
        
    def Start(self):
        start = None
        for state in self.States:
            if state.getStart():
                start = state
        if not start == None:
            nextstate = start
            while not nextstate == None:
                nextstate = self.execute(nextstate)
            print("<KaraPy>Finished\nClick to close. ")
            self.canvas.exitonclick()

        else:
            print("<KaraPy>You must define a Start State!")
            return

    def execute(self, state):
        ts = state.getTransitions()
        ft = None
        for t in ts:
            ks = t.getConditions()
            this = True
            for k in ks:
                result = self.getSensor(k[0]) == k[1]
                if not result:
                    this = False
            if this:
                ft = t
        if not ft == None:
            out = ft.getOutput()
            for o in out:
                self.Move(o)
            return ft.getNextState()
        else:
            print("<KaraPy>No Condition  matching!")
            return None
        print("<KaraPy>We are not sure what happened please try again.")
        return None
