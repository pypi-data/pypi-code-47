from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class MatchCardCharacter(Model, Base):
    __tablename__ = 'match_card_character'
    id = Column(Integer, primary_key=True)
    attachments = relationship("MatchCardAttachment", back_populates="attached_to")
    health = Column(Integer)
    sanity = Column(Integer)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", back_populates="characters", foreign_keys=[location_id])
    card_id = Column(Integer, ForeignKey('match_card.id'))
    card = relationship("MatchCard", back_populates="character", foreign_keys=[card_id])

    def get_id(self):
        return self.id

    def add_attachment(self, value):
        self.attachments.append(value)
        return self

    def remove_attachment(self, value):
        self.attachments.remove(value)
        return self

    def get_health(self):
        return self.health

    def set_health(self, value):
        self.health = value
        return self

    def get_sanity(self):
        return self.sanity

    def set_sanity(self, value):
        self.sanity = value
        return self

    def set_location_id(self, value):
        self.location_id = value
        return self

    def get_location_id(self):
        return self.location_id

    def get_location(self):
        return self.location

    def set_location(self, value):
        self.location = value
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
