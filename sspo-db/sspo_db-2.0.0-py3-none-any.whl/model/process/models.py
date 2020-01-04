from sspo_db.config.base import Entity
from sqlalchemy import Column, Boolean ,ForeignKey, Integer, DateTime, String
from sqlalchemy.orm import relationship
from sspo_db.model.activity.models import association_sprint_scrum_development_table

class ScrumProject(Entity):
    is_instance_of = "spo.software_project"
    __tablename__ = "scrum_project"

    root = Column(Boolean, unique=False, default=True)
    organization = Column(Integer, ForeignKey('organization.id'))
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'scrum_project',
        'polymorphic_on':type
    }
    
class ScrumComplexProject(ScrumProject):
    is_instance_of = "spo.software_project.complex"  
    __tablename__ = "scrum_complex_project"

    id = Column(Integer, ForeignKey('scrum_project.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity':'scrum_complex_project',
    }


class ScrumAtomicProject(ScrumProject):
    is_instance_of = "spo.software_project.atomic"
    __tablename__ = "scrum_atomic_project"

    id = Column(Integer, ForeignKey('scrum_project.id'), primary_key=True)

    complex_project = relationship(ScrumComplexProject,backref="scrum_atomic_projects", cascade="all, delete-orphan", single_parent=True)

    __mapper_args__ = {
        'polymorphic_identity':'scrum_atomic_project',
    }

class ScrumProcess(Entity):
    is_instance_of = "spo.performed.process.general.project"
    __tablename__ = "scrum_process"
    
    scrum_project = Column(Integer, ForeignKey('scrum_project.id'))
    

class ProductBacklogDefinition(Entity):
    is_instance_of = "spo.performed.process.specific.project"
    __tablename__ = "product_backlog_definition"
    scrum_project = Column(Integer, ForeignKey('scrum_project.id'))
    

class Sprint(Entity):

    is_instance_of = "spo.performed.process.specific.project"
    __tablename__ = "sprint"
    
    startDate  = Column(DateTime)
    endDate = Column(DateTime)
    scrum_project = Column(Integer, ForeignKey('scrum_project.id'))
    
    scrum_development_tasks = relationship("ScrumDevelopmentTask", secondary=association_sprint_scrum_development_table, back_populates="sprints")

    
class Cerimony(Entity):
    is_instance_of = "spo.performed.activity.project"
    __tablename__ = "cerimony"

    startDate  = Column(DateTime)
    endDate = Column(DateTime)
    sprint = Column(Integer, ForeignKey('sprint.id'))
    
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'cerimony',
        'polymorphic_on':type
    }

   
class PlanningMeeting(Cerimony):
    __tablename__ = "planning_meeting"
    
    id = Column(Integer, ForeignKey('cerimony.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity':'planning_meeting',
    }

   
class DailyStandupMeeting(Cerimony):
    __tablename__ = "daily_standup_meeting"
    
    id = Column(Integer, ForeignKey('cerimony.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity':'daily_standup_meeting',
    }


class ReviewMeeting(Cerimony):
    __tablename__ = "review_meeting"

    id = Column(Integer, ForeignKey('cerimony.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity':'review_meeting',
    }


class RetrospectiveMeeting(Cerimony):
    __tablename__ = "retrospective_meeting"

    id = Column(Integer, ForeignKey('cerimony.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity':'retrospective_meeting',
    }

