from database.models.common.Model import Model
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class Player(Model, Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    decks = relationship("Deck")

    def get_id(self):
        return self.id

    def add_deck(self, value):
        self.decks.append(value)
        return self

    def remove_deck(self, value):
        self.decks.remove(value)
        return self
