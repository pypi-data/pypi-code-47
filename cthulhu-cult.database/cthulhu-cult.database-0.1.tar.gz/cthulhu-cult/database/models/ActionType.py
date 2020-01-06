from sqlalchemy import Column, Integer, String
from database.models.common.Model import Model
from database.services.DbService import Base


class ActionType(Model, Base):
    HIDE = 'hide'
    SEIZURE = 'seizure'
    EXTORTION = 'extortion'
    SHOPPING = 'shopping'
    HARVEST = 'harvest',
    TRANSFER = 'transfer'
    RAID = 'raid'
    ATTACK = 'attack'
    TYPES = [
        HIDE,
        SEIZURE,
        EXTORTION,
        SHOPPING,
        HARVEST,
        TRANSFER,
        RAID,
        ATTACK
    ]

    __tablename__ = 'action_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def get_id(self):
        return self.id

    def set_name(self, value):
        Model.validate_set_property(value, 'name', str, ActionType.TYPES)
        self.name = value
        return self

    def get_name(self):
        return self.name
