from legimens import Object
from . import interface as ifc

class VisVars(Object):
    name='VisVar'
    def _before_send(self, name, value):
        value, type_= ifc.preprocess_value(value)
        o = {'value': value, 'type': type_}
        return name, o
