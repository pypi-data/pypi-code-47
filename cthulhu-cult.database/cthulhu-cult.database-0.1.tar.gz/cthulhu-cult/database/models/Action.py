from sqlalchemy import Column, Integer, ForeignKey
from database.models.common.Model import Model
from database.services.DbService import Base
from sqlalchemy.orm import relationship


class Action(Model, Base):
    __tablename__ = 'action'
    id = Column(Integer, primary_key=True)
    match_turn = Column(Integer, ForeignKey('match_turn.id'))
    type_id = Column(Integer, ForeignKey('action_type.id'))
    type = relationship("ActionType")

    def get_id(self):
        return self.id

    def set_type_id(self, value):
        self.type_id = value
        return self

    def get_type_id(self):
        return self.type_id

    def set_type(self, value):
        self.type = value
        return self

    def get_type(self):
        return self.type
