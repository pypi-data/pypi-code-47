from database.models.common.Model import Model
from sqlalchemy import Column, Integer, String, Boolean
from database.services.DbService import Base


class LocationType(Model, Base):
    __tablename__ = 'location_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    earning = Column(Integer)
    buyout_sum = Column(Integer)
    takeover_difficulty = Column(Integer)
    is_hideout = Column(Boolean)

    def get_id(self):
        return self.id

    def set_name(self, value):
        self.name = value
        return self

    def get_name(self):
        return self.name

    def set_earning(self, value):
        self.earning = value
        return self

    def get_earning(self):
        return self.earning

    def set_buyout_sum(self, value):
        self.buyout_sum = value
        return self

    def get_buyout_sum(self):
        return self.buyout_sum

    def set_takeover_difficulty(self, value):
        self.takeover_difficulty = value
        return self

    def get_takeover_difficulty(self):
        return self.takeover_difficulty

    def set_is_hideout(self, value):
        self.is_hideout = value
        return self

    def get_is_hideout(self):
        return self.is_hideout
