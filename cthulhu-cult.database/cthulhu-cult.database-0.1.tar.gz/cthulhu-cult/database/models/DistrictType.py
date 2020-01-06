from database.models.common.Model import Model
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database.services.DbService import Base
from sqlalchemy.orm import relationship
from database.models.Mana import Mana


class DistrictType(Model, Base):
    WARZONE = 'warzone'
    NECROPOLIS = 'necropolis'
    RUINS = 'ruins'
    SWAMP = 'swamp'
    PRISON = 'prison'

    SUBURBS = 'suburbs'
    RED_LIGHT_DISTRICT = 'red light district'
    HOLY_GROUND = 'holy ground'
    FOREST = 'forest'
    PARK = 'park'

    DOCKS = 'docks'
    COUNTRYSIDE = 'countryside'
    REFUGEE_CAMPS = 'refugee camps'
    ISLAND = 'island'
    MANNOR = 'mannor'

    TOWNHALL = 'town hall'
    RESEARCH_CENTER = 'research center'
    TOURISM_ZONE = 'tourism zone'
    DESERT = 'desert'
    TRAIN_STATION = 'train station'

    SLUMS = 'slums'
    BOHEMIAN_DISTRICT = 'bohemian district'
    COMMERCIAL_ZONE = 'commercial zone'
    MOUNTAINS = 'mountains'
    FLEA_MARKET = 'flea market'

    TYPES = {
        Mana.DEATH: [
            WARZONE,
            NECROPOLIS,
            RUINS,
            SWAMP,
            PRISON
        ],
        Mana.PASSION: [
            SUBURBS,
            RED_LIGHT_DISTRICT,
            HOLY_GROUND,
            FOREST,
            PARK
        ],
        Mana.SLEEP: [
            DOCKS,
            COUNTRYSIDE,
            REFUGEE_CAMPS,
            ISLAND,
            MANNOR
        ],
        Mana.TIMESPACE: [
            TOWNHALL,
            RESEARCH_CENTER,
            TOURISM_ZONE,
            DESERT,
            TRAIN_STATION
        ],
        Mana.MADNESS: [
            SLUMS,
            BOHEMIAN_DISTRICT,
            COMMERCIAL_ZONE,
            MOUNTAINS,
            FLEA_MARKET
        ]
    }

    WILDERNESS_TYPES = [SWAMP, FOREST, ISLAND, DESERT, MOUNTAINS]

    __tablename__ = 'district_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_wilderness = Column(Boolean)
    mana_id = Column(Integer, ForeignKey('mana.id'))
    mana = relationship("Mana")

    def get_id(self):
        return self.id

    def set_name(self, value):
        self.name = value
        return self

    def get_name(self):
        return self.name

    def set_is_wilderness(self, value):
        self.is_wilderness = value
        return self

    def get_is_wilderness(self):
        return self.is_wilderness

    def get_mana_id(self):
        return self.mana_id

    def set_mana(self, value):
        self.mana = value
        return self

    def get_mana(self):
        return self.mana

    def __repr__(self):
        if self.name:
            return self.name
        return ''
