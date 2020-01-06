from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class Map(Model, Base):
    __tablename__ = 'map'
    id = Column(Integer, primary_key=True)
    districts = relationship("District", back_populates="map")

    def get_id(self):
        return self.id

    def add_district(self, value):
        self.districts.append(value)
        return self

    def remove_district(self, value):
        self.districts.remove(value)
        return self
