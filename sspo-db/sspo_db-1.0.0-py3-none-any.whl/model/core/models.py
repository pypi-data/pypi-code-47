from sqlalchemy import Column, String,ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType, URLType
from sspo_db.config.base import BaseX

class ApplicationType (BaseX):
    
    __tablename__ = "application_type"

    name = Column(String(200), nullable=False)
    
    def __str__(self):
        return self.name
    
class Application(BaseX):
    
    __tablename__ = "application"
    
    name = Column(String(200), nullable=False)
    application_type = Column(Integer, ForeignKey('application_type.id'))

    def __str__(self):
        return self.name

class Configuration(BaseX):
    
    __tablename__ = "configuration"

    secret = Column(String(200), nullable=False)
    url = Column(URLType)
    application = Column(Integer, ForeignKey('application.id'))

class ApplicationReference(BaseX):

    __tablename__ = "application_reference"

    application = Column(Integer, ForeignKey('application.id'))
    external_id = Column(String(200), nullable=False)
    url = Column(URLType)
    type_entity = Column(String(200), nullable=False)


    