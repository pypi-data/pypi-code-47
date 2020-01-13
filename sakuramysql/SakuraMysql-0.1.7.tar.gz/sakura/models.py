from .exception import SakuraException
from .meta import ModelMetaclass
from .log import logger


class Model(metaclass=ModelMetaclass):

    def __init__(self, **kw):
        self.values = kw
        self.modify = False

    def __getattr__(self, key):
        try:
            if key in self.fields:
                return self.fields[key].convert(self.values[key])  # .value()
            else:
                return self.__dict__[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no field '%s'" % key)

    def __setattr__(self, key, value):
        if key in self.fields:
            self.modify = True
            self.values[key] = value
        else:
            self.__dict__[key] = value

    def __repr__(self):
        s = [f'{k}({self.fields[k].field_type}):{v}' for k,v in self.values.items()]
        return '\n'.join(s)

    def Create(self):
        field_value = dict(self.values)
        id = self.connection.insert(self.__class__, field_value)
        self.values[self.primary_key] = id

    def Update(self):
        if not self.modify:
            return
        if self.primary_key not in self:
            raise SakuraException('primary key is empty')
        cond = [[
            [self.primary_key, '=', self.values[self.primary_key]]
        ]]
        field_value = dict(self.values)
        field_value.pop(self.primary_key)
        return self.connection.update(self.__class__, field_value, cond)

    def Delete(self):
        if self.primary_key not in self:
            raise SakuraException('primary key is empty')
        cond = [[
            [self.primary_key, '=', self.values[self.primary_key]]
        ]]
        return self.connection.delete(self.__class__, cond)

    def Get(self):
        cond = [[
            [k, '=', v] for k, v in self.values.items()
        ]]
        info = self.connection.select_one(self.__class__, cond)
        self.values.update(info.values)

    @classmethod
    def Fetch(cls, cond=None, group_by=None, order_by=None, limit=100, fields=None):
        return cls.connection.select(cls, cond, group_by, order_by, limit, fields)
