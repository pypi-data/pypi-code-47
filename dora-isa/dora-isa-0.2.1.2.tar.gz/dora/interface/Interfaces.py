from enum import Enum

class Interfaces(Enum):
    GENERIC = 0
    ZEPPELIN = 1
    JUPYTER = 2

class Interface:

    @staticmethod
    def get_interface(interface, *args, **kargs):

        if (interface is Interfaces.ZEPPELIN):
            from .zeppelin import Zeppelin
            return Zeppelin(*args, **kargs)

        if (interface is Interfaces.JUPYTER):

            from .jupyter import Jupyter
            return Jupyter(*args, **kargs)
        else:

            from .generic import Generic
            return Generic(*args, **kargs)

    def get_interfaces(self):
        return Interfaces