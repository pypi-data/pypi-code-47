from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.services.DbService import Base
from database.models.common.WithCoordinates import WithCoordinates

district_district_connection = Table('district_district_connection', Base.metadata,
                                     Column('district_id', Integer, ForeignKey('district.id')),
                                     Column('connection_id', Integer, ForeignKey('district_connection.id'))
                                     )


class District(Model, Base, WithCoordinates):
    __tablename__ = 'district'
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey('district_type.id'))
    type = relationship("DistrictType")
    locations = relationship("Location")
    owner_id = Column(Integer, ForeignKey('player_avatar.id'))
    owner = relationship("PlayerAvatar")
    map_id = Column(Integer, ForeignKey('map.id'))
    map = relationship("Map", back_populates="districts")
    coordinates = relationship("DistrictCoordinates", uselist=False, back_populates="district")
    connections = relationship("DistrictConnection", secondary=district_district_connection, back_populates="districts")

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

    def add_location(self, value):
        self.locations.append(value)
        return self

    def remove_location(self, value):
        self.locations.remove(value)
        return self

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

    def set_map_id(self, value):
        self.map_id = value
        return self

    def get_map_id(self):
        return self.map_id

    def set_map(self, value):
        self.map = value
        return self

    def get_map(self):
        return self.map

    def set_coordinates(self, value):
        self.coordinates = value
        return self

    def get_coordinates(self):
        return self.coordinates

    def get_print(self):
        if self.type:
            return self.type.get_name()
        return ''

    def __repr__(self):
        if self.type:
            return 'x: {}, y: {}, type: {}'.format(self.coordinates.get_x(), self.coordinates.get_y(),
                                                   self.type.get_name())
        return 'x: {}, y: {}, type: {}'.format(self.coordinates.get_x(), self.coordinates.get_y(), '')
