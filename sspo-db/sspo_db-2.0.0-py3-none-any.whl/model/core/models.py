from sqlalchemy import Column, String,ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType, URLType
from sspo_db.config.base import Entity

class ApplicationType (Entity):
    
    __tablename__ = "application_type"

    
class Application(Entity):
    
    __tablename__ = "application"
    
    application_type = Column(Integer, ForeignKey('application_type.id'))

    def __str__(self):
        return self.name

class Configuration(Entity):
    
    __tablename__ = "configuration"

    secret = Column(String(200), nullable=False)
    url = Column(URLType)
    application = Column(Integer, ForeignKey('application.id'))

class ApplicationReference(Entity):

    __tablename__ = "application_reference"
    # external application's data
    application = Column(Integer, ForeignKey('application.id'))
    
    external_id = Column(String(200), nullable=False)
    external_url = Column(URLType)
    external_type_entity = Column(String(200), nullable=False)
    
    #Internal BD
    internal_uuid = Column(UUIDType(binary=False))
    entity_name = Column(String(200), nullable=False)



    