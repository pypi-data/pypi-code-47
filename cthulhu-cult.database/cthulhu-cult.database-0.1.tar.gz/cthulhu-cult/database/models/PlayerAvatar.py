from database.models.common.Model import Model
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class PlayerAvatar(Model, Base):
    player_avatar_mana = Table('player_avatar_mana', Base.metadata, Column('player_avatar_id', Integer, ForeignKey('player_avatar.id')),
                      Column('mana_id', Integer, ForeignKey('mana.id'))
                      )
    __tablename__ = 'player_avatar'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('match.id'))
    player_id = Column(Integer, ForeignKey('player.id'))
    player = relationship("Player")
    mana_pool = relationship("Mana", secondary=player_avatar_mana)
    match_deck_id = Column(Integer, ForeignKey('match_deck.id'))
    match_deck = relationship("MatchDeck")

    def get_id(self):
        return self.id

    def set_player_id(self, value):
        self.player_id = value
        return self

    def get_player_id(self):
        return self.player_id

    def get_player(self):
        return self.player

    def set_player(self, value):
        self.player = value

    def add_mana(self, value):
        self.mana_pool.append(value)
        return self

    def remove_mana(self, value):
        self.mana_pool.remove(value)
        return self

    def set_match_deck_id(self, value):
        self.match_deck_id = value
        return self

    def get_match_deck_id(self):
        return self.match_deck_id

    def get_match_deck(self):
        return self.match_deck

    def set_match_deck(self, value):
        self.match_deck = value
