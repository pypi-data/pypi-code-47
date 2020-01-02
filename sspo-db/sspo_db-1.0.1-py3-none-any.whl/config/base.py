from .config import Base
import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy_utils import UUIDType
import uuid

class BaseX(Base):
    
    __abstract__  = True
    
    id = Column(Integer, primary_key=True)
    uuid = Column(UUIDType(binary=False), unique=True, nullable=False, default=uuid.uuid4)
    date_created  = Column(DateTime,  default=datetime.datetime.utcnow)
    date_modified = Column(DateTime,  default=datetime.datetime.utcnow,
                                           onupdate=datetime.datetime.utcnow)    

#association_table = Table('association', Base.metadata,
#    Column('left_id', Integer, ForeignKey('left.id')),
#    Column('right_id', Integer, ForeignKey('right.id'))
#)

class Thing(BaseX):
    
    __abstract__  = True
    
    #application_reference = models.ManyToManyField(Application_Reference, blank=True)
    
    is_instance_of = ""

    def entity_name(self):
        return self.is_instance_of
    
class Relator(Thing):
    
    __abstract__  = True

class Entity(Thing):
    
    __abstract__  = True
    
    name = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)
    
    def __str__(self):
        return self.name
    
    
    
    