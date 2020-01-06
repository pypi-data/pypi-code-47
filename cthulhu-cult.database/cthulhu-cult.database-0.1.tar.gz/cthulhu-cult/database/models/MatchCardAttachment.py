from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class MatchCardAttachment(Model, Base):
    __tablename__ = 'match_card_attachment'
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey('match_card.id'))
    card = relationship("MatchCard", back_populates="attachment_data", foreign_keys=[card_id])
    attached_to_id = Column(Integer, ForeignKey('match_card_character.id'))
    attached_to = relationship("MatchCardCharacter", back_populates="attachments", foreign_keys=[attached_to_id])

    def get_id(self):
        return self.id

    def set_attached_to_id(self, value):
        self.attached_to_id = value
        return self

    def get_attached_to_id(self):
        return self.attached_to_id

    def set_attached_to(self, value):
        self.attached_to = value
        return self

    def get_attached_to(self):
        return self.attached_to
