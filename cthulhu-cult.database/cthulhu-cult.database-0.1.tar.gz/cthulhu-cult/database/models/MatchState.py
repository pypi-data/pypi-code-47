from database.models.common.Model import Model
from sqlalchemy import Column, Integer, String
from database.services.DbService import Base


class MatchState(Model, Base):
    __tablename__ = 'match_state'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    SELECTION = 'selection'
    PROGRESS = 'progress'
    CONCLUSION = 'conclusion'

    STATES = [SELECTION, PROGRESS, CONCLUSION]

    def get_id(self):
        return self.id

    def set_name(self, value):
        Model.validate_set_property(value, 'name', str, self.STATES)
        self.name = value
        return self

    def get_name(self):
        return self.name
