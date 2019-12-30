from .lib.solar_production_pb2 import Status

class Default:
    channel = "/SolarPowerProduction"
    rpcURL = "127.0.0.1:5555"

class State:
    CONNECTED = Status.CONNECTED
    DISCONNECTED = Status.DISCONNECTED

    def getLocals(self):
        return globals()
