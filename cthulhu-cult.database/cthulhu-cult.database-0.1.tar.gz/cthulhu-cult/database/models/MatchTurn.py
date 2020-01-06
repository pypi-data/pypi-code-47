from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class MatchTurn(Model, Base):
    __tablename__ = 'match_turn'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    actions = relationship("Action")
    match_id = Column(Integer, ForeignKey('match.id'))

    def get_id(self):
        return self.id

    def set_number(self, value):
        Model.validate_set_property(value, 'number', int)
        self.number = value
        return self

    def get_number(self):
        return self.number

    def add_action(self, value):
        self.actions.append(value)
        return self

    def remove_action(self, value):
        self.actions.remove(value)
        return self

    def set_match_id(self, value):
        self.match_id = value
        return self

    def get_match_id(self):
        return self.match_id
