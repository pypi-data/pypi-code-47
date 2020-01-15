from sspo_db.config.base import Entity
from sspo_db.config.config import Base
from sqlalchemy import Column, Boolean ,ForeignKey, Integer, DateTime, String, Table
from sqlalchemy.orm import relationship

association_sprint_backlog_scrum_development_table = Table('association_sprint_backlog_scrum_development', Base.metadata,
    Column('scrum_development_task_id', Integer, ForeignKey('scrum_development_task.id')),
    Column('sprint_backlog_id', Integer, ForeignKey('sprint_backlog.id'))
)

association_atomic_user_story_sprint_backlog_table = Table('association_atomic_user_story_sprint_backlog', Base.metadata,
    Column('atomic_user_story_id', Integer, ForeignKey('atomic_user_story.id')),
    Column('sprint_backlog_id', Integer, ForeignKey('sprint_backlog.id'))
)

class ProductBacklog(Entity):
    is_instance_of = "spo.document"
    __tablename__ = "product_backlog"

    product_backlog_definition = Column(Integer, ForeignKey('product_backlog_definition.id')) 

class UserStory(Entity):
    is_instance_of = "rsro.requirements.artifact"
    __tablename__ = "user_story"

    product_backlog =  Column(Integer, ForeignKey('product_backlog.id'))
    
    created_by = Column(Integer, ForeignKey('team_member.id')) 
    activated_by = Column(Integer, ForeignKey('team_member.id'))
    closed_by = Column(Integer, ForeignKey('team_member.id'))
    assigned_by = Column(Integer, ForeignKey('team_member.id'))

    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'user_story',
        'polymorphic_on':type
    }
    
class Epic(UserStory):

    __tablename__ = "epic"
    id = Column(Integer, ForeignKey('user_story.id'), primary_key=True)

    epic = Column(Integer, ForeignKey('epic.id'))

    __mapper_args__ = {
        'polymorphic_identity':'epic',
    }

class AtomicUserStory(UserStory):

    __tablename__ = "atomic_user_story"
    
    id = Column(Integer, ForeignKey('user_story.id'), primary_key=True)
    epic = Column(Integer, ForeignKey('epic.id'))
    sprint_backlogs = relationship("SprintBacklog", secondary=association_atomic_user_story_sprint_backlog_table, back_populates="atomic_user_stories")

    __mapper_args__ = {
        'polymorphic_identity':'atomic_user_story',
    }

class SprintBacklog(Entity):
    is_instance_of = "spo.document"
    __tablename__ = "sprint_backlog"

    sprint = Column(Integer, ForeignKey('sprint.id'))
    planning_meeting = Column(Integer, ForeignKey('planning_meeting.id'))
    
    scrum_development_tasks = relationship("ScrumDevelopmentTask", secondary=association_sprint_backlog_scrum_development_table, back_populates="sprint_backlogs")
    atomic_user_stories = relationship("AtomicUserStory", secondary=association_atomic_user_story_sprint_backlog_table, back_populates="sprint_backlogs")


class AcceptanceCriterion(Entity):
    is_instance_of = "rsro.requirements"
    __tablename__ = "acceptance_criterion"

    user_story =  Column(Integer, ForeignKey('user_story.id'))

    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'acceptance_criterion',
        'polymorphic_on':type
    }
    

class NonFunctionalAcceptanceCriterion(AcceptanceCriterion):
    is_instance_of = "rsro.non_functional_requirements"
    __tablename__ = "non_functional_acceptance_criterion"
    
    id = Column(Integer, ForeignKey('acceptance_criterion.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'non_functional_acceptance_criterion',
    }

class FunctionalAcceptanceCriterion(AcceptanceCriterion):
    is_instance_of = "rsro.functional_requirements"
    __tablename__ = "functional_acceptance_criterion"
    
    id = Column(Integer, ForeignKey('acceptance_criterion.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'functional_acceptance_criterion',
    }
    
'''
class ScrumCommonEntity(Entity):

    priority = models.CharField(max_length=10,blank=True, null=True)
    risk = models.CharField(max_length=10,blank=True, null=True)
    story_points = models.CharField(max_length=10,blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    
    activated_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    resolved_date = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)

    class Meta:
        abstract = True
        db_table = "scrum_common_entity"
'''