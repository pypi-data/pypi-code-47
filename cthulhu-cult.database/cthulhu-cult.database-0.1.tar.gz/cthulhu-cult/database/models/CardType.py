from sqlalchemy import Column, Integer, String
from database.models.common.Model import Model
from database.services.DbService import Base


class CardType(Model, Base):
    POSESSION = 'possesion'
    COVENANT = 'covenant' #gift
    INFLUENCE = 'influence' #sorcery / instant eldritch
    COMMANDMENT = 'commandment' #enchantment

    TYPES = [POSESSION]

    __tablename__ = 'card_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def get_id(self):
        return self.id

    def set_name(self, value):
        Model.validate_set_property(value, 'name', str, self.TYPES)
        self.name = value
        return self

    def get_name(self):
        return self.name
