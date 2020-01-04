from sspo_db.config.base import Entity
from sqlalchemy import Column, Boolean ,ForeignKey, Integer, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

class Organization(Entity):
     
    __tablename__ = "organization"

    is_instance_of = "eo.organization"

class Team(Entity):
    is_instance_of = "eo.team"
    __tablename__ = "team"

    organization = Column(Integer, ForeignKey('organization.id'))
    complex_team_id = Column(Integer, ForeignKey('team.id'))
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'team',
        'polymorphic_on':type
    }

class ComplexTeam(Team):
    is_instance_of = "eo.team.complex"
    __tablename__ = "complex_team"
    
    id = Column(Integer, ForeignKey('team.id'), primary_key=True)
    team = relationship("Team")
    
    __mapper_args__ = {
        'polymorphic_identity':'complex_team',
    }

class AtomicTeam(Team):
    is_instance_of = "eo.team.atomic"
    __tablename__ = "atomic_team"

    id = Column(Integer, ForeignKey('team.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity':'atomic_team',
    }


class ScrumTeam(ComplexTeam):
    
    is_instance_of = "spo.stakeholder.project_team"
    __tablename__ = "scrum_team"

    id = Column(Integer, ForeignKey('complex_team.id'), primary_key=True)
    scrum_project = Column(Integer, ForeignKey('scrum_project.id'))
    
    
    __mapper_args__ = {
        'polymorphic_identity':'scrum_team',
    }
    

class DevelopmentTeam(AtomicTeam):
    
    is_instance_of = "spo.stakeholder.project_team"
    __tablename__ = "development_team"
    
    id = Column(Integer, ForeignKey('atomic_team.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'development_team',
    }
