from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class Location(Model, Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    district_id = Column(Integer, ForeignKey('district.id'))
    type_id = Column(Integer, ForeignKey('location_type.id'))
    type = relationship("LocationType")
    owner_id = Column(Integer, ForeignKey('player_avatar.id'))
    owner = relationship("PlayerAvatar")
    suspicion_level = Column(Integer)
    characters = relationship("MatchCardCharacter", back_populates="location")

    def get_id(self):
        return self.id

    def set_district_id(self, value):
        self.district_id = value
        return self

    def get_district_id(self):
        return self.district_id

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

    def set_owner_id(self, value):
        self.owner_id = value
        return self

    def get_owner_id(self):
        return self.owner_id

    def set_owner(self, value):
        self.owner = value
        return self

    def get_owner(self):
        return self.owner

    def set_suspicion_level(self, value):
        self.suspicion_level = value
        return self

    def get_suspicion_level(self):
        return self.suspicion_level

    def add_character(self, value):
        self.characters.append(value)
        return self

    def remove_character(self, value):
        self.characters.remove(value)
        return self
