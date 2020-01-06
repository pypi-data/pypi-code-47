from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey
from database.services.DbService import Base
from sqlalchemy.orm import relationship


class CardCharacter(Model, Base):
    __tablename__ = 'card_character'
    id = Column(Integer, primary_key=True)
    max_health = Column(Integer)
    power = Column(Integer)
    card_id = Column(Integer, ForeignKey('card.id'))
    card = relationship("Card", back_populates="character")

    def get_id(self):
        return self.id

    def get_max_health(self):
        return self.max_health

    def set_max_health(self, value):
        self.max_health = value
        return self

    def get_power(self):
        return self.power

    def set_power(self, value):
        self.power = value
        return self

    def get_card_id(self):
        return self.card_id

    def set_card_id(self, value):
        self.card_id = value
        return self

    def get_card(self):
        return self.card

    def set_card(self, value):
        self.card = value
        return self


