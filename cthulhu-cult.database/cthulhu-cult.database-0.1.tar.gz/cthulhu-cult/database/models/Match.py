from database.models.common.Model import Model
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database.services.DbService import Base


class Match(Model, Base):
    match_player = Table('match_player', Base.metadata, Column('match_id', Integer, ForeignKey('match.id')),
                      Column('player_id', Integer, ForeignKey('player.id'))
                      )
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True)
    players = relationship("Player", secondary=match_player)
    state_id = Column(Integer, ForeignKey('match_state.id'))
    state = relationship("MatchState")
    turns = relationship("MatchTurn")
    player_avatars = relationship("PlayerAvatar")

    def get_id(self):
        return self.id

    def add_player(self, value):
        self.player.append(value)
        return self

    def remove_player(self, value):
        self.player.remove(value)
        return self

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

    def add_turn(self, value):
        self.turns.append(value)
        return self

    def remove_turn(self, value):
        self.turns.remove(value)
        return self

    def add_player_avatar(self, value):
        self.player_avatars.append(value)
        return self

    def remove_player_avatar(self, value):
        self.player_avatars.remove(value)
        return self
