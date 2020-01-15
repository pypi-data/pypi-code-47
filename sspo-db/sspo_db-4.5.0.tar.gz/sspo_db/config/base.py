from .config import Base
import datetime
from sqlalchemy import Column, String, Integer, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
import uuid


class Entity(Base):
    
    __abstract__  = True

    id = Column(Integer, primary_key=True)
    uuid = Column(UUIDType(binary=False), unique=True, nullable=False, default=uuid.uuid4)
    date_created  = Column(DateTime,  default=datetime.datetime.utcnow)
    date_modified = Column(DateTime,  default=datetime.datetime.utcnow,onupdate=datetime.datetime.utcnow)    

    name = Column(String(200), nullable=True)
    description = Column(String(200), nullable=True)
    is_instance_of = ""
    
    def __str__(self):
        return self.name
    
    def entity_name(self):
        return self.is_instance_of
    
    
    
    