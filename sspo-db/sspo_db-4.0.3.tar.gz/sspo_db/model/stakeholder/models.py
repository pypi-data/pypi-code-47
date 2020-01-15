from sspo_db.config.base import Entity
from sqlalchemy import Column ,ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

class Person (Entity):
    is_instance_of = "eo.person"    
    __tablename__ = "person"
    
    email = Column(EmailType, unique=True)
    type = Column(String(50))
    
    organization_id = Column(Integer, ForeignKey('organization.id'))
    organization = relationship("Organization", back_populates="people")

    __mapper_args__ = {
        'polymorphic_identity':'person',
        'polymorphic_on':type
    }

class TeamMember(Person):
    is_instance_of = "eo.team_member"
    __tablename__ = "team_member"
    
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship("Team",back_populates="team_members")
    team_role = Column(String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity':'team_member',
    }