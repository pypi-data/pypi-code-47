from sspo_db.config.base import Entity
from sqlalchemy import Column, Boolean ,ForeignKey, Integer, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from sspo_db.model.stakeholder.models import Person

class Organization(Entity):
    is_instance_of = "eo.organization" 
    __tablename__ = "organization"

    scrum_project = relationship("ScrumProject", back_populates="organization")
    team = relationship("Team", back_populates="organization")
    people = relationship(Person, back_populates="organization")
    configuration = relationship("Configuration", back_populates="organization") 

class Team(Entity):
    is_instance_of = "eo.team"
    __tablename__ = "team"

    type = Column(String(50))
    
    organization_id = Column(Integer, ForeignKey('organization.id'))
    organization = relationship("Organization", back_populates="team")

    complex_team_id = Column(Integer, ForeignKey('team.id'))
    complex_team = relationship("ScrumTeam",back_populates="teams", foreign_keys=[complex_team_id])

    team_members = relationship("TeamMember", back_populates="team")

    __mapper_args__ = {
        'polymorphic_identity':'team',
        'polymorphic_on':type
    }

class ScrumTeam(Team):
    is_instance_of = "eo.team.complex"
    __tablename__ = "scrum_team"
    
    id = Column(Integer, ForeignKey('team.id'), primary_key=True)
    
    teams = relationship("Team", back_populates="complex_team")
    
    __mapper_args__ = {
        'polymorphic_identity':'scrum_team',
    }

class DevelopmentTeam(Team):
    is_instance_of = "eo.team.atomic"
    __tablename__ = "development_team"

    id = Column(Integer, ForeignKey('team.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity':'development_team',
    }

'''
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
'''