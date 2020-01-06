from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class DistrictCoordinates(Model, Base):
    __tablename__ = 'district_coordinates'
    id = Column(Integer, primary_key=True)
    district_id = Column(Integer, ForeignKey('district.id'))
    district = relationship("District", back_populates="coordinates")
    x = Column(Integer)
    y = Column(Integer)

    def get_id(self):
        return self.id

    def set_district_id(self, value):
        self.district_id = value
        return self

    def get_district_id(self):
        return self.district_id

    def set_district(self, value):
        self.district = value
        return self

    def get_district(self):
        return self.district

    def set_x(self, value):
        self.x = value
        return self

    def get_x(self):
        return self.x

    def set_y(self, value):
        self.y = value
        return self

    def get_y(self):
        return self.y
