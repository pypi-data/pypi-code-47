from sspo_db.config.base import Entity
from sqlalchemy import Column ,ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

class Person (Entity):
    is_instance_of = "eo.person"    
    __tablename__ = "person"
    
    organization = Column(Integer, ForeignKey('organization.id'))
    email = Column(EmailType)
    
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'person',
        'polymorphic_on':type
    }

class TeamMember(Person):
    is_instance_of = "eo.team_member"
    __tablename__ = "team_member"
    
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    
    team = Column(Integer, ForeignKey('team.id'))
    team_role = Column(String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity':'team_member',
    }