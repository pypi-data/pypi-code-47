from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class MatchCard(Model, Base):
    __tablename__ = 'match_card'
    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey('match_deck.id'))
    card_id = Column(Integer, ForeignKey('card.id'))
    card = relationship("Card")
    state_id = Column(Integer, ForeignKey('match_card_state.id'))
    state = relationship("MatchCardState")
    character = relationship("MatchCardCharacter", uselist=False, back_populates="card")
    attachment_data = relationship("MatchCardAttachment", uselist=False, back_populates="card")

    #action_queue = Column(Integer)

    def get_id(self):
        return self.id

    def set_deck_id(self, value):
        self.deck_id = value
        return self

    def get_deck_id(self):
        return self.deck_id
    
    def set_card_id(self, value):
        self.card_id = value
        return self

    def get_card_id(self):
        return self.card_id

    def set_card(self, value):
        self.card = value
        return self

    def get_card(self):
        return self.card

    def set_state_id(self, value):
        self.state_id = value
        return self

    def get_state_id(self):
        return self.state_id

    def set_state(self, value):
        self.state = value
        return self

    def get_state(self):
        return self.state

    def set_character(self, value):
        self.character = value
        return self

    def get_character(self):
        return self.character

    def set_attachment_data(self, value):
        self.attachment_data = value
        return self

    def get_attachment_data(self):
        return self.attachment_data
