from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class Deck(Model, Base):
    deck_card = Table('deck_card', Base.metadata, Column('deck_id', Integer, ForeignKey('deck.id')),
                      Column('card_id', Integer, ForeignKey('card.id'))
                      )
    __tablename__ = 'deck'
    id = Column(Integer, primary_key=True)
    owner = Column(Integer, ForeignKey('player.id'))
    cards = relationship("Card", secondary=deck_card)

    def get_id(self):
        return self.id

    def add_card(self, value):
        self.cards.append(value)
        return self

    def remove_card(self, value):
        self.cards.remove(value)
        return self
