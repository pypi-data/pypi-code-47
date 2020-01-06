from database.models.common.Model import Model
from sqlalchemy import Column, Integer, String
from database.services.DbService import Base


class AbilityType(Model, Base):
    PASSIVE = 'passive'
    ACTIVE = 'active'
    COMBAT_ACTIVE = 'combat_active'
    COMBAT_PASSIVE = 'combat_passive'
    TYPES = [PASSIVE, ACTIVE, COMBAT_ACTIVE, COMBAT_PASSIVE]

    __tablename__ = 'ability_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def get_id(self):
        return self.id

    def set_name(self, value):
        Model.validate_set_property(value, 'name', str, self.TYPES)
        self.name = value
        return self

    def get_name(self):
        return self.name
