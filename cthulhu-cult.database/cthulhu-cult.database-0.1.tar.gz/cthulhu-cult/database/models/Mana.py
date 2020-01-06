from sqlalchemy import Column, Integer, String
from database.models.common.Model import Model
from database.services.DbService import Base


class Mana(Model, Base):
    __tablename__ = 'mana'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    PASSION = 'passion'
    DEATH = 'death'
    SLEEP = 'sleep'
    TIMESPACE = 'timespace'
    MADNESS = 'madness'

    TYPES = [PASSION, DEATH, SLEEP, TIMESPACE, MADNESS]

    def get_id(self):
        return self.id

    def set_name(self, value):
        Model.validate_set_property(value, 'name', str, Mana.TYPES)
        self.name = value
        return self

    def get_name(self):
        return self.name
