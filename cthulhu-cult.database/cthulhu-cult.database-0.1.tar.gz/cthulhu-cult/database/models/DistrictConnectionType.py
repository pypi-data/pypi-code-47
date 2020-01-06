from database.models.common.Model import Model
from sqlalchemy import Column, Integer, String
from database.services.DbService import Base


class DistrictConnectionType(Model, Base):
    SEA = 'sea'
    UNDERGROUND = 'underground'
    TRAIN = 'train'
    PORTAL = 'portal'
    STANDARD = 'standard'
    TYPES = [SEA, UNDERGROUND, TRAIN, PORTAL, STANDARD]

    __tablename__ = 'district_connection_type'
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
