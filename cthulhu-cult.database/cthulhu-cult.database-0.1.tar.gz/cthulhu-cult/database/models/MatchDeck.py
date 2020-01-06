from database.models.common.Model import Model
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class MatchDeck(Model, Base):
    __tablename__ = 'match_deck'
    id = Column(Integer, primary_key=True)
    match_cards = relationship("MatchCard")

    def get_id(self):
        return self.id

    def add_match_card(self, value):
        self.match_cards.append(value)
        return self

    def remove_match_card(self, value):
        self.match_cards.remove(value)
        return self
