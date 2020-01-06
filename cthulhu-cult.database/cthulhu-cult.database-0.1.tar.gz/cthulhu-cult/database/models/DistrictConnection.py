from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from database.services.DbService import Base
from database.models.District import district_district_connection
from sqlalchemy.orm import relationship


class DistrictConnection(Model, Base):
    __tablename__ = 'district_connection'
    id = Column(Integer, primary_key=True)
    districts = relationship("District", secondary=district_district_connection, back_populates="connections")
    type_id = Column(Integer, ForeignKey('district_connection_type.id'))
    type = relationship("DistrictConnectionType")
    is_active = Column(Boolean)

    def get_id(self):
        return self.id

    def add_district(self, value):
        self.districts.append(value)
        return self

    def remove_district(self, value):
        self.districts.remove(value)
        return self

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

    def set_is_active(self, value):
        self.is_active = value
        return self

    def get_is_active(self):
        return self.is_active
