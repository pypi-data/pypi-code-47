import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()

# Needed to initialize tables in the database
from database.models.Ability import Ability
from database.models.AbilityType import AbilityType
from database.models.Action import Action
from database.models.ActionType import ActionType
from database.models.Card import Card
from database.models.CardType import CardType
from database.models.CardCharacter import CardCharacter
from database.models.Deck import Deck
from database.models.District import District
from database.models.DistrictConnection import DistrictConnection
from database.models.DistrictCoordinates import DistrictCoordinates
from database.models.DistrictType import DistrictType
from database.models.Map import Map
from database.models.Location import Location
from database.models.LocationType import LocationType
from database.models.Mana import Mana
from database.models.Match import Match
from database.models.MatchCard import MatchCard
from database.models.CardCharacter import CardCharacter
from database.models.MatchCardCharacter import MatchCardCharacter
from database.models.MatchDeck import MatchDeck
from database.models.MatchState import MatchState
from database.models.MatchTurn import MatchTurn
from database.models.Player import Player
from database.models.PlayerAvatar import PlayerAvatar
from database.models.MatchCardAttachment import MatchCardAttachment
import json


class DbService:
    class __DbService:
        def __init__(self):
            self.base = None
            self.session = None
            self.base = create_engine('sqlite:///test.db')
            self.session = (sessionmaker(self.base))()

        def init_database(self):
            if os.path.exists('test.db'):
                os.remove('test.db')
            self.base = create_engine('sqlite:///test.db')
            self.session = (sessionmaker(self.base))()
            Base.metadata.create_all(self.base)

        def add(self, entity):
            self.session.add(entity)
            return self.session.commit()

        def delete(self, entity):
            self.base.session.delete(entity)
            self.base.session.commit()

        def select(self, class_name, properties, first=False):
            query = self.session.query(class_name)
            for attr, value in properties.items():
                query = query.filter(getattr(class_name, attr).like("%%%s%%" % value))
            return query.first() if first else query.all()

        def update(self):
            return self.session.commit()

    instance = None

    def __init__(self):
        if not DbService.instance:
            DbService.instance = DbService.__DbService()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def init_database(self):
        DbService.instance.init_database()
        return self

    def add(self, entity):
        return DbService.instance.add(entity)

    def delete(self, entity):
        return DbService.instance.delete(entity)

    def select(self, class_name, properties, first=False):
        return DbService.instance.select(class_name, properties, first)

    def update(self):
        return DbService.instance.update()


db_service = DbService()
