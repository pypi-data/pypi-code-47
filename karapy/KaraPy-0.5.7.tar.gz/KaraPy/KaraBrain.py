from KaraPy.Enums import Sensor, Move

class State:

    def __init__(self, _Name, _isStart=False):
        self.Name = _Name
        self.isStart = _isStart
        self.Transitions = []

    def AddTransition(self, t):
        self.Transitions.append(t)
        
        

    def getStart(self):
        return self.isStart

    def getTransitions(self):
        return self.Transitions


class Transition:

    def __init__(self, _condition, _output=[], _nextState=None):
        self.condition = _condition
        self.output = _output
        self.nextState = _nextState

    def getConditions(self):
        return self.condition

    def getOutput(self):
        return self.output

    def getNextState(self):
        return self.nextState

