from models.common import Model
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database.services.DbService import Base
from models.AbilityType import AbilityType


class Ability(Model, Base):
    ability_mana = Table('ability_mana', Base.metadata, Column('ability_id', Integer, ForeignKey('ability.id')),
                         Column('mana_id', Integer, ForeignKey('mana.id')))
    __tablename__ = 'ability'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_id = Column(Integer, ForeignKey('ability_type.id'))
    type = relationship("AbilityType")
    cost = relationship("Mana", secondary=ability_mana)
    description = Column(String)
    command = Column(String)

    def get_id(self):
        return self.id

    def set_name(self, value):
        Model.validate_set_property(value, 'name', str)
        self.name = value
        return self

    def get_name(self):
        return self.name

    def set_type_id(self, value):
        Model.validate_set_property(value, 'type_id', int)
        self.type_id = value
        return self

    def get_type_id(self):
        return self.type_id

    def set_type(self, value):
        Model.validate_set_property(value, 'type_id', AbilityType)
        self.type = value
        return self

    def get_type(self):
        return self.type

    def add_cost(self, value):
        self.cost.append(value)
        return self

    def remove_cost(self, value):
        self.cost.remove(value)
        return self

    def set_description(self, value):
        self.description = value
        return self

    def get_description(self):
        return self.description

    def set_command(self, value):
        self.command = value
        return self

    def get_command(self):
        return self.command
