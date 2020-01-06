from database.models.common.Model import Model
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class Card(Model, Base):
    card_mana = Table('card_mana', Base.metadata, Column('card_id', Integer, ForeignKey('card.id')),
                      Column('mana_id', Integer, ForeignKey('mana.id'))
                      )
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_id = Column(Integer, ForeignKey('card_type.id'))
    type = relationship("CardType")
    cost = relationship("Mana", secondary=card_mana)
    description = Column(String)
    flavour_text = Column(String)
    character = relationship("CardCharacter", uselist=False, back_populates="card")
    is_attachable = Column(Boolean)

    def get_id(self):
        return self.id

    def set_name(self, value):
        self.name = value
        return self

    def get_name(self):
        return self.name

    def set_type_id(self, value):
        self.type_id = value
        return self

    def get_type_id(self):
        return self.type_id

    def set_type(self, value):
        self.type = value
        return self

    def get_type(self):
        return self.type

    def add_cost(self, value):
        self.cost.append(value)
        return self

    def remove_cost(self, value):
        self.cost.remove(value)
        return self

    def set_description(self, value):
        self.description = value
        return self

    def get_description(self):
        return self.description

    def set_flavour_text(self, value):
        self.flavour_text = value
        return self

    def get_flavour_text(self):
        return self.flavour_text

    def set_character(self, value):
        self.character = value
        return self

    def get_character(self):
        return self.character

    def set_is_attachable(self, value):
        self.is_attachable = value
        return self

    def get_is_attachable(self):
        return self.is_attachable
