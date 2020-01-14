from sspo_db.config.base import Entity
from sspo_db.config.config import Base
from sqlalchemy import Column, Boolean ,ForeignKey, Integer, DateTime, String, Table
from sqlalchemy.orm import relationship
from sspo_db.model.process.models import Sprint
from sspo_db.model.artifact.models import SprintBacklog

association_sprint_scrum_development_activity_table = Table('association_sprint_scrum_development_activity', Base.metadata,
    Column('scrum_development_task_id', Integer, ForeignKey('scrum_development_task.id')),
    Column('sprint_id', Integer, ForeignKey('sprint.id'))
)

association_sprint_backlog_scrum_development_activity_table = Table('association_sprint_backlog_scrum_development_activity', Base.metadata,
    Column('scrum_development_task_id', Integer, ForeignKey('scrum_development_task.id')),
    Column('sprint_backlog_id', Integer, ForeignKey('sprint_backlog.id'))
)

class ScrumDevelopmentTask(Entity):
    
    is_instance_of = "spo.activity"
    __tablename__ = "scrum_development_task"

    created_date = Column(DateTime)
    created_by = Column(Integer, ForeignKey('team_member.id'))
    assigned_by = Column(Integer, ForeignKey('team_member.id'))
    type = Column(String(50))

    sprints = relationship(Sprint, 
                            secondary=association_sprint_scrum_development_activity_table, 
                            back_populates="scrum_development_tasks")

    sprint_backlogs = relationship(SprintBacklog, 
                        secondary=association_sprint_backlog_scrum_development_activity_table, 
                        back_populates="scrum_development_tasks")
    atomic_user_story = Column(Integer, ForeignKey('atomic_user_story.id'))
    
    __mapper_args__ = {
        'polymorphic_identity':'scrum_development_task',
        'polymorphic_on':type
    }
    
class DevelopmentTaskType(Entity):

    __tablename__ = "development_task_type"

    '''Analysis = 0
    deployment = 1
    design = 2
    development = 3
    documentation = 4
    requirements = 5
    testing = 6'''
    
class Priority(Entity):
    __tablename__ = "priority"
    '''High = 1
    Medium = 2
    Normal = 3'''
    
class Risk(Entity):
    __tablename__ = "risk"

    '''High = 1
    Medium = 2
    Normal = 3'''

class ScrumIntentedDevelopmentTask(ScrumDevelopmentTask):

    is_instance_of = "spo.intended.activity.x"
    __tablename__ = "scrum_intented_development_task"

    id = Column(Integer, ForeignKey('scrum_development_task.id'), primary_key=True)
    
    type_activity = Column(Integer, ForeignKey('development_task_type.id'))
    priority = Column(Integer, ForeignKey('priority.id'))
    risk = Column(Integer, ForeignKey('risk.id'))
    story_points = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'scrum_intented_development_task',
    }
    
class ScrumPerformedDevelopmentTask(ScrumDevelopmentTask):
    is_instance_of = "spo.performed.activity.x"
    __tablename__ = "scrum_performed_development_task"

    id = Column(Integer, ForeignKey('scrum_development_task.id'), primary_key=True)
    
    closed_date = Column(DateTime)
    activated_date = Column(DateTime)
    resolved_date = Column(DateTime)

    activated_by = Column(Integer, ForeignKey('team_member.id'))
    closed_by = Column(Integer, ForeignKey('team_member.id'))
    resolved_by = Column(Integer, ForeignKey('team_member.id'))
    
    caused_by = Column(Integer, ForeignKey('scrum_intented_development_task.id'))

    __mapper_args__ = {
        'polymorphic_identity':'scrum_performed_development_task',
    }

    #state = models.CharField(max_length=100,blank=True, null=True)
