from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.services.DbService import Base
from database.models.MapEffectType import MapEffectType


class MapEffect(Model, Base):
    __tablename__ = 'map_effect'
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey('map_effect_type.id'))
    type = relationship("MapEffectType")
    is_global = Column(Boolean)

    def get_id(self):
        return self.id

    def set_type_id(self, value):
        Model.validate_set_property(value, 'type_id', bool)
        self.type_id = value
        return self

    def get_type_id(self):
        return self.type_id

    def set_type(self, value):
        Model.validate_set_property(value, 'type', MapEffectType)
        self.type = value
        return self

    def get_type(self):
        return self.type

    def set_is_global(self, value):
        Model.validate_set_property(value, 'is_global', bool)
        self.is_global = value
        return self

    def get_is_global(self):
        return self.is_global
